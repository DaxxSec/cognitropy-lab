# /detect-aberration

Run prospective aberration / outbreak detection on a routine surveillance series, flagging where current counts exceed a modelled baseline.

## Inputs

- A surveillance count series, ideally with several years of history for a seasonal baseline.
- Disease context: established (long history) vs novel (short history) vs slow-drift concern.
- Overdispersion estimate, known past-outbreak periods to exclude from the baseline, and the alarm threshold (e.g. upper bound of the predictive interval).

## Steps

1. Read `context/workflows.md` "Workflow 5: Aberration / outbreak detection".
2. Build the **baseline**: exclude prior outbreak weeks, account for seasonality + secular trend, and fit an overdispersed (negative-binomial) reference model.
3. Choose the algorithm:
   - **Farrington / `farringtonFlexible`** — seasonal, overdispersion-aware; default for notifiable disease with history.
   - **EARS C1/C2/C3** — short 7-day sliding baseline; for novel diseases / no history.
   - **CUSUM** — sustained small upward drifts rather than sharp spikes.
4. Set the threshold and run prospectively over the recent weeks of interest.
5. For each flagged point: record observed, expected, exceedance, and alarm score.
6. Control false alarms across many strata (raise thresholds / FDR) if testing many series.
7. Write the alarm table + figure to `outputs/`.

## Output

`outputs/aberration-<stream>-<snapshot-date>.md` + figure: the series with baseline and threshold band, a table of flagged weeks (observed/expected/exceedance/score), the algorithm + parameters, and a triage note (investigate / data-artifact / known-seasonal).

## Notes

- Aberration detection answers "is *now* anomalous vs baseline?", not "is transmission growing?" — pair with `/estimate-rt` for the latter.
- Treating counts as Poisson when they are overdispersed produces a flood of false alarms — use NB.
- A flag is a hypothesis, not a confirmed outbreak; reconcile against reporting artifacts before escalating.
