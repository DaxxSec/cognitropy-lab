# /defect-grade

Apply the defect-severity taxonomy across appearance, texture, flavour, and safety to convert subjective complaints into graded, comparable defects for the review round.

## Inputs

- The specimen and the panel's raw observations (or your own structured inspection).
- The defect taxonomy and 0–4 severity scale (`context/concepts.md` + `references.md`).
- The intended use (sets which defects are disqualifying — a thin sauce is fine as a dressing, fatal as a coating).

## Steps

1. Inspect by class in order: **Safety** first (raw-egg/danger-zone hold), then **appearance** (break, weeping, dull), **texture** (thin/gluey/grainy), **flavour** (flat, over-acid, raw-oil, over-salt).
2. Grade each detected defect 0–4 against the scale; tie each grade to an observable anchor, not an impression.
3. Apply the override rule: any Safety defect ≥3, or any single class-4, forces an automatic reject.
4. Map each defect to its likely cause (cross-ref `/break-diagnose` for stability defects) so the grade points at a fix.
5. Tally grades per class and compute the defect contribution to the rubric.
6. Emit a defect sheet the review round and the author can both act on.

## Output

`outputs/defects-<formula-id>-YYYY-MM-DD.md`: per-class defect grades with observable anchors, override-rule result, likely causes, and a prioritised fix list.

## Notes

- Grade against the *intended use*; the same texture can be a 0 for a dip and a 3 for a glaze.
- Anchor grades to references during `/reviewer-calibrate` so "a 3" means the same thing to every reviewer.
