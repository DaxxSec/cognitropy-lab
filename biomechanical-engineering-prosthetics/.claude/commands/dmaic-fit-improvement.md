# /dmaic-fit-improvement

Drive a Six Sigma DMAIC (Define / Measure / Analyze / Improve / Control) cycle for a clinic-wide socket-fit improvement programme — produces the project charter, measurement plan, analysis findings, improvement piloting, and control-phase lock-in.

## Inputs

- **Problem statement** (preliminary) — what's the perceived issue (e.g. "90-day refit rate has risen from 12% to 19%", "patient PEQ-MS subscale has trended down across the cohort", "fit-related complaints up 40% YoY").
- **Cohort scope** — which patient subset (all TT, K3 only, specific fitter, specific component family, etc.).
- **Time horizon** — Six Sigma projects typically run 3-6 months. Define the DMAIC phase budget upfront (e.g. D=2wk, M=4wk, A=4wk, I=8wk, C=ongoing).
- **Project team** — sponsor (clinic medical director), champion (CPO lead), team members (fitters, technicians, scheduler), Black/Green Belt facilitator if available.
- **Quality goal** — target metric improvement (e.g. "reduce 90-day refit rate from 19% to <12% within 6 months").

## Steps

### Define

1. Write the project charter: problem statement (operational, quantified), goal statement (SMART), scope (in/out of scope), team roster, timeline, success criteria.
2. Build the SIPOC (Suppliers / Inputs / Process / Outputs / Customers) for the fit-and-follow-up process.
3. Voice of Customer: collate patient PROM feedback themes, complaint logs, fitter observations.
4. Output: `outputs/dmaic/<project-id>/D-charter.md`.

### Measure

5. Validate measurement systems via `/fitting-gauge-rr` for any measurement system being used in the project; remediate if R&R >30%.
6. Establish baseline:
   - Run `/socket-fit-control-chart` on affected cohort to characterise current process.
   - Run `/manufacturing-cpk-audit` on socket-build tolerances to characterise current capability.
   - Pull baseline refit-rate / complaint-rate / outcome distributions.
7. Compute baseline DPMO (defects per million opportunities) or refit-rate with CI.
8. Output: `outputs/dmaic/<project-id>/M-baseline.md`.

### Analyze

9. Cause-and-effect: fishbone (Ishikawa) diagram for contributing factors (Material, Method, Machine, Man, Measurement, Environment).
10. Statistical analysis:
    - Stratify baseline by fitter, by component family, by patient K-level, by season → identify largest variation contributors.
    - Run regression / classification on patient-level features → which predictors most predict refit?
    - Pareto chart of complaint reasons / failure modes.
11. Form 1-3 prioritised hypotheses for root cause.
12. Output: `outputs/dmaic/<project-id>/A-analysis.md`.

### Improve

13. Design 1-2 controlled interventions targeting the top-priority root cause(s).
14. Pilot on a subset (one fitter, one component family, one patient cohort) — measure pre/post.
15. Statistical comparison of pilot vs. baseline (paired or two-sample, FDR-adjusted across metrics).
16. Decide: roll out, modify, or scrap.
17. Output: `outputs/dmaic/<project-id>/I-improvement.md`.

### Control

18. Lock the improvement into standard work: update protocols, training materials, fitter competency checks.
19. Set up ongoing SPC (`/socket-fit-control-chart`, `/proms-trend-analysis`) on the improvement target metric — institute monthly review cadence.
20. Document the standard for future re-validation; schedule a 6-month and 12-month gain-retention check.
21. Output: `outputs/dmaic/<project-id>/C-control.md`.

## Output

Five markdown files (one per DMAIC phase) at `outputs/dmaic/<project-id>/`. Each phase output is signed off (clinic sponsor + CPO lead) before the next phase begins. Final deliverable is the control plan that the practice operates from going forward.

## Decision points

- **If Measure phase reveals the problem is smaller than perceived** → revise project charter or close the project; document the false alarm and the corrected baseline for future reference.
- **If Analyze phase reveals the root cause is outside the team's control (vendor quality, regulatory change, payer rule)** → escalate; DMAIC pivots to manage the symptom rather than fix the cause.
- **If pilot in Improve shows no significant gain** → don't roll out. Common reasons: wrong root cause, insufficient pilot duration, confounding from concurrent changes. Revisit Analyze.
- **If Control phase metric drifts within 3 months** → the improvement didn't stick; re-enter Improve to find the missing control element (training? incentive? tooling?).

## Notes

- DMAIC is iterative — don't expect a single pass to nail a complex programme. Many practices run DMAIC twice on the same problem with progressively narrower scope.
- Six Sigma's hard target is 3.4 DPMO (Cpk = 2.0). P&O fittings rarely operate at that capability; aim for 4-sigma (~6,210 DPMO, Cpk = 1.33) as a realistic target for socket fit.
- Document the sustained improvement at 6 months and 12 months; the gain that doesn't sustain isn't a gain.
- Pair the DMAIC project with the practice's broader QMS — ideally the project's control plan is referenced in the ISO 9001 / ISO 13485 quality manual.
