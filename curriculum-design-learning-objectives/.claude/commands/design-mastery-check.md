# /design-mastery-check

Blueprint a mastery checkpoint for an objective, sized so the resulting posterior credible
interval is narrow enough to support the intended decision.

## Inputs
- The objective, its prior, and the evidence model (item slip/guess).
- Target posterior precision (credible-interval width) and stakes (formative → certification).

## Steps
1. Set the target: how narrow must the posterior CI be to decide met/not-met at the required
   stakes (see threshold table in `context/references.md`)?
2. Given each candidate item's `(s, g)`, estimate the information it adds; high-guess items add
   little, so more are needed for the same precision.
3. Simulate or compute the expected posterior CI width as a function of item count and mix;
   choose the smallest blueprint that reaches the target.
4. Specify a stop rule for adaptive checks: stop once the CI clears the target or after a max
   item count (avoid over-testing a clearly-mastered learner).
5. Balance the item mix across the objective's facets to avoid construct underrepresentation.

## Output
An assessment blueprint: item count and mix, per-item evidence value, expected posterior CI width,
and the stop rule. Saved to `outputs/mastery-check-<objective>.md`.
