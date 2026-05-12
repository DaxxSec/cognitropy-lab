# Work Log Index

This file points to the per-session batch records and explains the naming convention. Real session content lives in dated files (`<YYYY-MM-DD><seq>.md`), not here.

## Naming Convention

- **One file per session.** A "session" is a continuous stretch of bench time under one artist.
- **Filename:** `YYYY-MM-DD<seq>.md` where `<seq>` is `A` for the first session of the day, `B` for the second, etc.
- **Schema:** every file follows `resources/batch-record-card.md`.

## Session Index

(Filled in by `/batch-log`. The first real entry will appear when the studio runs its first session under this workspace.)

| Date | Seq | Artist | Glass family | Pieces produced | Notes |
|------|-----|--------|---------------|------------------|-------|
| 2026-05-03 | A | <onboarded user> | <onboarded family> | 0 (workspace creation) | Initial workspace seeded; no glass worked |

## Hygiene Reminders

- A new session must not be opened while yesterday's outstanding follow-ups (24h, 7d, 30d, 90d inspections) are unattended
- A batch record is closed only when the **Outcomes** block, **Lehr program actually run** confirmation, and **Successional follow-ups scheduled** are populated
- If a record is reconstructed after the fact (artist forgot to log live), prefix the file with a `# RECONSTRUCTED` header so future `/lineage-trace` queries can weight the data appropriately
