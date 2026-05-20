# /cycle-replay — Ablation Replay of a Recorded Drive

Replay a logged drive against alternative fusion policies (source subsets, gating thresholds, trust-weight variants, strategy choices) to quantify the contribution of each source and configuration choice to the EMS outcome.

## Inputs

- **Recorded drive** — CAN + GPS + V2X + telematics log, matched to the original pre-drive prior used by the controller.
- **Ablation matrix** — a list of fusion-policy variants to compare, e.g.:
  - `nav_only`, `nav_plus_elev`, `nav_plus_elev_plus_traffic`, `all_sources`.
  - `gate_z=2.0`, `gate_z=3.0`, `gate_z=4.0`.
  - `strategy=a_ecms` vs. `strategy=mpc_stochastic` vs. `strategy=rl_policy`.
- **Reference policy** — the "as-driven" policy that the controller actually used (baseline).
- **Metric set** — fuel/energy consumption, CO2 g/km, battery wear units, SOC RMS deviation, engine on/off count, drivability score.

## Steps

### 1. Reconstruct the Pre-Drive Information State
For each ablation variant, re-construct the prior **as it would have been** with that variant's source subset and configuration, using the time-aligned source logs (not the realised drive data).

### 2. Run the Variant Pipeline End-to-End
For each variant:

1. Build variant prior (`/fuse-trip-prior` with variant config).
2. Run `/source-conflict` at variant gate threshold.
3. Run `/predict-load-envelope`.
4. Run `/optimize-split` with variant strategy.

### 3. Forward-Simulate Against the Realised Drive
With each variant's policy and the realised drive's actual demand:

- Simulate SOC trajectory using a calibrated battery model.
- Accumulate fuel / electric energy use.
- Compute drivability metrics (engine on/off transitions, torque rate, mode-change rate).
- Track all KPIs in `metric_set`.

### 4. Statistical Comparison
- Compute per-variant KPI deltas vs. the reference (as-driven) policy.
- Bootstrap-confidence intervals on each delta over the drive's distinct segments (city, highway, mountain).
- Identify variants with statistically significant improvement on each KPI.

### 5. Pareto Frontier
Project all variants onto the fuel-vs-battery-wear plane (or any user-specified pair). Highlight Pareto-dominated and Pareto-optimal variants. Flag variants that are Pareto-dominated under one metric pair but optimal under another.

### 6. Persist
- Write the comparison report to `outputs/replays/<vehicle>-<drive-id>-<timestamp>.md` with KPI tables, plots, Pareto frontier, and narrative summary.
- Save per-variant trajectory artefacts to `outputs/replays/<drive-id>/variants/<variant-name>/`.

## Output

A replay report markdown file in `outputs/replays/` with: per-variant KPI table with confidence intervals, side-by-side SOC and engine on/off plots, Pareto frontier scatter, and a narrative summary identifying which sources / thresholds / strategies actually improved outcomes and which were noise.

## Notes

- **Replay is an offline ablation, not a re-simulation of the original control loop.** Do not pretend the variant policy "would have" exactly matched the realised demand — the realised drive is fixed; only the policy varies.
- **Sources that are conflict-flagged frequently may still be valuable.** A flag is not the same as a degradation — the only honest evidence is the KPI delta in the replay.
- **Pareto-dominated variants on a single drive may be optimal in aggregate.** A single drive is one sample from a population; before retiring a variant, replay it on the full drive-cycle library and on multiple weather / season / driver conditions.
- **Drivability penalties are not always linear in mode-change count.** A single bad transition during a critical manoeuvre can outweigh ten mild transitions in steady-state. Use the calibration team's drivability scoring function, not a count.
