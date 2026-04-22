# Session Log

Append-only. One entry per agent session. De-identified metadata only — no PHI.

## Log format

```
[YYYY-MM-DDTHH:MM:SS±HH:MM] placeholder=Patient_A instrument=ESAS-r items_captured=9
  composite=44 flags=[pain_delta>=1, composite_delta>=3] output=outputs/2026-04-22-patient-a-esas.md
  duration_s=312 reviewer_tag=RN-001
```

## Rules

- No identifiers. Placeholders only.
- One line per session or a small multi-line block with indented detail.
- Do not log the content of the draft note — only its filename, composite, flag list, duration.
- Reviewer tag is a short role-scoped identifier the team chooses; it is not a user ID.

## Initial entry

No sessions yet. Pilot has not started.
