# Diplomatic Security Advance Planning Workspace

> A Claude Code workspace for diplomatic-security advance planners — RSOs, protective-services agents, contracted advance teams — framed throughout as **safety protocol enforcement**. Every venue, route, motorcade configuration, contact, and contingency runs through a documented protocol with explicit acceptance criteria, deviation handling, and post-mortem reporting.

## What This Workspace Does

This workspace turns a protective-services advance into a protocol-driven workflow rather than a narrative. Instead of "we walked the route and it looked OK", it produces signed-off survey checklists tied to venue type and threat tier, motorcade configurations sized to documented threat assessments, route reconnaissance with chokepoint and hospital-pre-positioning data, communications redundancy audits, and structured contingency decision trees keyed to named protocol triggers.

The agent guides the full advance cycle: pre-trip threat-stream synthesis, venue surveys, route reconnaissance, motorcade rehearsal, host-nation coordination matrix, contingency planning, real-time deviation logging during the visit, and the post-trip After Action Review that feeds protocol revisions.

## Why This Workspace Exists

Advance planning failures rarely show up as single dramatic events — they accumulate as small, undocumented protocol skips. A venue survey done in 20 minutes instead of the protocol's 90; a route alternate that was eyeballed rather than driven; a contingency tree that was discussed verbally but not committed to a checklist; a post-trip debrief that never happened. Each one is invisible until the day something escalates and the team discovers what wasn't documented.

This workspace codifies the discipline: every artifact has an owner, a protocol reference, a sign-off, and an audit trail. Threat tier drives configuration. Deviations are logged and reviewed. After-action findings revise the protocol library for the next trip.

## Getting Started

### Prerequisites

- **Operating authority** — RSO clearance, contracted EP services license, or equivalent. This workspace assumes you have authority to conduct advance planning for the named protectee class.
- **Data access** — protective intelligence feed (DS Watch, embassy reporting, host-nation MOI liaison, open-source HUMINT). Subscription or routing requirements vary by mission.
- **Coordination contacts** — host-nation police, military, EMS, fire, hospital POCs for each jurisdiction the visit touches.
- **Reference materials** — current DS regional protocols, jurisdictional SOFA/BIA/MOU, host-nation use-of-force regulations, applicable Federal Acquisition Regulation for contracted teams.
- **Output handling** — secure storage for outputs (this workspace's contents are sensitive — protective TTPs, routes, venue specifics, protectee schedules).

### Quick Start

1. Clone this workspace.
2. Drop the trip intake (protectee identity tier, dates, itinerary, host-nation contacts) and the current protective intelligence feed into `context/` (or `outputs/raw-intel/` for streaming data).
3. Run `/trip-advance-plan` to produce the master advance packet.
4. Run `/venue-survey-checklist` for each named venue; conduct surveys in person and complete the checklist.
5. Run `/route-recon-report` for primary + alternates; drive them in person at multiple times of day.
6. Run `/motorcade-config` and `/contingency-tree` to lock the operational picture.
7. During the visit, log deviations against the protocol matrix.
8. Post-visit, run `/aar-debrief` to feed findings back into the protocol library.

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/trip-advance-plan` | Master advance-packet generation | Trip kickoff — first command after intake |
| `/venue-survey-checklist` | Venue-specific survey tied to venue type + threat tier | Before every venue site visit |
| `/motorcade-config` | Motorcade configuration recommendation | After threat tier locked + route recon complete |
| `/route-recon-report` | Primary + alternates analysis | Before motorcade config; before visit |
| `/contingency-tree` | Decision tree (medical / hostile / disturbance / vehicle failure) | After motorcade + venue locked, before visit |
| `/threat-stream-synthesis` | Daily TBA-format intelligence brief | Daily during pre-trip and visit windows |
| `/jurisdiction-coord-matrix` | Host-nation coordination matrix with POCs + escalation | At trip kickoff, refresh weekly |
| `/comms-redundancy-audit` | Primary + alternate + emergency comms audit | Before visit; after any equipment change |
| `/aar-debrief` | Structured After Action Review | Within 72 hours of trip conclusion |

## Directory Structure

```
diplomatic-security-advance-planning/
├── CLAUDE.md                              # Agent role, available commands, foundational instructions
├── README.md                              # This file
├── .claude/commands/                      # 9 bespoke domain commands
│   ├── trip-advance-plan.md
│   ├── venue-survey-checklist.md
│   ├── motorcade-config.md
│   ├── route-recon-report.md
│   ├── contingency-tree.md
│   ├── threat-stream-synthesis.md
│   ├── jurisdiction-coord-matrix.md
│   ├── comms-redundancy-audit.md
│   └── aar-debrief.md
├── context/
│   ├── concepts.md                        # Advance fundamentals, threat taxonomy, motorcade doctrine, RSO doctrine refs
│   ├── workflows.md                       # Pre-trip advance, surveys, recon, rehearsal, contingency, debrief
│   └── references.md                      # DS regional standards, contingency-distance bands, motorcade configs, comms channels
├── prompts/                               # 4 reusable prompts
│   ├── protectee-threat-intake.md
│   ├── venue-advance-survey.md
│   ├── motorcade-config-decision.md
│   └── post-trip-aar.md
└── outputs/                               # Advance packets, AARs, route reports, contingency trees
```

## Example Use Cases

### Ministerial visit to a third-country bilateral
A Secretary-level principal visits a third country for a bilateral with the foreign minister and a working session at the prime minister's office. Run `/trip-advance-plan` against the itinerary, surfacing the threat tier (host nation MOI assessment + DS Watch synthesis), then `/venue-survey-checklist` for the foreign ministry and PM residence, `/route-recon-report` for primary + 2 alternates between airport / hotel / venues, `/motorcade-config` to lock the lead-CAT-follow-control configuration, and `/contingency-tree` for medical + hostile-action + civil-disturbance branches.

### Multi-stop conference circuit across three jurisdictions
A senior executive on diplomatic-adjacent travel attends three conferences in three consecutive countries. Each jurisdiction requires its own `/jurisdiction-coord-matrix`, host-nation police clearance, separate motorcade configs, and separate contingency trees. The workspace tracks all three trips with cross-references for shared personnel and reusable contingency patterns.

### Threat-stream change during a trip
Mid-trip, the host-nation MOI raises the alert level due to a regional incident. Run `/threat-stream-synthesis` to incorporate the new intelligence; trigger `/motorcade-config` re-evaluation (CAT presence escalation? alternate routes?); update `/contingency-tree` for the elevated hostile-action branch; document the protocol-driven changes in the visit's continuous log.

### Post-trip protocol revision
A trip surfaces a recurring weakness — a category of venue (boutique hotel ballroom) consistently underestimates standoff distances in `/venue-survey-checklist`. Run `/aar-debrief` to formalize the finding; propose a protocol revision adding a boutique-venue-specific section to the checklist; circulate revision proposal to the RSO leadership; lock revised protocol into the library for the next trip.

## Recommended MCP Servers / Tools

- **filesystem** — for advance packets, AARs, venue photos, route maps (with appropriate access control).
- **shell** — for invoking GIS / mapping tools (QGIS, ArcGIS), motorcade simulation tooling, route-timing scripts.
- **python** — for threat-tier scoring tools, contingency-time computation, communications dead-zone modeling.
- **sqlite** or **duckdb** — for protectee + jurisdiction + venue + AAR cross-referencing across trips.

## Legal & Ethical Considerations

- **Host-nation sovereignty.** All operations are subject to host-nation consent and SOFA / BIA / MOU constraints. Document any deviation request and resolution.
- **Use of force.** Standing rules for the use of force (SRUF) and rules for the use of deadly force (RUF) are host-nation- and mission-specific. The advance plan documents the applicable framework; it does not re-author or supersede it.
- **Privacy / OPSEC.** Outputs contain protectee schedules, venue specifics, and TTPs. Handle per the practice's classification and access-control regime. Never publish to public channels; pseudonymize protectee identifiers in shared documentation.
- **Contractor scope.** Contracted EP teams operate within their contract's defined scope. Out-of-scope requests are escalated to the contracting officer, not absorbed by the team.

## Technical References

- [US Department of State — Bureau of Diplomatic Security](https://www.state.gov/bureaus-offices/under-secretary-for-management/bureau-of-diplomatic-security/) — DS doctrine and regional standards.
- [Diplomatic Security Service overview](https://www.state.gov/bureaus-offices/under-secretary-for-management/bureau-of-diplomatic-security/diplomatic-security-service/) — DSS organization, responsibilities.
- [Overseas Security Advisory Council (OSAC)](https://www.osac.gov/) — open-source threat reporting + private-sector liaison.
- [International Association of Chiefs of Police — VIP Protection guidelines](https://www.theiacp.org/) — protective-services standards.
- [ASIS International — Protective Operations Standard](https://www.asisonline.org/standards-guidelines/) — industry-standard for protective services.
- [SAE J3061 — Cybersecurity Guidebook for Cyber-Physical Vehicle Systems](https://www.sae.org/standards/content/j3061/) — relevant for motorcade vehicle telematics security.
- [INTERPOL — VIP protection liaison resources](https://www.interpol.int/) — cross-border coordination.
- [GAO reports on DS / DSS operations](https://www.gao.gov/) — public-domain audit findings on protective-services operations.

## Optional plugin

If you have the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, additional global commands (`/workspace-foundational:context-sweep`, `/workspace-foundational:find-template`) are available. The workspace is self-contained without it.
