# Pilot Plan

Before any real-patient use, run a three-clinician pilot on fictitious cases.

## Goals
1. Verify scoring matches the team's hand-calculation of each instrument.
2. Verify escalation thresholds match the team's clinical policy.
3. Verify draft-note structure matches local documentation style enough to be worth editing from.
4. Verify PHI-handling policy holds (no identifiers on disk, session-scoped placeholders).

## Participants
- 1 medical director (or palliative attending)
- 1 nursing lead (hospice RN or palliative APRN)
- 1 other team member (social worker, chaplain, or pharmacist)

## Cases
Use three fictitious cases covering:
- Case A: advanced cancer, outpatient, self-reporting — ESAS-r focus
- Case B: advanced dementia, home hospice, proxy-reporting — PAINAD focus
- Case C: advanced CHF, inpatient consult, transition-of-care — IPOS + PPS + SBAR focus

## Metrics
- Time to complete each assessment (target: ≤ 5 minutes for ESAS-r, ≤ 10 for IPOS)
- Composite score agreement with hand-calculation (target: 100%)
- Draft note acceptance (target: ≥ 80% usable with light edits)
- Threshold tuning decisions made (document each in `resources/escalation-thresholds.md`)

## Exit criteria
- All three scoring validations pass
- Medical director sign-off on escalation thresholds
- PHI-handling spot check passes
- Documented training plan for the broader team
