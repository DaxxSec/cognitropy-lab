# /articulate-portfolio

Decompose a candidate renewable portfolio into joints (assets), linkages (transmission segments), and drives (control levers); emit the articulation graph that every downstream walk references.

## Inputs

- `project_id` — stable identifier for the portfolio (e.g. `miso-zone1-2026-wind-cluster`).
- `assets` — list of asset records: `{asset_id, tech, nameplate_mw, lat, lon, poi, coupling}`. `tech ∈ {wind, solar_pv_fixed, solar_pv_tracker, solar_csp, hydro_runofriver, hydro_reservoir, geothermal_flash, geothermal_binary, battery_lifepo4, battery_flow, demand_response}`. `coupling ∈ {dc, ac, dc_coupled_storage, ac_coupled_storage, standalone}`.
- `transmission` — list of relevant grid segments: `{line_id, from_bus, to_bus, voltage_kv, normal_rating_mva, emergency_rating_mva, current_loading_pct, queue_position}`. Public ISO planning data or in-house PSS/E case.
- `controls` — list of available control levers: curtailment authority (FERC OATT), storage dispatch authority, demand response authority, frequency-response obligation. Annotate each with `binding | non-binding`.
- `frame` — `asset_frame | load_frame`. Defaults to `asset_frame`. The frame determines whether downstream walks report capacity factor (asset frame) or capacity credit (load frame).

## Steps

1. Validate intake. Every asset record must have all six fields; every line record must have rating + loading. Abort with REJECT at `A-0` if any field is missing — articulation cannot proceed on partial data.
2. Assign joint IDs (`J-1`, `J-2`, …) per asset in nameplate order, descending. The joint ID is stable for the project lifetime; downstream walks reference it.
3. Assign linkage IDs (`L-1`, `L-2`, …) per transmission segment, in the order POI-to-load. Tag each linkage with its `slack_pct = 1 - current_loading_pct` and its `queue_class` (cluster / network-upgrade / parallel-flow).
4. Assign drive IDs (`D-1`, `D-2`, …) per control lever. Mark drives `binding` (curtailment under OATT, storage dispatch under a tolling agreement) vs `non-binding` (cooperative DR).
5. Build the adjacency table — joint → linkage → joint / linkage → load — for the articulation graph. Use ISO bus naming where available; fall back to lat/lon where not.
6. Compute resource-shed groupings. Joints whose centerlines (resource timeseries) live within the same MERRA-2 / WIND Toolkit cell, or within a 50 km radius for solar / 30 km for wind, are tagged with a shared `shed_id`. This is the structural setup for `/sympathetic-motion-audit`.
7. Compute initial nameplate-fraction capacity credit for each joint using the regional ISO's default ELCC class rating (`context/references.md` Table R-1). This is the *starting* capacity credit; `/lead-follow-pairing` refines it later.
8. Write the articulation graph to `outputs/<project_id>/articulation-graph.md` as a directed table plus a Mermaid diagram. The Mermaid block lets the analyst eyeball the topology; the table is the machine-readable source.
9. Emit the structural verdict: `A-PASS` (graph closes, every joint reaches load through ≥1 linkage), `A-REWORK` (one or more joints stranded), `A-REJECT` (no path to load — site is not buildable).

## Output

`outputs/<project_id>/articulation-graph.md` containing:

- Header: project_id, build_date, frame, total nameplate MW, total firm MW (joints with capacity credit ≥ 0.95).
- Joint table (`joint_id, asset_id, tech, nameplate, lat, lon, poi, shed_id, default_capacity_credit`).
- Linkage table (`linkage_id, from, to, voltage, normal_rating, slack_pct, queue_class`).
- Drive table (`drive_id, lever, scope, binding`).
- Mermaid diagram of the topology.
- Structural verdict (`A-PASS / A-REWORK / A-REJECT`) with the failing node cited if not PASS.
- Suggested follow-up commands: `/centerline-resource-walk` for each joint, `/sympathetic-motion-audit` if any `shed_id` is shared.

## Notes

- Joints are atoms. Do not silently combine two co-located assets into one joint just because they share a POI — that hides shed-correlation analysis and double-counts diversification.
- Storage joints (`battery_*`) carry capacity credit only as paired followers. The articulation graph assigns them a zero starting credit; `/lead-follow-pairing` is the one place storage earns its credit.
- Demand-response drives are `non-binding` by default. Treat DR-derived capacity credit with suspicion until a binding tolling or aggregator contract is shown.
- Re-running this command after an asset addition / removal regenerates *all* joint and linkage IDs unless `--preserve-ids` is passed. Downstream walks must be re-run on the new IDs.
