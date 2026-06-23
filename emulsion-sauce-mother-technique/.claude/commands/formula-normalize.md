# /formula-normalize

Convert any recipe — prose, screenshot, or scribbled card — into reproducible ratio / baker's-percentage notation with a complete controlled-variable log, so reviewers compare formulas, not paragraphs.

## Inputs

- The source recipe in whatever form (ingredient list + method, or a verbal description).
- The reference base for percentages (usually total water phase, or egg-yolk count).
- Known process variables, if any (shear method, temperatures, oil-addition rate).

## Steps

1. Parse ingredients into **water phase**, **fat phase**, **emulsifier(s)**, and **seasoning/acid**.
2. Express quantities as ratios (oil:water-phase) and baker's % against the chosen reference base.
3. Compute derived figures: oil per yolk, approximate emulsifier load vs the `references.md` capacity guide, and predicted stability tier.
4. Fill the reproducibility log fields from `references.md`; mark any **missing** variable explicitly as `UNSPECIFIED` rather than guessing.
5. Flag risks: ratio near the crowding limit, raw-yolk-without-pasteurisation, watery additions that threaten stability.
6. Emit the normalised formula card and list every `UNSPECIFIED` field as a blocker the author must resolve before review.

## Output

`outputs/formula-<id>-normalized.md`: ratio + baker's-% formula, oil-per-yolk, predicted stability tier, full variable log (with `UNSPECIFIED` blockers called out), and an allergen list.

## Notes

- Normalisation is the entry gate to `/review-round` — an un-normalised formula is not reviewable.
- Keep the original source verbatim in an appendix so the normalisation is auditable.
