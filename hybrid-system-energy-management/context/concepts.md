# Hybrid System Energy Management — Working Concepts

Background the agent should read before acting on EMS design, calibration, or evaluation tasks. Optimised for fast recall, not exhaustive theory.

## Hybrid Powertrain Architectures

| Architecture | Power flow | Examples | Trade-off |
|---|---|---|---|
| **Series** | ICE → generator → battery/inverter → motor → wheels | BMW i3 REx, older Chevrolet Volt (EREV) | ICE decoupled from wheels; great urban efficiency, double conversion losses on highway |
| **Parallel** | ICE and motor both drive wheels through transmission | Honda IMA, BMW xDrive40e | Mechanically simpler, but ICE always tied to road speed |
| **Power-split** | Planetary gearset blends ICE + 2 e-machines | Toyota HSD (Prius), Ford eCVT, Lexus Multi-Stage | eCVT lets ICE sit near sweet-spot; control complexity high |
| **P0–P4 (parallel sub-types)** | Motor position relative to engine and gearbox | P0 = belt-start-generator; P2 = between engine and gearbox; P4 = on the rear axle | Determines regen capability and engine-off coast behaviour |

PHEV adds a larger battery and on-board charger to a parallel/split base. MHEV is typically 48 V P0/P1 (BSG/ISG) with a small Li-ion pack — assistive only, no full EV mode.

## Energy-Management Strategies (EMS)

| Family | Idea | Strengths | Weaknesses |
|---|---|---|---|
| **Rule-based / heuristic** | Lookup tables on (speed, torque demand, SOC, state) | Deterministic, certifiable, fast | Hand-tuned, brittle off-cycle |
| **ECMS** | Equivalent Consumption Minimisation — convert electrical use to a virtual fuel cost via equivalence factor *s* | Near-optimal when *s* is right | *s* depends on future trip; needs adaptation (A-ECMS) |
| **Dynamic Programming (DP)** | Bellman backward pass over discretised SOC × time | Globally optimal benchmark | Offline only; needs known cycle |
| **Pontryagin's Minimum Principle (PMP)** | Continuous-time optimality with co-state λ | Analytical insight, lighter than DP | λ is the integration constant — needs estimation if cycle unknown |
| **Model Predictive Control (MPC)** | Roll a finite-horizon optimisation each step | Handles constraints, naturally accommodates forecasts | Compute load; tuning of horizon and weights non-trivial |
| **Reinforcement Learning** | Learn policy over states from reward (fuel + wear) | Generalises to distributions | Sample-hungry; safety/explainability concerns for production |
| **Stochastic DP / Robust MPC** | Optimise expected cost over a stochastic disturbance model | Naturally Bayesian — fits today's framing | Requires a credible distribution over disturbances |

## Bayesian Framing — Where Probabilities Live in EMS

EMS is a sequential decision under uncertainty. Bayes shows up at four well-defined surfaces:

1. **State estimation.** Battery SOC, SOH, internal temperatures, and resistance are not directly measured — they are inferred from current/voltage/temperature with sensor noise. Use **EKF / UKF** for unimodal posteriors over Thevenin-circuit parameters; **particle filters** when the posterior is multi-modal (e.g. multi-cell mismatch, capacity fade regime change).
2. **Disturbance / driver intention.** Future torque demand is the dominant unknown for any predictive controller. Build a posterior over the next *N*-second torque trajectory using a hierarchical model: prior over driver class (calm / sport / urban-stop-go), updated by recent pedal/brake history. Markov-chain models conditioned on speed band are a common discretisation.
3. **Route / trip prediction.** GPS + map prior + recent trips → posterior over remaining trip energy, elevation profile, and stop frequency. This drives the equivalence factor *s* in A-ECMS and the SOC reference in MPC's terminal cost.
4. **Parameter / model uncertainty.** Calibration coefficients (engine BSFC map scaling, motor efficiency map, battery capacity at age *t*) drift over the vehicle's life. Maintain posteriors and propagate them through the controller — credible-interval-aware decisions avoid the optimiser exploiting overconfident parameters.

### Aleatoric vs. epistemic uncertainty (don't conflate them)

- **Aleatoric** — irreducible randomness in driver/road behaviour. Cannot be reduced by more data; mitigated by chance-constrained / robust controllers.
- **Epistemic** — model or parameter ignorance. Reduced by data; mitigated by Bayesian updating and active learning.

A robust MPC that hedges against aleatoric variance with a margin tuned for epistemic uncertainty is leaving fuel on the table; the inverse over-trusts the model.

## Key States and Signals

| Signal | Source | Typical sample rate | Notes |
|---|---|---|---|
| Vehicle speed | Wheel speed sensor / CAN | 100 Hz | Filtered for noise |
| Pedal positions | APP / BPP sensors | 100 Hz | Driver intent input |
| Engine torque | Estimated by ECU model | 50–100 Hz | Inferred, not measured directly |
| Battery V/I | BMS | 10–100 Hz | Anti-aliased before SOC estimator |
| Pack temperature(s) | NTC / thermistors | 1–10 Hz | Critical for power limits |
| GPS / map data | Telematics | 1 Hz | Used for route prediction |
| Inverter DC bus V/I | Inverter MCU | 1–10 kHz internally; 100 Hz on CAN | Power flow accounting |

## Battery Models (depth → cost)

| Model | Form | Use case |
|---|---|---|
| **SOC-OCV table** | Static lookup `OCV = f(SOC, T)` | Fast online estimator |
| **Rint / Thevenin** | OCV with one or two RC pairs | Classic for UKF SOC estimation |
| **Single Particle Model (SPM)** | Solid-state Li diffusion + Butler-Volmer | Onboard SOH estimation |
| **Doyle–Fuller–Newman (DFN)** | Full pseudo-2D electrochemistry | Offline calibration / aging studies, not real-time |

Pair the chosen model with an estimator: UKF is the workhorse for Thevenin; particle filters or moving-horizon estimators for nonlinear electrochemistry.

## Validation Cycles and Why They Differ

| Cycle | Region | Profile shape | Catch |
|---|---|---|---|
| WLTP class 3b | EU / global | 1800 s, 4 phases, peaks ~131 km/h | Charge-sustaining mode tested at multiple SOC start points |
| CLTC-P | China | 1800 s, urban-heavy, lower top speed | Higher idle fraction → flatters HEVs |
| FTP-75 | US | 1874 s, hot/cold start | Cold-start hit dominates HEV result |
| HWFET | US | Gentle 765 s highway loop | ICE-dominated; HEV gain modest |
| ARTEMIS Urban / Road / Motorway | EU research | More transient than WLTP | Better proxy for real-world variability |

Charge-depleting (CD) vs. charge-sustaining (CS) reporting matters for PHEV utility-factor calculations (SAE J2841).

## Common Pitfalls

- Reporting fuel economy without naming the cycle — context-free numbers.
- Optimising on a deterministic cycle and assuming generality — real driving has wide variance.
- Using a Gaussian posterior for SOC near 0% or 100% — the constraint cuts the tail; truncated or particle representations are more honest.
- Ignoring battery wear in the cost function — short-horizon fuel optimum can hammer the pack via deep cycling.
- Mixing PHEV utility factor and CS-mode efficiency in the same headline number.
- Assuming MPC's prediction horizon is "long enough" without checking what fraction of trips it covers — the terminal-cost design carries the rest.

## Resource-Optimisation Patterns Familiar in EMS

These are the EMS-domain analogues of the "scarce-time vs. large-search-space" patterns common across this workspace family:

- **Equivalence factor adaptation.** Treat *s* in ECMS as a Bayesian estimate updated each segment; trip-prediction posterior shifts the prior.
- **Receding-horizon with scenario tree.** Sample *K* future-disturbance trajectories from the posterior; solve a stochastic MPC.
- **Information-theoretic sensor scheduling.** Prefer measurements (e.g. EIS pulses) that maximise expected information gain on SOH posterior — pay only when it pays back.
- **Pareto frontier of fuel vs. wear vs. NVH.** Multi-objective; do not collapse to a single weighted sum without showing the frontier.

## Operating constraints

- Production EMS must satisfy **functional safety (ISO 26262)** — controller hooks for limp-home and torque limiting are non-negotiable. Bayesian layers run *advisory* to a safety-rated supervisor.
- Emissions calibration is a **regulated artefact** — do not propose changes that shift CS-mode operation outside the certified envelope without a formal recalibration plan.
- Battery thermal and power limits from the BMS are hard constraints; the EMS proposes, the BMS disposes.
