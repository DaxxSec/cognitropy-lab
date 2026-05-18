# /thrust-uncertainty-budget

Propagate type-A and type-B uncertainties through the load-cell chain per JCGM 100 (the GUM) and emit a combined / expanded uncertainty value mapped to the test's measurement objective. Walks the `U-*` tree (`context/workflows.md` §3).

## Inputs

- `test_id` — test identifier.
- `cell_serial(s)` — load cell serial numbers in use; required to fetch the most recent ASTM E74 cert.
- `cal_cert_paths` — calibration certificate paths (one per cell) per ASTM E74.
- `amplifier_spec_path` — signal-conditioner datasheet + measured noise (shorted-bridge test data).
- `daq_spec` — ADC bits, range, sample rate.
- `alignment_data_path` — most recent stand alignment survey (axial tilt budget in degrees).
- `thermal_profile_path` — expected stand thermal sweep across the planned burn (or worst-case envelope).
- `gimbal_active` — boolean. If true, side-load cross-talk term enters the budget.
- `measurement_objective_tolerance` — e.g. `0.5%` for qualification, `2%` for development. With k value.

## Steps

1. Run `U-0` intake. Reject if calibration certificate or measurement objective is missing. Calibration check (`/load-cell-calibration-check`) must have passed first.
2. At `U-1`, enumerate every input term from `context/concepts.md` §"Typical Inputs to a Thrust Uncertainty Budget" that applies. Mark each as type-A (statistical) or type-B (other).
3. Assign standard uncertainty at `U-2`. Type-A: σ / √N from N observations. Type-B with manufacturer's `±a`: rectangular distribution, `u = a/√3`. Cite source per row.
4. Compute sensitivity coefficients at `U-3`. For thrust derived from cell output: `c_F-wrt-cell ≈ 1`. For alignment tilt: `c_F-wrt-θ ≈ -F · sin(θ)`. For thermal: `c_F-wrt-T = α · F`. Document each derivative.
5. At `U-4`, check for correlated inputs. Multi-cell stands with shared excitation supplies → correlated; include covariance terms. Tare and reading from same cell on same day → correlated through cell zero.
6. At `U-5`, compute combined standard uncertainty: `u_c² = Σ (c_i · u(x_i))² + 2 · Σ_{i<j} c_i · c_j · ρ_{ij} · u(x_i) · u(x_j)`.
7. At `U-6`, compute expanded uncertainty `U = k · u_c`. Default `k=2`. If effective degrees of freedom `ν_eff < 30`, derive k via Welch-Satterthwaite and report.
8. Compare to measurement objective at `U-7`. If `U > tolerance`, identify the dominant term(s) and emit a sensitivity-analysis-driven mitigation plan; do not propose blanket re-engineering.
9. Write the budget table to `outputs/uncertainty/<test_id>-thrust-budget-<YYYYMMDD>.md`.

## Output

Markdown file containing:
- Test ID, cell serials, calibration cert hashes, measurement objective.
- Budget table: term name, type (A/B), distribution, raw value, standard uncertainty `u(x_i)`, sensitivity `c_i`, contribution `c_i · u(x_i)`, contribution-to-`u_c²` percent.
- Correlation notes and covariance terms applied (if any).
- Combined standard uncertainty `u_c` in N and in % of expected reading.
- Expanded uncertainty `U_95 = 2·u_c` in same units; if k≠2 used, explanation and computed coverage.
- PASS / REWORK against the measurement objective.
- Dominant-term ranking and mitigation recommendations if REWORK.
- Reproducibility footer: cell serial(s), cert hash(es), `git SHA` of this workspace.

## Notes

- Do not skip `U-4` (correlation). Multi-cell stands are *not* independent measurements when they share excitation or cabling.
- Long-burn tests are usually thermal-dominated; if your dominant term is "alignment" on a 300-second burn, your thermal model is probably wrong.
- The k=2 convention is for ~95% coverage assuming Gaussian-like combined distribution. For low DOF, the t-distribution gives a larger k for the same coverage.
- `U` is reported on the thrust *value*, not on the engine performance metric. If the customer wants `±0.5%` on specific impulse, propagate further through the `Isp = F/ṁ` chain — that's a separate budget that depends on flow-rate uncertainty too.
- Rectangular distribution (`u = a/√3`) is the default for type-B without distribution evidence. Triangular, Gaussian, or U-shaped distributions are acceptable with justification.
