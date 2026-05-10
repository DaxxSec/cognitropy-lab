# Hybrid EMS — Workflows and Methodology

Step-by-step procedures the agent uses for EMS work, all framed through the Bayesian lens that this workspace's `technique` calls for.

## Workflow 1: Prior Elicitation Before Any Controller Design

**Goal:** Make every assumption about driver, route, and component state explicit and probabilistic *before* writing a single rule, so that downstream evaluation can isolate "the controller was wrong" from "the prior was wrong."

### Steps

1. **Driver class prior.** Tag historical trips (or sample drive cycles) into classes (calm urban, sport mixed, highway commute, stop-and-go congestion). Fit a categorical posterior; if no data, use a uniform prior over 3-4 classes and flag it.
2. **Trip distribution prior.** Build a posterior over trip-length distribution (mean + variance + tail) from historical telematics or representative cycle ensembles. PHEVs are especially sensitive — short trips never deplete; long trips spend most time in CS mode.
3. **Battery state prior.** From last EOL inspection or fleet aging curve, set a prior over (SOC at start, capacity, internal resistance, temperature). For new vehicles, use cell-vendor data; for older fleets, lean on UKF estimates from recent cycles.
4. **Model parameter prior.** BSFC map confidence, motor efficiency map confidence, transmission losses. Wider priors where the calibration data is older or scarcer.
5. **Document each prior in `outputs/priors-<date>.md`** before proceeding to controller design.

### Decision Points

- If no telematics available → start from population priors (e.g. ANL Autonomie default profiles), update as data arrives.
- If trip distribution is heavily bimodal (commute vs. road trip) → carry separate posteriors per mode, switch by GPS/calendar.
- If battery is past first warranty period → widen capacity-fade prior; UKF alone is not enough.

## Workflow 2: Bayesian SOC + SOH Estimation Pipeline

**Goal:** Produce a credible-interval-aware estimate of SOC (every control step) and SOH (per drive cycle) that a downstream controller can trust as a posterior, not a point.

### Steps

1. **Pick a battery model** matching the available compute and accuracy budget: Thevenin (1-2 RC pairs) for real-time onboard; SPM for periodic SOH refresh; DFN for offline benchmarking only.
2. **Pick an estimator**: UKF for unimodal Thevenin; particle filter (~100-1000 particles) for nonlinear electrochemistry or multi-modal posteriors near 0%/100% SOC.
3. **Bound the noise.** Sensor noise (current, voltage, temperature) sets the lower-bound posterior variance. Don't claim a tighter SOC interval than the sensors allow.
4. **Run estimation across recent cycles.** Log the running covariance — if it grows, the model is degrading; trigger a parameter re-identification.
5. **Update SOH posterior** at end-of-cycle by comparing modeled vs. measured terminal voltage trajectory; use coulomb-counting + voltage-fit jointly.
6. **Publish posterior summary** to `outputs/posteriors/YYYY-MM-DD.md` — mean, 5th/95th percentiles, model used, estimator, cycle context.

### Decision Points

- Posterior near a constraint (SOC ≤ 5% or ≥ 95%) → switch to truncated Gaussian or particle representation; Gaussian assumption is dishonest there.
- Innovation covariance > 3× expected → model mismatch; re-identify parameters before continuing.
- Two consecutive cycles with biased innovations → SOH update needed; capacity has moved.

## Workflow 3: ECMS Equivalence-Factor Tuning under Bayesian Update

**Goal:** Set and adapt the ECMS equivalence factor *s* such that expected fuel cost over the trip-length posterior is minimised, with charge sustainability respected in expectation.

### Steps

1. **Initialise *s*** from a coarse offline DP solution on representative cycles: choose the *s* that yields zero-net SOC change at end of typical CS-mode trip.
2. **Define the adaptation law.** A-ECMS variants: PI on SOC error, frequency-domain decomposition, or Kalman update on *s* itself given observed SOC trajectory. Pick one and document.
3. **Update *s* per segment** (e.g. every 30-60 s of driving): ingest current SOC error vs. reference, current trip-length posterior shift (route prediction), and current battery efficiency posterior; compute Δs.
4. **Bound Δs** to avoid oscillation — small absolute caps per step are safer than letting the adapter chase noise.
5. **Log per-segment (s, SOC, fuel rate)** for offline review.

### Decision Points

- If the adaptation oscillates → tighten Δs cap or lengthen segment.
- If *s* drifts out of [0.5×, 2×] of its DP-optimal value → trip-length prior is probably stale; refresh it.
- If charge sustainability fails consistently (net SOC down at trip end) → either *s* too low (favours electric) or terminal-cost weight needs raising.

## Workflow 4: MPC Horizon and Terminal-Cost Tuning

**Goal:** Choose MPC prediction horizon *N* and terminal-cost weight *Q_f* such that the controller's expected performance over the trip-length posterior matches DP within an acceptable gap, at acceptable compute cost.

### Steps

1. **Identify the cycle-time-scale** of the dominant disturbance (driver torque demand). Horizon should at minimum cover one full acceleration-cruise-deceleration triplet.
2. **Sweep N** (e.g. 5, 10, 20, 30 s) on a representative cycle ensemble; record fuel cost and per-step compute time.
3. **Sweep terminal-cost weight Q_f** for each N — controls how much the controller cares about end-of-horizon SOC vs. instantaneous cost.
4. **Pick N as the smallest** that gets within X% (e.g. 2%) of the largest-horizon fuel cost AND fits the embedded compute budget.
5. **Validate on out-of-sample cycles** — including cycles drawn from the *tails* of the trip-length posterior, not just the mean.

### Decision Points

- If compute exceeds budget → reduce horizon or switch to explicit MPC with offline-precomputed pieces.
- If fuel improvement plateaus quickly with N → terminal cost is doing the work; tune Q_f harder.
- If out-of-sample cycles show large regression → terminal cost is over-fit to in-sample trip lengths; widen the prior.

## Workflow 5: Cycle-Based Strategy Comparison

**Goal:** Compare two or more controller candidates fairly across standard cycles, with units that the certifier and the customer both recognise.

### Steps

1. **Fix vehicle parameters and battery state** identically across candidates — no controller comparison is honest with different starting SOC or temperature.
2. **Run each candidate** on the standard cycle suite (WLTP class 3b at minimum, plus regional cycles relevant to the launch market).
3. **For PHEV**, run charge-depleting and charge-sustaining phases separately; report both, plus the SAE J2841 utility-factor weighted result.
4. **Report per cycle**: fuel consumption (L/100km), CO₂ (g/km), net ΔSOC (%), peak motor / engine torque utilisation, and battery throughput (Ah).
5. **Tabulate side-by-side** in `outputs/strategy-comparison-<date>.md` — including which posteriors / priors each candidate assumes.

### Decision Points

- If results are within 1-2% of each other → noise of the simulation; rerun with different cycle phases or start SOC.
- If a "winner" depends entirely on a single cycle → it's not a winner, it's an overfit. Report the ensemble.
- If charge-sustaining is cheating (large negative ΔSOC) → re-equalise and rerun.

## Workflow 6: Pareto Frontier — Fuel vs. Battery Wear

**Goal:** Make the multi-objective trade-off between minimising fuel and minimising battery wear visible to stakeholders, instead of hiding it behind a single weighted-sum cost.

### Steps

1. **Define wear proxy.** Choices: throughput-based (Ah-equivalent), depth-of-discharge-weighted, or rainflow-counted equivalent full cycles. Document which.
2. **Sweep cost-function weights** between the fuel and wear terms (e.g. λ ∈ [0, 0.1, 0.5, 1, 2, 5, 10]).
3. **Run each** on the cycle ensemble; compute (fuel, wear) for each weight.
4. **Plot the Pareto frontier**; identify the knee.
5. **Pick a point on the frontier with stakeholders** — never in isolation. The choice depends on warranty period, electricity vs. fuel cost, customer use profile.

### Decision Points

- If the frontier is steep at the knee → small fuel concession buys large wear reduction; favour wear.
- If the frontier is flat → wear is decoupled from fuel in this regime; default to lowest fuel.
- If λ has to go very high to register on wear → the wear proxy is insensitive; pick a more discriminating proxy.
