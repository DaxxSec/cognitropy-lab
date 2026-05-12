# /map-stakeholders — Power–Interest, Salience, and RACI

Build the stakeholder register that drives every cadence decision downstream. Run this once after `/onboard`, then re-run at every phase boundary.

## Required Inputs
- A populated `context/project.md` (cohort, stakeholders, dates)
- A clear named accountable for sponsor approvals
- The user's read on which stakeholders are likely to escalate or block

## Steps

### 1. Pull the Stakeholder List
Read the initial roster from `context/project.md`. Confirm each named individual or named role; placeholder roles ("the L&D person") are not acceptable.

### 2. Score Power and Interest (1–5)
For each stakeholder, ask the user (or infer with caveats) two scores:
- **Power**: 1 = no influence on the cohort's success; 5 = can shut the program down or expand it
- **Interest**: 1 = does not care what happens; 5 = personally invested in the outcome

Tabulate in `outputs/stakeholder-register-{cohort_id}.md`.

### 3. Apply Power–Interest (Mendelow)
Map each stakeholder to a quadrant:
- **Manage closely** (Power ≥ 4, Interest ≥ 4) — full cadence, named approver
- **Keep satisfied** (Power ≥ 4, Interest < 4) — milestone-driven, never deluge
- **Keep informed** (Power < 4, Interest ≥ 4) — full content, no decision asks
- **Monitor** (Power < 4, Interest < 4) — single inform per phase boundary

### 4. Apply Mitchell-Agle-Wood Salience
For each stakeholder, mark Power / Legitimacy / Urgency present (Y/N). Combinations:
- Definitive (P + L + U) — cadence depth maximum, named approver, two-day SLA on questions
- Dominant (P + L) — full cadence
- Dependent (L + U) — supportive cadence; surface their needs to a Definitive stakeholder
- Discretionary (L only) — milestone touchpoints
- Dangerous (P + U, no L) — flag and resolve; this is rare but real (e.g., a politically empowered detractor)
- Demanding (U only) — single response then archive
- Dormant (P only) — monitor for activation

### 5. Build the RACI per Phase
For every artifact across phases (Pre / During / Midpoint / Post / Long-term), name:
- **Responsible** — does the work
- **Accountable** — single named signoff before send
- **Consulted** — must review (compliance, accessibility, legal if regulated)
- **Informed** — receives the result, no signoff

Artifacts to RACI explicitly:
- Kickoff invite (learner)
- Manager heads-up (manager)
- Sponsor pre-brief (sponsor)
- Module recap pack (multi)
- Midpoint pulse + summary (multi)
- Triggered learner outreach (learner; manager-CC after T+72h)
- Sponsor readout (sponsor)
- Cohort-close certificate (learner)
- Alumni invite (alumni)

### 6. Approver Conflict Resolution
If two stakeholders compete for accountable on the same artifact (e.g., compliance vs. sponsor on regulated language), document the conflict and resolve before any drafting. Default rule: in regulated industries, compliance is accountable on regulated content; sponsor is accountable on framing and direction.

### 7. Render the Register
Write to `outputs/stakeholder-register-{cohort_id}.md` with sections:
- Overview (one paragraph)
- Power–Interest grid (table)
- Salience map (table)
- RACI by phase (table)
- Approver conflicts and resolutions
- Re-rank schedule (when this register will be reviewed: phase boundaries)

Mirror the table-of-contents into `planning/plan.md` so the cadence calendar references the register, not duplicate stakeholder data.

## Output
- `outputs/stakeholder-register-{cohort_id}.md`
- Updated `planning/plan.md` with stakeholder reference block
- A one-line entry in `work-log/<YYYY-MM-DD>.md` recording who approved the register and when

## Decision Points
- If a stakeholder's salience is Definitive but no named approver exists: pause the workflow and ask the user to name one before drafting any send.
- If two phases will have very different salience profiles (e.g., compliance disappears post-cohort), build a "phase-2 register" alongside the main register.
- If the sponsor's chief of staff is the de facto accountable (common pattern), name them explicitly and copy the sponsor on the formal artifact.
