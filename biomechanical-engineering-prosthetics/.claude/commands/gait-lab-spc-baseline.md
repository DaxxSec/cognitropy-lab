# /gait-lab-spc-baseline

Establish Statistical Process Control baselines from a patient's gait-lab kinematic and kinetic data — locks the in-control distribution that all subsequent visits' control charts will reference.

## Inputs

- **Patient gait sessions** (≥20 separate sessions, ≥3 trials each) — CSV or C3D from Vicon / Qualisys / OptiTrack motion capture + AMTI / Bertec / Kistler force-plate exports. 20+ is the minimum for I-MR chart baseline stability; 30+ preferred for X-bar-R.
- **Kinematic variables of interest** — typically: step length (m), stride width (m), cadence (steps/min), swing time (s), stance time (s), peak knee flexion in swing (deg), peak hip flexion in stance (deg), trunk lean (deg).
- **Kinetic variables of interest** — typically: peak vertical GRF (BW), braking + propulsive impulses (BW·s), peak knee extension moment (N·m/kg), peak hip extension moment.
- **Patient context** — K-level, prosthesis side, time since fit, weight, walking aid (none / cane / crutches / walker), reason for gait-lab session (routine surveillance / problem-focused).

## Steps

1. Read `context/concepts.md` "Gait analysis fundamentals" + "QC statistical methods" sections.
2. Validate input completeness: each session has all selected variables; flag missing variables for re-collection vs. computational derivation.
3. Per variable, compute session-level mean and within-session SD across trials (so each session contributes one I-MR data point or one X-bar-R subgroup).
4. Check baseline stability: run Shewhart rules 1-4 across the candidate baseline sessions (Western Electric / Nelson rules). Any signal = baseline contaminated by assignable cause; document the cause and either exclude that session or re-collect.
5. For each clean variable, compute control limits: I-MR (UCL = mean + 2.66 × MR-bar, LCL = mean - 2.66 × MR-bar) or X-bar-R (constants per Montgomery Appendix Table VI).
6. Cross-check: peak knee flexion limits should fall within physiologically credible range (e.g. 30-80 deg in swing for a TT amputee). Limits outside known-population bounds = revisit input.
7. Write baseline JSON to `outputs/spc-baselines/<patient-id>/<YYYY-MM-DD>-baseline.json` with: variable list, control limits, contributing session IDs, exclusion notes, Shewhart-rule diagnostics, K-level / weight at baseline.
8. Generate a 1-page summary memo (`outputs/spc-baselines/<patient-id>/<YYYY-MM-DD>-summary.md`) for the CPO's chart with the baseline values, variation drivers, and recommended review cadence.

## Output

- **JSON baseline file** with per-variable control limits (UCL, CL, LCL), MR-bar, contributing sessions, exclusions, and timestamp.
- **Markdown summary memo** for the CPO chart: ~20 lines per variable, with a one-line interpretation each (e.g. "Step length CL = 0.61 m, UCL/LCL = 0.68/0.54 — within K3-population norms; tight MR-bar suggests reliable gait pattern").

## Decision points

- **If <20 clean sessions available** → either collect more data before locking baseline OR lock a "provisional" baseline flagged for re-evaluation at session 30.
- **If Shewhart rules trigger on >25% of candidate sessions** → the data isn't in control yet; investigate assignable causes (component change, walking-aid change, comorbidity event) before establishing baseline.
- **If kinetic variables are at known-population extremes** → measurement-system gauge R&R may be needed (see `/fitting-gauge-rr`) before treating data as process noise.

## Notes

- Per `context/concepts.md`, P&O gait literature varies in normative reference ranges by K-level, etiology (vascular vs. traumatic vs. congenital), and time since fit. Cite the reference population every time.
- Baseline must be re-established after: component change, weight change >5%, walking-aid change, surgical revision. Otherwise stale baselines produce false out-of-control signals.
- Don't confuse "in statistical control" with "clinically optimal." A patient can have tight in-control limits around a markedly asymmetric gait — that's a *capable* but *biased* process; see `/gait-asymmetry-detect` for the bias check.
