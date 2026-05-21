# Biomechanical Engineering — Prosthetics — Workflows and Methodology

Step-by-step procedures the agent uses for fitting, gait-analysis SPC, fatigue testing, gauge studies, recall response, and continuous improvement. Each workflow maps to one or more bespoke commands in `.claude/commands/`.

## Workflow 1: Initial Fitting and Baseline Lock

**Goal:** Take a new fitting from definitive socket through baseline-locked SPC charts at 90 days post-fit.

### Steps

1. **Definitive socket fabrication** — laminate per spec; run `/manufacturing-cpk-audit` on the build to confirm Cp/Cpk ≥ 1.33 on critical tolerances (lamination thickness, trim-line, alignment).
2. **Dynamic alignment session** — static alignment first (plumb-line); then dynamic via gait observation + pressure-map; iterate.
3. **Day-0 baseline gait session** — 3+ trials self-selected pace + 1-2 fast/slow if patient tolerance allows. Captures: spatiotemporal, kinematic, kinetic, pressure-mat at PTB / tibial crest / distal end.
4. **30-day follow-up** — re-collect gait + pressure-map (representative session). Check for early signs of drift.
5. **60-day follow-up** — same.
6. **90-day follow-up + baseline lock** — collect 3rd post-fit session; combined with day-0/30/60, run `/gait-lab-spc-baseline` to lock SPC limits for ongoing monitoring.
7. **PROM at 90 days** — administer PEQ + AMP-PRO + Houghton; store as cohort baseline.

### Decision points

- **If patient reports significant discomfort between visits** → that visit is *problem-focused*, not *representative*; exclude from SPC baseline calculation.
- **If significant component change occurs before 90 days** (e.g. liner replacement, foot upgrade) → restart the baseline clock from the change date.
- **If pressure-mat baseline shows ROI with very tight variation (<5% CV)** → consider whether the patient is gait-modifying to avoid loading that area; cross-check against PROMs.

### Output

A locked SPC baseline (`outputs/spc-baselines/<patient-id>/<date>-baseline.json`) and a 90-day PROM record. Subsequent visits use this baseline.

---

## Workflow 2: Periodic Surveillance and Out-of-Control Investigation

**Goal:** Run ongoing follow-up data through the SPC framework; investigate any out-of-control signals.

**When to run:** Every patient follow-up visit with pressure-map and/or gait-lab data; or on a quarterly cohort-review cadence.

### Steps

1. Run `/socket-fit-control-chart` on the patient's pressure-map regions; flag any Shewhart-rule signals.
2. Run `/gait-asymmetry-detect` on the patient's gait session; flag any asymmetry beyond population baseline.
3. If signals detected → start an investigation log:
   - What changed since the last in-control session? (component, sleeve, weight, walking aid, activity level, season, comorbidity event)
   - Cross-reference all signalled variables — are they consistent with a single root cause hypothesis?
   - Schedule a confirmatory measurement before clinical action (rule out measurement noise).
4. If signal confirmed → clinical action: re-cast, component adjustment, training referral, etc. Document in patient chart with reference to the control-chart event.
5. If signal disconfirmed → log as false alarm in the patient's SPC history; consider whether the chart's UCL/LCL needs tightening or loosening based on accumulated false-alarm rate.

### Decision points

- **If multiple ROIs trigger simultaneously** → system-level cause (full re-cast or alignment session needed), not isolated ROI fix.
- **If signals are persistent across visits despite intervention** → re-examine assumptions: is the baseline stale? Has the measurement system drifted? Has the patient's underlying biology changed (residual-limb shape evolution)?

---

## Workflow 3: New-Component Qualification (ISO 22675 + ISO 10328)

**Goal:** Qualify a new foot/ankle (or other structural) component before fitting first patient.

### Steps

1. Run `/iso-22675-cycle-plan` to design the cyclic fatigue test (load level per ISO load table, cycle count target, instrumentation, accept/reject criteria).
2. Run `/manufacturing-cpk-audit` on the as-manufactured tolerances of the test samples — confirm vendor delivers within spec before testing.
3. Execute the test (in-house lab or contracted lab — document chain-of-custody).
4. Periodic inspection per protocol; document any compliance change, dimension change, or crack initiation.
5. At test completion → ultimate-strength test per ISO 10328 on a separate sample (fatigue + ultimate are different tests, both required).
6. If all samples pass → component approved for fitting; add to practice formulary.
7. If any sample fails → root-cause analysis; either reject the component, request manufacturer remediation, or restrict the user-population indication.

### Decision points

- **If failure mode is unexpected (failure type not anticipated by ISO 22675 inspection criteria)** → escalate; this is a design-validation finding, not a test-pass-fail. Notify manufacturer + document in QMS.
- **If component passes by very narrow margin** → restrict user-population labelling to a more conservative K-level / weight bracket.

---

## Workflow 4: Measurement System Validation (Gauge R&R)

**Goal:** Establish or re-validate the measurement systems the practice depends on for SPC.

**Cadence:** Quarterly for high-criticality systems (pressure-mapping mat, scanner); annually for routine; immediately after hardware service or software update.

### Steps

1. Run `/fitting-gauge-rr` per the system being validated.
2. If % R&R < 10% → system acceptable; document study + schedule next re-validation.
3. If 10-30% → marginal; review whether the measurement is fit-for-purpose for the specific decision it informs. Some decisions tolerate marginal R&R; others don't.
4. If > 30% → system not fit for use in SPC. Triage:
   - Equipment issue → service, recalibrate, or replace.
   - Operator issue → retraining, written procedure, fixturing standardisation.
   - Procedure issue → revise measurement protocol.
5. Re-run after remediation; do not return to SPC use until R&R recovers.

### Decision points

- **If single operator dominates the AV** → that operator needs retraining or the procedure has ambiguity that operator interprets differently. Pair-shadow them with a known-good operator to identify the delta.
- **If R&R is acceptable but NDC < 5** → system can detect gross differences but not fine ones. Acceptable for go/no-go decisions, not for capability indices on tight tolerances.

---

## Workflow 5: Recall Response

**Goal:** Respond to a manufacturer field action or FDA recall affecting a component in the practice's formulary.

### Steps

1. Receive notice (FDA MAUDE, manufacturer bulletin, EU MDR FSCA). Categorise class (I / II / III).
2. Run `/component-recall-screen` against the practice's patient inventory to identify affected patients.
3. Stratify outreach by class + activity status (active vs. inactive patients).
4. Execute outreach per the stratification:
   - Class I active: immediate (24-72h) contact, schedule emergency refit.
   - Class I inactive: documented good-faith outreach attempts (certified mail, etc.).
   - Class II active: contact within 30 days, next routine visit ASAP.
   - Class III: incorporate into next routine visit.
5. Document every outreach attempt + response + action taken in the audit ledger.
6. Submit any required regulatory reports (FDA Form 3500A, MDR Article 87 notification).
7. At resolution (all affected patients addressed) → close the recall record in the compliance system.
8. Periodically (monthly) sweep MAUDE + manufacturer feeds proactively rather than waiting for direct notification — catches multi-vendor common-cause issues earlier.

### Decision points

- **If a Class I recall affects >5% of active cohort** → escalate to practice leadership as a programme-level emergency.
- **If a patient declines refit/removal** → document the informed-consent refusal; the practice's duty is documented offer + informed consent, not coercion.
- **If the manufacturer's recommended remediation differs from clinical judgement** → consult prescribing physician + document the deviation rationale.

---

## Workflow 6: DMAIC Continuous-Improvement Programme

**Goal:** Drive a Six Sigma DMAIC cycle on a clinic-wide quality issue (rising refit rate, declining cohort PROMs, recurring fit-related complaints).

Full steps in `/dmaic-fit-improvement` — five phases (Define / Measure / Analyze / Improve / Control) over 3-6 months.

### Cross-workflow patterns shared by all DMAIC projects

- Validate measurement systems before measuring anything else.
- Stratify baseline by every reasonable factor (fitter, component, K-level, season) before forming a root-cause hypothesis.
- Pilot improvements on a subset, not the whole practice, before rollout.
- Lock controls into standard work, not just memos. If it isn't in the protocol document, fitter competency check, and ongoing SPC review, it isn't a control.
