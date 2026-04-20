---
description: Schedule control work plus predictive-maintenance actions for instruments, observations, and assets.
---

# /mitigation-plan

## Inputs

- Current PM schedule in `resources/pm-schedule-template.md`
- Weather outlook (7 day)
- Known upcoming control missions
- Asset inventory (explosives, RACS charge counts, avalauncher readiness logs)

## Steps

1. Read the PM schedule. Compute days-since-last for each recurring item.
2. Flag **overdue** items: any item past its target cadence.
3. Flag **at-risk** items: within 2 days of cadence expiry.
4. Overlay the weather outlook:
   - Before any forecast storm cycle, require: weather station calibration current, precip gauge cleared, explosive inventory audited, delivery system pre-check complete.
   - Identify PM windows where weather permits access to remote sites.
5. Propose a 7-day combined schedule table:
   - Day / action / owner / location / estimated duration
6. Flag conflicts (e.g. PM visit to a site that overlaps a control mission same day).
7. Append the approved plan to `planning/plan.md`; pivots go to `planning/pivots/`.

## Output

- 7-day schedule table in markdown
- Overdue + at-risk lists
- Pre-storm readiness checklist for the next forecast cycle
