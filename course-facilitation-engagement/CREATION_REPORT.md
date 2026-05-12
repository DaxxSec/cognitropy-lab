# Course Facilitation Engagement Workspace — Creation Report

**Date Created:** 2026-05-04
**Template:** `course-facilitation-engagement` v1.0
**Category:** Education & Training
**Domain:** Course Facilitation Engagement
**Technique:** Using Stakeholder Communication Templates
**Cognitropy Day:** 40

## Purpose

This workspace operationalizes the multi-stakeholder communication system that keeps a live cohort course engaged from kickoff through certification. The technique that organizes the workspace — *stakeholder communication templates* — turns ad-hoc facilitator messaging into a parameterized library that scales across cohorts and audiences (learners, managers, sponsors, facilitators, admins, SMEs, alumni).

Course delivery is where most learning programs lose ROI: curriculum is solid but cadence falls off mid-cohort. The workspace pairs the engagement frameworks that actually predict completion (Community of Inquiry, Self-Determination Theory, Five Moments of Need, Kirkpatrick's New World Model, Universal Design for Learning, Mendelow's Power–Interest, Mitchell-Agle-Wood salience) with a 40+ template library that an L&D team can run from day one — and with seven slash commands that produce the cadence calendar, multi-stakeholder recaps, midpoint pulses, triggered escalations, and Kirkpatrick-aligned sponsor readouts.

## Workspace Contents

### Core Documentation (3 files)
- `CLAUDE.md` — agent role, command catalogue, foundational instructions
- `README.md` — full overview, command reference, directory structure, frameworks, use cases, references
- `CREATION_REPORT.md` — this file

### Context (3 files at top + 4 in `for-agent/`)
- `context/project.md` — course profile placeholder, populated by `/onboard`
- `context/role.md` — facilitator/L&D role placeholder
- `context/constraints.md` — privacy, accessibility, brand voice, compliance, channel etiquette
- `context/for-agent/domain-knowledge.md` — substance: four-layer engagement model, stakeholder taxonomy, communication phases, template grammar, signals, frameworks crib sheet, common failure modes
- `context/for-agent/workflows.md` — five concrete workflows with decision trees (mapping, cadence, triggered outreach, sponsor readout, alumni hand-off)
- `context/for-agent/environment.md` — LMS / email / messaging / calendar / pulse / video setup placeholder
- `context/for-agent/tools.md` — channel and integration cheatsheets (Canvas, Moodle, Cornerstone, Docebo, Workday Learning, 360Learning, Gmail, Outlook, Slack, Teams, calendar, pulse tools, video, accessibility tooling, MCP recommendations)

### Slash Commands (7 files)
- `.claude/commands/onboard.md` — interview to capture course / cohort / stakeholders / channels / voice / goals / privacy
- `.claude/commands/map-stakeholders.md` — Power–Interest scoring, Mitchell-Agle-Wood salience, RACI by phase
- `.claude/commands/draft-cadence.md` — pre/during/post calendar generator with template IDs and approver attach
- `.claude/commands/recap-module.md` — four-audience module recap pack (learner, manager, facilitator, sponsor)
- `.claude/commands/pulse-check.md` — pulse design, deploy, aggregate, stakeholder-specific summaries, change-in-response
- `.claude/commands/at-risk-outreach.md` — triggered escalation chain (learner → cohort → manager → sponsor) with suppression conditions
- `.claude/commands/sponsor-readout.md` — Kirkpatrick-aligned executive readout

### Multi-Step Prompts (3 files)
- `prompts/cohort-kickoff-pack.md` — render the entire pre-launch artifact pack in one pass
- `prompts/silent-cohort-revival.md` — whole-cohort disengagement intervention (diagnose-first pulse, format change, published change-in-response, recovery tracking)
- `prompts/exec-sponsor-quarterly-readout.md` — ongoing-program quarterly aggregation across cohorts

### Resources / Reference (3 files)
- `resources/stakeholder-template-library.md` — 40+ parameterized templates organized by `<phase>-<stakeholder>-<intent>-<channel>`
- `resources/engagement-frameworks-reference.md` — operational gloss for CoI, SDT, Kirkpatrick, Five Moments of Need, Power–Interest, salience, UDL, Knowles, plain-language, WCAG 2.1 AA, flow
- `resources/engagement-metrics-reference.md` — signal catalog by layer (Logistical / Behavioral / Cognitive / Affective), thresholds, severity classification, source-quality caveats, suppression conditions, privacy floor

### Planning / Working Files
- `planning/plan.md` — live cadence calendar template
- `outputs/.gitkeep` — destination for rendered drafts, recaps, readouts, pulse summaries
- `work-log/session-log.md` — daily log template
- `work-log/2026-05-04.md` — workspace-creation log entry
- `user-docs/getting-started.md` — facilitator quick-start
- `user-docs/report.md` — cohort-close retrospective template

## Key Design Decisions

1. **The single canonical skeleton was authored from scratch.** Per `WORKSPACE_SPEC.md` and the wireless-protocol-re quality bar, every `{{PLACEHOLDER}}` was replaced with bespoke content written specifically for *course facilitation engagement using stakeholder communication templates* — no generic `/analyze` or `/triage` carried in.

2. **Frameworks anchor every template.** Each template in the library carries a CoI-presence tag, an SDT-driver tag, and (where applicable) a Five-Moments-of-Need tag. The agent uses these to verify cadence balance during `/draft-cadence`.

3. **Stakeholder taxonomy is the schema.** Twelve named stakeholder roles with default salience classes; the `<phase>-<stakeholder>-<intent>-<channel>` template ID grammar makes the library searchable and extensible.

4. **Triggered outreach is autonomy-preserving by default.** The escalation chain begins with the lightest learner-facing nudge and only escalates to manager / sponsor lanes after time has been given for the lighter touch to land — and never without consent and salience scoring.

5. **Sponsor readouts move attention up the Kirkpatrick levels.** The default sponsor cadence and the `/sponsor-readout` command resist the smile-sheet trap by demanding Level-3 evidence (manager-observed change, application plans, peer-reviewed artifacts) by D+30.

6. **Privacy and accessibility are floors, not options.** UDL multiple-means and WCAG 2.1 AA appear as required checks before any send; learner behavioral traces are aggregated by default and only individualized to managers under named consent.

## Files Created
Total: **27 files** across **10 directories**

| Directory | Files | Purpose |
|-----------|-------|---------|
| Root | 3 | Core documentation |
| context/ | 3 | Project, role, constraints |
| context/for-agent/ | 4 | Domain knowledge, workflows, environment, tools |
| .claude/commands/ | 7 | Slash command implementations |
| prompts/ | 3 | Multi-step prompt templates |
| resources/ | 3 | Template library + frameworks + metrics references |
| planning/ | 1 | Live cadence calendar template |
| outputs/ | 1 | (.gitkeep) |
| user-docs/ | 2 | Quick start + cohort-close report template |
| work-log/ | 2 | Session-log template + creation-day log |

---

**Workspace Status:** READY FOR USE
**Last Updated:** 2026-05-04
**Version:** 1.0
