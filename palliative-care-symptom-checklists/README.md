# Palliative Care Symptom Checklist Assistant

A Claude agent workspace for interdisciplinary palliative care teams that want to apply validated symptom-assessment instruments — consistently, quickly, and with documentation that survives audit.

> **Scope:** Decision-*support* for licensed clinicians. Not a clinical decision-maker. Not a diagnostic tool. Not a prescriber. Every draft it produces is reviewed by a human in the care team before anything is entered into the medical record.

---

## Why this workspace exists

Palliative care lives in structured, symptom-centric data. A hospice nurse on a home visit has twenty minutes with a patient, a partner, a dog, and a stack of paper scales. A palliative medicine attending rounding on an inpatient service may see twelve patients before lunch, each with ten scored symptoms. The instruments exist — ESAS-r, IPOS, PAINAD, Abbey Pain Scale, RASS, CAM, Karnofsky/PPS — and they are validated. What's missing is a consistent, auditable workflow that applies them the same way each time, flags meaningful changes, and produces a structured note the rest of the team can act on.

This agent does three things well:

1. **Administers checklists.** It walks the clinician through each item of a chosen instrument, enforces completeness, and computes composite scores using the published scoring rules.
2. **Trends data.** It compares today's scores against the last 3–7 captures for that patient, flags changes that cross clinically meaningful thresholds (e.g., ESAS-r item delta >= 1, IPOS aggregate delta >= 3), and highlights symptom-cluster patterns (pain + anxiety + sleep; dyspnea + cough + fatigue).
3. **Drafts structured documentation.** SBAR, progress note, family-meeting prep, goals-of-care discussion brief — all built from the structured data, all marked "Draft — clinician review required."

## What's in the workspace

```
palliative-care-symptom-checklists/
├── CLAUDE.md                              # Agent identity, capabilities, hard constraints
├── README.md                              # You are here
├── CREATION_REPORT.md                     # Why this workspace, build notes, design choices
├── context/
│   ├── role.md                            # Clinician's expectation of the agent
│   ├── project.md                         # Where this fits in the care pathway
│   ├── constraints.md                     # Legal, safety, PHI, and scope guardrails
│   └── for-agent/
│       ├── domain-knowledge.md            # ESAS-r, IPOS, PAINAD, Abbey, RASS, CAM, PPS
│       ├── workflows.md                   # Step-by-step procedures for each instrument
│       ├── environment.md                 # Where the agent runs, what it touches
│       └── tools.md                       # Tools available and how to use them
├── .claude/
│   └── commands/
│       ├── onboard.md                     # /onboard — introduces the agent to a user
│       ├── esas.md                        # /esas — run an ESAS-r assessment
│       ├── ipos.md                        # /ipos — run an IPOS assessment
│       ├── painad.md                      # /painad — Pain in Advanced Dementia
│       ├── trend.md                       # /trend — show symptom trajectory
│       └── sbar.md                        # /sbar — draft SBAR from captured data
├── prompts/
│   ├── admission-intake.md                # Starter prompt for initial consult
│   ├── weekly-ambulatory-review.md        # Starter prompt for outpatient follow-up
│   └── family-meeting-prep.md             # Starter prompt for goals-of-care conversations
├── planning/                              # Agent's working plans
├── resources/
│   ├── instruments.md                     # Canonical sources for each scale
│   ├── scoring-rules.md                   # How each instrument is scored
│   └── escalation-thresholds.md           # Default thresholds (tunable per team)
├── user-docs/
│   ├── getting-started.md                 # For the clinician lead
│   └── report.md                          # Example draft output
├── work-log/
│   └── session-log.md                     # Append-only log of agent sessions
└── outputs/                               # De-identified draft notes the agent produces
```

## Who this is for

- **Hospice and home-based palliative nurses** who do the bulk of symptom capture and need the checklist ritual to be lighter.
- **Palliative medicine clinicians** rounding on inpatient consult services who want trend-aware summaries.
- **Palliative care program directors** standardizing documentation across a team.
- **Clinical informatics groups** piloting structured palliative data before it enters the EHR.

It is *not* for patients or families to self-administer. It is not a replacement for a clinician's judgment. And it is not a prescribing tool.

## Supported instruments

| Instrument | Purpose | Items | Score range |
|---|---|---|---|
| ESAS-r (Edmonton Symptom Assessment System — revised) | Nine symptoms, 0–10 self-report | 9 | 0–90 composite |
| IPOS (Integrated Palliative care Outcome Scale) | Patient/staff-rated needs | 17 | 0–68 composite |
| POS-S (Palliative care Outcome Scale — Symptoms) | Symptom-focused subset | 10 | 0–40 |
| Abbey Pain Scale | Observer-rated pain in non-verbal adults | 6 | 0–18 |
| PAINAD (Pain in Advanced Dementia) | Observer-rated pain, dementia | 5 | 0–10 |
| RASS (Richmond Agitation-Sedation Scale) | Sedation / agitation level | 1 | -5 to +4 |
| CAM (Confusion Assessment Method) | Delirium screen | 4 features | present / absent |
| Karnofsky / PPS | Functional status | 1 | 0–100 / 0–100% |
| FICA | Spiritual assessment framework | 4 prompts | qualitative |

Scoring rules live in `resources/scoring-rules.md`. The agent applies them; it does not improvise them.

## Design principles

- **Instrument fidelity over convenience.** If an item says "over the past 24 hours" the agent asks about the past 24 hours. It does not paraphrase validated wording.
- **Clinician-in-the-loop.** Every output is a draft. Nothing is "final." Every note ends with the reviewing clinician's name field blank, awaiting human sign-off.
- **PHI-aware.** The workspace does not keep identifiers. Draft notes use a session-scoped placeholder ("Patient A", DOB redacted, MRN redacted). The clinician re-identifies at the EHR.
- **Trend-aware, not alarm-aware.** The agent surfaces changes. It does not trigger alerts to anyone but the clinician in front of it. There is no outbound notification channel.
- **Auditable.** Every session writes a `work-log` entry: which instrument, which thresholds tripped, what was drafted, timestamps.

## Getting started

Open `user-docs/getting-started.md` for the clinician-lead onboarding walkthrough. The short version:

1. Read `context/role.md`, `context/constraints.md`, and `resources/instruments.md`.
2. Try `/onboard` to see how the agent introduces itself.
3. Try `/esas` on a fictitious case to see a full assessment flow.
4. Review `resources/escalation-thresholds.md` and tune them with your medical director before using on a real case.
5. Do a three-clinician internal pilot before any real patient use.

## What this workspace is *not*

- Not a diagnostic tool.
- Not a prescribing tool.
- Not an EHR integration. (It drafts notes for a clinician to paste or rewrite into the EHR.)
- Not a patient-facing chatbot.
- Not HIPAA-certified infrastructure. Teams bringing this into a clinical environment must deploy inside their own compliant environment.

## License and attribution

Instrument reproduction rights, scoring methodology, and terms of use are the responsibility of the deploying team. Some instruments are free for clinical use with attribution; others require a license (e.g., IPOS through the Cicely Saunders Institute). The agent refuses to reproduce full instrument text unless the deploying team confirms licensing is in place — it references items by number and topic and relies on the team's licensed copy of the scale.

This workspace (the agent scaffolding, prompts, commands, and documentation) is part of the Cognitropy Lab. It is not itself a medical device. Use at your own discretion and under appropriate clinical governance.
