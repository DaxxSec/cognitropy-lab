# /carve-sqlite

Recover deleted and pre-checkpoint records from iOS SQLite databases by examining the WAL, rollback journal, freelist pages, and unallocated space — not just the live tables.

## Inputs

- Target database(s) (`sms.db`, `CallHistory.storedata`, `KnowledgeC.db`, etc.) **with** their `-wal` and `-shm` sidecars (and any `-journal`).
- The records of interest (time window, contact, message thread).
- A SQLite tool / carver (`sqlite3`, a WAL parser, a forensic recovery tool).

## Steps

1. **Preserve sidecars** — copy the DB *and* its `-wal`/`-shm`/`-journal` together; analysing the main file alone loses recent and deleted rows.
2. **Read the WAL** — extract frames not yet checkpointed into the main DB; these often hold the newest and some deleted rows.
3. **Walk freelist pages** — pages released by `DELETE` frequently retain intact row data until reused; recover them.
4. **Scan unallocated/slack** — after `VACUUM`, fragments may remain; carve record patterns where structure survives.
5. **Classify each recovered row** — *deleted-but-recoverable* vs *never-existed/partial fragment*; record source (WAL/freelist/unallocated) and confidence.
6. **Normalise timestamps** to UTC (note the epoch) and feed rows to `/reconstruct-timeline` and `/build-diagnosticity-matrix`.

## Output

`outputs/carve-<db>-YYYY-MM-DD.md`: recovered rows with their source location, recoverability classification, normalised timestamps, and a reliability note per row.

## Notes

- WAL vs main DB disagreement is normal; the WAL is usually more recent — report both states.
- A fragment without corroboration is low-weight evidence — never present a partial carve as a confirmed record.
