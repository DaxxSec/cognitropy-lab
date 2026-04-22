# Creation Report: palliative-care-symptom-checklists

**Date built:** 2026-04-22
**Cognitropy Day:** 28
**Primary Category:** Medical & Health
**Primary Domain:** palliative care symptom management
**Technique Prompt:** using standardized inspection checklists
**Crossover:** No

## Why this workspace

Palliative care lives in structured symptom data, and the instruments to capture that data already exist and are validated: ESAS-r, IPOS, PAINAD, Abbey Pain Scale, RASS, CAM, Karnofsky/PPS, FICA. What palliative teams typically don't have is a consistent, auditable workflow that applies those instruments the same way every visit, flags clinically meaningful changes across serial captures, and produces a structured draft note that saves the clinician the mechanical write-up time while keeping human judgment firmly in the loop.

The Cognitropy technique for today is "using standardized inspection checklists." Palliative symptom assessment is a near-textbook fit: each instrument is itself a checklist, and the workflow the agent enforces is essentially a sequence of inspection passes — verify item-level completeness, compute the composite, compare against prior captures, note what crossed a threshold, draft the documentation.

## Design choices

**Decision-support, never decision-maker.** The hard constraint — no prescribing, no dosing, no diagnosis — runs through CLAUDE.md, constraints.md, and every slash command. The agent's value is in *structure and consistency*, not in clinical judgment. Anything that starts to look like judgment gets deferred back to the licensed clinician.

**Instrument fidelity.** The agent asks the exact items of the published scale with the exact time windows and wording. It does not paraphrase validated language. This is what makes longitudinal comparison meaningful.

**PHI-aware by default.** No patient identifiers in the workspace. Session-scoped placeholders ("Patient A"). The clinician re-identifies at the EHR. The workspace documents assume the deploying team will bring their own compliant infrastructure.

**Trend-aware, not alarm-aware.** The agent surfaces changes to the clinician in front of it. It does not page, email, or notify externally. There is no outbound channel.

**Licensing awareness.** Some instruments (notably IPOS) require a license from the Cicely Saunders Institute. The agent references items by number and topic rather than reproducing copyrighted full-text items. Teams must bring their own licensed copies.

## Commands built

- `/onboard` — introduces the agent to a new clinician-user
- `/esas` — walk through the ESAS-r assessment, compute composite
- `/ipos` — walk through the IPOS assessment, compute composite
- `/painad` — Pain in Advanced Dementia observer assessment
- `/trend` — display symptom trajectory across last N captures
- `/sbar` — draft an SBAR handoff note from captured data

## Reference instruments documented

| Instrument | Documented in resources/ |
|---|---|
| ESAS-r | Yes |
| IPOS | Yes |
| POS-S | Yes |
| Abbey Pain Scale | Yes |
| PAINAD | Yes |
| RASS | Yes |
| CAM | Yes |
| Karnofsky / PPS | Yes |
| FICA | Yes |

## Security scan

Workspace scanned for leaked secrets (API keys, tokens, passwords, private keys) prior to commit. None found. Placeholders and example values only.

## Pilot recommendation

Before any real-patient use, the deploying team should do a three-clinician internal pilot on fictitious cases to validate:

1. Scoring matches their own hand-calculation of the instruments.
2. Escalation thresholds in `resources/escalation-thresholds.md` match their team's policy.
3. Draft notes match their local documentation style enough to be worth editing from.
4. PHI-handling policy is followed.

## Notes for future iteration

- An EHR integration (FHIR write-back of structured observations) is the obvious next step, deliberately out of scope for this initial workspace.
- A caregiver-facing interview mode (proxy-reported symptom assessment for home hospice) would extend utility but needs careful framing to avoid turning the agent into a patient-facing tool.
- Bereavement-risk screening (e.g., PG-13, Brief Grief Questionnaire for caregivers) could live alongside the patient instruments.
