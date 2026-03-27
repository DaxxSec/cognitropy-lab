# /build-log — Modification History & Parts Log

Add entries to or review the complete modification and build history for your vehicle.

---

## When to Use This Command
- After installing any new part or performing any modification
- After a dyno session with new numbers to record
- When you want to review what's been done to the vehicle
- When troubleshooting and you need to know the last known-good configuration
- To generate a build summary for sharing or selling

---

## Sub-Commands

### Add a New Entry
Say: "add entry" or just describe what you did.

Provide:
1. **Date:** When was this done?
2. **What was done:** Description of the work or modification
3. **Parts used:** Brand, part number, source, cost (if you want to track it)
4. **Who performed the work:** You / shop / tuner
5. **Odometer at time of work:** Current mileage/km
6. **Before/after measurements:** (compression, power, AFR, boost — if applicable)
7. **Observations after install:** Did anything change in behavior?
8. **Notes:** Any issues, torque specs used, special considerations

The agent will save this to `work-log/YYYY-MM-DD-[descriptor].md`

---

### Review Build History
Say: "review history" or "show me what's been done."

The agent will:
1. Load all entries from `work-log/`
2. Present a chronological summary table
3. Calculate total documented spend (if costs were logged)
4. Identify the last dyno session and numbers
5. Note any open items or follow-ups from previous entries

---

### Find Last Known-Good Config
Say: "what was the last known-good state?" or "when was it running well?"

The agent will search work-log entries for the last time the car was noted as running properly, cross-reference any issues logged after that point, and help identify what changed.

---

### Generate Build Summary
Say: "generate build summary" or "write up what I've done."

The agent will create a formatted build summary document in `user-docs/build-summary-YYYY-MM-DD.md` covering:
- Full parts list
- Timeline of modifications
- Power progression (if dyno numbers are logged)
- Current configuration snapshot

---

## Entry Template

When saving to work-log/, each entry follows this format:

```markdown
# Build Log Entry — [DATE]

## Work Performed
[Description]

## Parts Used
| Part | Brand | Part # | Source | Cost |
|------|-------|--------|--------|------|
| | | | | |

## Performed By
[Self / Shop / Tuner — name if applicable]

## Odometer
[XXXXX miles / km]

## Measurements
- Before: [compression / power / other baseline if taken]
- After: [same measurements if taken]

## Post-Install Observations
[How did the car behave after this change?]

## Open Items / Follow-Up
[Anything to check or monitor after this change]

## Notes
[Torque specs, special considerations, lessons learned]
```
