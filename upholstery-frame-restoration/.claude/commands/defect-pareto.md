# /defect-pareto — Pareto of Restoration Defect Causes

Rank the defect causes across a batch of restored frames by frequency (or cost) to focus the shop's improvement effort on the vital few rather than the trivial many.

## Inputs

- A defect log across the batch: each occurrence tagged by **cause category** (loose corner block, hide-glue release, dowel rock, rail split, off-square assembly, wet glue-up, finish/cosmetic, etc.).
- Optional **weighting**: rework time or material cost per occurrence (to Pareto by impact, not just count).
- The batch scope (date range, number of frames, restorers involved).

## Steps

1. Tally occurrences per cause category; if weighting is supplied, also compute weighted impact.
2. Sort descending; compute the **cumulative percentage** line.
3. Identify the **vital few** — the categories that together reach ~80% of occurrences (or impact).
4. Cross-reference the top causes with `/control-chart` history — is a top cause also producing chart signals? That is the highest-priority OCAP target.
5. Recommend one or two improvement actions aimed only at the vital few (e.g. standardize corner-block re-gluing; add a glue-up MC gate via `/moisture-spc`).

## Output

A Pareto report: ranked cause table (count, %, cumulative %), the vital-few set, the count-vs-impact comparison if weighted, and the targeted action list. Save to `outputs/<batch-id>-defect-pareto.md`.

## Notes

- Pareto by **count** and by **cost** can disagree — a rare rail-split may dominate rework hours. Show both when weighting exists.
- The point is to *not* spread effort evenly; resist fixing the trivial many first because they're easy.
- Recompute each batch — the vital few shift as you fix them; today's #1 cause should fall next quarter if the action worked.
