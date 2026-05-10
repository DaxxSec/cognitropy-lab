# MPC Tuning Under Uncertainty Prompt

## Purpose
Use this prompt when calibrating a model-predictive-control (MPC) supervisor that consumes Bayesian forecasts of driver demand, route load, and parameter posteriors.

## Prompt Template

I'm tuning an MPC supervisor for hybrid energy management with the following structure:

- **Plant model used inside MPC:** [linearised at operating point / quasi-static / nonlinear with sequential QP]
- **Decision variables:** [e.g. ICE torque split fraction, e-machine torque, gear, mode]
- **Prediction horizon Np:** [seconds, with sample time Ts]
- **Forecast inputs:**
  - Future torque demand: [posterior source — driver-class HMM, telematics, none]
  - Future road grade / speed: [map prior, none]
  - Future SOC of charge availability: [grid-aware? plug-in scheduling?]
- **Stochastic handling:** [deterministic / scenario tree (K scenarios) / chance-constrained / robust min-max]
- **Cost-function terms:** [fuel, electrical equivalence, battery aging, NVH, mode-change penalty, terminal SOC]
- **Hard constraints:** [SOC window, motor torque limit, BMS power limit, emissions calibration envelope]
- **Compute budget:** [target solve time per step, ECU/HiL platform]

Please:
1. Recommend horizon and sample time given the disturbance autocorrelation and compute budget — quote the rule used (e.g. cover one mode-change time-constant; horizon ≥ 3× longest closed-loop time constant).
2. Decide which forecast inputs need full posterior treatment vs. point estimate, and justify by sensitivity to that input's variance.
3. Set the cost weights with a procedure, not a guess: scaling each term by its expected magnitude and tuning by Pareto walk on a representative cycle.
4. Specify the terminal cost on SOC consistent with the trip-end posterior — both for charge-sustaining and charge-depleting operation.
5. Define safety fallbacks: when does MPC defer to the rule-based limp policy? Which infeasibility modes should trigger this?
6. Define the validation gauntlet: nominal cycle, perturbed cycle (driver class shifted), cold-start, low-SOC start, fault-injection (sensor dropout, parameter mis-estimation).

## Expected Output
- Horizon, sample time, and solver class with one-paragraph rationale.
- Cost-function expression with weights and the unit-balancing argument.
- Constraint tightening recipe for the chance-constrained / robust formulation, including the confidence level and where it came from.
- A tuning checklist the calibration engineer can execute without re-deriving the formulation.
- A risk matrix: failure mode × severity × proposed test that exposes it before production calibration.
