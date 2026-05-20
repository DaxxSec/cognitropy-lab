# /optimize-split — Torque-Split + SOC-Trajectory Optimisation

Given a fused load envelope, compute the torque-split between engine and electric machine(s) and the SOC reference trajectory across the horizon, using an EMS strategy appropriate for the envelope's uncertainty structure.

## Inputs

- **Load envelope** — output of `/predict-load-envelope`.
- **EMS strategy choice** — one of `ecms`, `a_ecms`, `dp_offline`, `mpc_deterministic`, `mpc_stochastic`, `rl_policy` (loaded from `outputs/policies/`).
- **Cost weights** — `α_fuel`, `α_battery_wear` (Ah-throughput penalty), `α_emissions` (NOx/CO/PM-specific if RDE-relevant), `α_drivability`.
- **SOC constraints** — `SOC_min`, `SOC_max`, optional terminal `SOC_target` (for PHEV CD/CS scheduling).
- **Strategy-specific parameters** — see strategy taxonomy in `context/concepts.md`.

## Steps

### 1. Match Strategy to Envelope Type
Pick strategy by `scenario_tail`:

- `nominal_only` → ECMS / A-ECMS / deterministic MPC.
- `nominal_plus_band` → A-ECMS with band-aware equivalence factor adaptation, robust MPC, or chance-constrained MPC.
- `multi_scenario` → stochastic MPC with explicit scenario tree, multi-stage scenario decomposition, or sample-average approximation.

Reject mismatched combinations (e.g. running deterministic MPC on `multi_scenario`) and emit a warning.

### 2. Pre-Compute Auxiliary Maps
- Engine BSFC map at operating points.
- Motor efficiency map at operating points.
- Battery V-OCV(SOC), R(SOC, T, SOH).
- Powertrain inefficiency at each candidate operating point.

### 3. Run the Strategy
**ECMS / A-ECMS:** Compute equivalence factor `s_eq` adaptively from horizon prior; minimise instantaneous cost
`H = P_fuel(t) + s_eq · P_batt(t) + α_battery_wear · |I_batt(t)|^β`
over the powertrain mode choice at each sample.

**MPC (any variant):** Solve the receding-horizon problem with state x = SOC, control u = (T_engine, T_motor), dynamics from battery + drivetrain, constraints from capability envelope.

**Dynamic programming:** Run offline only — for benchmark reference, not real-time.

**RL policy:** Forward-rollout the trained policy on the envelope; flag any sample where the policy operates outside its training distribution.

### 4. Quality Gates
Before emitting, reject the solution if:

- Terminal SOC violates target by more than tolerance.
- Battery wear penalty exceeds budget.
- Drivability cost (engine on/off count, torque rate) exceeds calibration limits.
- Any sample saturates the battery capability envelope continuously for >2 s (likely an infeasibility the strategy is masking).

### 5. Persist + Compare
- Write the policy and SOC trajectory to `outputs/policies/<vehicle>-<route-hash>-<strategy>-<timestamp>.json`.
- If a previous policy exists for the same `(vehicle, route-hash)`, render a side-by-side comparison (fuel, energy, emissions, SOC RMS, battery wear) as part of the output report.

## Output

Policy file in `outputs/policies/` with: per-sample `(T_engine, T_motor, mode, SOC)`, summary KPIs (fuel L/100km, electric kWh/100km, CO2 g/km, battery wear units), and (if applicable) the comparison report against the previous policy. Plots include SOC trajectory, engine on/off raster, and Pareto position in `(fuel, battery_wear)` space.

## Notes

- **Equivalence factor adaptation is the make-or-break for A-ECMS.** Static `s_eq` defeats the purpose. Drive `s_eq` from the envelope's horizon-integrated energy and the `(SOC_now − SOC_target)` gap.
- **Don't switch strategies inside a trip.** Pick one at trip start (or at major reroute) and stick with it; mode-switching inside a trip causes drivability anomalies that calibration teams will refuse to sign off.
- **Battery wear weight has the biggest leverage on long-trip cumulative cost.** A policy that looks optimal on a single drive may be the worst over 100,000 km if `α_battery_wear` is set too low.
- **Cross-check against an offline DP benchmark on canonical cycles.** A real-time strategy that recovers <90% of the DP optimum on WLTP class 3b probably has a tuning issue, not a fundamental limitation.
