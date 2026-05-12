# /draft-cadence — Generate the Pre/During/Post Cadence Calendar

Produce the full communication calendar with template IDs, channels, and approvers populated for every required touchpoint. The output of this command is the operational backbone of the cohort.

## Required Inputs
- `context/project.md` populated (key dates, channels, goals)
- `outputs/stakeholder-register-{cohort_id}.md` from `/map-stakeholders`
- `resources/stakeholder-template-library.md` available
- Confirmation from the user that the register is approved

## Steps

### 1. Lay the Phase Backbone
In `planning/plan.md`, write the phase headers in order:

```
## Phase 1 — Pre-launch (T-30 to T-1)
## Phase 2 — During (per module)
## Phase 3 — Midpoint pulse
## Phase 4 — Post-cohort (D+0 to D+30)
## Phase 5 — Long-term reinforcement (D+60 to D+180)
```

### 2. Pre-launch Touchpoints
Default rows (skip any that do not apply):

| ISO date | T- | Stakeholder | Template ID | Channel | Approver | Status |
|----------|----|-------------|-------------|---------|----------|--------|
| {{T-30}} | T-30 | Sponsor | `pre-sponsor-inform-email` | email | sponsor-CoS | draft |
| {{T-21}} | T-21 | Learner | `pre-learner-invite-email` | email + LMS | facilitator | draft |
| {{T-21}} | T-21 | Manager | `pre-manager-inform-email` | email | facilitator | draft |
| {{T-14}} | T-14 | Learner | `pre-learner-invite-calendar` + welcome Loom | calendar | facilitator | draft |
| {{T-14}} | T-14 | Manager | `pre-manager-nudge-email` | email | facilitator | draft |
| {{T-7}}  | T-7  | Learner | `pre-learner-remind-email` | email | facilitator | draft |
| {{T-3}}  | T-3  | Admin | `pre-admin-inform-email` | email | facilitator | draft |
| {{T-1}}  | T-1  | Learner | `pre-learner-remind-email` | email + LMS | producer | draft |
| {{T-1}}  | T-1  | Facilitator | cohort dossier (internal) | internal doc | producer | draft |

### 3. During-Phase Cadence (per module)
For each module, instantiate this block:

| ISO date | Relative | Stakeholder | Template ID | Channel | Approver |
|----------|----------|-------------|-------------|---------|----------|
| {{module_session_date - 2d}} | T-2 | Learner | `during-learner-invite-email` | email + LMS | facilitator |
| {{module_session_date}} | T0 | Learner | live session | conferencing | facilitator |
| {{module_session_date + 1d}} | T+1 | Learner | `during-learner-recap-email` | email + LMS | facilitator |
| {{module_session_date + 1d}} | T+1 | Manager | `during-manager-nudge-email` | email | facilitator |
| {{module_session_date + 1d}} | T+1 | Facilitator | `during-facilitator-recap-internal` | internal doc | facilitator |
| {{module_session_date + 1d}} | T+1 | Sponsor | `during-sponsor-recap-email` (Definitive only) | email | sponsor-CoS |
| {{module_session_date + 3d}} | T+3 | Learner | `during-learner-nudge-slack` | slack | producer |
| {{module_session_date + 5d}} | T+5 | Manager | `during-manager-reinforce-email` | email | facilitator |

### 4. Midpoint Pulse
| ISO date | Stakeholder | Template ID | Channel | Approver |
|----------|-------------|-------------|---------|----------|
| {{midpoint_date}} | Learner | `during-learner-pulse-email` | email + LMS | facilitator |
| {{midpoint_date + 3d}} | Learner | `during-learner-pulse-recap-email` (close the loop) | email + LMS | facilitator |
| {{midpoint_date + 3d}} | Facilitator | facilitator pulse summary | internal doc | facilitator |
| {{midpoint_date + 3d}} | Sponsor | sponsor pulse summary | email | sponsor-CoS |

### 5. Post-cohort
| ISO date | Stakeholder | Template ID | Channel | Approver |
|----------|-------------|-------------|---------|----------|
| {{D+0}} | Learner | `post-learner-celebrate-email` (certification) | email + LMS | facilitator |
| {{D+0}} | Sponsor | `post-sponsor-recap-email` (Levels 1+2) | email | sponsor-CoS |
| {{D+1}} | Learner | `post-learner-reflect-email` (commitments) | email | facilitator |
| {{D+7}} | Manager | `post-manager-nudge-email` (3-question check-in) | email | facilitator |
| {{D+14}} | Learner | `post-learner-apply-slack` (peer-share) | slack | producer |
| {{D+30}} | Sponsor | `post-sponsor-recap-email` (Level 3 readout) | email | sponsor-CoS |
| {{D+30}} | Alumni | `post-alumni-invite-email` | email | facilitator |

### 6. Long-term Reinforcement
- D+60: reinforcement micro-module (`post-learner-apply-email` variant)
- D+90: manager ROI check-in (`post-manager-roi-email`)
- D+180: alumni success-story collection (`post-alumni-celebrate-email`)

### 7. Channel & Time-Zone Audit
- For each row, compute send time in each represented learner time zone.
- Move any send that falls outside 08:00–20:00 local for ≥10% of the cohort to a second wave.
- Verify ≥2 means of representation per outbound module recap (text + Loom is the default).

### 8. CoI Balance Check
Sum the cognitive / social / teaching presence tags across the during-phase rows. Each presence should be ≥25% of the touchpoint count. If imbalanced, swap or add a row to rebalance.

### 9. Approver Attach
Pull the named Accountable from the RACI for every row. If a row has no approver, mark it `BLOCKED — no approver` and surface to the user.

### 10. Render
Write the calendar to `planning/plan.md` with:
- A "How to read this calendar" preamble (3 lines)
- The phase tables
- A summary block: total touchpoints, by stakeholder, by channel, CoI balance, time-zone audit result
- A "Templates that need authoring" list — any `<<NEW>>` rows from the template library check

## Output
- `planning/plan.md` — the live cadence calendar
- A `cadence-summary.md` snapshot in `outputs/` for stakeholder review
- Work-log entry recording the version of the calendar shipped for review

## Decision Points
- If two sends to the same audience fall within 24 hours, merge into one digest unless one is a triggered urgent message.
- If a manager send precedes the parallel learner send, reorder; learners always hear first about their own course.
- If the cohort spans more than three time zones, choose two send waves rather than one global wave.
- If `<<NEW>>` rows appear, schedule the template authoring before the send date the row depends on.
