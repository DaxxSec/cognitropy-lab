# /trend-test

Run Mann-Kendall + Theil-Sen on a univariate time series; report monotonic trend with magnitude.

## Inputs

- Path to a time series (CSV or TSV with `date` and `value` columns; one series per file or column).
- Series type: alpha-diversity index, qPCR copy number, CLR-transformed taxon, soil-health proxy.
- Seasonality flag (annual / sub-annual / none); if annual, switch to Seasonal Mann-Kendall.
- Multiple-testing context (single series vs. many-taxa; FDR control needed if many).

## Steps

1. Read `context/workflows.md` "Monotonic Trend Testing (Mann-Kendall + Theil-Sen)".
2. Verify the series is on the right scale (CLR for taxa, log for qPCR, untransformed for diversity).
3. Diagnose ties (`Kendall::Kendall` warns) and autocorrelation (`acf()` lag-1).
4. Choose the test:
   - Heavy ties → exact Kendall variance.
   - Annual seasonality → `Kendall::SeasonalMannKendall` or `trend::smk.test`.
   - Sub-annual autocorrelation → block-bootstrap MK or `trend::partial.mk.test`.
5. Run the test; record τ, S, p-value, N.
6. Run Theil-Sen for slope: median pairwise slope + 95% bootstrap CI.
7. If many taxa being tested simultaneously → apply Benjamini-Hochberg FDR.
8. Write report.

## Output

A markdown file `outputs/trend-test-<series-name>-YYYY-MM-DD.md` containing: input series description, test variant chosen and why, τ + S + p-value (FDR-adjusted if applicable), Theil-Sen slope + 95% CI, and a one-line interpretation (direction, magnitude per unit time, agronomic significance).

## Notes

- p > 0.05 with small N → report "absence of evidence not evidence of absence"; lean on the slope CI rather than the p-value.
- Statistical significance ≠ biological significance — always report effect size.
- Non-monotonic trends (unimodal, with a peak) → MK will miss them; switch to STL decomposition or change-point detection.
- Two-time-point "trends" are not trends; require ≥4 time points before running this command.
