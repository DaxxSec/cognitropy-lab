# /review-round

Run one structured peer-review round on a formula end-to-end: assign reviewers, gather rubric scores and graded defects, aggregate, and issue a verdict.

## Inputs

- A normalised formula (from `/formula-normalize`) and its round number.
- Reviewer roster (≥3, author excluded from blinded scoring) and confirmation the panel is calibrated (`/reviewer-calibrate`).
- Available evidence: `/stability-assay` result and `/tasting-panel` scores; defect grades from `/defect-grade`.
- The rubric weights (default in `references.md`) and use-case (which may re-weight, e.g. stability up for hold-for-service).

## Steps

1. **Safety gate.** Confirm the safety pre-screen passed; a Safety defect ≥3 ends the round in reject.
2. Confirm inter-rater agreement meets threshold; if not, stop — recalibrate the panel before scoring (the panel failed, not the formula).
3. Collect each reviewer's rubric scores (stability, texture, flavour balance, reproducibility, safety) and defect grades.
4. Compute the weighted score, defect tally, and agreement statistic; note any reviewer split the moderator must resolve.
5. Check the reproducibility gate: ≥2 preparers × ≥2 replicates with logged variables. No sign-off without it, however high the taste score.
6. Issue the verdict — **sign-off / minor revise / major revise / reject** — with the scoped delta for any revise.

## Output

`outputs/review-<formula-id>-R<n>.md`: per-reviewer scores, aggregated weighted score, defect tally, inter-rater agreement, reproducibility check, verdict, and (for revise) the exact delta to re-review next round.

## Notes

- Minor revise re-reviews only the changed delta; major revise triggers a full re-review. Don't re-validate an unchanged mother.
- Record reviewer identities and any conflict of interest — an author scoring their own sauce invalidates the round.
