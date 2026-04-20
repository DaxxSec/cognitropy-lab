# Baseline Profile Intake

Use when the user wants to add a new subject to the tracked caseload. Drops into the `/intake-subject` flow.

```
I need to onboard a new subject for tracking. Let's walk through a baseline profile intake, step by step, using placeholder identifiers only.

For each item below, either give me the answer or say "skip":

1. Clearance level (TS, S, Public Trust, Tier 1/2/3/4/5, etc.):
2. Year of last eligibility determination:
3. Current investigation tier (T3R, T5R, etc.):
4. Position sensitivity / mission criticality on a 1-5 scale, where 5 = national-security critical:
5. Access program *categories* (I do NOT want program names — categories like "compartmented," "special access," "cryptologic," "fiscal"):
6. Any prior adverse issue categories by SEAD 4 guideline letter (A-M):
7. Any mitigation already on record (SOI, remediation, program enrollment):

Once I have those, assign a SUBJ-NNNN ID, write the baseline under outputs/subjects/, and propose a first drift-scan date.
```
