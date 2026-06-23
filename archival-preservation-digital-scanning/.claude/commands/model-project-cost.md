# /model-project-cost — Cost-per-image model and in-house vs. vendor optimization

Build a defensible cost model for a digitization project and solve the make-vs-buy decision: which lots are cheaper (and safer) to capture in-house vs. send to a service bureau.

## Inputs

- The lot list with image counts, material types, and condition grades.
- In-house cost drivers: loaded labor rate, equipment amortization per hour, facilities/overhead allocation, storage cost per TB.
- Vendor quote(s): price per image by material type, minimums, transit/insurance, and any prep the lab must still do.
- Risk tolerance for off-site transport of fragile/unique material.

## Steps

1. **Compute fully-loaded in-house cost-per-image.** `(labor + equipment amortization + overhead) / images_per_hour`, by material type. Don't omit metadata, QA, and storage — they are often half the true cost.
2. **Add lifecycle storage.** Project master + derivative storage over the retention horizon (TIFF masters are large; multiply by replication factor and years). Use figures from `context/references.md`.
3. **Lay vendor cost beside it.** Per-lot vendor total = `images × per-image price + prep + transit + insurance`, respecting minimums.
4. **Solve make-vs-buy per lot.** Choose the cheaper option *unless* a risk gate fires: unique/fragile material that cannot be safely transported stays in-house even at higher cost. Record every risk-override explicitly.
5. **Optimize the split under a budget.** If the in-house queue exceeds capacity, treat outsourcing as the overflow valve and select which lots to send so total cost is minimized while the in-house lot count fits the schedule from `/optimize-scanner-schedule`.
6. **Sanity-check against benchmarks.** Compare the derived cost-per-image to published benchmarks (FADGI/NDSA, Library of Congress program figures) and flag any line item that's an order of magnitude off.

## Output

`outputs/cost-model-<project>.md`: the in-house cost-per-image breakdown by material, the lifecycle storage projection, the per-lot make-vs-buy table with the chosen option and any risk-override reason, the budget-constrained outsourcing split, and the benchmark comparison.

## Notes

- "Vendor is cheaper per image" frequently flips once prep, transit, insurance, and the value-at-risk of irreplaceable originals are priced in. Make the full cost visible.
- Storage is a recurring cost, not a one-time one. A model that ignores 10 years of TIFF storage understates the project badly.
- The make-vs-buy answer is partly ethical, not purely financial: some material must never leave the building. Encode that as a hard gate, not a tunable weight.
