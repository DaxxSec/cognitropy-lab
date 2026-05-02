# /risk-matrix — Build or Refresh the Principal-Specific Risk Scoring Matrix

Produce a principal-specific 5×5 likelihood × impact matrix populated across the 10 standard threat categories, with evidence-graded cells, posture mapping, and explicit assumptions.

## Required Inputs

- `context/project.md`, `context/role.md`, `context/constraints.md` populated (run `/onboard` first if not)
- Active engagement reference (engagement-id), if scoring for a specific window
- Latest 14-day reporting on threat environment (named actors, sector incidents, geography signals)
- Vehicle inventory from `context/for-agent/environment.md` (for the kinematics handoff in category 2)

## Procedure

### 1. Load the rubric and confirm calibration
Read `resources/threat-tier-rubric.md`. Confirm whether principal-specific tuning is current. If the principal's class has shifted (e.g. now subject to active threat) re-tune likelihood and impact bands before scoring.

### 2. Walk the 10 categories from `domain-knowledge.md` §1.6
For each category, score:

- **Intent** (1–5): Does the actor want to harm or disrupt this principal? What's the source?
- **Capability** (1–5): Vehicles, weapons, technique, access — what's documented?
- **Opportunity** (1–5): Does the engagement give them a window?
- **Likelihood** = combined judgment, conservative median of the three legs (1–5)
- **Impact** (1–5): Worst plausible outcome — see §1.3 of `domain-knowledge.md`
- **Evidence grade** (A/B/C/D) for the highest-grade anchor backing the cell
- **Mitigation layer** engaged or proposed (§1.8)

### 3. Apply the kinematics override for category 2
For "Vehicle-borne attack", do **not** score impact qualitatively. Hand off to `/crash-kinematics` for the most credible scenario. Take the AIS-band output and map directly:

| AIS band from kinematics | Matrix Impact score |
|--------------------------|---------------------|
| AIS 1–2 (minor) | 2 |
| AIS 2–3 (moderate) | 3 |
| AIS 3–4 (serious-severe) | 4 |
| AIS 4–5+ (severe-fatal) | 5 |

### 4. Score each cell with explicit evidence anchors
For every cell:
- One-sentence cell description ("ramming attempt on motorcade during venue arrival, full-size SUV class")
- Primary evidence anchor (source, grade, date)
- Secondary anchor if available
- Assumption(s) underlying the score
- One unknown that, if collected, would shift the grade upward

### 5. Render the matrix

Output a Mermaid heatmap showing all 10 cells positioned on the 5×5 grid, plus a row table listing each threat with its L, I, posture, evidence grade, and mitigation layer.

### 6. Sanity checks (run before saving)
- More than two Red cells without grade-A evidence anchors → flag overweighting; ask the user to defend or downgrade.
- All Green cells → flag under-collection; a real engagement always has some Yellow.
- Mitigation layer empty for any Orange/Red → flag coverage gap.

### 7. Save and log
Save as `outputs/<engagement-id>-risk-matrix.md`. Log session summary in `work-log/<YYYY-MM-DD>.md` including cell-count summary by posture (e.g. "13 G, 4 Y, 2 O, 1 R").

## Output

A markdown artefact in `outputs/` with:
- Matrix heatmap (Mermaid)
- Cell-by-cell table (10 rows minimum)
- Evidence anchor list
- Assumptions and unknowns section
- Posture summary (count by colour)
- Recommended follow-up workflows (typically `/threat-assessment` and `/crash-kinematics` for any Orange/Red vehicle row)

## Refresh / recalibration mode

When called with `--recalibrate`, reload the previous matrix and:
- Increase likelihood +1 in any row where a pre-attack indicator (§1.7) was detected since the previous run
- Re-grade evidence where collection has improved
- Append a "Δ since previous run" section to the saved artefact rather than overwriting
