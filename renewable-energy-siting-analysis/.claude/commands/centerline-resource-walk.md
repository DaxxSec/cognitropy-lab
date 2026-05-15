# /centerline-resource-walk

Walk a joint's centerline (resource-intensity timeseries) through the capacity-factor envelope decision tree (`context/workflows.md` §2) and emit a per-month verdict tied to ISO ELCC class assumptions.

## Inputs

- `joint_id` — the joint to walk (from the articulation graph).
- `centerline_path` — path to the resource timeseries CSV: `t, value` where `value` is wind speed at hub height (m/s), GHI (W/m²), DNI (W/m²), hydro inflow (m³/s), or geothermal gradient (°C/km), per the joint's tech.
- `source` — `WIND_TOOLKIT | NSRDB | MERRA-2 | ERA5 | met-mast | usgs-gauge`. Required. Bias adjustments are source-specific.
- `years_of_record` — int. <5 = REWORK at intake; ≥20 = full pass.
- `nameplate_mw` — joint nameplate (from articulation graph).
- `power_curve` — for wind: IEC class + manufacturer power curve (or a default Class II curve). For PV: module derate, inverter clipping, soiling, availability. Defaults are conservative; cite them in the walk.
- `losses` — wake (wind), inter-row shading (PV), penstock (hydro). Defaults documented in `context/concepts.md` §4.

## Steps

1. **Intake gate (`C-0`).** Verify `source`, `years_of_record ≥ 5`, hourly or better resolution, no >5% missing data. Abort with REWORK at `C-0` on any gate fail.
2. **Source bias adjustment.** Apply the published bias correction for the source (Table R-3 in `context/references.md`): MERRA-2 over-predicts wind ~3-7% in low terrain, under-predicts ~5-10% in complex terrain; NSRDB under-predicts GHI ~1-2% in arid sites. Annotate the adjustment.
3. **Power-curve mapping.** Convert resource timeseries to AC power timeseries: wind via the manufacturer curve with wake and availability derate; PV via module efficiency × inverter efficiency × DC-AC ratio with clipping; hydro via head-flow rating × penstock efficiency × generator efficiency.
4. **Walk `C-1` — annual envelope.** Compute annual capacity factor `CF_annual = E_year / (8760 × nameplate)`. Compare to the tech-class envelope in Table R-2 (`context/references.md`). Cite the node and the value.
5. **Walk `C-2` — monthly envelope.** Compute per-month CF; flag any month where CF is outside [μ - 2σ, μ + 2σ] of the multi-year monthly distribution. These are the "weight transfer" candidates — months where the joint contributes more or less than its annual nameplate share.
6. **Walk `C-3` — capacity-coincident envelope.** Compute CF over the top-100 net-load hours of each year (the hours that drive ELCC). For wind, this is usually summer evenings and winter mornings; for solar, summer afternoons. This is what *capacity credit* is built from, not the annual mean.
7. **Walk `C-4` — drought-year envelope.** Repeat C-1 through C-3 over the worst year in the record (typically the lowest-CF wind year or the highest-cloud solar year). The drought year is the floor; the rehearsal command (`/load-following-rehearsal`) consumes it.
8. **Aggregate to `C-5`.** Emit a per-month verdict (`PASS / REWORK / REJECT / MONITOR`) and an annual verdict tied to the joint's nameplate.
9. Save the walk to `outputs/<project_id>/centerline-walks/<joint_id>-<YYYYMMDD>.md`.

## Output

Markdown walk containing:

- Joint identity, source, years of record, bias adjustment applied.
- Annual CF, P50 / P75 / P90 (exceedance probabilities), drought-year CF, capacity-coincident CF.
- Monthly CF table (12 rows, with envelope flag).
- Per-month and annual verdicts.
- Top-100 net-load hours coincident-CF — this number flows into `/lead-follow-pairing` as the starting capacity credit.
- Reproducibility footer: source URL or in-house dataset hash, power-curve identifier, git SHA of this workspace.

## Notes

- *Never* compute capacity credit as `annual CF` — that is the joint's *energy* contribution, not its *capacity* contribution. The two are different numbers; ISOs price capacity credit, not energy CF, in their capacity markets.
- A 0.42 wind CF at MERRA-2 cell scale is not the same as 0.42 measured at a met-mast. Reanalysis products smooth orography; complex-terrain sites can swing ±10%.
- Solar PV CF degrades ~0.5%/year for typical c-Si modules; if the project life is 25-35 years, walk the *lifetime average* CF, not the year-1 CF. The walk's annual CF should be the year-15 expected value unless `--year=N` is passed.
- A `REJECT` verdict at C-1 is rare and almost always means the resource timeseries source is wrong (e.g. wind speed at 10 m AGL passed in instead of hub height). Re-check input before sending the joint back to the siting team.
