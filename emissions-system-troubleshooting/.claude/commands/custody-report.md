# /custody-report

Verify the ledger's integrity end-to-end and export the full chain-of-custody dossier + committed diagnosis — the defensible artifact for a warranty claim, CARB referee, or fleet audit.

## Inputs

- A case ledger (ideally with a committed diagnosis and a passing verification)
- The recipient context: owner handoff, warranty claim, referee program, or fleet audit

## Steps

1. **Integrity check:** walk the ledger from genesis; confirm each entry's `prev-hash` matches the previous entry's hash (the log-matching property), timestamps are monotonic, and there are no gaps. Report any break — a broken chain invalidates the dossier.
2. Assemble the dossier: case header, the ordered evidence log, the sensor-trust map (including any Byzantine sensors and why), the causal DAG, the quorum tally, the committed diagnosis with its supporting hashes, and the verification result.
3. Redact or gate PII (VIN, location) per the recipient — share only with the owner, authorized repairer, or adjudicator.
4. Render to a clean document under `outputs/cases/<case-id>/custody-dossier.md` (and PDF if needed).
5. State the integrity verdict (chain intact / broken) at the top so the reader knows the evidence is tamper-evident.

## Output

`outputs/cases/<case-id>/custody-dossier.md` — an integrity-verified, provenance-complete record from complaint to verified fix.

## Notes

- This is the workspace's payoff: a diagnosis another party can audit and trust because the evidence trail is intact and reproducible.
- If the integrity check fails, **do not** ship the dossier — find where the chain broke (an edited-in-place entry?) and reconstruct from the append-only history.
