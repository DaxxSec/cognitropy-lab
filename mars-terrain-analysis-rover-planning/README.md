# Mars Terrain Analysis & Rover Traverse Planning Workspace

> An agent workspace for turning orbital terrain data into safe, science-rich rover sol plans — using a borrowed analytical framework from jazz harmony (chord progressions, voice leading, cadence, substitution) to evaluate traverse candidates, and a structured peer review workflow (driver / science / mech / autonomy / safety) to gate every uplink.

## What This Workspace Does

This workspace turns a stack of HiRISE/CTX orthoimages and DEM tiles into reviewed, ready-to-uplink sol plans. Rather than treating traverse planning as either pure pathfinding (shortest safe route) or pure science prioritization (highest-value targets), it borrows the analytical framework jazz composers use for chord progressions:

- **Each waypoint is a chord** — a triad of (terrain class, slope class, science value).
- **Each segment is a voice-leading move** — smooth slope and heading transitions are good voice leading; abrupt changes are voice crossings to avoid.
- **The traverse as a whole is a progression** — it must build tension (risky segments) and resolve to safe cadence points (verified safe parking with rock abundance < threshold and slope < parking limit).
- **Substitutions are first-class moves** — if a candidate traverse has a risky chord, search for a tritone substitute (different terrain, same destination) or modal interchange (a chord borrowed from a more conservative plan variant) before rejecting the whole progression.

Every traverse goes through a structured **peer review** before it can be promoted from `planning/` to `outputs/`. Reviewers play roles (rover driver, science PI, mechanical/safety, autonomy lead) and score against a published rubric; dissents are captured, not averaged out.

## Why This Workspace Exists

Mars rover tactical planning is inherently multi-objective: science return, energy budget, comms windows, mechanical stress, autonomy confidence, and a sliding wall of operational risk. Most planning tools optimize one of these and treat the rest as constraints. The harmonic framework gives you a vocabulary for *trade-offs* — "this segment is a tritone substitution that buys us 3 m of clearance from a rock field at the cost of 8% more drive time" — that maps cleanly onto the actual conversations the tactical uplink team has every sol.

The peer review workflow is the second half of the answer: aerospace flight readiness reviews (FRRs) and the JPL Tactical Uplink Process (TUP) already work this way; this workspace makes the same structure accessible for individual planners, mission concept studies, analog field tests, and student rover teams.

## Getting Started

### Prerequisites

- A target landing site or extended-mission map area (Jezero, Gale, Meridiani Planum, or analog site)
- HiRISE orthoimage + DEM (25 cm/px) — or CTX (6 m/px) for wider-area planning
- Rover platform spec: wheel diameter, ground clearance, maximum drivable slope, drive-distance budget per sol, comms relay schedule
- Sol-plan cadence: how many sols ahead are you planning? (typical: 1 sol tactical, 3–5 sols look-ahead)
- Python 3.x with `numpy`, `scipy`, `rasterio`, `gdal`, `networkx`, `matplotlib`
- (Optional) JMARS, ArcGIS Pro, or QGIS for visual review

### Quick Start

1. Clone this workspace
2. Run `/onboard` to record your rover platform, mission, terrain dataset, and reviewer panel
3. Run `/terrain-assess` on the relevant DEM/orthoimage tile to produce a hazard map
4. Run `/traverse-compose` to build a candidate traverse from the current rover position to the next strategic target
5. Run `/risk-cadence` on the candidate to verify every tension resolves
6. Run `/substitution-search` on any flagged segment to look for safer equivalents
7. Run `/peer-review` to drive the candidate through the multi-reviewer rubric
8. Run `/sol-plan` to produce the final sol plan with science, comms, and contingency blocks

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/onboard` | Initialize workspace — rover platform, mission, terrain, panel | First time setup |
| `/terrain-assess` | Per-tile hazard map (slope, rock abundance, terrain class) from a DEM/orthoimage | Before composing any traverse over new ground |
| `/traverse-compose` | Build a candidate traverse using the harmonic framework | When you have a strategic target waypoint and need a tactical path |
| `/substitution-search` | Search for safer alternate segments (tritone / modal-interchange substitutions) | When `/risk-cadence` flags a risky segment |
| `/risk-cadence` | Analyze tension/resolution pattern across the traverse | After every `/traverse-compose` and after every substitution |
| `/peer-review` | Run the multi-reviewer rubric, capture dissent, log decisions | Once a candidate has passed `/risk-cadence` |
| `/sol-plan` | Synthesize the reviewed traverse + science + comms into a sol plan | Final step before uplink handoff |

## Directory Structure

```
mars-terrain-analysis-rover-planning/
├── CLAUDE.md                          # Agent role, commands, foundational instructions
├── README.md                          # This file
├── CREATION_REPORT.md                 # Workspace provenance
├── context/
│   ├── project.md                     # Mission, target site, sol-plan cadence
│   ├── role.md                        # Your role on the planning team
│   ├── constraints.md                 # Flight rules, ethics, planetary-protection scope
│   └── for-agent/
│       ├── domain-knowledge.md        # Terrain analysis + jazz harmony framework + peer review theory
│       ├── workflows.md               # Per-sol planning loop, replan-on-anomaly loop, look-ahead loop
│       ├── environment.md             # Rover platform, datasets, processing pipeline
│       └── tools.md                   # GDAL, rasterio, networkx, JMARS, ROAMS-style sims
├── .claude/commands/
│   ├── onboard.md                     # First-time setup interview
│   ├── terrain-assess.md              # Hazard-map generation from DEM/orthoimage
│   ├── traverse-compose.md            # Harmonic-framework traverse composition
│   ├── substitution-search.md         # Find tritone & modal-interchange substitutions
│   ├── risk-cadence.md                # Tension/resolution pattern analysis
│   ├── peer-review.md                 # Multi-reviewer rubric + dissent capture
│   └── sol-plan.md                    # Final sol plan synthesis
├── prompts/
│   ├── traverse-rationale.md          # Template for explaining a traverse to non-planners
│   ├── new-terrain-class.md           # Template for documenting a newly observed terrain class
│   └── post-drive-debrief.md          # Template for debriefing after a drive completes
├── resources/
│   ├── flight-rules-quickref.md       # Per-rover slope/tilt/drive/comms hard limits
│   ├── harmony-to-traverse-cheatsheet.md  # The mapping table (chord type → terrain hazard class, etc.)
│   ├── reviewer-rubric.md             # The 5-axis peer-review scoring rubric
│   └── dataset-index.md               # Where to get HiRISE, CTX, MOLA, HRSC tiles
├── planning/                          # Active sol plans (one plan.md, plus pivots/)
├── outputs/                           # Reviewed, uplink-ready sol plans
├── user-docs/
│   ├── getting-started.md             # First-sol walkthrough
│   └── harmony-framework-explained.md # Plain-language explanation of the jazz mapping
└── work-log/                          # Daily session logs
    └── session-log.md                 # Session logging template
```

## The Harmonic Framework — One-Paragraph Summary

A waypoint is a **chord** built from three tones: terrain class (bedrock / regolith / aeolian / mixed), slope class (flat / inclined / steep / extreme), and science value (none / opportunistic / strategic / priority-1). The chord is **consonant** when the tones agree (flat bedrock with priority-1 science is a major triad; steep aeolian with no science is fully diminished). A **segment** is a voice-leading move from one chord to the next; smooth slope and heading transitions (≤ 5° change per metre, no contour crossings) are good voice leading. A **traverse** is a chord progression that must end on a **resolution chord** — a verified safe parking spot. **Tritone substitution** swaps one segment for another with a different terrain class but the same destination chord. **Modal interchange** borrows a segment from a parallel "conservative" plan variant. The whole framework is a structured way to talk about *what to give up to gain what* — exactly the conversation the tactical team has every sol.

## The Peer Review Workflow — One-Paragraph Summary

The reviewer panel is five roles: **rover driver** (drivability), **science PI** (return on science budget), **mechanical/safety** (slope, tilt, mechanism load), **autonomy lead** (whether AutoNav can handle the segment), and **uplink/comms lead** (pass coverage and uplink window). Each scores the candidate traverse on a 1–5 rubric across feasibility, science return, risk, comms alignment, and contingency coverage. Quorum is 4-of-5; any single hard-fail (a 1 on risk from safety, or a 1 on feasibility from driver) blocks the candidate regardless of average. Dissents are recorded verbatim, not averaged out. The output is a decision log: who reviewed, what changed, what was rejected, and why.

## Example Use Cases

### Tactical Uplink Support for a Mars Mission

A tactical uplink scientist needs to turn yesterday's downlinked imagery into tomorrow's sol plan in a few hours. The agent ingests the latest hazard map, composes 2–3 candidate traverses, applies substitution search to the riskiest segments, runs the rubric, and produces a sol plan ready for the strategic team's review.

### Mars Analog Field Test (Atacama, Devon Island, Black Rock Desert)

A university rover team is running a field test with a tethered or autonomous rover on Earth analog terrain. The same workflow applies — the DEM is from drone photogrammetry instead of HiRISE, but the harmonic framework and peer review structure transfer directly.

### Mission Concept Study for a Future Rover

A study team is evaluating candidate landing sites and traverse plans for a proposed mission. The agent helps them generate apples-to-apples comparisons across sites by composing comparable traverses for each, applying the same rubric, and surfacing the trade-offs in a common vocabulary.

### Strategic Look-Ahead for an Extended Mission

The rover has been on Mars for years; the science team wants to plan a multi-sol traverse to a high-value target 500 m away. The agent generates a look-ahead plan with branch points, identifies which waypoints are good "pivot chords" (work in multiple traverse keys), and flags where the look-ahead becomes too uncertain to commit.

### Educational / Outreach Sol Planning

A planetarium or museum is running a hands-on rover-planning activity. The harmonic framework gives non-experts a vocabulary they can grasp in 10 minutes (chord progressions, tension and release) and lets them produce traverses that are actually defensible against a flight-rules check.

## Recommended MCP Servers / Tools

- **filesystem** — Read/write GeoTIFFs, hazard maps, plan files
- **shell** — Run GDAL/rasterio/networkx pipelines, drive ROAMS-style sims
- **python** — Custom DEM processing, slope/aspect computation, graph search
- **PDF/markdown** — Generate the final sol plan handoff document

## Legal, Ethical, & Operational Considerations

- **Planetary protection.** If the agent is supporting a real mission, planetary-protection requirements (COSPAR Category IV/IVa for Mars) constrain where the rover can drive, especially near possible Recurring Slope Lineae (RSL) or other Special Regions. The agent must defer to the project's approved planetary-protection plan; no traverses into Special Regions without explicit project approval.
- **Mission data licensing.** HiRISE, CTX, and MOLA data are publicly released through the PDS Geosciences Node and PDS Imaging Node. Respect any project-specific embargoes on unreleased data.
- **No flight-software simulation claims.** This workspace produces planning artifacts; it does not replace ROAMS, RSVP, ROVERS, or any flight-qualified simulator. Do not present its output as a flight-qualified safety analysis.
- **Authorship transparency.** When a traverse is uplinked, the decision log must record human reviewers — the agent is a planning aid, not a decision authority.

## Technical References

- [Mars 2020 Mission Overview (NASA/JPL)](https://mars.nasa.gov/mars2020/)
- [Mars Science Laboratory Mission (Curiosity)](https://mars.nasa.gov/msl/)
- [HiRISE — High Resolution Imaging Science Experiment](https://www.uahirise.org/)
- [CTX — Context Camera (MRO)](https://mars.nasa.gov/mro/mission/instruments/ctx/)
- [PDS Geosciences Node — Mars](https://pds-geosciences.wustl.edu/missions/mro/)
- [Maki et al., "Mars 2020 Engineering Cameras" (Space Sci Rev, 2020)](https://link.springer.com/article/10.1007/s11214-020-00765-9)
- [Rankin et al., "Driving Curiosity: Mars Rover Mobility Trending During the First 7 Years" (IEEE Aerospace, 2020)](https://ieeexplore.ieee.org/document/9172469)
- [Verma et al., "Autonomous Driving Software on the Mars Rover" (RA-L, 2023)](https://ieeexplore.ieee.org/document/10122610)
- [Mark Levine, "The Jazz Theory Book" (Sher Music, 1995)](https://www.shermusic.com/) — canonical reference for the harmony framework borrowed here
- [NASA Systems Engineering Handbook — Peer Reviews](https://www.nasa.gov/reference/systems-engineering-handbook/) — the peer review structure used here is a tactical-scale adaptation
