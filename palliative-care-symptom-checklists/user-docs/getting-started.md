# Getting Started — For the Clinician Lead

This is the onboarding document for the person bringing this workspace into a palliative / hospice team. If you are a field clinician, you do not need to read this — start with the `/onboard` command.

## What this is

A Claude agent workspace that helps your team administer validated palliative symptom assessments (ESAS-r, IPOS, Abbey, PAINAD, RASS, CAM, PPS, FICA), compute composite scores, trend them across encounters, and draft structured notes for the EHR — all with the clinician kept firmly in the loop.

## What this is not

- Not a prescribing tool.
- Not a diagnostic tool.
- Not a medical device.
- Not HIPAA-certified infrastructure on its own — you bring that.
- Not a replacement for your documentation system; it drafts, you edit and sign.

## Step 1 — Read the scope

Before touching a clinical flow, read:
1. `CLAUDE.md` — the agent's identity and hard constraints.
2. `context/role.md` — what the agent does and doesn't do.
3. `context/constraints.md` — the guardrails.
4. `resources/instruments.md` — which instruments are supported and what licensing looks like.
5. `resources/escalation-thresholds.md` — the starting thresholds (you will tune these).

## Step 2 — Try the agent on fictitious cases

Use the `/onboard` command to meet the agent. Then try:
- `/esas` with a fictitious outpatient case
- `/painad` with a fictitious advanced-dementia case
- `/sbar` after you have captured a couple of instruments
- `/trend` after three ESAS-r captures on the same placeholder

No real patient data. Use "Patient A", "Patient B" placeholders.

## Step 3 — Tune the escalation thresholds

Open `resources/escalation-thresholds.md` with your medical director. The defaults are intentionally conservative; you will almost certainly want to tune them. Every change should be versioned with reviewer initials and date.

## Step 4 — Run the pilot

Work through `planning/pilot-plan.md`:
- Three clinicians (medical director, nursing lead, one other)
- Three fictitious cases (cancer outpatient, dementia home hospice, CHF inpatient)
- Metrics: time to complete, scoring agreement, draft acceptance

## Step 5 — Clear the readiness checklist

Work through `planning/deployment-readiness-checklist.md`. Every box checked. Compliance officer signs off. Medical director signs off.

## Step 6 — Train the team

One training session. One quick-reference card. One feedback channel.

## Step 7 — Use on real cases

With all of the above in place. Session-log review weekly. Threshold re-review every 180 days or sooner when clinical policy changes.

## When not to use the agent

- When the clinical question is clearly outside symptom assessment (diagnosis, prognosis, prescribing).
- When the clinician doesn't have a licensed copy of IPOS (for IPOS specifically).
- When you haven't yet tuned thresholds with the medical director.
- When the user is not a licensed clinician.
- When the situation is an emergency — call the on-call / 911 / local emergency services first.
