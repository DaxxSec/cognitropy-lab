# /decay-monitor

Record a dated time-series of decay indicators per elevation/zone as the monitoring baseline for predictive maintenance.

## Inputs

- Indicator readings for this epoch: joint recession depth (mm), scratch/drilling-resistance hardness, capillary absorption (Karsten/RILEM tube, mL/min), soluble-salt content (% by ion), biofilm coverage (% from `/biodeteriogen-survey`), crack width (mm), surface moisture.
- Zone/elevation identifiers, instrument + method, date, operator.
- Prior monitoring records, if any.

## Steps

1. Read `context/workflows.md` "Monitor → forecast → schedule" and `context/references.md` "Decay-indicator failure thresholds".
2. Validate each reading: correct method, units, and a consistent measurement location (same spot across epochs — recession and capillarity are location-sensitive).
3. Append the epoch to the per-zone time-series (one row per indicator per zone per date), tagging method and operator for reproducibility.
4. Flag any indicator crossing its "watch" or "intervene" threshold.
5. Note candidate change-points (a step coinciding with a weather event, works, or a season).
6. Report current status per zone and the number of epochs accumulated (≥3–4 needed before a forecast).

## Output

An updated monitoring dataset `outputs/monitoring/<building>.(md|csv)` plus an epoch summary `outputs/monitoring/<building>-epoch-YYYY-MM-DD.md`: readings, threshold flags, change-point notes, and epoch count.

## Notes

- Two points are not a trend — resist forecasting until ≥3–4 epochs exist; report "monitoring" until then.
- Keep the measurement location and instrument constant across epochs; record any change so the series stays comparable.
- Capillary readings vary with surface wetness/temperature — standardise conditions or record them.
