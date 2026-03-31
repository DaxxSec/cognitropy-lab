# Pipe Network — Probabilistic Pipe Network Analysis

Design or evaluate pipe network hydraulics with Monte Carlo simulation to quantify reliability under demand and roughness uncertainty.

## Required Inputs
1. **Network definition** — EPANET .inp file, or node/pipe tables with:
   - Nodes: ID, elevation, base demand
   - Pipes: ID, start/end node, length, diameter, material, age
2. **Demand variability** — Peaking factors, diurnal patterns, or demand distributions per node
3. **Performance criteria** — Minimum pressure (e.g., 20 psi at all nodes), maximum velocity

## Analysis Steps
1. Import network model (EPANET .inp or build from tables via WNTR)
2. Define demand uncertainty: log-normal or normal distributions per node from billing/metering data
3. Define roughness uncertainty: age-dependent Hazen-Williams C distributions
4. Monte Carlo sampling: N=1000+ scenarios (Latin Hypercube for efficiency)
5. Hydraulic solve each scenario via WNTR/EPANET
6. Calculate reliability metrics:
   - P(pressure < minimum) at each node
   - P(velocity > maximum) in each pipe
   - System reliability = P(all criteria met simultaneously)
7. Identify critical components: pipes whose roughness most affects system reliability
8. Optional: evaluate upgrade scenarios (pipe replacement, booster pumps)

## Output Artifacts
- `outputs/pipe-network/reliability_map.png` — Spatial reliability visualization
- `outputs/pipe-network/critical_pipes.csv` — Ranked list of reliability-critical pipes
- `outputs/pipe-network/pressure_distributions.png` — Pressure CDFs at key nodes
- `outputs/pipe-network/network_report.md` — Analysis summary with recommendations

## Usage
```
/pipe-network
```
Provide your EPANET .inp file or network data tables.
