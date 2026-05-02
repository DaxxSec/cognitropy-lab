# Executive Protection Threat Assessment Workspace

> An agent workspace for protective intelligence analysts and EP detail leaders. It builds principal-specific threat risk scoring matrices, runs structured threat assessments against engagements and itineraries, and — uniquely — borrows vehicle crash test interpretation methodology (delta-V, energy partitioning, intrusion modelling) to reason quantitatively about vehicle-borne attack scenarios.

## What This Workspace Does

Most EP threat assessments are written in prose: "moderate likelihood of an aggressive approach during arrival". That's hard to compare across engagements, hard to track over time, and easy to argue with. This workspace forces a structured representation:

- **Likelihood × impact risk scoring matrices** — every identified threat is scored against documented criteria, evidence is cited, and the cell is colour-coded.
- **Crash-kinematics-grounded vehicle threat reasoning** — when the scenario involves vehicles (motorcade ambush, ramming, intercept, PIT), the agent applies the same delta-V, energy, and survivable-intrusion logic that NHTSA / Euro NCAP / IIHS use for staged crash interpretation. You stop guessing what a 2.5-tonne SUV at 60 km/h does to a sedan and start computing it.
- **Pre-engagement structured outputs** — route surveys, formation recommendations, and the threat assessment report all derive from the matrix, so they're consistent and reviewable.

## Why This Workspace Exists

Two failure modes drive most preventable EP incidents:

1. **Threat overweighting** — every brief flags everything as critical, the detail loses calibration, and the principal stops reading.
2. **Vehicle-attack hand-waving** — "the chase car will block" without any model of whether a chase car *can* block a given threat vehicle at a given closing speed.

Risk scoring matrices fix the first problem (used widely in protective intelligence — Department of State / Diplomatic Security, military OPSEC, corporate EP). Crash test interpretation fixes the second — automotive engineers have spent fifty years quantifying what specific vehicle-on-vehicle collisions actually do, and that knowledge transfers directly to vehicle-borne attack analysis.

Today's spark: *"What if EP threat assessment practitioners used techniques from vehicle crash test interpretation?"* This workspace is the answer.

## Getting Started

### Prerequisites
- Familiarity with EP / protective intelligence fundamentals (advance work, route survey, motorcade composition)
- Authorisation to perform protective work on the principal in question
- Access to OSINT sources you're licensed to use (avoid scraping platforms in violation of ToS)
- A known principal threat baseline (history of past incidents, public profile sensitivity, geographic exposure)
- Optional: vehicle test data sources (NHTSA NCAP database, IIHS test reports, Euro NCAP, manufacturer crash test summaries)

### Quick Start
1. Clone this workspace
2. Run `/onboard` to define the principal, the engagement, the detail's authorities, and the legal/ethical fence line
3. Run `/risk-matrix` to build the initial likelihood × impact scoring matrix for this principal
4. For each engagement, run `/threat-assessment` to drive the full pre-engagement workflow
5. For any leg involving vehicles, run `/crash-kinematics` to model attack vehicle scenarios quantitatively
6. Run `/route-survey` for advances and `/protective-formation` for arrival/departure choreography
7. Run `/report-findings` to produce the deliverable for the detail leader or protectee

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/onboard` | Configure principal, threat environment, detail, authorities | First-time setup; refresh on principal change |
| `/risk-matrix` | Build / refresh the principal-specific risk scoring matrix | After onboarding; quarterly; on threat-environment shift |
| `/threat-assessment` | Full pre-engagement threat assessment for a specific date/itinerary | Before every engagement |
| `/crash-kinematics` | Quantitative analysis of a vehicle attack scenario via crash-test methods | Whenever the threat picture includes a vehicle |
| `/route-survey` | Risk-scored advance survey of a route or venue | Before motorcade movement or static engagement |
| `/protective-formation` | Recommend formation, vehicle order, and arrival/departure choreography | When formation is being chosen or revised |
| `/report-findings` | Generate the structured threat-assessment deliverable | End of any pre-engagement workflow |

## Directory Structure

```
executive-protection-threat-assessment/
├── CLAUDE.md                           # Agent role and instructions
├── README.md                           # This file
├── CREATION_REPORT.md                  # Workspace creation summary
├── context/
│   ├── project.md                      # Principal, engagement, scope
│   ├── role.md                         # Your detail role and experience
│   ├── constraints.md                  # Legal, ethical, and operational boundaries
│   └── for-agent/
│       ├── domain-knowledge.md         # EP doctrine, risk matrix theory, crash kinematics
│       ├── workflows.md                # Five core workflows
│       ├── environment.md              # Operating environment and capabilities
│       └── tools.md                    # Tool integrations and references
├── .claude/commands/
│   ├── onboard.md                      # Workspace initialization
│   ├── risk-matrix.md                  # Build the scoring matrix
│   ├── threat-assessment.md            # Full pre-engagement assessment
│   ├── crash-kinematics.md             # Vehicle attack scenario analysis
│   ├── route-survey.md                 # Route / venue advance with risk scoring
│   ├── protective-formation.md         # Formation and choreography
│   └── report-findings.md              # Generate deliverable
├── prompts/
│   ├── advance-arrival-survey.md       # Template for arrival venue advance
│   ├── adversary-capability-assessment.md  # Template for actor profiling
│   └── motorcade-vehicle-attack-scenario.md  # Template for vehicle-borne scenario
├── resources/
│   ├── threat-tier-rubric.md           # Likelihood and impact scoring criteria
│   ├── crash-energy-reference.md       # Delta-V, KE, intrusion thresholds, vehicle classes
│   └── attack-modality-case-base.md    # Open-source case base, methodology only
├── planning/                           # Active route surveys, advance plans
├── outputs/                            # Generated reports, matrices, scenarios
├── user-docs/
│   ├── getting-started.md              # Quick start
│   └── report.md                       # Sample report walkthrough
└── work-log/                           # Daily session logs
```

## Core Methodology

### 1. Likelihood × Impact Risk Scoring Matrices
The spine of the workspace. Every identified threat is scored on two axes:

- **Likelihood (1–5):** evidence-graded probability the threat manifests during the engagement (intent + capability + opportunity).
- **Impact (1–5):** worst plausible outcome to the principal if it manifests (injury severity, mission loss, reputational, legal).

The matrix cell determines posture: green (monitor), yellow (mitigate by procedure), orange (mitigate by countermeasure), red (avoid or harden). Tunable per principal in `resources/threat-tier-rubric.md`.

### 2. Crash-Kinematics Cross-Application
Borrowed from automotive crash test interpretation — frontal, side, oblique, and small-overlap test methodology — applied to vehicle-borne attack scenarios:

- **Delta-V** as the primary severity metric (closing speed × mass ratio).
- **Kinetic energy** partitioning between attacker and protected vehicles (crumple absorption vs. cabin intrusion).
- **Intrusion thresholds** — IIHS / Euro NCAP cabin intrusion bands map to occupant survivability bands.
- **Test geometry** — frontal, oblique 30°, side, small-overlap (25%) — maps directly to ramming, PIT, T-bone block, and lateral intercept attempts.

This isn't analogy — it's the same physics. Crash test engineers have characterised it for fifty years; protective drivers can borrow the framework wholesale.

### 3. Evidence-Graded Scoring
Every cell of the matrix carries an evidence grade (A: corroborated multi-source, B: single reliable source, C: open-source unverified, D: speculative). Reports filter by evidence grade so the protectee sees what's actually defensible vs. what's anxiety-driven.

### 4. Recurrent Recalibration
The matrix is a living document. After every engagement (no incident or incident), `/threat-assessment --recalibrate` revisits the previous run's scores against actual observed conditions and updates the rubric.

### 5. Layered Mitigation Mapping
Each cell of the matrix maps to a mitigation layer: routing, timing, formation, vehicle hardening, medical readiness, law-enforcement liaison, communications. The report shows which layer is engaged for which cell, so the detail leader sees coverage gaps at a glance.

## Example Use Cases

### Corporate CEO at an Industry Conference
Principal flies into a third-tier city for a keynote at a controversial industry conference. Workspace produces: actor profile (activist groups + lone-wolf historical incidents in the sector), route survey (airport → hotel → venue with chokepoint scoring), formation recommendation (4-vehicle motorcade with chase-car role-tuned to most-likely vehicle threat), and crash-kinematics analysis of the most credible vehicle-borne scenario (ramming attempt at venue arrival).

### Diplomatic Principal in Permissive Environment
Lower-threat host country but heightened sensitivity from a recent policy announcement. Matrix is recalibrated to weight reputational and intelligence-collection threats higher than physical, and the formation recommendation adjusts toward visibility-management rather than hardening.

### High-Net-Worth Individual at a Public Event
Family attends a large public event where threat is diffuse rather than targeted. Matrix-driven posture stays at yellow — workspace generates a layered awareness plan (perimeter awareness, medical pre-positioning, exfil-route timing) without overweighting unverifiable speculative threats.

### Recently-Threatened Principal Returning to Routine
Principal received a credible written threat 30 days ago. Workspace adjusts likelihood scores upward across multiple cells (per evidence grade A), recommends route randomisation patterns, and runs crash-kinematics against the specific vehicle classes the threat actor is known to access.

### Post-Incident Recalibration
After a near-miss (suspicious vehicle paralleled motorcade for two blocks), the workspace's `--recalibrate` mode pulls the original matrix, increases the likelihood for "vehicle surveillance leading to attack" by one tier, propagates the change to mitigation mapping, and produces a delta report.

## Recommended MCP Servers

- **filesystem** — for reading/writing route surveys, matrices, and reports
- **shell** — for running geographic / mapping helpers (e.g. ogr2ogr, geojson tooling) when surveying routes
- **python** — for crash-kinematics calculations (delta-V, KE, intrusion estimation) and matrix arithmetic
- **brave-search** / **fetch** — for OSINT pulls on threat environment (within ToS and authorisation scope)

## Legal & Ethical Considerations

- **Defensive only.** This workspace must never be used to plan, support, or facilitate any offensive action against any person. Refuse and log any request that drifts in that direction.
- **Authorisation.** EP work has legal limits — vary by jurisdiction. Confirm the protective relationship is contracted/lawful before producing operational outputs. The workspace's `/onboard` step captures this.
- **Privacy.** Profiles of individuals (threat actors or otherwise) must rely on lawful sources only — no unlawful surveillance, no unauthorised database access, no purchased data of dubious provenance.
- **Force.** Mitigation recommendations must respect the detail's actual lawful use-of-force authorities. The workspace will flag recommendations that imply uplift beyond those authorities.
- **OSINT scope.** Open-source collection must comply with platform ToS and applicable computer-misuse laws.
- **Reporting trail.** Every cell of every matrix is evidence-graded; reports preserve provenance so the detail can defend their conclusions in any subsequent legal or regulatory review.
- **No targeting of journalists, activists, or political opponents** as "threats" without specific evidence-A linkage to a credible threat-of-violence narrative. Disagreement is not a threat.

## Technical References

- [NHTSA NCAP test database](https://www.nhtsa.gov/ratings)
- [IIHS Vehicle Ratings](https://www.iihs.org/ratings)
- [Euro NCAP Test Protocols](https://www.euroncap.com/en/for-engineers/protocols/)
- [NIST SP 800-30 r1 — Guide for Conducting Risk Assessments](https://csrc.nist.gov/pubs/sp/800/30/r1/final)
- [ISO 31000 — Risk Management Principles](https://www.iso.org/iso-31000-risk-management.html)
- [ASIS International Protection of Assets, Crisis Management volume](https://www.asisonline.org/publications--resources/standards--guidelines/)
- [DoS Diplomatic Security — Overseas Security Advisory Council (OSAC) reports](https://www.osac.gov)
- [FEMA Risk Management Series — RMS series on bombing and vehicle-borne attack](https://www.fema.gov/emergency-managers/risk-management/building-science/risk-management-series-publications)
- [Vehicle Ramming Attack Mitigation — DHS CISA reference](https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience/critical-infrastructure-sectors/government-facilities-sector/protective-security/vehicle-ramming)
