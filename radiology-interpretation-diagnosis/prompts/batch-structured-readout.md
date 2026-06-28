# Batch Structured Readout

## Purpose

Turn raw inspection notes into the canonical six-section structured report with a Sphere-RADS category and a corrective action. Use to document and sign off a batch after `/read-batch`.

## Prompt Template

```
You are issuing a structured spherification QA report in the format defined by
/structured-report and the Sphere-RADS table in context/references.md.

- **Liquid / batch ID:** [VALUE]
- **Technique:** [METHOD + FULL RECIPE: alginate %, calcium salt + %, bath time, pH, temp, rest interval, sample size]
- **Raw findings (per station):** [SHAPE / MEMBRANE / SURFACE / BUOYANCY / BURST / FLAVOR notes + frequencies]
- **Intended use:** [CAVIAR GARNISH / FEATURE SPHERE]

Please produce:
1. **Technique** — the reproducible recipe + conditions block.
2. **Findings** — per-station, neutral, with frequencies; flag co-occurrences.
3. **Impression** — dominant defect + most-likely cause.
4. **Category** — Sphere-RADS-n (graded to the worst finding, use-adjusted).
5. **Corrective action** — specific change + which command runs it.
6. **Re-test interval** — when to re-read.
```

## Expected Output

- A complete six-section report saved to `outputs/`.
- Findings and impression kept distinct.
- A single Sphere-RADS category bound to a concrete next action.
