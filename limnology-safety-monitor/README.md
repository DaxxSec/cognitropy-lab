# Limnology Safety Monitor

**A freshwater field science workspace with integrated safety protocol enforcement.**

> Built by [The Cognitropy Lab](https://github.com/DaxxSec/cognitropy-lab) — Day 2 (2026-03-27)

---

## What This Is

The Limnology Safety Monitor is an AI-assisted workspace for planning, executing, and documenting freshwater field science operations — with safety woven into every step. It's designed for anyone who works on or near inland water bodies: lake researchers, environmental monitoring teams, water quality analysts, municipal water managers, and graduate students heading into the field for the first time.

The core design principle is that **safety protocols are not separate from the science — they are part of the science.** Every sampling plan includes safety checkpoints. Every data analysis flags conditions that affect field team safety. Every workflow gates on hazard assessment before operations begin.

Limnology — the study of inland waters (lakes, reservoirs, rivers, ponds, wetlands) — involves fieldwork in environments where conditions change fast. Wind picks up on open water. Ice that was safe yesterday isn't today. A lake that looked clear last week now has a toxic cyanobacterial bloom. This workspace treats those realities as first-class concerns, not footnotes.

---

## Getting Started

```bash
# Clone the cognitropy-lab repo (or just this workspace)
git clone https://github.com/DaxxSec/cognitropy-lab.git
cd cognitropy-lab/limnology-safety-monitor

# Launch Claude Code
claude

# Initialize the workspace for your project
/onboard
```

The `/onboard` command will walk you through setting up your specific project — which water body you're working on, what kind of campaign you're running, who's on your team, and what hazards you already know about. Everything you provide gets stored in the workspace so the agent has full context for all future commands.

---

## Commands

| Command | What It Does |
|---|---|
| `/onboard` | Initialize the workspace for your lake, campaign, and team |
| `/site-risk` | Assess field site hazards before deployment — produces a scored risk matrix and go/no-go recommendation |
| `/sampling-plan` | Design a water sampling campaign with integrated safety protocols, QA/QC, and timeline |
| `/water-quality` | Analyze water quality data — threshold comparison, trophic state calculation, anomaly detection |
| `/incident-report` | Document a field safety incident or near-miss with root cause analysis |
| `/gear-check` | Pre-deployment equipment and PPE inspection checklist tailored to your activity |
| `/compliance-audit` | Audit sampling procedures against EPA, state, or institutional standards |
| `/weather-hold` | Evaluate weather conditions for a go/no-go field deployment decision |

---

## What's Inside

### Context Layer
The `context/` directory gives the agent deep domain knowledge:

- **`context/for-agent/workflows.md`** — 7 detailed workflows covering the full lifecycle of limnological fieldwork: site risk assessment, sampling campaign design, water quality analysis, HAB response, ice safety, incident response, and compliance auditing. Each workflow embeds safety checkpoints as gating steps.
- **`context/for-agent/environment.md`** — Reference catalog of field equipment (sampling gear, instruments, safety equipment, watercraft), software tools, and calibration standards.
- **`context/role.md`** — Defines who this workspace serves and the boundaries of what the agent does and does not do.
- **`context/constraints.md`** — Safety-first operating rules, data quality constraints, regulatory awareness expectations, and communication style guidelines.

### Resources
Reference materials you'll actually use in the field:

- **`water-quality-thresholds.md`** — EPA recreational criteria, cyanotoxin advisories, dissolved oxygen standards, nutrient reference conditions, ammonia criteria, metals criteria, Carlson's TSI formulas, and sample holding times with container/preservation requirements.
- **`field-safety-checklist.md`** — Pre-departure, site arrival, watercraft launch, hourly in-field, return, and post-field checklists. Plus emergency quick-reference cards for person-in-water, hypothermia, lightning, HAB exposure, and capsized boat scenarios.
- **`ice-thickness-guide.md`** — Minimum clear ice thickness standards by activity, ice type strength comparisons, critical danger zones, seasonal risk progression, and measurement protocols.

### Prompt Templates
Reusable prompts for common scenarios:

- **`hab-response-briefing.md`** — Generate a complete HAB response briefing for stakeholders with health risk assessment, required actions, monitoring plan, and public communication template.
- **`seasonal-monitoring-design.md`** — Design a year-round monitoring program adapted to seasonal dynamics, configurable by latitude, depth, use, budget, and known issues.
- **`post-incident-debrief.md`** — Structure a blame-free safety debrief using 5-Whys root cause analysis with corrective actions and lessons learned.

---

## Use Cases

**Municipal water quality manager** running monthly compliance monitoring on a drinking water reservoir — use `/sampling-plan` to design a program that hits all EPA requirements, `/water-quality` to analyze each month's results against thresholds, and `/compliance-audit` annually to make sure everything is documented properly.

**Graduate researcher** planning their first field season on a remote lake — start with `/onboard` to set up the project, `/site-risk` to understand what they're getting into, `/gear-check` before every field day, and `/weather-hold` each morning to decide whether it's safe to go out.

**State environmental agency** responding to a reported algal bloom — use `/water-quality` to analyze initial samples, the HAB response workflow kicks in automatically when cyanotoxins are detected, and `/incident-report` documents the response for the record.

**Volunteer lake monitoring program** with limited resources — `/sampling-plan` can scale to budget constraints, the field safety checklist works for anyone regardless of experience level, and the trophic state analysis helps volunteers understand what their data means.

---

## Safety Philosophy

This workspace operates on three principles borrowed from high-reliability organizations:

1. **Preoccupation with failure.** Every workflow starts with "what could go wrong?" before "what do we want to accomplish?"
2. **Reluctance to simplify.** A weather check isn't just "looks fine" — it's specific numbers against specific thresholds with a documented decision.
3. **Deference to expertise.** If a team member is uncomfortable with conditions, that's a valid no-go signal regardless of what the numbers say.

The agent will never recommend proceeding when conditions are ambiguous. It will always recommend documenting incidents and near-misses. It will always flag regulatory triggers. This is by design.

---

## Technical Notes

This workspace follows the [Agent Workspace Model](https://github.com/danielrosehill/Claude-Agent-Workspace-Model). It requires [Claude Code](https://claude.ai/claude-code) or a compatible AI CLI. No API keys, external services, or special software are needed beyond the CLI itself.

All outputs (sampling plans, risk assessments, incident reports, analysis reports) are saved to the `outputs/` directory as Markdown files. The `work-log/` directory captures session-level decisions and weather holds.

Water quality thresholds in `resources/` are based on EPA National Recommended Water Quality Criteria (2024 revision) and EPA recreational water quality criteria (2019). State-specific standards may differ — the agent will note this and ask for your jurisdiction when relevant.

---

## License

MIT — Use, modify, and adapt freely. If you're using this for actual field operations, please have a qualified safety officer review any protocols before relying on them. This workspace is an aid, not a replacement for professional safety training.
