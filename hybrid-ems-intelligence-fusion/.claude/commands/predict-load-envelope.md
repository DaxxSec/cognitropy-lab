# /predict-load-envelope — Look-Ahead Power-Demand Distribution

Emit a horizon-aware power-demand distribution (mean, credible bands, dominant-uncertainty tag, scenario tail) suitable for direct consumption by an EMS controller — ECMS / A-ECMS equivalence-factor adaptation, MPC, RL state representation, or rule-based with adaptive thresholds.

## Inputs

- **Fused prior** — `/fuse-trip-prior` output, optionally post-`/source-conflict`.
- **Horizon configuration** — length (distance or time), discretisation (default 1 Hz or 10 m per sample), and downstream consumer's expected schema.
- **Vehicle state at horizon start** — SOC, battery temperature, engine warm-up state, HVAC mode.
- **Scenario tail policy** — `nominal_only` (mean only), `nominal_plus_band` (mean + credible band), or `multi_scenario` (mean + N percentile scenarios for stochastic MPC).

## Steps

### 1. Resample to Controller Cadence
Re-sample the fused prior to the controller's expected cadence. Preserve credible bands through linear interpolation in the mean and quadratic in the variance.

### 2. Add State-Dependent Components
Augment the road-load prior with state-dependent demand:

- **Cold-start enrichment** — extra fuel demand if engine is cold (look up the vehicle's warm-up power offset curve).
- **HVAC** — fold in expected cabin conditioning load from weather + cabin setpoint.
- **Auxiliary electrical** — accessories: lights, heated surfaces, infotainment idle power.

### 3. Battery Capability Envelope
Constrain demand by battery instantaneous capability:

- Pull `P_chg_max(SOC, T, SOH)` and `P_dis_max(SOC, T, SOH)` from battery model.
- Mark horizon samples where unconstrained demand exceeds battery capability — these are forced-engine-on segments regardless of EMS strategy.

### 4. Generate the Output Object
Depending on `scenario_tail`:

- `nominal_only`: `[ { t, P_demand_mean } ]`
- `nominal_plus_band`: `[ { t, P_demand_mean, P_demand_lower, P_demand_upper, dominant_uncertainty } ]`
- `multi_scenario`: `[ { t, scenarios: [ {prob, P_demand}, … ] } ]` with N=3–10 scenarios sampled by importance sampling.

### 5. Sanity Checks Before Emission
- Integrated horizon energy is within ±20% of historical drives on the same route (else flag).
- No sample exceeds the powertrain's physical absolute power capability (else clamp + log).
- Variance is monotonically non-decreasing with horizon distance (else flag — likely a fusion artefact).

### 6. Persist
Write to `outputs/envelopes/<vehicle>-<route-hash>-<timestamp>.json` and emit the envelope to stdout for piping to `/optimize-split`.

## Output

A load-envelope object (file + stdout) matching the requested `scenario_tail` schema, with `dominant_uncertainty` tagging whether the band is dominated by source-disagreement (fix with `/source-conflict`) or source-noise (cannot be fixed without better instrumentation).

## Notes

- **Battery capability envelope is non-negotiable.** EMS strategies that ignore it produce torque-split policies the powertrain physically cannot follow; the controller silently saturates and you get worse outcomes than rule-based.
- **Don't emit a `nominal_only` envelope to a stochastic MPC.** The MPC's value is in handling uncertainty — feeding it the mean is a category error. Match the schema to the consumer.
- **Cold-start enrichment shows up as the largest cycle-to-cycle variance source on short trips.** If `dominant_uncertainty=cold_start_noise` over the first 2–5 km, the right mitigation is engine pre-conditioning (for PHEV) or a different EMS warm-up policy — not better fusion.
