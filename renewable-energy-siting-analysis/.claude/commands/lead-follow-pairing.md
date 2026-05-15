# /lead-follow-pairing

Pair each variable-renewable joint with a firm or storage **follower** so the forecast-error and ramp budgets close. Emit a pairing table with per-pair Effective Load Carrying Capability (ELCC) contribution.

## Inputs

- `project_id` — articulation graph identifier.
- `joints` — joints to pair (defaults to all variable-renewable joints from the articulation graph: wind, solar PV/CSP, run-of-river hydro).
- `followers` — available firm or storage joints: storage joint IDs from the graph, plus any external firm capacity (PPA, tolling, gas firm). Each follower needs `mw_available, hours_of_duration_or_firm, cost_per_mw_year`.
- `target_capacity_credit` — desired pair capacity credit as a fraction of paired nameplate (default 0.85 for capacity-market clearance, 0.95 for resource-adequacy obligation).
- `forecast_error_p` — operational forecast-error percentile to size against, default P95 day-ahead (`hourly_error_mw`). Pull from in-house operations or use the ISO-published value in `context/references.md` Table R-5.
- `ramp_budget` — BA's 10-minute ramp ceiling per BAL-001 (sub-MW for small BAs, multi-GW for ISOs). Defaults documented per BA.

## Steps

1. **Pair-feasibility gate (`P-0`).** Verify each lead joint has its centerline walk's capacity-coincident CF available (`C-3` output). Lead joints without C-3 results cannot pair — route them back to `/centerline-resource-walk` first.
2. **Compute lead profile.** For each lead joint, extract the top-100 net-load hours from C-3 and the day-ahead forecast-error series. The pair must absorb both the capacity-coincident *level* shortfall and the *forecast-error* variance.
3. **Storage follower sizing.** For each candidate storage follower, size against:
   - Power: `P_storage = max(forecast_error_p95_hourly, lead_capacity_shortfall_at_top100)`.
   - Energy: `E_storage = P_storage × min(4h, hours_until_lead_recovery_at_p95)`. The 4-hour cap reflects most ISO capacity-market ELCC-saturation curves; longer-duration storage gets diminishing capacity credit.
   - Augmentation reserve: ~12-18% over year-1 size to cover lithium calendar degradation (Ah loss + impedance growth) over project life. Cite the assumed degradation profile.
4. **Firm follower sizing.** For firm capacity (gas peaker, hydro reservoir, contracted PPA), size against the *deeper* of the two shortfalls — capacity-coincident or the worst 8-hour event from `/load-following-rehearsal` if available.
5. **ELCC computation per pair.** Compute ELCC using one of: (a) ISO published class rating (fastest, lowest-fidelity), (b) regression on the ISO's published ELCC class curve adjusted for pair-specific resource shed, (c) production-cost-model rerun with and without the pair (highest-fidelity, requires PLEXOS / GridView / Aurora). Tag the method on the face of the output.
6. **Sympathetic-motion adjustment.** Pull the correlation matrix from `/sympathetic-motion-audit`. Pair ELCC is *not* additive when leads share a shed; the audit's correlation penalty applies to the pair's marginal ELCC.
7. **Walk `P-1` — pair-level verdict.** Compare pair ELCC × paired nameplate to the target capacity credit. PASS / REWORK / REJECT per pair.
8. **Walk `P-2` — portfolio-level verdict.** Sum pair ELCC contributions (post-sympathetic-motion adjustment) against the project's stated capacity-market obligation or RA bucket. If the portfolio sum < obligation, walk back to step 3 with a larger follower or to `/articulate-portfolio` with an added joint.
9. Write the pairing to `outputs/<project_id>/pairing-table-<YYYYMMDD>.md`.

## Output

Markdown pairing table containing:

- Pair table: `pair_id, lead_joint, follower_joint, follower_size_mw, follower_size_mwh, ELCC_pair, capacity_credit_mw, verdict`.
- ELCC computation method per pair (with citation).
- Sympathetic-motion correlation adjustment applied (link back to `/sympathetic-motion-audit` output).
- Portfolio-level capacity credit total vs target.
- Per-pair and portfolio verdicts.
- Cost summary at the pair level (`$/MW-yr` follower CAPEX amortised vs ELCC value at the prevailing capacity market clearing price).
- Reproducibility footer.

## Notes

- ELCC saturates. Adding a second 4-hour battery follower to the same lead earns roughly 50-70% of the first's marginal ELCC; a third earns ~30-50%. Plot the saturation curve and stop adding storage at the point where the marginal $/MW exceeds the capacity-market clearing price.
- ELCC is technology-class-specific *and* portfolio-specific. A 4-hour battery in a PJM portfolio with 30% solar penetration earns more ELCC than the same battery in a portfolio with 60% solar — the cleared LSE shape changes.
- A `REJECT` at P-1 means the pair cannot close even with infeasibly large storage — usually because the lead's capacity-coincident CF is too low. Walk back to `/centerline-resource-walk` and reconsider the lead.
- *Never* pair two variable-renewable joints with each other as lead-and-follow. Wind does not follow solar reliably enough to count toward capacity credit; the empirical correlation is 0.1-0.3, far below what ELCC math needs.
