# /report-findings — Generate Pre-Engagement Threat Assessment Report

Produce the formal deliverable for the detail leader and protectee. This is the artefact that ends a pre-engagement workflow chain (`/onboard` → `/risk-matrix` → `/threat-assessment` → `/route-survey` → `/crash-kinematics` → `/protective-formation` → here).

## Required Inputs

- Engagement-id with all upstream artefacts populated:
  - Refreshed risk matrix
  - Threat assessment with leg-keyed posture
  - At least one route survey
  - At least one kinematics scenario for any vehicle-borne row at Orange or Red
  - Formation plan
- Distribution list (codename only) — who gets the report

## Procedure

### 1. Pull upstream artefacts
Read every dependent artefact under `outputs/` and `planning/` for the engagement-id. If any is missing, refuse to generate and tell the user which workflow needs to run first.

### 2. Authoring discipline
Before writing a single sentence:
- Confirm every threat statement carries an evidence grade
- Confirm every recommendation carries a matrix-cell trace
- Confirm every kinematics number declares its assumptions
- Confirm no real PII is anywhere in the source artefacts (codenames only)

If any of those fail, fix the source artefacts first; do not paper over in the report.

### 3. Report skeleton
Build the deliverable in this order:

1. **Executive summary** (≤ 200 words) — purpose, posture verdict, top 3 findings, recommendation
2. **Engagement scope** — codename, dates, geography, mission objective
3. **Methodology in one paragraph** — likelihood × impact 5×5, evidence grades A–D, kinematics override on vehicle-borne rows
4. **Refreshed risk matrix** — embed the heatmap; cell table with L, I, evidence grade, mitigation layer
5. **Itinerary leg-by-leg posture** — one row per leg with worst-cell posture and driving cells
6. **Route / venue advance findings** — chokepoints, IED predictability, bollard verdicts
7. **Vehicle-borne scenario bands** — for each kinematics scenario: ΔV / KE / AIS / intrusion band / mitigation deltas
8. **Formation and choreography** — vehicle order diagram, distance schedule, arrival/departure choreography, comms plan
9. **Mitigation coverage map** — every Orange/Red cell with engaged layers and gaps
10. **Recommendation** — proceed / proceed-with-mitigation / reschedule / cancel; if proceed-with-mitigation, the specific actions and owners
11. **Pre-attack indicator scan** — what was looked for in the last 14 days, what was found
12. **Assumptions and unknowns** — explicit list, ranked by what would most shift posture if known
13. **Distribution** — codename-keyed recipient list with classification handling instructions
14. **Appendix A** — kinematics worked calculations
15. **Appendix B** — full evidence anchor list with sources and grades

### 4. Tone discipline
- Neutral, evidence-graded, decision-oriented
- No catastrophising; no soft-pedalling
- No vague verbs ("monitor closely") without a defined mitigation owner
- Numbers in ranges where uncertainty is non-trivial

### 5. Save and version
Save as `outputs/<engagement-id>-tha-report-<YYYY-MM-DD>-v<n>.md`. Increment v on each regeneration. Never overwrite.

### 6. Distribution audit
Append a "Distribution" entry to `work-log/<date>.md` with:
- Engagement-id
- Report version
- Recipient codenames
- Report hash (SHA-256 of file contents)
- Time of distribution

The hash is the workspace's tamper-evidence; if the report changes after distribution it will not match.

## Output

A versioned markdown report under `outputs/` ready to brief.

## Refusal triggers

Refuse to generate if:
- Any source artefact contains real PII
- Any cell in the matrix lacks an evidence grade
- Any kinematics scenario lacks declared assumptions
- The user requests removal of evidence-grade or matrix-cell traceability to "tighten" the deliverable (constraint violation; log refusal)
- The user requests publication / external distribution beyond the codename-keyed list
