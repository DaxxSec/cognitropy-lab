# Project Context

This workspace is one agent instance within a palliative / hospice program's documentation and decision-support stack. It is intentionally small in scope: it replaces paper-and-clipboard symptom capture with a structured, trend-aware, draft-generating assistant.

## Where it fits in the care pathway

1. **Referral / intake.** Patient is referred to palliative care. A baseline is needed.
   → Clinician runs `/esas` or `/ipos` with the agent to capture the first structured symptom profile.
2. **Serial assessment.** Home visits, clinic follow-ups, or inpatient rounds.
   → Clinician re-runs the same instrument. Agent compares against prior captures and flags meaningful changes.
3. **Interdisciplinary team meeting.** The IDT reviews cases weekly.
   → Agent produces a one-page trend summary per patient: symptom trajectory, notable changes, draft SBAR.
4. **Family / goals-of-care meeting.** The team prepares for a conversation about goals.
   → Agent drafts a meeting-prep brief from the structured data: symptom burden, functional trajectory, open unmet needs.
5. **Transition of care.** Change in site of care (home → inpatient, inpatient → hospice unit, etc.).
   → Agent produces a draft handoff note from the most recent captures.

## What the workspace does *not* do

- It is not an EHR. Draft notes are *drafts*; a clinician pastes, edits, and signs in the actual EHR.
- It is not a population-health tool. It works one patient, one session at a time.
- It does not integrate with remote patient monitoring, wearables, or home sensors.
- It does not make prognostic predictions. Instruments like PPS/Karnofsky capture functional status; the clinician interprets what that implies for prognosis.

## Stakeholders

- **Medical director / palliative lead** — sets the escalation thresholds, approves use.
- **Nursing / APRN lead** — approves workflow fit, trains field clinicians.
- **Compliance / privacy officer** — approves PHI handling and deployment environment.
- **Clinical informatics** — decides whether and how output flows into the EHR.

## Deployment assumption

The workspace is assumed to run inside the deploying organization's compliant environment. Patient data never leaves that environment. No identifiers are written to this workspace on disk unless the team's compliance officer has explicitly approved a local working copy.
