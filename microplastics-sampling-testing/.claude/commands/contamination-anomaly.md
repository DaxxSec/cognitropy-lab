# /contamination-anomaly

Compare a result against the site baseline and the polymer watchlist, and escalate deviations. This is the watchlist-hit / anomaly-alert layer: most results are unremarkable, but the ones that deviate are exactly what the program exists to catch.

## Inputs

- A blank-corrected result from `/concentration-report` (concentration + polymer/size/morphology breakdown).
- The site's rolling baseline (mean, variability) from prior campaigns in `outputs/baselines/`.
- The polymer/additive watchlist (e.g. tire-wear particles, banned microbeads, a signature copolymer for a known source, sudden nanoplastic-fraction shifts).

## Steps

1. **Baseline deviation.** Compute the result's departure from the site baseline (e.g. z-score, or ratio to the historical IQR). Account for season/flow if the baseline is stratified — a wet-weather spike may be expected, not anomalous.
2. **Watchlist match.** Scan the polymer/morphology breakdown for any watchlist signature. A watchlist hit escalates regardless of total concentration (a small but distinctive industrial copolymer can matter more than a large generic load).
3. **Composition shift.** Flag changes in the *mix* even when total count is stable — e.g. fiber→fragment shift, or a new dominant polymer — which can indicate a new source.
4. **Distinguish contamination from environment.** Before escalating, confirm the anomaly survived `/blank-audit` and isn't a lab artifact (a polyester-fiber spike is a HEPA-filter suspect first, a real signal second). A failed cross-check routes to a maintenance/process incident instead of a field alert.
5. **Assign a severity tier** and the action: `routine` (log to baseline), `watch` (re-sample next campaign), `alert` (notify program lead / trigger source-attribution sampling), `incident` (lab-contamination root cause).
6. **Update the baseline** with routine results so the detector adapts as the site's normal evolves.

## Output

An anomaly record under `outputs/anomalies/<site>-<date>.md`: baseline deviation stats, watchlist hits, composition-shift notes, the contamination-vs-environment verdict, severity tier, recommended action, and the baseline update.
