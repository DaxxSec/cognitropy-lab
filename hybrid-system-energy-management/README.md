# Hybrid System Energy Management Workspace

> A Claude Code workspace for designing and tuning energy-management strategies (EMS) for hybrid electric powertrains — HEV, PHEV, and MHEV — across parallel, series, and power-split architectures, framed throughout as **Bayesian probability assessment**.

## What This Workspace Does

This workspace turns hybrid powertrain analysis into a structured, repeatable controller-design lab. Rather than ad-hoc rule tuning, it treats every controller decision (torque split, mode arbitration, SOC target shaping) as a posterior under explicit priors over driver intention, route load, battery state-of-health, and model parameters.

The agent guides the full EMS design cycle: prior elicitation, posterior updates from telemetry (UKF / particle filters / moving-horizon estimators), strategy comparison against optimal benchmarks (DP, PMP), online controller selection (rule-based, ECMS / A-ECMS, MPC, RL), validation across standard cycles (WLTP, CLTC, FTP-75, HWFET, ARTEMIS), and Pareto-aware trade-offs between fuel economy, battery wear, and NVH.

## Why This Workspace Exists

EMS work spans control theory, electrochemistry, embedded software, regulatory certification, and fleet data analysis — and most "hybrid efficiency" claims are made without naming the cycle, the prior, or the cost weights. This workspace codifies a discipline: every strategy proposal is paired with the prior it assumes, the posterior it produces, and the cycle/dataset it was evaluated on. Bayesian framing makes the assumptions visible, which is what makes results comparable.

## Getting Started

### Prerequisites

- A simulator: MATLAB/Simulink + Powertrain Blockset, Autonomie (ANL), GT-SUITE, AVL Cruise M, or open-source FASTSim.
- Vehicle parameter sheet (engine BSFC map, motor efficiency map, battery OCV-SOC table, transmission ratios, vehicle mass / drag).
- One or more drive-cycle traces (WLTP class 3b, CLTC-P, FTP-75, or measured fleet telemetry).
- Optional: a controller prototyping environment (Simulink Stateflow, Python with `cvxpy` or `do-mpc`).
- Conceptual familiarity with state estimation (Kalman / UKF / particle), MPC, and basic vehicle longitudinal dynamics.

### Quick Start

1. Clone this workspace.
2. Drop drive-cycle traces and the vehicle parameter sheet into `context/` (or `outputs/raw-traces/`).
3. Run `/torque-split-design` to draft a baseline rule-based or ECMS policy with explicit priors.
4. Run `/cycle-evaluate` to benchmark the baseline against WLTP/CLTC/FTP-75.
5. Run `/posterior-update` to refresh battery SOH and driver-intention posteriors from any telemetry available.
6. Iterate: `/ecms-tune` or `/mpc-horizon-tune` to improve, then `/wear-vs-fuel-pareto` to see the trade-off frontier.

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/torque-split-design` | Baseline torque-split policy (rule-based or ECMS) with prior-over-driver framing | First pass on a new vehicle / architecture |
| `/soc-trajectory-plan` | Plan SOC reference trajectory for a known route (PHEV utility factor + CS phase) | Route-aware PHEV calibration |
| `/posterior-update` | Update battery SOH/capacity or driver-intention posteriors from telemetry | After ingesting new fleet data |
| `/cycle-evaluate` | Benchmark the controller against standard cycles, report fuel/emissions/SOC | Comparing strategies; certification dry-run |
| `/ecms-tune` | Tune the ECMS equivalence factor *s* (or A-ECMS adaptation law) | When the baseline ECMS underperforms off-cycle |
| `/mpc-horizon-tune` | Pick MPC prediction horizon + terminal cost weights from a trip-length posterior | Moving from rule-based to predictive control |
| `/wear-vs-fuel-pareto` | Compute Pareto frontier of fuel consumption vs. battery wear over a cycle ensemble | Multi-objective trade-off conversations |

## Directory Structure

```
hybrid-system-energy-management/
├── CLAUDE.md                                    # Agent role, context refs, command list
├── README.md                                    # This file
├── .claude/commands/
│   ├── torque-split-design.md
│   ├── soc-trajectory-plan.md
│   ├── posterior-update.md
│   ├── cycle-evaluate.md
│   ├── ecms-tune.md
│   ├── mpc-horizon-tune.md
│   └── wear-vs-fuel-pareto.md
├── context/
│   ├── concepts.md                              # Architectures, EMS strategy families, Bayesian framing, battery models
│   ├── workflows.md                             # Step-by-step procedures tied to today's Bayesian technique
│   └── references.md                            # Standards, datasets, tools, EMS strategy comparison
├── prompts/
│   ├── bayesian-soc-soh-estimation.md
│   ├── drive-cycle-strategy-evaluation.md
│   ├── mpc-tuning-under-uncertainty.md
│   └── torque-split-policy-design.md
└── outputs/                                     # Tuned controllers, posterior reports, Pareto plots, sim logs
```

## Example Use Cases

### PHEV controller calibration for a new model year
Build a baseline ECMS policy, calibrate the equivalence factor against WLTP charge-sustaining and FTP-75 cold-start cycles, then layer route-aware MPC on top once map/GPS data is wired in. Bayesian update of *s* between segments keeps off-cycle performance from drifting.

### Battery prognostics integration with EMS
Replace a static SOC-OCV table with a Thevenin model + UKF, route the SOH posterior into the EMS cost function so deep-discharge cycling is penalised as the pack ages. Validate that warranty-period fuel economy does not regress.

### Fleet-data-driven driver-intention prior
Mine telematics for pedal/brake patterns by trip class (urban / highway / mixed), fit a hierarchical posterior, and feed the trip-class posterior into the controller's torque-demand prediction. Quantify the fuel benefit vs. a class-agnostic baseline.

### Regulatory dry-run before homologation
Run the candidate controller through the regulator's exact cycle (WLTP class 3b for EU, FTP-75 + HWFET for US, CLTC-P for China) at the prescribed start-SOC/temperature combinations; report the certified fuel consumption with confidence intervals reflecting the controller's posterior.

### Comparing rule-based vs. MPC vs. RL on the same vehicle
Use Dynamic Programming as the offline benchmark, ECMS as the conventional online floor, MPC as the predictive challenger, and a constrained-RL policy as the experimental ceiling. Report each on the same Pareto axes (fuel vs. wear vs. NVH) instead of single-number "fuel economy."

## Recommended MCP Servers

- **filesystem** — for reading drive-cycle CSVs, vehicle parameter sheets, and writing simulation logs.
- **shell** — for invoking simulators (`matlab`, `python -m fastsim`, `cruise_m_runner`) and post-processing scripts.
- **python** — for custom Bayesian estimators (`pymc`, `numpyro`, `filterpy`), MPC (`do-mpc`, `cvxpy`), and Pareto-front analysis.
- **sqlite** or **duckdb** — for querying multi-trip telematics datasets to fit driver-intention priors.

## Legal & Ethical Considerations

- **Functional safety:** Production EMS must satisfy ISO 26262. Bayesian / learned components run *advisory* to a safety-rated supervisor; the supervisor enforces torque limits and limp-home behaviour.
- **Emissions certification:** Do not propose changes that shift CS-mode operation outside the certified envelope without a formal recalibration plan. The "Volkswagen Defeat Device" precedent applies — controller behaviour must be representative across the full operating envelope, not just on the certification cycle.
- **OEM IP boundaries:** Internal calibration data, BSFC maps, and motor efficiency maps are typically proprietary. Treat any non-public material as confidential; do not export to third-party cloud APIs without authorisation.

## Technical References

- [SAE J1711 — Recommended Practice for Measuring the Exhaust Emissions and Fuel Economy of Hybrid-Electric Vehicles](https://www.sae.org/standards/content/j1711_202303/) — the foundational HEV measurement standard.
- [SAE J2841 — Utility Factor Definitions for PHEVs](https://www.sae.org/standards/content/j2841_201009/) — defines CD vs. CS mode reporting.
- [WLTP Regulation (EU) 2017/1151](https://eur-lex.europa.eu/eli/reg/2017/1151) — global Worldwide Light Vehicle Test Procedure.
- [Argonne National Lab — Autonomie](https://www.autonomie.net/) — vehicle simulation toolchain widely used for EMS prototyping.
- [NREL FASTSim](https://www.nrel.gov/transportation/fastsim.html) — open-source vehicle dynamics + EMS simulator.
- [Sciarretta & Guzzella, *Vehicle Propulsion Systems*](https://link.springer.com/book/10.1007/978-3-642-35913-2) — canonical EMS textbook (ECMS / PMP / DP derivations).
- [Doyle, Fuller & Newman, *Modeling of Galvanostatic Charge and Discharge of the Lithium / Polymer / Insertion Cell* (1993)](https://iopscience.iop.org/article/10.1149/1.2221597) — the DFN battery model.
- [Plett, *Battery Management Systems Vol. 1 & 2*](https://artechhouse.com/Battery-Management-Systems-Volume-I-P2087.aspx) — practical EKF/UKF for SOC estimation.

## Optional plugin

If you have the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, additional global commands (`/workspace-foundational:context-sweep`, `/workspace-foundational:find-template`) are available. The workspace is self-contained without it.
