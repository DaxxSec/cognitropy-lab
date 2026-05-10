# /torque-split-design

Draft a baseline torque-split policy for a hybrid vehicle, with explicit Bayesian priors over driver intention and vehicle state.

## Inputs

- Vehicle architecture (parallel / series / power-split / P0–P4 sub-type).
- Vehicle parameter sheet (BSFC map, motor efficiency map, battery OCV-SOC table, mass, drag).
- Driver class prior (or "default population prior" if none).
- Strategy family preference: rule-based / ECMS / MPC.

## Steps

1. Read `context/concepts.md` for architecture-specific torque-flow physics.
2. State the prior over driver class (categorical) and trip class (categorical) explicitly. If the user has not provided one, use the population default and flag.
3. Sketch the torque-split decision logic:
   - For rule-based: enumerate (speed band × torque demand × SOC) cells, fill from BSFC + motor-efficiency sweet spots.
   - For ECMS: write the cost function `J = ṁ_fuel + s · P_elec / Q_LHV` with *s* placeholder for tuning.
   - For MPC: define horizon, decision variables, constraints (motor torque limit, battery power limit, SOC bounds).
4. Note the engine on/off threshold logic (hysteresis required to avoid chattering).
5. Document expected coverage of the prior — what fraction of likely trips this baseline handles vs. needs MPC layered on top.

## Output

A markdown file `outputs/torque-split-baseline-YYYY-MM-DD.md` containing: stated priors, chosen strategy family, decision logic sketch, expected fuel-economy range under the prior, and the next tuning task (typically `/ecms-tune` or `/mpc-horizon-tune`).

## Notes

- Never propose a baseline without the prior. A "baseline" with implicit assumptions is not a baseline.
- For PHEV, separate the CD (charge-depleting) and CS (charge-sustaining) phases — different decision logic in each.
- Cite the BSFC sweet-spot speed and torque from the actual map; do not approximate from memory.
