# Getting Started — Course Facilitation Engagement Workspace

This guide assumes you have a cohort course you are about to launch (or are mid-flight on) and you want to put a structured stakeholder communication system in place.

## In 30 minutes

1. **Run `/onboard`.** Allow ~20 minutes; have your cohort dates, stakeholder names, and channel access on hand. The agent populates `context/project.md`, `context/role.md`, `context/constraints.md`, `context/for-agent/environment.md`, and `context/for-agent/tools.md`.

2. **Run `/map-stakeholders`.** Allow ~10 minutes. The agent produces `outputs/stakeholder-register-{cohort_id}.md` with the Power–Interest matrix, salience, and RACI.

3. **Quick scan of `resources/stakeholder-template-library.md`.** The library is the operational asset — skim it once to know what is there before you draft the first send.

## Before kickoff

1. **Run `/draft-cadence`.** The agent populates `planning/plan.md` with the full pre/during/post calendar and surfaces any `<<NEW>>` template gaps.

2. **Run `prompts/cohort-kickoff-pack.md`.** The agent renders all pre-launch artifacts as approval-ready drafts in `outputs/{cohort_id}/`.

3. **Route through approvers.** The RACI from the stakeholder register names who signs off on what; do not skip this step even if it feels redundant on the first cohort.

## During the cohort

- **After every module: `/recap-module`.** Within 24h. Four artifacts: learner recap, manager nudge, facilitator log, sponsor highlight (if Definitive).
- **At the midpoint: `/pulse-check`.** Five working days from pulse close, publish what you are changing in response.
- **Whenever a signal trips: `/at-risk-outreach`.** Run for individual or cohort scope; the chain is autonomy-preserving by default.
- **If the cohort goes silent: `prompts/silent-cohort-revival.md`.** Diagnose first, message second.

## After the cohort

- **`/sponsor-readout`** within D+30. Kirkpatrick-aligned, ≤2 pages, named decision asked.
- **`post-learner-celebrate-email`** at D+0, **`post-learner-reflect-email`** at D+1, **`post-manager-nudge-email`** at D+7.
- **Alumni invitation** at D+30.
- **Long-term reinforcement** at D+60, D+90, D+180.

## Operating principles

1. **Templates are drafts.** The agent renders; the human approves and sends.
2. **One ask per message.** If the message has three asks, send three messages or build a checklist asset.
3. **Plain language, Grade 8 default** for learner copy.
4. **Time-bound deadlines** with ISO dates and time zones. No "next Tuesday".
5. **Graceful exit** on every nudge. Always a path to opt out.
6. **No surprises in the sponsor readout.** Anything the sponsor reads at close should have appeared in cadence at least once before.

## Where things live

- `CLAUDE.md` — agent role and stub
- `README.md` — comprehensive overview (read once)
- `context/` — your cohort, role, constraints, environment, tools
- `context/for-agent/` — domain knowledge, workflows, depth-of-substance
- `.claude/commands/` — slash commands
- `prompts/` — multi-step prompts the agent executes against the workspace state
- `resources/` — the template library and the framework reference
- `planning/plan.md` — the live cadence calendar
- `outputs/` — rendered drafts, recaps, readouts, pulse summaries
- `work-log/<YYYY-MM-DD>.md` — daily log of communications and signals
- `user-docs/` — facilitator-facing reference

## When to ask for help

- The cadence calendar feels too heavy for the cohort: re-run `/draft-cadence` with a "lighter" preference and trim the optional rows.
- Sponsor wants a pre-cadence preview: render `cohort-kickoff-pack.md` and walk it with the sponsor's chief of staff first.
- Compliance reviewer is a bottleneck: front-load a batch review at T-21 covering all pre-launch artifacts; per-message review is the wrong shape.
- The cohort is regulated: confirm `context/constraints.md` carries the named compliance owner and SLA before any send.
