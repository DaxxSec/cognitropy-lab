# /recovery-prioritization

When the budget cannot recover everything, rank artefacts and site areas by **benefit-per-cost** so a fixed budget captures the most value.

## Inputs

- Candidate recovery units: artefacts, cargo lots, structural elements, or site areas.
- Per-unit benefit estimate (research/significance contribution) — from `/site-significance-score`.
- Per-unit cost: recovery effort + conservation + curation (from `/conservation-cost-forecast`).
- The fixed budget (and/or fixed conservation capacity) constraint.
- Per-unit threat/urgency (from `/threat-decay-model`), if rescue-driven.

## Steps

1. For each unit, compute a **benefit-per-cost ratio** (significance contribution ÷ lifecycle cost). Include conservation — a fragile waterlogged timber can have a high benefit but a crushing cost.
2. If rescue-driven, weight benefit by urgency (at-risk units rise; safe units can wait or stay in situ).
3. Rank units by ratio and fill the budget greedily (a knapsack heuristic), respecting any indivisible groups (a cargo lot, a structural assembly) that must move together.
4. Check the **binding constraint**: if conservation capacity, not money, is the limit, rank against capacity instead.
5. Mark units below the cut for **record-in-situ** rather than recovery — they are documented, not lifted.
6. Sanity-check against bias: are high-ratio-but-unglamorous units actually selected over photogenic-but-costly ones?

## Output

`outputs/recovery-priority-<site>-YYYY-MM-DD.md`: the ranked benefit-per-cost table, the selected recovery set within budget, the binding constraint, the record-in-situ remainder, and a note on any indivisible groups.

## Notes

- The binding constraint is often conservation capacity, not field budget — prioritise against whichever runs out first.
- Resist recovering the photogenic over the informative; the ratio, not the display appeal, drives the cut.
- Anything below the line is *recorded*, not abandoned — in-situ documentation preserves its context for the future.
