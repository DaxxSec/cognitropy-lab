# Active Plan

## Phase 1 — Stand-up (Day 1-7)
- Run `/onboard` to capture agency, role, authorities.
- Review `context/for-agent/` to validate domain knowledge matches local policy.
- Tune `resources/risk-scoring-rubric.md` weights to mission.
- Intake 3-5 test/synthetic subjects with `/intake-subject` to exercise the flow.

## Phase 2 — Baseline caseload (Day 8-30)
- Intake a representative slice of real caseload (pseudonymized).
- Run `/drift-scan` against each with current evidence.
- Produce initial prioritization report via the batch-drift-scan prompt.

## Phase 3 — Operational cadence
- Weekly: triage new CE alerts with `/continuous-eval`.
- Monthly: run batch drift scan on subjects whose scan interval has elapsed.
- Quarterly: review the rubric weights and thresholds; adjust based on hit-rate experience.
- As needed: use `/adjudicate` to pre-stage adjudicative memos.

## Risks and open questions
- The risk-score rubric is a starting point. Real calibration requires feedback from adjudicative outcomes — which may take months.
- This tool does not replace DISS/NBIS workflows. It supplements.
- Guideline weights must not drift away from agency policy. Log every change.

## Success criteria
- Condition-based scan intervals are being applied, not just calendar PR.
- At least one out-of-cycle action per quarter was driven by a drift scan rather than a calendar tickler.
- No real PII ever appears in a committed file.
