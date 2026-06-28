# Wildfire Management & Containment Workspace

> Turn a chaotic, deteriorating fire environment into explicit go/no-go decision trees — structure triage, suppression capability, evacuation staging, and containment strategy — so the commit decision is fast, legible, and defensible.

## What This Workspace Does

This is a Claude Code workspace for **wildfire suppression and containment decision support**. It helps an analyst or planner work the full arc of a fire: size it up, project where it's going, decide whether and how to engage, triage which structures can be saved, set evacuation triggers, order resources, and plan the transition from contained to controlled to out.

The organizing idea — today's technique — is **decision-tree triage workflows**. Wildfire decisions are made under time pressure, with incomplete information, and with lives on the line. The antidote to that is *structure*: every recommendation here is built as a branching decision tree with the selecting condition shown, so a reviewer can audit exactly why a structure was called "non-defensible," why a division was held direct, or why crews were pulled to a safety zone. The four canonical trees this workspace operationalizes are (1) NWCG structure-protection triage, (2) flame-length → suppression-capability (the "Hauling Chart"), (3) the go/no-go risk-management gate, and (4) Ready-Set-Go evacuation staging.

It is explicitly **not** a fire-spread simulator, an autonomous decision-maker, or a replacement for trained personnel. Treat it as a sharp, well-organized planning assistant that always shows its reasoning and always defaults toward life safety.

## Why This Workspace Exists

Wildland fire kills firefighters and civilians in predictable ways: line built without escape routes, structures defended past the point of survivability, evacuations triggered too late, and resources committed to fronts they cannot hold. The fire-service answer is a body of hard-won doctrine — the 10 Standard Firefighting Orders, the 18 Watch Out Situations, LCES, structure-triage categories, the flame-length interpretation chart. This workspace codifies that doctrine into runnable commands so the decisions are made the same disciplined way every time, the assumptions are written down, and the "we should disengage" call is just as easy to produce as the "we can hold this" call.

## Getting Started

### Prerequisites

- A fire-weather data source for the incident (RAWS/MesoWest, NWS spot forecast, or a fire-weather MCP) — wind, RH, temperature, fuel moisture
- Fuel and terrain context: a fuel model (Anderson 13 or Scott & Burgan 40), slope %, aspect, and a rough perimeter or point of origin
- A values-at-risk list for the WUI segment (addresses/structures, critical infrastructure, evacuation routes)
- Optional: a GIS/mapping tool for perimeter and values-at-risk visualization; BehavePlus or equivalent for independent fire-behavior checks

### Quick Start

1. Clone this workspace and read `context/concepts.md` and `context/workflows.md` to load the doctrine.
2. Drop the current fire-weather, fuels, and values-at-risk data into `context/` (or `outputs/raw/`).
3. Run `/red-flag-readiness` to set the day's posture, then `/spread-projection` to see where the fire is going this operational period.
4. Run `/containment-strategy` for the engagement plan and `/structure-triage` on the threatened structure list.
5. Gate every committed assignment through `/lces-check` before resources go in, and close the shift with `/after-action-review`.

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/structure-triage` | Decision-tree classification of structures into Defensible–Stand Alone / Defensible–Prep & Hold / Non-Defensible–Prep & Leave / Non-Defensible–Rescue Drive-By | When the fire threatens a WUI segment and you must decide what to defend |
| `/fireline-capability` | Converts flame length / ROS to fireline intensity and the resource type that can hold the line | When sizing up a flank or deciding handcrew vs. dozer vs. air vs. withdraw |
| `/containment-strategy` | Direct vs. indirect vs. parallel attack, anchor-flank-pinch plan, line location | At strategy development for an operational period |
| `/lces-check` | Builds/verifies Lookouts-Comms-Escape Routes-Safety Zones with a hard go/no-go gate | Before any crew commits to a division — every time |
| `/spread-projection` | Projects head/flank/spotting spread and ranks values at risk over the period | At the start of each operational period and on significant weather shifts |
| `/evac-triggers` | Sets staged Ready/Set/Go trigger points from fire arrival time and protective-action zones | When civilian areas are within the projection envelope |
| `/resource-order` | Prioritized, qualification-aware resource order from a containment plan | When the plan exceeds on-scene capability |
| `/red-flag-readiness` | Fire-weather risk read (red flag, Haines, ERC, fuel moisture) → operational posture | Each morning briefing and on a red-flag warning |
| `/mop-up-plan` | Mop-up gridding, cold-trailing, and contained → controlled → out criteria | After the perimeter holds and you're chasing heat |
| `/after-action-review` | Structured plan-vs-actual AAR (sustain / improve) | End of every shift or operational period |

## Directory Structure

```
wildfire-management-containment/
├── CLAUDE.md                 # Agent role, context refs, command list
├── README.md                 # This file
├── .claude/commands/         # 10 bespoke wildfire-containment commands
├── context/
│   ├── concepts.md           # Fire behavior, anatomy, triage taxonomies, fire weather
│   ├── workflows.md          # The decision trees + size-up→mop-up methodology
│   └── references.md         # Flame-length chart, triage table, fuel moisture, IRPG links
├── prompts/                  # Reusable prompt templates (briefing, defensibility, go/no-go, behavior forecast)
└── outputs/                  # Size-ups, triage runs, projections, AARs
```

## Example Use Cases

### WUI structure-defense triage during a wind-driven run
A fire is making a wind-driven push toward a subdivision. Run `/structure-triage` on the address list to sort homes into the four defensibility categories, then `/resource-order` to assign engines only to "Prep & Hold" structures with viable safety zones — and explicitly walk away from "Rescue Drive-By" structures.

### Flank engagement go/no-go
A division supervisor reports 6-foot flames on the right flank in chaparral. `/fireline-capability` says direct attack by handcrew is no longer viable (>4 ft) and points to dozers/engines or an indirect line; `/lces-check` confirms whether escape routes and a safety zone actually exist before anyone commits.

### Late-day evacuation decision
Weather is forecast to align the wind with a drainage at 1600. `/spread-projection` estimates arrival time at the protective-action zone; `/evac-triggers` converts that into Ready/Set/Go trigger points the IC can hand to the sheriff before the window closes.

## Recommended MCP Servers

- **A fire-weather / NWS data MCP** — pull spot forecasts, RAWS observations, and red-flag warnings directly into `/red-flag-readiness` and `/spread-projection`.
- **A GIS / geospatial MCP** — overlay perimeter, values at risk, and protective-action zones for triage and evacuation planning.
- **Filesystem MCP** — persist size-ups, triage outputs, and AARs into `outputs/` across sessions.

## Legal & Ethical Considerations

- **Decision support only.** Every output is advisory to a qualified IC operating under ICS/NIMS and the local AHJ. Nothing here authorizes a tactic, deploys a resource, or overrides the chain of command.
- **Life safety over property, always.** The workspace must produce "disengage" recommendations as readily as "engage" ones. A structure is never worth a firefighter's life.
- **Respect qualifications and jurisdiction.** Do not recommend committing resources beyond their red-card qualifications or outside their jurisdictional/mutual-aid authority.
- **Evacuation orders are a law-enforcement/AHJ function.** This workspace produces trigger-point *recommendations*; the order itself belongs to the authority with the legal mandate.

## Technical References

- [NWCG Incident Response Pocket Guide (IRPG), PMS 461](https://www.nwcg.gov/publications/pms461) — the field standard for tactics, triage, and risk
- [10 Standard Firefighting Orders & 18 Watch Out Situations](https://www.nwcg.gov/committee/6mfs/10-standard-firefighting-orders-18-watchout-situations) — the non-negotiable safety doctrine
- [LCES — Lookouts, Communications, Escape Routes, Safety Zones](https://www.nwcg.gov/committee/6mfs/lces) — Gleason's safety framework
- [Andrews & Rothermel — flame length / fireline intensity interpretation ("Hauling Chart")](https://www.fs.usda.gov/research/treesearch/29615) — the suppression-capability decision basis
- [NFPA 1144 — Reducing Structure Ignition Hazards from Wildland Fire](https://www.nfpa.org/codes-and-standards/nfpa-1144-standard-development/1144) — WUI structure standard
- [Ready, Set, Go! Program](https://www.wildlandfirersg.org/) — staged evacuation framework
- [Scott & Burgan 40 Standard Fire Behavior Fuel Models (RMRS-GTR-153)](https://www.fs.usda.gov/treesearch/pubs/9521) — fuel model catalogue
- [BehavePlus fire modeling system](https://www.firelab.org/project/behaveplus) — independent fire-behavior checks

## Optional plugin

If you have the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, additional global commands (`/workspace-foundational:context-sweep`, `/workspace-foundational:find-template`) are available; the workspace works without it.
