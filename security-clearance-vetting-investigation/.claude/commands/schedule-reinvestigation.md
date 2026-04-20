# /schedule-reinvestigation

Convert a calendar-based reinvestigation plan into a condition-based schedule. This is the "predictive maintenance plan" equivalent.

## Inputs
- `SUBJ-ID` (required).
- Optional: override thresholds.

## Steps
1. Load baseline, last N scans.
2. Identify three families of triggers:
   - **Calendar anchor** — when is the legacy PR due, if any? (keep as a backstop)
   - **Event triggers** — list CE event categories that force out-of-cycle action (from `resources/continuous-vetting-triggers.md`).
   - **Condition triggers** — composite or per-guideline thresholds from `resources/risk-scoring-rubric.md`.
3. Choose the next scheduled scan interval:
   - Stable trend + composite < 1.5 → 180 days.
   - Stable + composite 1.5-2.5 → 120 days.
   - Stable + composite 2.5-3.5 → 90 days.
   - Any degrading trend → 30-60 days.
   - Composite ≥ 4 → escalate (not "wait for scan").
4. Write `user-docs/subjects/<id>/reinvest-plan-YYYYMMDD.md` with:
   - Calendar anchor.
   - Event triggers table.
   - Condition triggers table.
   - Next scheduled scan date.
   - "If X happens sooner, do Y."
5. Optionally emit `outputs/subjects/<id>/reinvest.ics` using the user's calendar MCP.
6. Log to work-log.

## Output sketch
A one-page plan the user can hand to a co-analyst and have it be actionable without further explanation.
