# Discordance Reconciliation

## Purpose

Reconcile a disagreement between two assessors double-reading the same batch (typically on "burst" or "texture"), and decide whether the fix is a tighter scale definition or accepting real batch variability. Use after `/double-read` finds low agreement.

## Prompt Template

```
You are reconciling a discordant double-read using the agreement bands and
double-read protocol in context/references.md and context/workflows.md.

- **Scale in question:** [BURST / TEXTURE / OTHER] — current definition: [STATE IT]
- **Assessor A scores:** [LIST]
- **Assessor B scores:** [LIST]
- **Sample size:** [N]
- **Notes on the discordant spheres:** [ANY DETAIL]

Please:
1. Compute % concordance and Cohen's κ; band the agreement.
2. For each discordant sphere, classify the disagreement as definition drift
   (ambiguous scale) or real batch variability.
3. If definition drift dominates, propose a tightened, testable scale definition.
4. If real variability dominates, route it to /differential and /fmea-process as a
   batch-consistency problem, not a scoring problem.
5. State the expected κ improvement from the change.
```

## Expected Output

- A κ value with its agreement band.
- A per-sphere drift-vs-variability classification.
- Either a sharpened scale definition or a referral to the differential/FMEA path — with the rationale.
