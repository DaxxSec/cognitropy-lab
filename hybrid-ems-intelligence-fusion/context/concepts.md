# Hybrid EMS — Multi-Source Intelligence Fusion: Core Concepts

Background the agent should read before acting on tasks in this workspace. Calibrated for fast recall, not exhaustive theory.

## Hybrid Powertrain Architectures

The energy-management problem is shaped by the architecture; an EMS strategy that works on a series hybrid is rarely transferable to a power-split hybrid without re-design.

| Architecture | Engine ↔ Wheels Coupling | EMS Decision Surface | Typical Vehicle |
|---|---|---|---|
| **Series (REEV / extended-range EV)** | Engine drives generator only; wheels always electric. | When + how hard to run the engine as a generator; SOC reference trajectory. | BMW i3 REx, early Chevy Volt (mostly). |
| **Parallel (P0–P4)** | Engine and motor can both drive wheels. P0=BSG belt, P1=crank-attached, P2=between engine and gearbox, P3=on gearbox output, P4=on driven axle. | Torque split between engine and motor; clutch state; gear selection. | Honda IMA, many P2 mild/full hybrids. |
| **Power-Split (eCVT)** | Engine, motor, generator coupled via planetary gear set; mechanical and electric paths simultaneously possible. | Engine speed/torque set point; motor and generator currents; mode (input-split vs. compound-split). | Toyota Hybrid System (Prius), Ford PowerSplit. |
| **Mild Hybrid (MHEV, 48V)** | Small BSG/ISG only; cannot drive vehicle alone. | Boost/regen amplitude; start/stop policy. | Audi A6 48V, Mercedes EQ Boost. |
| **PHEV (any of above + larger battery)** | As above, but with grid-charging and meaningful all-electric range. | All of above + CD/CS scheduling along route. | Toyota RAV4 Prime, BMW 330e. |

## EMS Strategy Taxonomy

EMS strategies cluster by where they sit on the **online ↔ offline** and **rule-based ↔ optimisation-based** axes.

### Rule-Based / Heuristic
Engine-on threshold + load-following + SOC deadbands. Fast, calibratable, transparent. Loses 5–15% vs. optimal on most cycles. Production-default for cost-sensitive vehicles.

### Equivalent Consumption Minimisation Strategy (ECMS)
Convert battery energy use to an equivalent fuel consumption via an **equivalence factor** `s_eq`. Minimise the instantaneous Hamiltonian
`H(t) = m_dot_fuel(t) + s_eq · P_batt(t)`
over the powertrain mode at each step. Real-time, near-optimal if `s_eq` is set well.

### Adaptive ECMS (A-ECMS)
ECMS with `s_eq` adapted online from horizon information. The fusion stack's primary product is exactly this `s_eq` schedule.

### Model Predictive Control (MPC)
Solve a finite-horizon optimisation at each control step. Variants:

- **Deterministic MPC** — uses the mean horizon prediction.
- **Robust MPC** — guarantees performance under worst-case bounded uncertainty.
- **Stochastic MPC** — explicit scenario tree or chance constraints.
- **Tube MPC** — nominal trajectory + ancillary controller within a tube of disturbances.

### Dynamic Programming (DP)
Offline, given the full cycle in advance. Bellman backward recursion over the SOC grid. Yields the global optimum. Used as benchmark, never as production controller.

### Reinforcement Learning
Train a policy `π(s) → u` on simulator + real drives. Strengths: handles complex state representations (e.g. fused horizon priors). Weaknesses: sim-to-real gap, distributional shift, hard certification path. Mostly research-grade for production.

## Multi-Source Intelligence Fusion: The Fusion Stack

Fusion in this workspace = **probabilistic combination of asynchronous, heterogeneous, partially-reliable predictions of future driving conditions**. Not the same as classical sensor fusion for perception (which estimates current state); here we are predicting an external disturbance trajectory.

### Source Taxonomy

| Class | Examples | Update Period | Typical TTL | Notes |
|---|---|---|---|---|
| **Static maps** | Road class, posted speed, curvature, lane count | One-time / monthly | n/a | Trust very high once vetted. |
| **Topographic** | OSM SRTM elevation, HD-map elevation | One-time / quarterly | n/a | HD-map > SRTM; SRTM canopy bias in forested terrain. |
| **Live routing** | Cloud-routed traffic, ETA | 30–60 s | 5 min | Coverage degrades in fringe regions. |
| **Vehicle-to-X (V2X)** | J2735 BSM, SPaT, MAP, RTCM | 10–100 Hz | 200 ms – 2 s | Adversarial input — see security note. |
| **Weather** | Wind vector, ambient T, precipitation, humidity | 10 min – 1 h | 30 min | Major impact via aero (wind) and aux (HVAC). |
| **Driver model** | Style fingerprint, predicted speed profile | Per-trip | n/a | Sticky; updates with EWMA. |
| **Telematics history** | Per-route historical mean speed | Per drive | 6 months | Useful baseline; degrades with seasonality. |
| **Fleet learning** | Aggregated per-corridor priors from fleet | Daily | 1 month | Anonymised, privacy-controlled. |
| **On-board CAN** | Vehicle speed, accelerator/brake pedal, gear, SOC, T | 10–100 Hz | n/a | Ground truth for state; not for forecast. |

### Fusion Algorithms

- **Inverse-variance weighting** — when sources are zero-bias Gaussian, optimal in MSE. Sensitive to mis-stated variance.
- **Bayesian model averaging** — weights sources by posterior probability of being correct. Costlier; needs offline calibration.
- **Robust fusion** — Huber loss, M-estimators, RANSAC-style consensus; tolerates outliers.
- **Covariance Intersection** — combines two estimates with unknown cross-correlation conservatively. Use when sources share upstream feeds.
- **Particle filter / sequential Monte Carlo** — multi-modal posteriors, non-Gaussian noise; expensive but most flexible.
- **Federated Kalman filter** — distributed fusion with local + global filters; useful for partial-coverage source feeds.

### Trust-Weight Update

Trust weights `w_i` for source `i` evolve from per-drive audits:

`w_i_new = (1 − α) · w_i_old + α · w_i_audited`

with `α ∈ [0.1, 0.3]` (one drive should not dominate). Audit weight `w_i_audited` derives from inverse RMS, capped to keep any single source from going to 0 or 1.

### Calibration vs. Bias

Two independent failure modes:

- **Bias** — `E[μ_i − truth] ≠ 0`. Source is systematically off. Recoverable by calibration.
- **Calibration error** — `P(truth ∈ μ_i ± σ_i) ≠ 0.68`. Source mis-states its own uncertainty. Recoverable by re-tuning σ.

A well-calibrated biased source is more usable than a mis-calibrated unbiased one — you can subtract bias, but you cannot recover the right variance.

## Uncertainty Taxonomy

- **Aleatoric** — irreducible randomness (driver inattention, traffic noise). Mitigation: robust control, hedging.
- **Epistemic** — model / parameter ignorance. Mitigation: better data, better fusion, more diverse sources.
- **Source-noise** — within-source variance. Affects credible bands but not arbitration.
- **Source-disagreement** — between-source variance. Affects arbitration and may indicate fault.

Every emitted credible band must tag which class dominates — different downstream mitigations apply.

## Common Failure Modes

- **Silent equal-vote averaging.** Inverse-variance weight without per-source variance estimation collapses to mean; loses the whole point of trust budgets.
- **Coordinated stale sources.** If two feeds share a cloud upstream, both can be stale together — gating fails to fire because they agree.
- **Optimistic cold-start prediction.** Engine warm-up power offsets are routinely under-modeled, biasing early-trip priors low.
- **Drift in driver-style fingerprint after a vehicle handover.** Pickup time goes wrong when the same vehicle has multiple drivers and fingerprint isn't keyed to identity.
- **Battery capability envelope ignored in strategy.** Producing infeasible torque splits the controller silently saturates.
- **Equivalence factor frozen.** A-ECMS with a static `s_eq` is just ECMS with extra steps and worse traceability.
- **V2X treated as authoritative.** Adversarial / spoofed V2X is a known attack vector — always corroborate with on-board sensors before letting V2X drive a power decision.

## Operating Constraints

- **Functional safety (ISO 26262).** EMS function chains have ASIL classifications; modifying any element of the chain requires re-running hazard analysis. The fusion layer is part of the chain.
- **Cybersecurity (UN R155 / ISO/SAE 21434).** External-data sources are attack surface. Default assumption is intermittently-malicious V2X / cloud traffic / weather feeds.
- **Type approval (WLTP, RDE, CLTC-P).** Changes that affect engine on/off scheduling, EAT temperature, fuel/electric energy partitioning may require re-certification.
- **Data privacy (GDPR / CCPA / KVKK / PIPEDA / LGPD).** GPS, driver fingerprints, behavioural data are personal data. Anonymise before fleet aggregation; document retention policy.
- **OBD / regulated diagnostics.** EMS faults must be observable through OBD per regional regulations (J1979, ISO 15031); fusion-layer faults need an OBD path.
- **HIL/SIL gating.** Real-vehicle control changes only after Software-in-the-Loop and Hardware-in-the-Loop validation. The agent's role is upstream — it informs, never directly writes calibrations.
