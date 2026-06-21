# /propagation-forecast

Forecast a rule's reliability across the diurnal/weekly cycle — the VOACAP REL analog. Volumetric, no labels required: it predicts *when* the rule will be reliable, storm, or go blind. Phase 4.

## Inputs

- Candidate rule + chosen FOT threshold band (`/threshold-band`).
- Diurnal baseline (`/diurnal-baseline`).
- Noise floor (`/noise-floor`).
- Forecast horizon (24 h or 7 d).

## Steps

1. For each hour-of-day bucket, project expected benign fires at the FOT threshold using the baseline envelope.
2. Translate that into predicted FP load per analyst shift.
3. Estimate per-bucket reliability: the fraction of buckets where the SNR margin holds (malicious signal would clear the elevated daytime floor).
4. Flag **blackout windows** — peak buckets where the rule will either storm (FP load > budget; below LUF locally) or be muted into noise (the daytime D-layer-absorption analog).
5. Recommend a remedy: per-bucket thresholds, a scheduled enable/disable, or routing blackout-window alerts to batch review.

## Output

`outputs/propagation-forecast-<rule>-YYYY-MM-DD.md` — a reliability curve (per hour-of-day), predicted FP-by-hour, the blackout-window list, and the scheduling/threshold recommendation.

## Notes

- This is the predict-before-you-operate step. It does not replace the labeled `/backtest-rule` gate — it complements it: forecast = volumetric reliability over conditions, backtest = precision/recall on known data.
- A rule reliable at the mean but with a midday blackout is the most common and most missed failure — surface it explicitly.
