# /diurnal-baseline

Build a time-of-day / day-of-week baseline so a rule's threshold adapts to the cycle instead of being tuned to the daily mean — Phase 6 support.

## Inputs

- Event stream (the source the rule keys on).
- Observation window (≥ 2–4 weeks of representative activity).
- Bucket granularity (hourly or 30-minute).
- Operational calendar: business hours, maintenance/patch windows, holidays.

## Steps

1. Bucket benign counts by `(hour-of-day, weekday)`.
2. For each bucket compute a robust center + spread: median and MAD (median absolute deviation) — robust to the transient spikes that would skew a mean/stddev.
3. Tag maintenance/patch-window buckets so the rule can widen or suppress during them (the gray-line boundary effect).
4. Produce a per-bucket envelope: `expected ± k·MAD` (k from the required-SNR margin in `/noise-floor`).
5. Export the envelope as a lookup the production rule references (Splunk lookup / Elastic enrich policy / Sentinel watchlist).

## Output

`outputs/diurnal-baseline-<source>.csv` (per-bucket median, MAD, envelope) plus an `.md` summary noting peak/trough buckets and maintenance windows.

## Notes

- Re-build after any K5+ disturbance has *fully* passed — never during one.
- If weekends differ sharply from weekdays, keep weekday and weekend baselines separate rather than averaging them.
