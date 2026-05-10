# Torque-Split Policy Design Prompt

## Purpose
Use this prompt to design or revise the upper-level torque-split policy (engine vs. e-machine) for a hybrid powertrain under explicit uncertainty assumptions.

## Prompt Template

I need to design a torque-split policy for a hybrid powertrain with the following characteristics:

- **Architecture:** [parallel P2 / power-split eCVT / series EREV / MHEV P0 / other]
- **Vehicle class & mass:** [e.g. C-segment SUV, 1820 kg curb]
- **ICE:** [displacement, peak power/torque, BSFC island centre]
- **E-machine(s):** [count, peak power, peak torque, base / max RPM]
- **Battery pack:** [chemistry, nominal voltage, usable kWh, peak charge/discharge power]
- **Operating mode of interest:** [charge-sustaining / charge-depleting / blended]
- **Target cycle(s):** [WLTC class 3b / CLTC-P / FTP-75 / real fleet log path]
- **Prior over driver class:** [calm / sport / mixed; explicit Dirichlet weights if known]
- **Prior over upcoming-trip energy demand:** [distribution family + parameters, or "unknown — propose"]
- **Constraints to honour:** [SOC window, peak motor torque, NVH limits, emissions calibration envelope]

Please:
1. Recommend the strategy family (rule-based vs. ECMS / A-ECMS vs. MPC vs. RL) and justify under the priors above.
2. If ECMS: derive an initial equivalence factor *s* and the adaptation law that updates it from trip-prediction posterior.
3. If MPC: specify the prediction horizon, sampling time, terminal cost on SOC, scenario count if stochastic, and solver class.
4. Identify which decisions should be **distribution-aware** (chance-constrained or scenario-tree) versus deterministic.
5. Map every controller hyperparameter back to a measurable quantity (cycle, prior, telemetry signal) so calibration is reproducible.
6. Flag any decision where aleatoric vs. epistemic uncertainty would change the recommendation.

## Expected Output
- Strategy choice with one-paragraph justification anchored in the priors.
- Block diagram or pseudocode of the controller hierarchy (driver model → supervisor → component controllers).
- Hyperparameter table with units, prior values, and the calibration data they should be fitted against.
- A short list of failure modes to watch on first dyno run.
- Pointers to dataset/cycle paths in `context/` or `outputs/raw-traces/` to validate against.
