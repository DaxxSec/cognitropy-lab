# Custody Dossier Template

## Purpose

Render an integrity-verified chain-of-custody dossier — complaint to verified fix — for an external adjudicator (warranty, CARB referee, fleet audit, or owner handoff).

## Prompt Template

```
You are an emissions root-cause adjudicator producing a defensible case dossier. Verify integrity first; do not paper over a broken chain.

I have:

- **Case ID / VIN / vehicle:** [VALUES]
- **The ledger (ordered evidence entries with hashes):** [PASTE or path]
- **Committed diagnosis:** [ROOT CAUSE + supporting entry hashes]
- **Verification result:** [monitor pass/fail + drive cycle]
- **Recipient:** [owner / warranty / referee / fleet audit]

Please:
1. Walk the ledger and confirm each entry's prev-hash matches; report chain intact or the exact break point.
2. Assemble: case header → ordered evidence log → sensor-trust map → causal DAG → quorum tally → committed diagnosis → verification.
3. Gate PII (VIN/location) appropriately for the recipient.
4. Put the integrity verdict at the top, and write it so a non-specialist adjudicator can follow the reasoning.
```

## Expected Output

- An integrity verdict (chain intact / broken at entry N) up front
- A complete, ordered dossier from complaint to verified fix
- PII handled per recipient; saved to `outputs/cases/<case-id>/custody-dossier.md`
