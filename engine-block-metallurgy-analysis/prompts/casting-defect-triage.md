# Casting Defect Triage

## Purpose

Use when one or more casting defects have been observed and you need to classify each by origin (gas, shrinkage, cold shut, inclusion/dross) and attribute it to a foundry process step — turning a defect observation into actionable corrective-action evidence.

## Prompt Template

```
Triage the observed casting defects in this engine block as a foundry-quality metallurgist.
Classify each defect by origin from its morphology, chemistry, and location, then point at the
process step responsible.

Inputs:
- **Material & casting process:** [e.g. gray iron, green-sand gravity cast]
- **Defect observations:** [morphology, size, location relative to geometry; radiograph/CT if available]
- **EDS chemistry (for inclusions):** [if available]
- **Section geometry context:** [junction, hot spot, gate, last-to-freeze region]

Please:
1. Classify each defect: gas vs. shrinkage vs. cold shut vs. inclusion/dross/sand, citing the distinguishing morphology.
2. Attribute each to a likely process cause (gating turbulence, feeding/riser, melt degassing, mold condition).
3. Rank the defects by severity to the part's function (which sit on a load path or near a crack origin).
4. Give the likelihood ratio that this defect population contributes toward a casting-defect root cause, and propose the foundry corrective action.
```

## Expected Output

- A per-defect classification with the morphological/chemical basis
- Process-step attribution for each defect type
- A severity ranking against the part's function
- The LR contribution to the posterior and a corrective-action recommendation
