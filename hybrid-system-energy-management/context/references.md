# Hybrid EMS — Reference Tables

Lookup data the agent reaches for during EMS design, calibration, and evaluation. Compact by design — defer to upstream sources for fuller specs.

## Standards and Regulations

| Standard | Scope | Notes |
|---|---|---|
| UN GTR No. 15 / WLTP | Global light-duty test procedure | WLTC class 3b is the workhorse cycle for HEV/PHEV homologation |
| UN GTR No. 22 / WLTP-PHEV | PHEV-specific procedure | Defines charge-depleting vs charge-sustaining and utility factor |
| GB 18352.6 / CLTC-P | China light-duty | Replaces NEDC for China since 2020 |
| EPA FTP-75 / SFTP / HWFET | US light-duty | "5-cycle" composite for window-sticker label |
| SAE J1711 | HEV measurement procedures | OEM/lab procedures for charge-sustaining and charge-depleting |
| SAE J2841 | PHEV utility factor | Maps trip distance distribution → real-world weighting |
| ISO 26262 | Functional safety, road vehicles | ASIL decomposition guides where Bayesian advisory layers fit |
| ISO 21434 | Cybersecurity for road vehicles | Relevant when EMS consumes cloud-route or telematics priors |
| UN R100 | Electric powertrain safety | Battery and HV-system requirements |
| ISO 12405 / IEC 62660 | Battery testing | Used to populate priors for SOH and capacity-fade models |

## Datasets and Drive-Cycle Sources

| Source | What's there | Useful for |
|---|---|---|
| **EPA Dynamometer Drive Schedules** (epa.gov/vehicle-and-fuel-emissions-testing) | FTP-75, HWFET, US06, SC03, cold-FTP traces | Reference cycles, time-series CSV |
| **DieselNet emissions cycles archive** | NEDC, WLTC, CLTC, ARTEMIS, JC08 | Region-by-region cycle library |
| **NREL FleetDNA / Fleet DNA** (nrel.gov/transportation/fleettest-fleet-dna.html) | Real-world commercial vehicle drive cycles | Building empirical priors over driver class |
| **NREL Drive-Cycle Analysis Tool (DriveCAT)** | Vocational duty cycles | Prior over urban-delivery, transit, refuse routes |
| **Argonne D3 (Downloadable Dynamometer Database)** | Vehicle test results, second-by-second logs | Calibration ground truth for hybrid models |
| **NASA Battery Aging Datasets (Prognostics CoE)** | 18650 cells under various cycling regimes | SOH model calibration, Bayesian aging priors |
| **CALCE Battery Datasets (UMD)** | Cell-level capacity and impedance over life | Particle-filter SOH estimator priors |

## Tooling

| Tool | Role | Notes |
|---|---|---|
| MATLAB / Simulink | DSP, control synthesis, plant modelling | De-facto for OEM EMS work; Powertrain Blockset and Stateflow |
| Autonomie (Argonne National Lab) | Vehicle-system simulation, EMS benchmarking | Open-licence; large vehicle library |
| GT-SUITE | Engine + driveline + thermal co-sim | Industry standard for predictive plant models |
| AVL Cruise M | System-level vehicle simulation | Strong on hybrid architectures and HiL |
| Dymola / OpenModelica | Modelica-based multi-physics | Useful for DFN-class battery models |
| FASTSim (NREL) | Lightweight Python vehicle simulator | Open-source; fast first-pass studies |
| CarMaker / VTD | Driver-in-the-loop, virtual proving ground | When driver behaviour priors need closed-loop validation |
| Stan / PyMC / NumPyro | Probabilistic programming | Hierarchical Bayesian fits for trip and aging models |
| Filterpy / pykalman | Python KF / UKF / particle filters | Online state estimation prototypes |

## Foundational Papers and Books

- Sciarretta & Guzzella, *Vehicle Propulsion Systems*, Springer (3rd ed.) — canonical EMS reference; ECMS, PMP, DP framings.
- Onori, Serrao & Rizzoni, *Hybrid Electric Vehicles: Energy Management Strategies*, Springer — modern survey including A-ECMS and stochastic methods.
- Plett, *Battery Management Systems Vol. I & II*, Artech — definitive reference on equivalent-circuit models, SOC/SOH estimation, EKF/UKF derivations.
- Murphy, *Probabilistic Machine Learning: Advanced Topics*, MIT Press — Bayesian state-space models, sequential Monte Carlo, used here as the Bayesian foundation.
- Borrelli, Bemporad & Morari, *Predictive Control for Linear and Hybrid Systems*, CUP — MPC with explicit constraint handling, foundational for receding-horizon EMS.

## Standard Reporting Conventions

| Quantity | Units | Convention |
|---|---|---|
| Fuel economy | L/100 km (EU), MPG (US), MPGe (US PHEV) | Always state the cycle |
| Equivalent CO₂ | g/km (EU), g/mi (US) | WTW and TTW differ — say which |
| SOC | % of usable capacity, *or* kWh available | Define the window (e.g. 20–80% usable) |
| Battery aging | % capacity remaining, % resistance growth | Reference temperature mandatory |
| Energy consumption | Wh/km (EV mode), MJ/km (energy total) | Don't quote without temperature, payload, HVAC state |

## Online Catalogues and Communities

- ANL / DOE Vehicle Technologies Office reports — open-access EMS and battery research.
- IEEE VPPC and IFAC AAC proceedings — yearly conferences on vehicle propulsion control.
- SAE WCX / SAE Hybrid & EV symposium proceedings — industry-side calibration practice.
- battery-prognostics community on GitHub — open implementations of UKF/PF SOC/SOH estimators.

## Bayesian Workflow Cheat-Sheet for EMS

1. **Specify** the prior — driver class, route, parameters, SOH — with explicit distributional families and hyperpriors.
2. **Generate** synthetic data and run prior predictive checks before touching real telemetry.
3. **Condition** on data with the appropriate algorithm (UKF / particle filter for state, MCMC / VI for offline parameter posteriors).
4. **Diagnose** — trace plots, R-hat, ESS, posterior predictive checks. Reject silently-fitting models.
5. **Decide** with credible intervals, not point estimates. Quantify the cost of overconfidence.
6. **Update** as new fleet / vehicle data arrives — the prior for the next vehicle is the posterior of the current cohort.
