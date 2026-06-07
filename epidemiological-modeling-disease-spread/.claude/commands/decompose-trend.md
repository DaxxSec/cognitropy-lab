# /decompose-trend

Decompose a surveillance series into trend, seasonal, and remainder components — isolating the secular trend from day-of-week reporting structure and annual seasonality.

## Inputs

- A surveillance time series (counts or rates), daily or weekly.
- Known periodicities to remove (7 for day-of-week on daily data; 52/53 for annual on weekly data; possibly both).
- Variance behaviour (constant vs increasing with level — drives log/sqrt transform).

## Steps

1. Read `context/workflows.md` "Workflow 4: Trend / seasonal decomposition".
2. Choose the scale: for count data with variance growing with the mean, decompose on `log(count+1)` or `sqrt`; record the transform.
3. Select the method: **STL** (`stl`/`feasts::STL`/`statsmodels.tsa.STL`) for one seasonality; **MSTL** or Prophet for weekly + annual.
4. Set the seasonal window (periodic for stable seasonality; finite for evolving) and the trend smoother span.
5. Run the decomposition; extract trend, seasonal, remainder.
6. Inspect the **remainder** for structured spikes (→ candidate aberration, `/detect-aberration`) or level shifts (→ data definition change).
7. For seasonal pathogens, persist the seasonal component as a baseline for `/wave-phase` and threshold work.
8. Write components + figure to `outputs/`.

## Output

`outputs/decomp-<stream>-<snapshot-date>.md` + figure: the trend/seasonal/remainder panels, the transform and periods used, the day-of-week profile, and a one-line read of the de-seasonalised trend direction.

## Notes

- The seasonal (weekly) component is the reporting artifact you are removing — never report it as signal.
- STL is robust to outliers with the robust option on; use it when sporadic spikes are present.
- Decomposition de-noises for *visualisation and seasonality removal*; it is not a substitute for Rt as the formal trend estimate.
