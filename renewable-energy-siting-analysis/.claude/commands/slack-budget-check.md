# /slack-budget-check

Audit **slack** across the articulation graph — the curtailment headroom on transmission linkages and the cushion in storage drives. The puppetry analogy: when the strings go taut, motion stops; when storage cushion empties, the next renewable ramp can't be absorbed.

## Inputs

- `project_id` — articulation graph identifier.
- `loading_series` — pre-contingency and post-contingency line loading timeseries for the linkages in the graph (from PSS/E case run or the ISO's published TLR / congestion data).
- `storage_state` — SOC timeseries for each storage joint under the weight-transfer plan, hourly or sub-hourly.
- `slack_thresholds` — pass/rework/reject thresholds for linkage loading and storage SOC. Defaults:
  - Linkage: PASS < 75% pre-contingency, REWORK 75-90%, REJECT > 90%.
  - Storage: PASS minimum SOC > 20% & maximum SOC < 90% over the year, REWORK in [10-20%] floor or [90-95%] ceiling, REJECT outside.
- `contingencies` — `n-0 | n-1 | n-1-1`. Default n-1 per NERC TPL-001-5.

## Steps

1. **Slack intake (`S-0`).** Verify loading series cover at least 8760 hours and storage state covers the same. Mismatched horizons fail at S-0.
2. **Linkage walk per `L-id` (`S-1`).** Compute the hourly loading distribution for each linkage. Flag:
   - Hours over the REWORK threshold (75% pre-contingency, 90% post-n-1).
   - Hours where the post-contingency loading exceeds the emergency rating (a structural FAIL).
   - The annual energy-curtailed implied by the linkage being the binding constraint (lost MWh on the lead joint upstream).
3. **Storage walk per storage joint (`S-2`).** Compute:
   - Minimum SOC seen across the year and the hour of that minimum.
   - Maximum SOC, with the same.
   - The number of full-equivalent cycles per year (degradation input).
   - Hours where SOC is < 5% (cushion closed) or > 95% (cushion saturated). Cushion closure on either end is a `REWORK`.
4. **Drive walk per drive `D-id` (`S-3`).** For each control lever — curtailment, DR, dispatchable hydro — compute the saturation hours. Curtailment used > the PPA cap is a REJECT for the relevant pair. DR called more than the contract maximum is a REJECT for the drive (not the pair).
5. **Cross-walk `S-4`: slack closure traces.** For each REWORK / REJECT flag, trace upstream: a linkage saturating means the lead joint upstream is curtailing; a storage cushion exhausting means a lead joint upstream is producing more than the follower can absorb. Name the upstream joint on the face of the output — `L-3 saturates 287 hrs/yr at 92% post-n-1 → curtails J-2 wind farm 41 GWh/yr` is the form.
6. **Aggregate `S-5`.** Emit a per-linkage / per-storage / per-drive verdict and a portfolio-level slack score (`slack_score = 1 − max(saturation_fraction over all components)`).
7. Write to `outputs/<project_id>/slack-budget-<YYYYMMDD>.md`.

## Output

Markdown audit containing:

- Linkage table: `linkage_id, hours_>75%_pre, hours_>90%_pre, hours_>emergency_post-n-1, MWh_curtailed_implied, verdict`.
- Storage table: `joint_id, min_SOC, max_SOC, hours_<5%, hours_>95%, cycles_per_year, verdict`.
- Drive table: `drive_id, saturation_hrs, contract_cap, verdict`.
- Slack closure trace for each non-PASS finding.
- Portfolio slack score (0-1).
- Recommended remediation per non-PASS: storage upsizing, transmission upgrade, pair re-selection, curtailment-cap renegotiation.

## Notes

- A REJECT on a single linkage is rarely fatal — the network-upgrade allocation process exists to handle this — but it shifts cost and time. Flag the network-upgrade dollar estimate from the ISO cluster study (`context/references.md` Table R-7 has typical ranges per kV class).
- Storage cushion closure on the *bottom* is more dangerous than on the top. Hitting 5% SOC means the follower failed to absorb a lead-side dip; hitting 95% means the follower clipped a renewable peak (revenue lost, but the lights stayed on).
- Slack closure traces are how you find the *real* bottleneck. A solar joint's CF is irrelevant if the linkage upstream is the binding constraint — adding more PV to the joint will simply increase curtailment, not deliverable energy.
- This command is idempotent against weight-transfer-plan changes — re-run after any plan change.
