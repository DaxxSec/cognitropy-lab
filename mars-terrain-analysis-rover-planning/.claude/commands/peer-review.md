# /peer-review — Multi-Reviewer Rubric With Dissent Capture

Run a candidate traverse through the 5-role reviewer panel and produce a decision log.

## Required Inputs

- Candidate file (`planning/candidates/<sol>-<id>.md`) — must have already passed `/risk-cadence` with no hard fails
- Reviewer panel composition (read from `context/project.md`, or solo-mode where the planner plays each role)
- Sol number
- Chair (default: rover driver; for recovery plans: mech/safety)

## Procedure

### 1. Pre-Flight Checks

Refuse to proceed if any of:
- Candidate has not been through `/risk-cadence`
- `/risk-cadence` returned a HARD FAIL
- Candidate's hazard map is older than the latest available downlink
- Reviewer panel has fewer than 4 reachable reviewers (quorum will fail)

### 2. Distribute the Candidate Package

For each reviewer, prepare a package:
- The candidate file
- The cadence report
- The hazard summary PNG
- The relevant section of the strategic plan from `planning/plan.md`
- The reviewer's role-specific checklist (from `resources/reviewer-rubric.md`)

If reviewers are async, send via the configured channel and set a deadline (default: end of planning shift).

### 3. Collect Scores

Each reviewer scores the candidate on 5 axes, 1–5:

| Axis | Driver | Science | Mech/Safety | Autonomy | Comms |
|------|--------|---------|-------------|----------|-------|
| Feasibility | primary | secondary | secondary | primary | secondary |
| Science | secondary | primary | n/a | n/a | secondary |
| Risk | primary | secondary | primary | primary | secondary |
| Comms | n/a | n/a | n/a | n/a | primary |
| Contingency | secondary | secondary | primary | secondary | secondary |

A reviewer scoring **1** on their primary axis is a **hard fail**.

### 4. Solo-Mode (Educational / Single-Planner)

When there is no live panel, the planner must explicitly walk through each role and argue from that perspective:

- For each role: write down what *that* role would object to in the candidate. Force yourself to find at least one objection.
- For each role: write down what *that* role would defend about the candidate.
- Score the candidate from each perspective.
- Capture both the objections and the scores in the decision log.

Solo-mode does not lower the bar; it requires the planner to be more rigorous, not less.

### 5. Tally

Compute:
- Total score per reviewer
- Average score per axis
- Overall average
- List of hard fails (if any)
- Quorum count (number of reviewers participating)

### 6. Capture Dissents

For any reviewer who is outvoted (e.g., scored ≤ 3 average while the panel approved):

```yaml
dissent:
  role: <reviewer role>
  score_summary: { avg: 2.6, hard_fails: [] }
  position_against: APPROVAL
  concern: |
    <verbatim text — what specifically concerns this reviewer about the candidate>
  what_would_change_position: |
    <verbatim text — what could be added/changed to bring this reviewer to approval>
```

Dissents are mandatory; a panel that "all agreed" should be re-checked because it usually means a reviewer didn't engage.

### 7. Apply Decision Rules

| Outcome | Conditions |
|---------|-----------|
| **STRONG PASS** | Quorum, no hard fails, average ≥ 4.5, no individual axis below 3 |
| **PASS** | Quorum, no hard fails, average ≥ 3.5 |
| **REVISE** | Quorum, no hard fails, average 2.5–3.5 |
| **REJECT** | Any hard fail OR average < 2.5 OR quorum not met |

### 8. Write the Decision Log

Save to `outputs/decision-log/<sol>-<id>.md`:

```yaml
sol: <N>
traverse_id: <id>
candidate_path: <hash>
reviewers:
  rover_driver: { name: <>, score: { feas: 4, sci: 3, risk: 4, comms: 5, cont: 4 }, total: 4.0 }
  science:     { name: <>, score: { feas: 4, sci: 5, risk: 3, comms: 4, cont: 4 }, total: 4.0 }
  mech_safety: { name: <>, score: { feas: 4, sci: 3, risk: 4, comms: 5, cont: 4 }, total: 4.0 }
  autonomy:    { name: <>, score: { feas: 5, sci: 3, risk: 4, comms: 5, cont: 4 }, total: 4.2 }
  comms:       { name: <>, score: { feas: 4, sci: 3, risk: 4, comms: 5, cont: 4 }, total: 4.0 }
quorum: 5/5
hard_fails: []
overall_average: 4.04
decision: PASS
chair: rover_driver
revision_history:
  - rev1: composed (chord sequence: I → ii → V7 → vi → ii → V7 → I)
  - rev2: substituted segment 4 (tritone sub: rocky climb → contoured detour)
  - rev3: passed peer review
dissents:
  - role: science
    position_against: APPROVAL
    concern: "Recommend extending dwell at WP-3 by 30 min for SuperCam raster on the layered outcrop."
    what_would_change_position: "Add 30 min science block at WP-3 to the sol plan."
follow_up_actions:
  - Pass dissent to /sol-plan as input
  - Confirm with science PI whether the WP-3 extension fits the data-volume budget
```

### 9. Notify the User

Print a concise summary:
- Decision (STRONG PASS / PASS / REVISE / REJECT)
- Quorum and hard-fail status
- Number of dissents captured
- Path to the decision log
- Recommended next command (`/sol-plan` for PASS; `/substitution-search` or `/traverse-compose` for REVISE; back to `/traverse-compose` from scratch for REJECT)

## Output

The decision log file (the canonical "why was this traverse approved" artifact) and a recommendation. On PASS, the candidate is now eligible for `/sol-plan`.
