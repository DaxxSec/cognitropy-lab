# Defect Differential Workup

## Purpose

Take a single observed spherification defect and run the full radiology-style workup — finding → ranked differential → discriminating test → corrective action — without anchoring on one cause. Use after `/read-batch` surfaces a non-normal finding.

## Prompt Template

```
You are reading a spherification defect using the gamut and differential
discipline in context/concepts.md and context/references.md.

- **Method:** [BASIC / REVERSE / FROZEN REVERSE]
- **Recipe:** [ALGINATE %, CALCIUM SALT + %, BATH TIME, pH, TEMP]
- **Rest/degas interval:** [TIME / "none"]
- **Defect finding:** [e.g. "floating spheres, thin top membrane"]
- **Co-occurring findings:** [LIST / "none noted"]

Please:
1. Restate the finding(s) separately from any cause.
2. Pull the gamut for each finding and rank candidate process causes for THIS recipe.
3. Give the discriminating test that confirms/excludes the top one or two causes.
4. Name the most-likely cause + corrective action, and the runner-up to keep in mind.
5. Flag whether this is a one-off transient or a recurring mode for the FMEA.
```

## Expected Output

- Findings cleanly separated from causes.
- A ranked, recipe-adjusted differential per finding.
- A concrete discriminating test and a single recommended action.
- A transient-vs-recurring verdict so the team doesn't over-correct on noise.
