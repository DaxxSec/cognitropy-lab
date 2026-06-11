# /eco-performance-frontier

The capstone: build the Pareto frontier between functional performance and environmental cost across candidate alloy/processing/design choices, so the transformation decision and the life-cycle ledger are made together, not in sequence.

## Inputs

- The candidate design points to compare — each a bundle of (alloy + composition, processing route, part geometry, training state, surface finish).
- Functional metrics per candidate: transformation-temperature accuracy, recoverable strain / stroke, functional-fatigue life, superelastic margin.
- Environmental metrics per candidate, pulled from the other commands: cradle-to-gate GWP + CED, use-phase balance / break-even, recyclability rating, Ni-release risk.

## Steps

1. Read `context/workflows.md` for the integrated decision flow — this command consumes the outputs of `/composition-temperature-tune`, `/functional-fatigue-budget`, `/lca-cradle-to-gate`, `/use-phase-energy-balance`, and `/recyclability-eol-assessment`.
2. Normalize each metric to a common scale and define the performance axis (composite of stroke, fatigue life, Af accuracy) and the environmental-cost axis (composite of embodied GWP, use-phase net, recyclability, Ni risk) — state the weighting explicitly.
3. Plot the candidates; identify the **Pareto-non-dominated set** (no other candidate is better on both axes).
4. Annotate the dominated candidates with *why* they lose (e.g. "Pt addition buys +40 °C Af but doubles embodied carbon and adds supply risk").
5. Surface the **knee of the frontier** — the design where further performance costs disproportionate environmental burden — and recommend it unless a hard requirement forces a corner.
6. Document the value judgments transparently: changing the weighting changes the recommendation, so make the weighting a visible input the reader can challenge, not a hidden default.

## Output

`outputs/eco-performance-frontier-<application>-YYYY-MM-DD.md`: the candidate table (performance + environmental metrics), the Pareto frontier description, the dominated-candidate rationale, the recommended knee-of-curve design, and the explicit weighting/value-judgment statement.

## Notes

- A frontier with a hidden weighting is just an opinion wearing a chart — keep the weighting on the page and invite the reader to re-run with their own.
- The greenest *material* choice and the greenest *system* choice can differ; let the use-phase break-even decide which dominates for this application.
- Re-run when any upstream command's inputs change; the frontier is only as current as its feeds.
