# /product-mix-plan

Reconcile GFA-limited castability against a demand forecast to produce a capacity-constrained product mix — what to make, in which alloy, and what to defer or redesign.

## Inputs

- Product list with demand forecast (units/period) and each product's **minimum-cooling section** (mm).
- Available alloys with their Dmax (from `/gfa-assess`) and cost/precious-metal content.
- Per-product yield (from `/crystallization-yield`) and line capacity / bottleneck (from `/line-throughput`).
- Constraints: feedstock supply (e.g. Pd, Be handling), capacity cushion target.

## Steps

1. Build a **castability matrix**: for each (product × alloy), feasible only if min-cooling section < Dmax. Mark infeasible cells.
2. For feasible cells, attach **yield** and **cost** (alloy cost + processing). Each product gets its cheapest feasible alloy unless capacity forces otherwise.
3. Compute **capacity demand** per product = forecast / yield (gross parts needed) and compare to available bottleneck capacity.
4. If demand exceeds capacity, **allocate** by a stated objective (margin, strategic priority, contractual commitment) — make the objective explicit, not hidden.
5. Apply a **capacity cushion** for yield variance and oxygen risk; forecast feedstock (precious-metal lead times, Be-handling constraints).
6. Flag products that are **infeasible in every alloy** (section > all Dmax) → redesign geometry, qualify a higher-GFA alloy, or decline; and products feasible only in a costly alloy → cost-vs-capacity trade.

## Output

`outputs/product-mix-YYYY-MM-DD.md`: the castability matrix, the recommended alloy per product, the capacity-constrained make/defer plan against the forecast, feedstock forecast, capacity cushion, and the explicit allocation objective. Infeasible products listed with their redesign/alloy options.

## Notes

- Castability is a **hard** feasibility gate, not a preference — a product whose section exceeds every available Dmax cannot be planned in, however high the demand.
- Keep the allocation objective on the page (margin vs strategy vs commitment) and invite the planner to re-run with their own weighting — a hidden weighting is an opinion wearing a plan.
- Precious-metal (Pd) and Be-handling products carry supply and safety constraints beyond pure capacity — surface them here, don't bury them in the throughput math.
