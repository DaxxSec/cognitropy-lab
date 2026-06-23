# /tasting-panel

Design and execute a blind sensory panel for a formula and aggregate the scores into review-ready evidence.

## Inputs

- The formula(s) under test and the comparison reference (usually the baseline/mother).
- The question being asked: *different?* (discrimination), *how different?* (descriptive), or *preferred?* (affective).
- The panel (calibrated for descriptive/affective; can be naïve consumers for hedonic) and blinding level (single- or double-blind).

## Steps

1. Pick the test type from `context/workflows.md` "Sensory test selection": triangle/duo-trio for discrimination, QDA for description, 9-point hedonic for preference.
2. Code samples with random 3-digit blinds; randomise serving order; use identical vessels, temperature, and palate cleansers.
3. For discrimination: serve the set, collect odd-sample picks. For descriptive: collect attribute ratings on fixed scales. For hedonic: collect liking scores.
4. Analyse: binomial significance for triangle tests; means + spread (and agreement) for descriptive/hedonic.
5. Sanity-check against the calibration record — if agreement is poor, flag the panel, not the sauce.
6. Summarise into a panel result the review round can consume.

## Output

`outputs/panel-<formula-id>-YYYY-MM-DD.md`: test type, blinding, sample codes, raw scores, statistical result (e.g. "triangle test: 9/12 correct, p<0.05 — difference detectable"), and a plain-language verdict.

## Notes

- Run discrimination *before* preference — proving people *like* it more is meaningless if they can't even tell it apart.
- Never let the author serve or score in a single-blind panel; that reintroduces the bias blinding removes.
