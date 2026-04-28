# VIP Motorcade Planning & Route Risk Workspace

> An agent workspace for designing, quantifying, and briefing VIP motorcade routes using formal risk scoring matrices (likelihood × impact), so primary, alternate, and abort legs are chosen on auditable, defensible numbers rather than intuition.

## What This Workspace Does

This workspace turns the protective movement planning cycle — from advance survey, through threat baselining, route segmentation, scoring, and brief — into a structured pipeline. Rather than ad-hoc map-staring and "this corner looks bad," it applies a 5×5 likelihood-vs-impact matrix at the *segment* level, rolls those up to a route-level risk number, and lets the detail leader compare candidate routes on the same axes.

The agent guides the protection lead through:

- **Threat baselining** — building a documented threat-actor / capability profile for the principal and movement window.
- **Route survey** — turning a candidate route into a list of ~10–40 numbered segments, each geocoded, photographed (offline), and tagged with chokepoint, overpass, ingress/egress, and overwatch features.
- **Risk scoring** — scoring every segment with explicit likelihood and impact criteria, plus a residual risk after countermeasures (advance, counter-surveillance, intervention vehicle posture, hardening).
- **Comparison** — side-by-side multi-criteria comparison of primary / alternate / abort with weighted scoring (risk, time, deconfliction, deniability, principal comfort).
- **Briefing & rehearsal** — generating the operational movement brief, contingency drills, and after-action debrief.

## Why This Workspace Exists

Protective movement is a low-frequency, high-consequence activity: most movements are uneventful, but a single ambush, IED, or medical event on a poorly chosen route can be catastrophic. Despite that, route choice is often documented as prose ("we'll take the river road, fall back to the highway"), with no record of *why* the river road beat the highway, or what threats and impacts were considered. That makes the choice impossible to audit, hard to teach, and brittle when threat conditions shift.

Risk scoring matrices — long standard in safety engineering, financial risk, and HAZOP — give protection a common language. ISO 31000 and U.S. State Dept DS High-Threat Protection methodology both treat the matrix as the central artefact: every identified hazard is plotted, ranked, and mitigated to a documented residual level. This workspace operationalizes that for motorcade routing.

## Getting Started

### Prerequisites
- Trained protection lead, advance team lead, or detail leader (this workspace assumes operator competence — it does not teach close-protection fundamentals).
- Map/imagery access: Google Maps, Apple Maps, or — preferably for OPSEC — offline OpenStreetMap exports (e.g. via QGIS or Organic Maps).
- An understanding of the principal's threat tier (corporate, public-figure, government, high-threat post).
- Local liaison contacts (host-nation police, traffic control, hospital networks, embassy duty officer).
- Optional: GPX / KML editor (e.g. Gaia GPS, GPX Studio) for waypoint files.
- Authorization: a written EP contract or government-issued protective tasking. **Do not use this workspace to plan movements you are not authorized to plan.**

### Quick Start
1. Clone this workspace into your detail's case folder (one workspace per principal × movement-window).
2. Run `/onboard` to capture principal profile, threat tier, movement window, jurisdictions, and motorcade resources.
3. Run `/threat-baseline` to build the actor/capability baseline that drives likelihood scoring.
4. For each candidate route, run `/route-survey` followed by `/risk-score`.
5. Run `/route-compare` to pick the primary, designate the alternate(s), and lock the abort.
6. Run `/contingency-plan` for ambush, IED, medical, breakdown, and crowd-surge contingencies tied to specific waypoints.
7. Run `/advance-checklist` 24–72 h before movement, then `/movement-brief` at T-2 h.
8. Run `/after-action` within 24 h of the movement closing — even uneventful movements feed the residual-risk model for the next cycle.

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/onboard` | Initialize with principal profile, threat tier, jurisdictions, motorcade composition | First time setup, or new principal |
| `/threat-baseline` | Build threat actor + capability baseline driving likelihood values | Once per movement window or when threat shifts |
| `/route-survey` | Segment a candidate route, geocode waypoints, log chokepoints/overwatch | For each candidate route, after physical drive-through |
| `/risk-score` | Apply 5×5 L×I matrix to every segment + route roll-up | After `/route-survey` is complete |
| `/route-compare` | Multi-criteria weighted comparison of primary / alternate / abort | After all candidate routes are scored |
| `/contingency-plan` | Generate waypoint-tied contingency drills (ambush, IED, medical, etc.) | After primary route is selected |
| `/advance-checklist` | Pre-movement advance team checklist (counter-surveillance, sweep, liaison) | T-72 h to T-12 h |
| `/movement-brief` | Generate the operational order / drivers' brief / staff brief | T-2 h to T-0 |
| `/after-action` | Post-movement debrief, residual risk update, lessons learned | T+0 to T+24 h |

## Directory Structure

```
vip-motorcade-planning-route/
├── CLAUDE.md                          # Agent role and instructions
├── README.md                          # This file
├── CREATION_REPORT.md                 # Workspace creation details
├── context/
│   ├── project.md                     # Principal, movement window, mission objectives
│   ├── role.md                        # Detail leader's experience and unit
│   ├── constraints.md                 # Legal/jurisdictional/ethical boundaries
│   └── for-agent/
│       ├── domain-knowledge.md        # Risk scoring methodology, attack typologies, motorcade doctrine
│       ├── workflows.md               # 5 core workflows with decision trees
│       ├── environment.md             # Tools, GIS sources, comms equipment
│       └── tools.md                   # Software references (QGIS, Gaia GPS, ATAK, etc.)
├── .claude/commands/
│   ├── onboard.md                     # Workspace initialization
│   ├── threat-baseline.md             # Threat actor and capability baseline
│   ├── route-survey.md                # Route segmentation and geocoded survey
│   ├── risk-score.md                  # 5×5 likelihood×impact scoring
│   ├── route-compare.md               # Multi-criteria route comparison
│   ├── contingency-plan.md            # Contingency drill generation
│   ├── advance-checklist.md           # Pre-movement advance team checklist
│   ├── movement-brief.md              # Operational order / drivers' brief
│   └── after-action.md                # Post-movement debrief
├── prompts/
│   ├── threat-baseline-interview.md   # Structured interview to build threat baseline
│   ├── chokepoint-analysis.md         # Per-waypoint chokepoint analysis prompt
│   └── ambush-survivability.md        # Survivability analysis given an ambush profile
├── resources/
│   ├── 5x5-risk-matrix.md             # The canonical L×I matrix with tier definitions
│   ├── attack-typology-reference.md   # Ambush, IED, snipe, swarm, breach: indicators + mitigations
│   ├── route-segment-checklist.md     # 32-point per-segment survey checklist
│   └── doctrine-references.md         # Curated standards bibliography (DS, NPSA, ASIS, ISO)
├── planning/                          # Active route plans, candidate route trees, pivots
├── outputs/                           # Generated briefs, after-action reports, residual-risk logs
├── user-docs/
│   ├── getting-started.md             # First-movement walk-through
│   └── risk-matrix-explained.md       # Why a 5×5 matrix, calibration, common abuse patterns
└── work-log/                          # Session logs and per-movement records
    └── session-log.md                 # Session logging template
```

## How the Risk Scoring Works

### The 5×5 Matrix

Each identified hazard for a given route segment receives:

- **Likelihood (1–5):** 1 = Rare, 2 = Unlikely, 3 = Possible, 4 = Likely, 5 = Almost Certain. Anchored by the threat baseline's documented capability and intent.
- **Impact (1–5):** 1 = Negligible, 2 = Minor injury / brief delay, 3 = Significant injury / forced abort, 4 = Critical injury or principal capture, 5 = Catastrophic (principal KIA / mass casualty).
- **Risk (L × I, 1–25):** Plotted on a heat map: 1–4 Low / 5–9 Moderate / 10–14 High / 15–19 Very High / 20–25 Extreme.
- **Residual Risk:** Re-scored after applying countermeasures (advance team, low-profile motorcade, hardened vehicle, alternate timing, route closure). The detail leader signs off on the *residual* number, not the inherent number.

### Segment Roll-Up

A route's risk score is **not** the average of its segments — it's the maximum residual risk of any segment, with a tie-breaker on the count of High+ segments. Routes with one Extreme chokepoint are unacceptable even if the other 39 segments are Low.

### Multi-Criteria Comparison

Final route selection weights:

| Criterion | Default Weight | Notes |
|-----------|----------------|-------|
| Max residual risk | 35% | Hard ceiling — Extreme = veto |
| Count of High+ segments | 20% | Tail risk |
| Total time / time variance | 15% | Predictability also matters |
| Deconfliction (traffic, public events) | 10% | Crowd density is itself a hazard |
| Profile / deniability | 10% | Low-profile vs. overt motorcade |
| Principal comfort / stamina | 10% | Real factor, especially for elderly or post-medical principals |

Weights are tunable per movement; they are stored in `planning/comparison-weights.md` and reviewed at after-action.

## Example Use Cases

### Diplomatic Visit, Capital City
Foreign minister visits a host capital for a 48-hour bilateral. Three legs daily (hotel ↔ ministry, hotel ↔ palace, hotel ↔ airport on day 2). Workspace produces 3 × 3 routes (primary/alternate/abort each), threat-baselined against host-nation political climate, with crowd-surge as the dominant hazard.

### Corporate CEO, Latin American Operations Visit
Fortune-100 CEO tours a portfolio company in a high-kidnap-for-ransom region. Workspace integrates kidnap-intel feeds, prefers low-profile (unmarked) motorcade, weights deniability heavily, and ties contingency plans to embassy and private QRF response timing.

### Returning Athlete / Public Figure Procession
A celebrated athlete returns home; the movement is *intended* to be public, with a fixed waving route. Workspace inverts: the threat baseline now includes lone-actor stalker profiles and crowd-crush impact, and the matrix is re-tuned (likelihood of disruption is high but impact-on-life is lower than diplomatic threat).

### Trial Witness Movement
A protected witness moves from safe house to courthouse and back, daily, for two weeks. Workspace optimizes for *unpredictability* — rotates primary/alternate/abort assignments daily, suppresses pattern-of-life, and integrates with U.S. Marshals / WITSEC handling guidance.

### Post-Incident Re-Routing
A previous movement faced an actual incident (ambush, IED find, crowd surge). Workspace pulls the after-action, updates residual risk per segment, and forces re-survey of any segment now categorized High+ that was previously Moderate.

## Recommended MCP Servers

- **filesystem** — For reading/writing route survey logs, GPX/KML waypoints, and brief outputs.
- **shell** — For running offline GIS tooling (QGIS, gpsbabel, OSM extracts) and PDF generation for printed briefs.
- **fetch** (read-only, sanctioned sources only) — For pulling open-source threat advisories (OSAC, U.S. State Dept Travel Advisories, NPSA UK) into the threat baseline. Disable for high-OPSEC engagements.

## Legal & Ethical Considerations

- **Authorization:** Only plan movements for which you hold a written EP contract or lawful protective tasking. Do not "war-game" public officials' or private individuals' movements as a hobby; the work is functionally indistinguishable from attack planning.
- **Jurisdictional law:** Motorcade behavior (use of escort vehicles, lights/sirens, weapons carry, traffic control) varies enormously by jurisdiction. The agent always asks for and respects the host-nation legal framework. In the U.S., this includes federal (DSS, USSS), state, and municipal layers; in host-nation work, it includes diplomatic notification (note verbale, ID&L) and host-nation security liaison.
- **Privacy:** The principal's movement schedule, address, and identifying data are highly sensitive. Sanitize before any artefact leaves the local clone. Never paste real schedules into chat with non-cleared parties.
- **Defensive posture:** This workspace explicitly refuses requests to model attacks, evaluate routes from an attacker's POV beyond what is required for defensive planning, or generate content that primarily serves an offensive use case (e.g. "where would *I* set up an ambush?").
- **No surveillance of third parties:** Counter-surveillance focuses on protecting the principal, not surveilling unrelated members of the public.
- **Reporting obligations:** If the threat baseline development reveals a credible, specific threat to a third party, escalate per your unit's reporting chain (and, where applicable, host-nation law enforcement / embassy RSO).

## Technical References

- [ISO 31000:2018 Risk Management Guidelines](https://www.iso.org/iso-31000-risk-management.html)
- [U.S. Department of State Diplomatic Security — Overseas Security Advisory Council (OSAC)](https://www.osac.gov/)
- [NPSA — National Protective Security Authority (UK)](https://www.npsa.gov.uk/)
- [ASIS International Executive Protection (PSC.1) Standard](https://www.asisonline.org/publications--resources/standards--guidelines/)
- [DHS / FEMA HAZUS — Hazards Methodology](https://www.fema.gov/flood-maps/products-tools/hazus)
- [INTERPOL — Project Geiger / Travel Threat Resources](https://www.interpol.int/)
- [U.S. Secret Service Protective Methodology (overview)](https://www.secretservice.gov/protection)
- [QGIS — Open-source GIS](https://qgis.org/)
- [Organic Maps — offline OSM viewer](https://organicmaps.app/)
- [ATAK / iTAK Civil overview](https://tak.gov/)
