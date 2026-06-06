# /maintenance-forecast

Forecast the remaining useful life of the pointing from monitored decay indicators and colonisation growth, then schedule the next intervention inside the P-F interval and a lime-curing-compatible weather window.

## Inputs

- The monitoring time-series from `/decay-monitor` (≥3–4 epochs per zone).
- Failure thresholds per indicator (`context/references.md`, tuned for the site).
- Exposure ranking (orientation / driving-rain) and consequence (visible / structural).
- Local climate/curing constraints (frost windows, drying conditions).

## Steps

1. Read `context/concepts.md` "Predictive-maintenance concepts" and `context/workflows.md` "Monitor → forecast → schedule".
2. Fit a decay trajectory per indicator per zone (linear recession, exponential capillarity rise, logistic biofilm growth; lichenometry growth curve as a colonisation clock). Respect any change-point — don't extrapolate across a break.
3. Estimate **RUL** = time for the governing indicator to reach its failure threshold, with a confidence band (not a point).
4. Rank zones by RUL × exposure × consequence.
5. Schedule the intervention inside the **P-F interval** *and* a lime-curing weather window (≈ 5–25 °C, frost- and rapid-dry-free); sequence repointing, biocide (cause-first), and detailing/sheltering fixes.
6. Set the next inspection date proportional to the shortest RUL / steepest trajectory.

## Output

A maintenance plan `outputs/forecast-<building>-YYYY-MM-DD.md`: per-zone RUL with confidence bands, the governing indicator, the priority ranking, the scheduled intervention windows and sequence, and the next inspection date.

## Notes

- Wide RUL bands (few epochs) → schedule a re-inspection, not a premature campaign; say "monitor," not "intervene."
- Accelerating (non-linear) indicators collapse the P-F interval — shorten the cadence.
- Never schedule lime repointing into a frost window; curing constraints override convenience.
