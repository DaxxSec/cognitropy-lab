# /spindle-runout-trend — Trend Spindle Runout, Forecast Breach

Log a spindle/quill total-indicator-runout (TIR) measurement, trend it against history, and forecast when it will cross the angle-error budget — predictive maintenance for the single most angle-critical component.

## Inputs

- A fresh TIR reading: dial indicator on the dop/quill, machine running slow or rotated by hand, peak-to-peak deflection in µm.
- The measurement's machine-hours or stones-cut counter, and the date.
- The machine baseline and prior readings from `outputs/machine-baseline.md` / the runout log.
- Dop length (to express runout as an angle).

## Steps

1. Append the new reading (date, hours, TIR µm) to the runout log in `outputs/`.
2. Convert TIR to delivered angle error: `σ_spindle ≈ arctan(TIR / dop_length)`.
3. Fit the trend over recent readings — slope in µm per machine-hour (use a simple linear fit; flag if the slope is accelerating).
4. Locate the **P-point** (watch threshold, ~8–20 µm) and the **limit** (~20 µm / ±0.1°) from `context/references.md`.
5. Forecast machine-hours until the limit (RUL) and until the P-point if not already past it.
6. Classify green / watch / limit and recommend: continue, schedule spindle service inside the P-F interval, or stop fine work now.

## Output

A trend report: latest TIR, angle equivalent, fitted slope, RUL to limit, status, and recommended action with a target service date/hours. Save/append to `outputs/runout-trend.md`.

## Notes

- One reading is noise; the slope is the signal. Don't react to a single spike — re-measure to confirm before scheduling.
- Runout is multiplicative with dop length — long dops amplify the same TIR into more angle error; note the dop used.
- Accelerating slope (super-linear) usually means a failing bearing, not gradual wear — shorten the P-F interval.
