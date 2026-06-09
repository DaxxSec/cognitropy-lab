# Practice-Selection Decision

## Purpose

Use this when you have a field's slope, soil, land use, and flow conditions and need a justified choice among contour cultivation, strip cropping, terracing, waterways, diversions, and check dams — the minimal set that brings A ≤ T and conveys runoff safely.

## Prompt Template

```
You are an erosion-control agent. Read context/workflows.md "Workflow B: Practice-selection decision tree".
Walk the decision tree explicitly for my field and justify each branch.

- **Slope steepness & length:** [VALUE]
- **Soil texture / permeability / hydrologic group:** [VALUE]
- **Climate regime:** [humid / subhumid / semiarid / arid]
- **Land use:** [row crop / pasture / orchard / construction site]
- **Concentrated flow:** [none / ephemeral gully / active incised gully]
- **Current A/T (from /estimate-soil-loss):** [VALUE]
- **Constraints:** [farm-machinery width, budget, cost-share standard, permitting]

Please:
1. Walk the decision tree node by node, stating which branch and why.
2. Recommend the minimal practice set (cheapest-first: cover → contour → earthwork).
3. Note where contour cultivation would exceed its critical row length and must escalate.
4. Specify required stable outlets for any graded structure.
5. List the sizing commands to run next for the chosen practices.
```

## Expected Output

- The decision-tree walk with a one-line rationale per branch.
- A recommended minimal practice set, cheapest-effective-first.
- Critical-length / outlet-requirement flags.
- The ordered list of sizing commands to run for the selected practices.
