# /seasonal-decompose

STL decomposition of a time series to isolate trend from seasonal cycle.

## Inputs

- Path to an evenly-spaced (or interpolatable) univariate time series.
- Period (e.g. 12 for monthly with annual seasonality, 4 for quarterly, or the rotation length for crop-rotation cycles).
- Span of the seasonal smoother (`s.window`); robust flag (default TRUE).
- Output preference: trend component for downstream MK testing, full decomposition for visualisation, or both.

## Steps

1. Read `context/workflows.md` "Seasonal Decomposition (STL)".
2. Verify the series spans ≥2 full seasonal cycles — STL underestimates the seasonal component otherwise.
3. Handle gaps: small gaps via interpolation; large gaps via Kalman-smoothed state-space model first.
4. Run `stl(series, s.window=<period>, robust=TRUE)` (R) or `STL` from `statsmodels.tsa.seasonal` (Python).
5. Plot the four panels: observed, trend, seasonal, remainder.
6. Diagnose the remainder: ACF should show no significant autocorrelation. If it does, the seasonal model is misspecified.
7. Optionally: pass the trend component to `/trend-test` for monotonic trend testing.

## Output

Two artifacts:
- `outputs/decomposition/stl-<series>-YYYY-MM-DD.csv` — time-aligned columns: observed, trend, seasonal, remainder.
- `outputs/decomposition/log-<series>-YYYY-MM-DD.md` — period chosen, span, robust flag, gap handling, remainder diagnostics, and a textual description of what the trend component shows.

## Notes

- Period must match the actual seasonal cycle. For crop rotations (e.g. 3-year), use period = 36 if monthly; default annual will mislead.
- Robust mode (`robust=TRUE`) downweights outliers — useful for ecological data with occasional extreme weather years.
- If the seasonal component is small relative to the trend → STL was overkill; just run MK on the raw series.
- If the remainder shows clear structure → ARIMA or state-space modelling fits better than STL alone.
