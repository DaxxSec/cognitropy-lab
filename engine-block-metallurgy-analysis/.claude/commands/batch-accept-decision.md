# /batch-accept-decision

Make a decision-theoretic accept / reject / screen call on a casting lot, weighing the posterior probability the lot is out of spec against the costs of a field escape versus scrap.

## Inputs

- Sampled test results from the lot (tensile bars, hardness, nodularity, composition) and sample size vs. lot size
- The grade spec and acceptance criteria
- Cost inputs: cost of a field escape (warranty + reputational), cost of scrapping a good lot, cost of 100% screening

## Steps

1. From the sampled results, compute a posterior probability the lot is out of spec (Bayesian update on the defect fraction from the sample, with a prior from this supplier/process history).
2. Define the action space: accept, reject/scrap, or 100% screen; and the loss of each action under "lot good" vs. "lot bad."
3. Compute expected loss for each action: `E[loss | action] = P(bad)·loss(action|bad) + P(good)·loss(action|good)`.
4. Recommend the minimum-expected-loss action; report the decision threshold (the P(bad) at which the recommendation flips) so the user sees the sensitivity.
5. State the value of an additional sample — how much it would move P(bad) and whether it changes the action — before defaulting to expensive 100% screening.

## Output

`outputs/<case-id>/lot-disposition.md`: posterior P(out-of-spec), the expected-loss table per action, the recommended action with its flip threshold, and the value-of-more-sampling note.

## Notes

- This command is for **lot QC disposition**, not single-part failure analysis — it answers "what do we do with the remaining parts," not "why did this one break."
- Sensitivity matters more than the point decision: if the action flips at a P(bad) close to the estimate, take another sample rather than committing.
