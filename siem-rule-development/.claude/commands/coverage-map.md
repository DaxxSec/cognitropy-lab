# /coverage-map

Map the rule inventory to MITRE ATT&CK and find the "blackout" techniques — those with no usable detection, the D-layer-absorption analog where the circuit simply cannot open on current telemetry.

## Inputs

- Current rule inventory with ATT&CK tags.
- Available log sources / telemetry catalogue.
- The threat model: which techniques matter most for this environment.

## Steps

1. Build an ATT&CK matrix from the inventory: which technique cells have a rule.
2. Classify each prioritized cell:
   - **Covered** — a rule exists and passed backtest (circuit open at the FOT).
   - **Weak** — a rule exists but lives below its LUF (perpetually muted / alert-fatigued) or above its MUF (never fires). Counts as a gap.
   - **Blackout** — no telemetry carries the technique at all. No threshold can help — like D-layer absorption, the band is closed.
3. Separate blackouts into "no rule, but telemetry exists" (write a rule) vs "no telemetry" (needs new logging).
4. Prioritize gaps by the threat model, not by raw count.
5. Recommend the cheapest move to "open" each high-priority blackout: enable a log source, add a sensor, or author a rule.

## Output

`outputs/coverage-map-YYYY-MM-DD.md` (and optionally an ATT&CK Navigator layer JSON) — the coverage matrix, the blackout list split by cause, and the prioritized remediation plan.

## Notes

- A blackout is never solved by tuning — stop trying to lower a threshold on telemetry that doesn't exist.
- "Weak" cells are the most dangerous: they *look* covered on the matrix but never reliably fire. Audit them against `/propagation-forecast`.
