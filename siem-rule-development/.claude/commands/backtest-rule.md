# /backtest-rule

Replay a candidate rule against a historical log window before production — the prediction-before-deployment go/no-go gate (a VOACAP point-to-point run before you pick the frequency). Phase 5.

## Inputs

- The rule + its FOT threshold band.
- A historical log window (state the exact range and index/data-source versions — reproducibility).
- Known-bad markers: Atomic Red Team executions, purple-team runs, or confirmed prior incidents in the window.
- The FP budget (alerts/day).

## Steps

1. Run the rule over the historical window exactly as it would run in production.
2. Count would-be alerts; project them to alerts/day and compare to the FP budget.
3. Sample the alerts and classify TP/FP to estimate precision.
4. Confirm the rule fires on the known-bad markers — measure recall on that labeled subset.
5. Note any blackout buckets where it stormed or went silent (cross-check `/propagation-forecast`).
6. Issue a verdict: **GO** (within budget + meets recall on known-bad), **TUNE** (back to `/threshold-band`), or **NO-GO** (closed window / no telemetry → `/coverage-map`).

## Output

`outputs/backtest-<rule>-YYYY-MM-DD.md` — alert volume, estimated precision/recall, known-bad hit list, FP-budget comparison, pinned window + data versions, and the GO/TUNE/NO-GO verdict.

## Notes

- No rule reaches production without a GO here. A rule that has never been replayed is an untested transmitter.
- If there are no known-bad markers in the window, generate them with Atomic Red Team first — recall on zero positives is meaningless.
