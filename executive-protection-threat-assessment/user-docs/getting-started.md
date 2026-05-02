# Getting Started

This is the user-facing quick-start for the Executive Protection Threat Assessment workspace. It exists to get a competent EP detail leader or protective intelligence analyst from "fresh clone" to "first deliverable" in a single session.

## Who this is for

You are one of:
- A protective detail leader running pre-engagement workflows for a principal you protect
- A protective intelligence analyst supporting a detail
- A corporate security director consolidating threat assessments for executive travel
- An EP-adjacent practitioner (operations centre lead, family office security manager) who wants disciplined risk-scored deliverables

Not for:
- Anyone targeting an individual
- Journalism or research that does not have a protective relationship to the principal
- Offensive security practitioners — this workspace is defensive only

## Before you start

You will need:
- A codename for your principal (never their real identity in this workspace)
- The engagement window and geography
- Your detail's vehicle inventory and authorities
- Access to lawful OSINT and any LE liaison reporting you're authorised to receive

## First-session flow

### 1. Run `/onboard`
The agent walks you through six sections (principal profile, engagement, detail composition, authorities, your role, threat environment snapshot). Plan ~30 minutes. Output: populated `context/` files, principal-specific tuning of the threat-tier rubric.

### 2. Run `/risk-matrix`
The agent walks the 10 standard threat categories and scores each with you. For the vehicle-borne row, it hands off to `/crash-kinematics` automatically and uses the AIS band for impact. Plan ~45–60 minutes for a fresh principal. Output: a 5×5 matrix with cell-by-cell evidence anchors and posture mapping.

### 3. Run `/threat-assessment` for your engagement
Walk the itinerary leg-by-leg. The agent applies the matrix to each leg and identifies which legs warrant `/route-survey` and `/crash-kinematics` drill-down. Plan ~45 minutes plus ~30 minutes per drill-down. Output: a leg-keyed posture summary.

### 4. Run `/route-survey` and `/crash-kinematics` as called out
Each one drills into its specific component and produces a targeted artefact. The kinematics outputs feed the matrix's impact column directly.

### 5. Run `/protective-formation`
Once the matrix and surveys are populated, formation choices fall out of them. The agent recommends vehicle order, distances, and arrival/departure choreography keyed to the dominant cells.

### 6. Run `/report-findings`
Aggregates everything into a single deliverable. Versions on each regeneration; never overwrites.

## What "good" looks like

A finished pre-engagement assessment in this workspace has:
- A risk matrix with every cell evidence-graded (no D-grade in Red cells)
- A leg-keyed posture summary for the engagement
- At least one kinematics scenario for any Orange/Red vehicle-borne row
- A formation plan with explicit vehicle-class match against credible attacker
- A report with executive summary ≤ 200 words, recommendation block, and full appendix

## What "bad" looks like (and what to fix)

- "Everything is Red" — almost always overweighting; demand a defence per cell
- "Everything is Green" — almost always under-collection; you missed something
- Vehicle-borne row scored qualitatively — should have come from `/crash-kinematics`, run it
- Recommendation that implies use-of-force authority you don't have — workspace will flag, you adjust
- Report that omits assumptions — never accept; require the agent to declare them

## Daily / weekly cadence

For an active principal:
- **Daily:** pre-attack indicator scan; update `work-log/<date>.md`
- **Weekly:** review the matrix's cell traces; recalibrate if any indicator detected
- **Per engagement:** the full 1–6 sequence above
- **Quarterly:** clean recalibration with no engagement context (catches drift)

## Where to read deeper

- `context/for-agent/domain-knowledge.md` — Part 1 (risk scoring) and Part 2 (crash kinematics). Read both at least once.
- `resources/threat-tier-rubric.md` — likelihood and impact rubric, posture mapping
- `resources/crash-energy-reference.md` — vehicle classes, ΔV bands, IIHS intrusion bands, bollard ratings

## Help / refusal patterns

The agent will refuse and log if you ask for:
- Targeting packages or surveillance instructions
- Mischaracterisation of non-violent activity as threat-of-violence
- Recommendations exceeding your detail's lawful authorities
- Removal of evidence-grade or matrix-cell traceability from a deliverable
- Real PII in any persisted artefact (use codenames)

Refusals appear in `work-log/<date>.md` and are not negotiable.
