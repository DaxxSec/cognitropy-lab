# /gait-asymmetry-detect

Statistically detect prosthetic-vs-sound-side gait asymmetry beyond known-population baselines — paired-sample inference with effect size.

## Inputs

- **Single gait session** (multiple trials) OR a series of sessions at standard intervals (30/60/90/180 days post-fit).
- **Variables to test** — symmetric variables that should be bilateral: step length, stance time, swing time, peak vertical GRF, braking + propulsive impulses, peak knee flexion in swing, peak hip extension in stance, single-limb support time.
- **Population reference** — known-population asymmetry baseline (Symmetry Index for unilateral TT amputees varies 5-12% by variable per published lit; cite source for the comparison).
- **Patient context** — K-level, time-since-fit, prosthetic side, any known asymmetry-inducing factors (residual limb pain, knee-flexion contracture, comorbidity).

## Steps

1. Read `context/concepts.md` "Gait analysis fundamentals" + `context/references.md` "Population asymmetry baselines".
2. Compute per-variable asymmetry across trials:
   - Symmetry Index SI = 100 × |X_prosthetic - X_sound| / (0.5 × (X_prosthetic + X_sound))
   - OR Symmetry Ratio = X_prosthetic / X_sound (centred at 1.0)
   - OR Gait Asymmetry Index per Robinson 1987
3. Test against population reference:
   - One-sample t-test of patient's mean SI vs. population mean SI for that K-level
   - OR Wilcoxon signed-rank if non-normal
   - Apply FDR-BH correction across all tested variables
4. Compute effect size (Cohen's d) for the patient-vs-population difference; report alongside p-value.
5. Identify clinically meaningful vs. statistically significant asymmetries:
   - SI > 10% with d > 0.5 = meaningful asymmetry, investigate
   - SI > 10% with d < 0.2 = within-population variability, no action
   - SI < 5% across all variables = clinically excellent symmetry
6. Cross-reference with `/socket-fit-control-chart` outputs from same period — fit-pressure signals on the prosthetic side concurrent with asymmetry = unified hypothesis.
7. Write asymmetry report at `outputs/asymmetry/<patient-id>/<YYYY-MM-DD>-asymmetry.md` with per-variable SI, statistical test result, effect size, clinical interpretation, recommended follow-up.

## Output

A markdown asymmetry report containing: session/series metadata, per-variable SI with 95% CI, statistical test results (FDR-adjusted), effect sizes, clinical-vs-statistical significance flagging, hypothesized causes (residual-limb / alignment / component / training), recommended actions (none / monitor / gait-training referral / component adjustment / re-cast).

## Decision points

- **If population reference unavailable for the patient's specific K-level / etiology** → use the closest match with explicit caveat; report patient-only asymmetry without the population comparison.
- **If statistical significance is reached but effect size is tiny (d < 0.2)** → the asymmetry is real but probably not clinically actionable. Document as monitoring item, not action item.
- **If asymmetry is in the *sound side* favourable direction (e.g. patient overloading prosthetic side)** → uncommon but important — often indicates patient is over-compensating with the prosthesis. Triangulate against `/proms-trend-analysis` for sound-side pain reports.

## Notes

- Symmetry Index has known issues at low absolute values (denominator near zero) — switch to absolute-difference reporting for variables that approach zero.
- Population asymmetry baselines vary by K-level + etiology + time-since-fit. Vascular TTs at 6 months post-fit show different baseline asymmetry than traumatic TTs at 6 months. Cite the matching subgroup.
- Repeated asymmetry detection over time on the same patient creates a multiple-testing burden — apply sequential FDR across visits, not per-visit.
- "Asymmetry" doesn't necessarily mean "bad outcome." Some patients adopt asymmetric strategies that minimise residual-limb stress at the cost of symmetric kinematics — that's a trade-off, not a defect.
