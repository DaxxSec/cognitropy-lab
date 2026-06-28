# /sphere-rads

Assign the batch a standardized Sphere-RADS category (0–5) that carries a management action — the structured-reporting deliverable.

## Inputs

- The findings table (from `/read-batch`) and the dominant differential (from `/differential`).
- The intended use (caviar garnish vs feature sphere) — raises the bar for service-critical batches.

## Steps

1. Map the **worst applicable** finding to a category using the Sphere-RADS table in `references.md` (0 non-diagnostic → 5 failing).
2. Apply a use-context adjustment: a feature sphere with a "weak burst" is scored stricter than the same finding in a scattered caviar garnish.
3. Read off the **management action** bound to the category (serve / re-rest / adjust recipe / reject).
4. If RADS-3+, set the **re-test trigger** and route the dominant cause to `/fmea-process`.
5. State the category, the single finding that drove it, and the action in one line.

## Output

`Sphere-RADS-<n>` + driving finding + management action, embedded in the structured report. Categories accumulate over batches to trend the recipe.

## Notes

- The category is the *deliverable* — it standardizes language across cooks and forces a decision, exactly as BI-RADS does for mammography.
- Always grade to the worst finding, but record all findings; the category summarizes, it doesn't replace the read.
