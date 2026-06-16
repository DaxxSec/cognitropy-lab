# /ingest-scan

Pull the OBD-II diagnostic feed into the ledger as structured evidence nodes — **before** clearing anything.

## Inputs

- A live scan-tool session or an exported scan report for the case vehicle
- Access to Mode 01 (live), 02 (freeze frame), 03/07/0A (DTCs), 06 (monitor results)
- The open case ID from `/open-case`

## Steps

1. **Capture freeze frame (Mode 02) first** — the snapshot of conditions when the code set. This evidence is destroyed by a code clear, so log it before any clearing.
2. Read stored (03), pending (07), and **permanent (0A)** DTCs; record each with its status. Permanent codes are the system's already-"committed" failures.
3. Pull **Mode 06** monitor test results (TID/MID, value vs limits) for any monitor implicated by the codes — these are the numbers behind a P0420-style code.
4. Capture a Mode 01 live-data baseline: STFT/LTFT, O₂/wideband, MAF, MAP, load, ECT/IAT, RPM at idle and at a steady cruise if drivable.
5. Append each item as its own evidence node (what/value/when/who/conditions/prev-hash). Do **not** interpret yet — that's later phases.

## Output

A batch of hash-linked evidence nodes appended to `outputs/cases/<case-id>/ledger.md`, tagged by source mode. A short index of what was captured.

## Notes

- **Never clear codes to "test" before this runs** — clearing resets freeze frame and readiness, erasing your best evidence.
- Note which readiness monitors are *incomplete*; an unrun monitor is missing evidence, not a pass.
