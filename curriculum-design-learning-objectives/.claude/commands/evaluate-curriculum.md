# /evaluate-curriculum

Evaluate whether a curriculum revision actually improved learning using a Bayesian A/B or
pre-post comparison — a posterior over the effect, a ROPE decision, and `P(improvement)`, not a
p-value.

## Inputs
- Outcome data for control (old design) and treatment (revision): e.g. proportion of objectives
  met, or mean posterior mastery, per learner.
- A ROPE (region of practical equivalence) appropriate to the outcome.

## Steps
1. Define the outcome metric and the comparison (A/B between cohorts, or pre/post within a cohort).
2. Put a prior on the effect and compute the **posterior over the effect size** (PyMC/Stan, or a
   Beta-difference for a proportion-met metric).
3. Define the **ROPE** — effect sizes too small to act on (see defaults in `context/references.md`).
4. Decide:
   - credible interval wholly outside ROPE on the positive side → **adopt**;
   - wholly inside ROPE → **practically equivalent**, don't churn;
   - straddling → **inconclusive**, collect more cohorts.
5. Report `P(effect > 0)` and the decision; check for confounds (cohort differences, attrition).

## Output
A Bayesian evaluation write-up: posterior summary, credible interval vs. ROPE, `P(improvement)`,
the adopt/equivalent/inconclusive decision, and caveats. Saved to `outputs/eval-<revision>.md`.
