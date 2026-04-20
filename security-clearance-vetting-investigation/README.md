# Security Clearance Vetting & Predictive Reinvestigation

> **Cognitropy Lab — Day 26 (2026-04-20)**
> Category: *Security & Intelligence* · Domain: *security clearance vetting investigation* · Technique: *with predictive maintenance scheduling*

A Claude Code / Cowork agent workspace for personnel security specialists, background investigators, and adjudicators. It adapts **predictive-maintenance scheduling** — the reliability-engineering discipline that services equipment based on observed condition rather than fixed calendar intervals — to the world of **personnel security vetting**.

In the 5-year / 10-year Periodic Reinvestigation (PR) model, a cleared subject is re-examined on a fixed cadence regardless of what has happened in the intervening years. That model is being retired in favor of **Trusted Workforce 2.0 / Continuous Vetting (CV)**, where alerts from a suite of data providers flow into the adjudicating agency in near real-time. The missing piece for most shops is a disciplined way to **prioritize the human investigative capacity** across hundreds or thousands of CV subjects. This workspace gives an analyst the scaffolding to do exactly that — the same way a manufacturing plant uses vibration, temperature, and oil-analysis trends to schedule bearing changes before a failure.

---

## Who this is for

- **Personnel security specialists** working Industrial Security (NISP) or federal civilian / DoD cases.
- **Background investigators** (Tier 3 / Tier 5, periodic reinvestigations, and CE triage) at agencies such as DCSA, OPM-era successors, DoS/DS, IC components, or cleared primes.
- **Insider-threat analysts** who receive alerts and need to decide "inquiry vs. full reinvestigation vs. escalate to adjudicator."
- **Facility Security Officers (FSOs)** running internal cleared-personnel programs under 32 CFR Part 117 / NISPOM.

It is **not** a replacement for DISS, NBIS, or any authoritative adjudication system. It is a planning and reasoning aid that sits alongside them.

---

## The predictive-maintenance analogy

| Reliability Engineering | Personnel Security |
|---|---|
| Asset (pump, bearing, HVAC unit) | Cleared subject |
| Nameplate data / manufacturer specs | Original SF-86 + baseline investigation |
| Condition sensors (vibration, temp, oil) | CE data feeds (financial, criminal, foreign travel, public records) |
| Health index trending upward | Risk-indicator drift |
| P-F curve (Potential → Functional failure) | Mitigation window between first anomaly and disqualifying event |
| Planned maintenance window | Scheduled inquiry, expanded investigation, or re-adjudication |
| Run-to-failure (for cheap assets) | Calendar-based PR (legacy model) |
| Condition-based maintenance | Continuous Vetting with risk-weighted review |
| Prescriptive maintenance (AI-driven) | Risk model that recommends *when* and *what kind* of investigative action |

The **drift-scan** command is the sensor reading. The **schedule-reinvestigation** command is the maintenance plan. The **adjudicate** command is what happens after the wrench goes in.

---

## Getting started

```bash
# 1. Clone (or pull) this workspace into your Claude Code / Cowork session
git clone https://github.com/DaxxSec/cognitropy-lab.git
cd cognitropy-lab/security-clearance-vetting-investigation

# 2. Run the onboard command in your agent
/onboard

# 3. Ingest your first subject (use a test/synthetic profile first\!)
/intake-subject

# 4. Run a drift scan
/drift-scan SUBJ-0001
```

The agent will read `CLAUDE.md`, pull context stubs, and walk you through each step. All artifacts land in `outputs/`; polished deliverables land in `user-docs/`.

---

## Command reference

| Command | Purpose | Typical output |
|---|---|---|
| `/onboard` | Interview to capture your role, agency/company, authorities, caseload shape, and tool stack | `context/role.md`, `context/project.md`, `context/constraints.md` |
| `/intake-subject` | Ingest baseline profile (pseudonymized). Captures SF-86 scope answers, clearance level, eligibility date, access programs | `outputs/subjects/<id>/baseline.md` |
| `/drift-scan` | Score each of the 13 SEAD 4 guidelines against current evidence; compute a risk index and trend | `outputs/subjects/<id>/scan-YYYYMMDD.md` |
| `/adjudicate` | Apply the SEAD 4 *whole-person concept* to the current findings; produce a mitigating-vs-disqualifying analysis | `user-docs/subjects/<id>/adjudicative-memo.md` |
| `/schedule-reinvestigation` | Condition-based reinvestigation plan: calendar triggers, event triggers, and inspection intervals | `user-docs/subjects/<id>/reinvest-plan.md` |
| `/continuous-eval` | Triage a single CE alert end-to-end: initial inquiry, evidence gathering, recommended disposition | `outputs/ce-alerts/<alert-id>.md` |

All commands are defined under `.claude/commands/` and can be edited to match your agency's terminology.

---

## Directory layout

```
security-clearance-vetting-investigation/
├── CLAUDE.md                        # Lightweight agent brief (loaded every prompt)
├── README.md                        # This file
├── CREATION_REPORT.md               # Why this workspace exists
├── context/
│   ├── project.md                   # Project definition (populated by /onboard)
│   ├── role.md                      # User's role
│   ├── constraints.md               # Boundaries, handling caveats
│   └── for-agent/
│       ├── domain-knowledge.md      # SEAD 4, TW 2.0, CE, PM analogy
│       ├── workflows.md             # Step-by-step workflows
│       ├── environment.md           # User's tool stack
│       └── tools.md                 # MCPs and integrations
├── .claude/
│   └── commands/                    # Slash commands
├── prompts/                         # Reusable prompt templates
├── resources/                       # Checklists, schemas, reference data
├── planning/                        # Active plan + pivots
├── work-log/                        # Dated session logs
├── user-docs/                       # Polished, user-facing deliverables
└── outputs/                         # Agent-generated raw artifacts
```

---

## Recommended MCP servers / integrations

You do **not** plug authoritative clearance systems into an LLM. That would violate every rule in the IS book. Instead, think in terms of **scratchpad integrations** that help you triage and plan outside of DISS/NBIS:

- **Filesystem MCP** — for ingest of exported CSV/PDF case files (after redaction).
- **Obsidian / Notes MCP** — if you keep case notebooks locally.
- **Calendar MCP** — for materializing the reinvestigation schedule.
- **SQLite MCP** — for small local risk-score history per subject.
- **Time-series MCPs** — if you want real PM-style trending.

Do **not** connect: authoritative PII sources, DISS / NBIS / Scattered Castles, FBI / LEA systems, financial provider APIs, or anything that could pull real subject data into a model without an explicit authority letter. See `context/constraints.md`.

---

## Example use cases

1. **Quarterly book review** — Run `/drift-scan` in batch across your caseload, sort by risk index delta, produce a prioritized list of ten subjects warranting extra attention.
2. **Single CE alert** — A subject hits a bankruptcy alert; `/continuous-eval` walks you through an inquiry, maps it to Guideline F (Financial Considerations), and drafts initial interview questions.
3. **Pre-SOR preparation** — Before drafting a Statement of Reasons, use `/adjudicate` to organize mitigating vs. disqualifying conditions under the whole-person concept.
4. **Reinvestigation backlog planning** — Use `/schedule-reinvestigation` to convert a calendar-based backlog into a condition-based queue, freeing investigator hours for actual risk.

---

## Ethical / legal considerations

This workspace is a **reasoning aid**. It does not make determinations. It does not talk to adjudicators on your behalf. It does not store PII that is not already under your lawful custody, and it should never be pointed at systems where you lack authority.

- **Adjudicative determinations** remain the responsibility of the agency adjudicator under SEAD 4 / EO 12968 / EO 13467.
- **Due process** for the subject is non-negotiable. Nothing produced here is a substitute for a Statement of Reasons, Reply, or Personal Appearance.
- **Bias awareness** — a risk model is only as good as its inputs. If a guideline's weighting feels off for your mission, tune it in `resources/risk-scoring-rubric.md` and document the rationale.
- **Handling caveats** — Artifacts may be FOUO / CUI depending on inputs. Decorate the agent's outputs with the appropriate banner via `/onboard`.

---

## Cognitropy Lab metadata

- **Day number:** 26
- **Built:** 2026-04-20
- **Primary category:** Security & Intelligence
- **Primary domain:** security clearance vetting investigation
- **Technique:** with predictive maintenance scheduling
- **Crossover:** no
- **Seed hash:** cognitropy.py date-seeded RNG for 2026-04-20

See `CREATION_REPORT.md` for why this particular combination was interesting.
