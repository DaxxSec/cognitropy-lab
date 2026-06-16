# /cross-validate-sensors

Byzantine-fault detection for the emissions network: cross-check each sensor against an independent reference and flag the ones that are lying *before* any of their data is trusted.

## Inputs

- The live-data and freeze-frame evidence nodes from `/ingest-scan`
- The cross-validation reference table (`context/workflows.md`)
- Vehicle-specific expected ranges where available

## Steps

1. For each sensor you might rely on, pick an **independent** cross-check: MAF vs MAP+RPM+VE; upstream O₂ vs commanded-λ / propane response; downstream O₂ vs exhaust-leak check; ECT vs ambient at cold soak; fuel-pressure PID vs mechanical gauge.
2. Classify each node: **faithful** (agrees with its check), **crashed** (no/dead signal — exclude), or **Byzantine** (alive but disagreeing — quarantine).
3. For each Byzantine flag, record *the lying signature* (e.g. "MAF reads 3.1 g/s at idle vs ~4.5 expected from MAP/RPM → reads low, drives false-lean trims").
4. Treat a Byzantine sensor as a **candidate root cause itself**, not as input evidence.
5. Append the validation verdicts as evidence nodes; list which sensors are now admissible into quorum.

## Output

A sensor-trust map appended to the ledger: faithful / crashed / Byzantine with the cross-check that decided each, plus any sensor promoted to candidate root cause.

## Notes

- A skewed O₂ or a low-reading MAF is the single most common reason a P0420/P0171 is misdiagnosed — never accept a sensor's value as ground truth without an independent witness.
- A downstream O₂ that's "active" with a good front sensor usually means an **exhaust leak fooling it**, not a dead catalyst.
