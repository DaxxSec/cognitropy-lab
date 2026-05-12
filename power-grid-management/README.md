# Power Grid Management Workspace

> **Cognitropy Lab** · Engineering & Technical · Day 29 · Technique: Geographic/spatial analysis

A structured analytical environment for electrical power grid operations, planning, and incident investigation — framed through geographic and spatial reasoning. Grid Spatial Analyst helps you turn topology diagrams, GIS layers, SCADA exports, outage logs, weather feeds, and satellite imagery into defensible answers about the grid's exposure, vulnerability, and behavior in space.

This workspace is optimized for analyses where *where* matters at least as much as *what* — outage clustering, vegetation management prioritization, interconnection studies, wildfire ignition risk along transmission corridors, substation siting, phasor correlation across a disturbance, and cyber-physical incident geolocation.

---

## What This Workspace Does

- **Grounds every conversation in spatial data.** Answers reference actual GIS layers, coordinates, and topology you supply — no invented locations.
- **Bridges electrical and geographic reasoning.** Helps translate between electrical distance (impedance, contingency depth) and geographic distance (feeder length, right-of-way exposure).
- **Supports outage investigation with spatial pattern analysis** — identifying whether a pattern is radial, clustered, along a corridor, or consistent with a shared asset.
- **Guides map design for operational use** — which layers, which projection, which symbology, which color ramps for reliability vs. safety vs. outage-severity maps.
- **Tracks your active analysis across sessions** via `work-log/session-log.md` and `context/project.md`.
- **Stays within the informational/advisory lane.** Operational decisions route through the user's authority chain and NERC/regional procedures.

---

## Who This Is For

- Transmission and distribution utility engineers doing reliability or planning analysis
- System operators and reliability coordinators during post-event review
- DER/interconnection engineers assessing geographic exposure of new resources
- Vegetation management and wildfire mitigation planners
- Grid cyber-physical security analysts correlating events with asset geography
- Researchers and students working on power-system spatial analytics

---

## Quick Start

1. Open this workspace in your Claude environment
2. Run `/onboard` — the agent will capture your role, utility type, jurisdiction, and current analysis goal
3. Drop your data (or a sample of it) into `resources/` or reference it by path — GIS layers, topology exports, outage logs, SCADA extracts
4. Use `/analyze`, `/map`, `/outage`, or `/topology` depending on the task
5. At the end of each session, ask the agent to log what was done in `work-log/session-log.md`

---

## Directory Structure

```
power-grid-management/
├── CLAUDE.md                        # Agent identity and command list
├── README.md                        # This file
├── CREATION_REPORT.md               # Why this workspace was built
├── context/
│   ├── project.md                   # Active analysis / investigation
│   ├── role.md                      # User's role and utility context
│   ├── constraints.md               # Data-handling, regulatory, safety constraints
│   └── for-agent/
│       ├── domain-knowledge.md      # Grid architecture + spatial data reference
│       ├── workflows.md             # Canonical spatial-analysis workflows
│       ├── tools.md                 # GIS stacks, simulators, data formats
│       └── environment.md           # User's operating environment
├── .claude/commands/
│   ├── onboard.md                   # Workspace initialization
│   ├── analyze.md                   # Structured spatial analysis
│   ├── map.md                       # Map design proposal
│   ├── outage.md                    # Outage/event spatial investigation
│   └── topology.md                  # Topology exploration
├── prompts/                         # Reusable prompt templates
├── resources/                       # Standards guide, sample data, reference material
├── planning/                        # Analysis plans and milestone tracking
├── work-log/                        # Session history
└── outputs/                         # Generated maps, reports, analyses
```

---

## Domain Overview: Power Grid Management, Spatially

The electric power grid is inherently a geographic system — generation, transmission, distribution, and load are all located in space and connected by conductors that follow terrain, rights-of-way, and corridors. Most operational decisions have a spatial dimension even when the immediate electrical question is non-spatial.

### Grid Segments

| Segment | Typical voltage (US) | Spatial character |
|---------|---------------------|-------------------|
| Bulk transmission | 230 – 765 kV | Long-distance corridors, interstate, few assets per mile |
| Sub-transmission | 69 – 161 kV | Regional, feeds substations |
| Primary distribution | 4 – 34.5 kV | Dense, follows streets, radial feeders with ties |
| Secondary distribution | 120 – 480 V | Neighborhood-scale, customer-facing |
| Distributed energy resources | Varies | Rooftop + utility-scale solar/wind, battery storage, dispersed |

### Spatial Data That Matters

**Asset layers:**
- Substations (point features with attributes: voltage, capacity, ownership, criticality rating)
- Transmission lines (line features with attributes: voltage, conductor type, rating, circuit ID, year of install)
- Distribution feeders (line features, often in a connected network topology)
- Poles, transformers, reclosers, capacitor banks, switches (point features along feeders)
- Service territories and franchise boundaries (polygon features)

**Exposure layers:**
- Vegetation (canopy height models from LiDAR, change detection from satellite)
- Terrain (slope, aspect, elevation — wildfire ignition + access)
- Fire weather zones, Red Flag Warning areas
- Flood zones (FEMA FIRM maps), storm surge, hurricane tracks
- Ice loading zones, lightning density maps
- Wildlife habitat (owl/raptor areas influence pole-top mitigation)

**Operational layers:**
- Outage logs (point-in-time events; commonly not natively geocoded)
- Load density (customer-weighted or measured MW/mi²)
- SCADA/EMS alarm geolocations
- PMU locations and areas of coverage
- DER interconnection points

### Key Standards and Frameworks

| Standard / framework | Scope |
|---------------------|-------|
| NERC Reliability Standards (TPL, PRC, FAC, CIP) | US bulk power system reliability and security |
| FAC-003 | Transmission vegetation management |
| CIP-014 | Physical security of critical substations |
| IEEE 1547 | DER interconnection requirements |
| IEEE C2 (NESC) | National Electrical Safety Code — clearances, work practices |
| IEC 61850 | Substation automation, communications |
| Common Information Model (CIM) — IEC 61968/61970 | Grid data model used across EMS/DMS/GIS integration |
| OGC Simple Features / GeoJSON / Shapefile / GeoPackage | Vector GIS interchange formats |
| CF Conventions / NetCDF | Raster climate and weather data |

### Common Spatial-Analysis Questions

The agent is tuned to help with questions like:

- Where are our outages concentrated this storm, and does the pattern match the storm track or a shared feeder?
- Which 5 miles of transmission right-of-way have the highest combined vegetation and fire-weather risk?
- If we lose substation X, which customers lose power, and how far do the alternative supply paths travel geographically vs. electrically?
- Where should a new 69 kV substation go to minimize losses and serve the forecast load growth polygon?
- Which distribution feeders intersect the new battery storage facility's interconnection study area?
- Where along the grid did a given disturbance propagate, based on PMU phase-angle data, and is that consistent with the geographic topology?
- Which critical assets fall inside the impact radius of a cyber-physical incident reported at coordinates (x, y)?

---

## Analyst Experience Levels

Grid Spatial Analyst calibrates depth to your documented experience. The levels below are a rough guide — tell it your actual background in `/onboard`.

| Level | Typical profile | Calibration cue |
|-------|----------------|-----------------|
| L1 Orientation | New to power systems and/or GIS | Uses analogies; avoids per-unit math; names every acronym |
| L2 Practitioner | Can run routine GIS queries or read one-line diagrams | Explains terms on first use; walks through methodology |
| L3 Analyst | Produces outage/reliability/planning analyses independently | Peer-level discussion; cites standards clauses |
| L4 Specialist | Leads studies; reviews others' work | Challenges assumptions; debates trade-offs |
| L5 Expert | Authoritative in spatial grid analytics | Collaborator on novel problems |

---

## Slash Command Reference

| Command | Usage |
|---------|-------|
| `/onboard` | First-run setup: role, utility, jurisdiction, active analysis, available data |
| `/analyze` | Run a structured spatial analysis on supplied data or a scenario |
| `/map` | Propose a map design (layers, symbology, projection) for a stated goal |
| `/outage` | Investigate an outage/event with spatial reasoning |
| `/topology` | Explore grid topology questions (contingencies, islanding, distance) |

---

## Tips for Using This Workspace

- Tell the agent what data you actually have access to, in what format, at the start of a session. That prevents it from assuming an idealized dataset you don't.
- For real operational data, sanitize or redact before pasting into chat — utility GIS is often sensitive (CIP-protected, trade-secret, or customer-level). See `context/constraints.md`.
- Ask for *methods*, not just answers — a good spatial analysis is reproducible, and the agent can walk you through the steps so you can run them in your own tooling.
- When you get a map or analytical output you like, log it in `work-log/session-log.md` with the date and the question it answered. Over time this builds a durable record of what you've learned and what you've shipped.
- For cross-discipline questions (grid + cyber, grid + vegetation, grid + weather), say so explicitly up front — the agent will pull from multiple `context/for-agent/*` references.

---

*Built by Cognitropy Lab · 2026-04-23 · Engineering & Technical domain · Technique: geographic/spatial analysis*
