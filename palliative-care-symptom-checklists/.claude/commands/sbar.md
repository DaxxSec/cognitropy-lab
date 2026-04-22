# /sbar

Draft an SBAR (Situation-Background-Assessment-Recommendation) handoff note from captured data.

## Input

- Session placeholder.
- Clinical question driving the handoff (e.g., "transfer from inpatient to home hospice", "urgent medical director review of symptom escalation", "pharmacist review for opioid rotation consideration").
- Most recent captures to reference.

## Steps

1. **Situation** — one-sentence statement of why the handoff is needed. Clinician-provided; agent structures.
2. **Background** — structure from clinician-provided key diagnoses, goals-of-care status, current phase of care.
3. **Assessment** — pull from most recent structured captures for this placeholder (ESAS-r / IPOS / Abbey / PAINAD / RASS / CAM / PPS). Report numbers and flags. Do not interpret.
4. **Recommendation** — leave as a clinician fill-in. The agent does **not** propose specific interventions.
5. "Draft — clinician review required" footer.

## Reminders

- The agent does not make the recommendation. It drafts the structured shell for the clinician to finish.
- PHI stays out of the draft. Use the session placeholder.
