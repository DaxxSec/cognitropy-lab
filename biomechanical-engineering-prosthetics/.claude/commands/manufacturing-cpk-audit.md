# /manufacturing-cpk-audit

Calculate Cp and Cpk on socket manufacturing tolerances vs. specification — catches drift in lamination thickness, alignment angles, geometric features before they reach the patient.

## Inputs

- **Manufacturing measurement data** — recent in-house lamination batches OR vendor incoming-QC measurements. ≥30 parts per measurement variable for reliable capability estimation.
- **Spec for each variable** — USL (Upper Spec Limit), LSL (Lower Spec Limit), target (nominal). Typical variables: lamination thickness (mm) per zone, socket trim-line position (mm from anatomic landmark), alignment angles (sagittal tilt, coronal lean, in degrees), distal-end-to-knee-axis offset.
- **Gauge R&R** for the measurement system (from `/fitting-gauge-rr`) — required input; capability claims are invalid if R&R isn't acceptable.
- **Subgroup structure** — were parts measured one-at-a-time (use Cp, Cpk, sigma estimated from MR) OR in rational subgroups (use X-bar/R-based sigma estimate)?

## Steps

1. Read `context/references.md` "Cp/Cpk interpretation table".
2. Validate measurement system: confirm Gauge R&R % contribution <10% (or document the exception and inflate uncertainty accordingly).
3. Check distribution: per variable, test for normality (Anderson-Darling p>0.05 typical threshold). Non-normal → either transform (Box-Cox) or use non-parametric capability (Cnpk via Burr percentile method).
4. Compute process statistics:
   - Mean (x̄), within-subgroup sigma (σ_within) for capability; total sigma (σ_total) for performance.
   - Cp = (USL - LSL) / (6σ_within)
   - Cpk = min[(USL - x̄)/(3σ_within), (x̄ - LSL)/(3σ_within)]
   - Pp, Ppk (performance) same formulae with σ_total
   - Cpm (Taguchi capability index, penalises deviation from target)
5. Interpret:
   - Cpk < 1.0 → process not capable; producing nonconforming parts
   - 1.0 ≤ Cpk < 1.33 → marginal; expect occasional non-conformance
   - 1.33 ≤ Cpk < 1.67 → capable; standard manufacturing target
   - Cpk ≥ 1.67 → highly capable; world-class
   - Cp > Cpk → process is off-centre (centring issue, not spread issue)
6. Identify root cause for any sub-1.33 variable: centring (mean shift) vs. spread (excess variation) vs. mixture (bimodal distribution suggesting two sub-processes).
7. Generate audit report at `outputs/cpk-audits/<batch-id>/<YYYY-MM-DD>-cpk.md` with: per-variable Cp/Cpk/Pp/Ppk, normality verdicts, capability verdicts, root-cause hypothesis, recommended actions (recentre / reduce variation / segregate vendor lots / improve fixture).

## Output

A markdown audit report containing: batch identification, measurement-system R&R citation, per-variable distributional analysis, Cp/Cpk/Pp/Ppk table, capability verdicts colour-coded (green Cpk≥1.33, yellow 1.0-1.33, red <1.0), root-cause hypothesis per yellow/red variable, recommended actions. Capability histograms with spec lines overlaid, saved as PNG.

## Decision points

- **If sigma_within differs substantially from sigma_total** → process is unstable across subgroups; address stability (control chart, SPC) before claiming capability.
- **If data is non-normal but Box-Cox transformation succeeds (W>0.95)** → report Cpk on transformed scale with the transformation noted; users must interpret in original units via inverse-transform.
- **If Cpk is high but parts are still failing downstream** → suspect that the measured variable isn't the variable that drives the failure. Re-examine the failure mode and re-select measurements.

## Notes

- Cp ≠ Cpk: Cp ignores centring; Cpk penalises it. Always report both; a process with Cp=2.0 but Cpk=0.8 has tight variation but is off-target — fixable by recentring without reducing spread.
- Performance indices (Pp, Ppk) use total sigma; capability indices (Cp, Cpk) use within-subgroup sigma. Ppk < Cpk by a lot = process is drifting between subgroups, not just noisy within them.
- Don't over-trust capability indices computed from <30 parts; the sigma estimate is noisy. Report with confidence intervals (Bissell's approximation: Cpk ± 1.96 × Cpk × √(1/(9n) + 1/(2(n-1)))).
- Spec limits should be customer-meaningful (does a 0.5mm trim-line deviation actually affect fit?). Tight specs with capable processes are pointless if the spec doesn't matter to fit; loose specs with incapable processes are dangerous.
