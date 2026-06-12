# Executive Protection — Threat Assessment & Apprenticeship Progression Workspace

> A close-protection training officer's workspace where every threat assessment is also a graded step in an agent's apprenticeship — operational product and competency evidence in one artifact.

## What This Workspace Does

Executive protection (EP) lives and dies on **threat assessment**: knowing who might attack a principal, how, where, and when — and closing the gap between a hostile actor's plan and the protective measures that defeat it. This workspace gives a protective-detail training officer a structured way to produce that assessment work: protectee risk profiles, adversary work-ups, advance surveys, route analyses, surveillance-detection plans, attack-cycle mapping, and emergency action plans.

The twist — and the reason this workspace exists as a distinct artifact — is **apprenticeship progression tracking**. EP is a craft learned the way trades and clinical medicine are learned: by doing real work under graduated supervision until you can be *entrusted* to do it alone. This workspace treats each threat-assessment deliverable as a **workplace-based assessment (WBA)**. The same advance survey that protects tonight's venue is graded against a competency rubric, logged as evidence toward an **Entrustable Professional Activity (EPA)**, and used to decide whether the apprentice who wrote it is ready to run the next advance with less supervision. Operational quality drives the assessment; assessment drives progression; progression is bounded so that no apprentice ever works a live detail above their proven entrustment level.

The result is two products from one effort: a protectee is safer, and a named agent is measurably closer to journeyman.

## Why This Workspace Exists

Protective programs chronically separate "doing the job" from "developing the people who do the job" — and both suffer. Threat assessments get written once and filed; apprentice agents get advanced on tenure and gut feel rather than evidence. By making the assessment artifact and the competency record the *same object*, this workspace closes that loop: every piece of real protective work leaves an auditable training trail, and every progression decision is anchored to artifacts a second assessor could re-grade. It codifies the entrustment model (borrowed from competency-based medical and trade education) into close-protection terms, so a detail can grow its bench without ever putting an under-qualified agent between a principal and a threat.

## Getting Started

### Prerequisites

- A defined **protectee** (principal) and a lawful protective mandate / engagement.
- A **named apprentice roster** with each agent's current Dreyfus stage and EPA entrustment levels (seed `outputs/roster.md` from `context/references.md`).
- Open-source and client-provided **protective-intelligence inputs** (threat communications, prior incidents, public schedule, residence/venue details).
- Familiarity with `context/concepts.md` (threat model + competency model) before running graded commands.

### Quick Start

1. Clone this workspace and read `CLAUDE.md` and `context/concepts.md`.
2. Seed `outputs/roster.md` with your apprentices, their stage, and current EPA entrustment levels (template in `context/references.md`).
3. Run `/protectee-risk-profile` to establish the baseline threat exposure for the principal — assign an apprentice as author.
4. Run an operational command for the upcoming movement (`/advance-survey`, `/route-threat-analysis`, or `/surveillance-detection-plan`).
5. Run `/competency-signoff` on the produced artifact to grade it and log entrustment evidence, then `/progression-review` periodically to advance the apprentice and `/apprentice-tasking` to set the next assignment.

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/protectee-risk-profile` | Baseline threat-exposure profile for a principal (exposure factors, threat landscape, risk tier) | At engagement start and on any material change in the principal's profile |
| `/adversary-assessment` | Work up a specific threat actor across capability × intent × opportunity with BTAM warning behaviours | When a person of concern, fixated individual, or threat communication surfaces |
| `/advance-survey` | Venue / residence / route advance security survey with vulnerabilities, safe haven, medical, EAP hooks | Before any principal movement to a new site |
| `/route-threat-analysis` | Primary/alternate route analysis: choke points, ambush exposure, AOP drill points, timing | When planning vehicular movement between sites |
| `/surveillance-detection-plan` | Design a surveillance-detection route (SDR) and a pre-attack indicator watch list | When hostile surveillance is suspected or for routine pattern-of-life protection |
| `/attack-cycle-map` | Map a known/hypothesised threat onto the hostile planning cycle and find interdiction windows | When triaging a credible threat or red-teaming the protective posture |
| `/eap-builder` | Build and table-top a scenario emergency action plan (AOP, medical, fire, evac) | When finalising a movement plan or running contingency drills |
| `/competency-signoff` | Grade a finished assessment artifact against the rubric and log EPA entrustment evidence | Immediately after an apprentice completes any assessment deliverable |
| `/progression-review` | Place the apprentice on the ladder, gap-analyse the portfolio, set objectives | At review cadence (e.g. monthly) or before an entrustment decision |
| `/apprentice-tasking` | Generate the next supervised tasking targeting the apprentice's weakest competency | After a progression review, to assign deliberate practice |

## Directory Structure

```
executive-protection-threat-assessment-apprenticeship/
├── CLAUDE.md                 # Agent role, context refs, command list
├── README.md                 # This file
├── .claude/commands/         # 10 bespoke EP + apprenticeship commands
├── context/
│   ├── concepts.md           # Threat model, EPAs, entrustment scale, attack cycle, BTAM
│   ├── workflows.md          # Advance methodology, progression review, deliberate-practice loop
│   └── references.md         # Threat tiers, EPA roster, trauma criteria, standards & links
├── prompts/                  # Reusable prompt templates
└── outputs/                  # Graded assessments, roster, progression records
```

## Example Use Cases

### Onboarding a new principal with a trainee author
A new client engagement starts. A Shift-Agent apprentice runs `/protectee-risk-profile` under direct supervision; the artifact is graded with `/competency-signoff` against EPA-2, contributing the first evidence toward letting them profile principals with indirect supervision.

### A fixated individual surfaces in the client's mail
`/adversary-assessment` works the person of concern through capability/intent/opportunity and TRAP-18 warning behaviours; `/attack-cycle-map` locates where on the planning cycle they sit and which interdiction window (e.g. disrupt pre-attack surveillance) is most cost-effective.

### Advancing an agent from Advance Agent to Detail Leader
`/progression-review` shows EPA-1, -2, and -4 at unsupervised entrustment but EPA-6 (attack-cycle interdiction) lagging. `/apprentice-tasking` assigns a supervised `/attack-cycle-map` on a live person of concern as deliberate practice, with the gap closed before the entrustment decision.

### Pre-movement contingency rehearsal
Before a high-exposure public appearance, `/eap-builder` produces an attack-on-principal and medical EAP and a table-top script; the drill doubles as a WBA of the detail's junior agents' immediate-action competency.

## Recommended MCP Servers

- **Filesystem** — read/write graded assessments, the roster, and progression records under `outputs/`.
- **Web search / fetch** — open-source protective intelligence: news, court records, public schedules (lawful, protective-nexus OSINT only).
- **Mapping / geocoding** — route analysis, choke-point identification, nearest Level I/II trauma-center lookup for advance surveys.
- **Calendar** — ingest the principal's movement schedule to drive advance and route tasking.

## Legal & Ethical Considerations

- **Defensive scope only.** This workspace exists to protect a principal. It is not a tool for offensive targeting, harassment, or building dossiers on people absent a lawful, documented protective-intelligence nexus.
- **Privacy & data protection.** Protectee PII and any subject information are sensitive. Apply GDPR/CCPA principles (minimisation, purpose limitation, retention limits); never commit real PII to a public repository.
- **No surveillance of protected activity.** Do not treat lawful protest, journalism, or political speech as a threat absent articulable indicators of intended violence.
- **Lawful authority & use of force.** Detentions, searches, and force are governed by jurisdiction and licensing (PSP/PI/guard licensing, local firearms law). EP doctrine is *cover and evacuate*, not engage.
- **Entrustment as a safety control.** Apprentice progression is a duty-of-care matter: advancing an agent beyond demonstrated competency endangers the principal. Keep entrustment evidence-based and auditable.

## Technical References

- [U.S. Secret Service NTAC — Protective Intelligence & Threat Assessment](https://www.secretservice.gov/protection/ntac) — Exceptional Case Study Project; the "path to intended violence" research base.
- [ten Cate, *Entrustable Professional Activities* (NCBI / Academic Medicine)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3613304/) — the EPA + entrustment-scale model adapted here for EP.
- [Dreyfus model of skill acquisition](https://en.wikipedia.org/wiki/Dreyfus_model_of_skill_acquisition) — the novice→expert ladder mapped onto EP roles.
- [Meloy et al., TRAP-18 (terrorist radicalization assessment protocol)](https://www.gifrinc.com/trap-18/) — proximal warning behaviours used in `/adversary-assessment`.
- [ASIS International — Protection of Assets & risk standards](https://www.asisonline.org/) — professional body of knowledge and risk-assessment standards.
- [ISO 31000 — Risk management guidelines](https://www.iso.org/iso-31000-risk-management.html) — likelihood × impact framing for threat tiering.

## Optional plugin

If you have the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, additional global commands (`/workspace-foundational:context-sweep`, `/workspace-foundational:find-template`) are available; the workspace works without it.
