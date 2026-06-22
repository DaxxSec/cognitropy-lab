# /proof-ledger

Maintain the obligation ledger — the documentation-and-tracking spine of the workspace — across every revision of the show.

## Inputs

- The current spec catalog and verification report.
- The previous ledger snapshot (`outputs/proof-ledger-*.md`), if one exists.
- The cue-sheet revision id this snapshot pins to.

## Steps

1. For every obligation, record its current status: `discharged` (with evidence + robustness margin), `refuted` (with the counterexample), `open` (with the reason it isn't checkable), or `assumed` (with the assumption id and where it's gated — usually the weather tree).
2. Diff against the previous snapshot: which obligations changed status, which were added/removed, which assumptions were exercised on show day (actual vs. assumed wind, any failed cues from the as-fired log).
3. Compute the sign-off readiness: PASS only if every **safety** obligation is `discharged` or explicitly `assumed`-and-gated, and no safety obligation is `open` or `refuted`.
4. Record open items and their owner/next-action (which command re-runs to close each).
5. Pin the snapshot to the cue-sheet revision so the audit trail ties a discharge to an exact model.

## Output

`outputs/proof-ledger-YYYY-MM-DD.md`: the full obligation table with statuses and evidence, the diff vs. last snapshot, the sign-off readiness verdict, and the open-items list. This is the show's safety/quality record.

## Notes

- `assumed` ≠ `discharged`. The ledger must keep them visibly distinct or it lies about what's been proved.
- Never let the ledger drift from the actual cue-sheet revision — a snapshot against a stale model is worse than no snapshot.
- The ledger is the deliverable a reviewer or AHJ reads to understand *why* the show is believed safe and on-time; write it for that reader.
