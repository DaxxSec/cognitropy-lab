# /reviewer-calibrate

Calibrate the tasting/review panel for inter-rater reliability before any verdict is trusted — untrained panels produce noise dressed as data.

## Inputs

- The panel roster (the same people must persist across sessions for calibration to mean anything).
- A calibration set: reference specimens with known attributes (e.g. a broken vs intact emulsion, a graded acidity ladder, the signed-off baseline).
- The scoring tools in use (rubric scale, defect 0–4 scale, descriptive attributes).

## Steps

1. Present the calibration set **blind** under identical vessels/lighting/temperature.
2. Have each reviewer score independently — no discussion during scoring.
3. Compute the agreement statistic appropriate to the scale: Cohen's κ (two raters, categorical), Krippendorff's α (n raters), or ICC (n raters, ratings) — thresholds in `references.md`.
4. Identify outlier reviewers or attributes with poor agreement; run a brief alignment discussion (anchor what a "3 — major texture defect" actually tastes/looks like).
5. Re-score a fresh blind set; confirm agreement now clears threshold.
6. Record the calibration so `/review-round` can confirm the panel is current.

## Output

`outputs/calibration-YYYY-MM-DD.md`: agreement statistics per attribute, reviewer outliers, alignment notes, the threshold used, and a pass/fail with an expiry (re-calibrate when tasters change or drift).

## Notes

- Calibrate against references that span the scale — a panel that only ever sees "good" sauce can't grade defects.
- A failed calibration is a finding, not a delay: a verdict from an uncalibrated panel is worse than no verdict.
