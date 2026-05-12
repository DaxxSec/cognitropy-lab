# /process-capability-report

Compute Cp / Cpk / Pp / Ppk capability indices for a spectrum process against either an SLA, a regulatory limit, or a link-budget spec, and produce a capability verdict — *is the process capable?* — that a non-RF stakeholder can read.

## Inputs

- **Process metric** — same metric tracked by an existing control chart (noise-floor, occupancy %, packet-loss %, peak power).
- **Specification limits** — at least one of: USL (upper spec limit), LSL (lower spec limit), or both. Source: SLA, regulator, link-budget design.
- **Data window** — default `last-30-days` of subgroup data from `subgroups.parquet`.
- **Subgroup-level vs long-term flag** — `short-term` uses within-subgroup σ_within (Cp/Cpk); `long-term` uses overall σ_overall (Pp/Ppk). Default: report both.

## Steps

1. **Confirm stability first.** Check the most recent control chart for the metric. If the process is out-of-control, capability indices are meaningless — abort and recommend resolving the OOC condition before reporting capability.
2. **Test normality.** Apply Anderson–Darling or Shapiro–Wilk to the data window. If `p < 0.05` AND a clear distribution alternative fits (lognormal, Weibull), use Box–Cox or the Z-method against the chosen distribution; otherwise apply non-parametric percentile-based capability (NIST/SEMATECH 6.1.6) and note the deviation.
3. **Compute indices.**
   - `Cp = (USL − LSL) / (6·σ_within)`
   - `Cpk = min((USL − μ)/(3·σ_within), (μ − LSL)/(3·σ_within))`
   - `Pp = (USL − LSL) / (6·σ_overall)`
   - `Ppk = min((USL − μ)/(3·σ_overall), (μ − LSL)/(3·σ_overall))`
   - For one-sided specs, use the relevant single term only.
4. **Interpret the verdict.** Map the worst of Cpk/Ppk:
   - ≥ 1.67 → **excellent** (Six Sigma target; ≤ 3.4 DPMO).
   - ≥ 1.33 → **capable** (industry default acceptance).
   - ≥ 1.00 → **marginal** (one shift away from non-conforming).
   - < 1.00 → **not capable** (current process cannot meet spec; intervene or revise spec).
5. **Project DPMO.** Compute the expected defects-per-million-opportunities at current Cpk (table in `context/references.md`).
6. **Recommend action.** If not capable: choose between (a) shifting μ via intervention (which `/intervention-ladder` rung?), (b) reducing σ (better mitigation, narrower channel, antenna improvement), or (c) renegotiating the spec.

## Output

`outputs/capability/<YYYY-MM-DD>-<metric>.md` containing:
- Spec limits, sample size, time window.
- Stability confirmation (linked control chart) and normality test result.
- Cp / Cpk / Pp / Ppk values with one-sided/two-sided handling noted.
- Verdict (excellent / capable / marginal / not-capable).
- Projected DPMO.
- Recommended action (μ shift / σ reduction / spec change), tied to the appropriate intervention rung if applicable.

## Notes

- **Stability before capability.** Reporting Cpk on an out-of-control process is the single most common SPC malpractice and produces wildly optimistic numbers.
- **Cpk vs Ppk distinction matters in audits.** Short-term Cpk reflects achievable potential; long-term Ppk reflects what stakeholders actually experience. Always report both.
- A `not-capable` verdict is sometimes the right *answer* — it tells the business the spec was unrealistic for the chosen technology / band / site.
- DPMO numbers should be quoted with caveats: they assume the fitted distribution, which is itself an assumption.
