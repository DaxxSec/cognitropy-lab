# /reconstruct-timeline

Fuse iOS pattern-of-life artifacts into a single, time-normalised activity timeline so events can be ordered and gaps surfaced — the raw material for the diagnosticity matrix.

## Inputs

- Parsed `KnowledgeC.db` (app usage, device lock/unlock, focus, now-playing).
- `powerlog` / `CurrentPowerlog.PLSQL` (charge, screen-on, battery events).
- `CallHistory.storedata` and `sms.db` (communications), plus carved rows from `/carve-sqlite`.
- The window of interest.

## Steps

1. **Extract events** from each source with their native timestamps and event types.
2. **Normalise time to UTC** — resolve Unix vs Mac-absolute (2001 epoch) vs Mach-continuous, recording the conversion per source (see `context/references.md`).
3. **Merge** into one ordered timeline; tag each event with its source DB for provenance.
4. **Flag gaps and overlaps** — periods with no activity, or contradictory events (e.g. screen-on during a claimed power-off), are themselves evidence.
5. **Mark corroboration** — events confirmed by ≥2 independent sources get higher weight; single-source events are flagged.

## Output

`outputs/timeline-YYYY-MM-DD.md` (and optional CSV): the unified UTC timeline with per-event source/provenance, corroboration level, and a list of flagged gaps/contradictions for the ACH matrix.

## Notes

- A timeline is an interpretation, not a fact — every event keeps its source and conversion so it can be challenged.
- Device-usage events (KnowledgeC) often discriminate "was the user active then?" better than communications artifacts alone.
