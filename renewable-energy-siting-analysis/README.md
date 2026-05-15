# Renewable Energy Siting Analysis Workspace

> A siting workspace that reads capacity planning models through a puppetry movement-mechanics lens — every portfolio is an articulated body of joints, linkages, and drives.

## What This Workspace Does

Renewable-energy siting sits at the intersection of geophysical resource (wind, sun, water, geothermal gradient), grid physics (line ratings, interconnection-queue position, contingency analysis), and capacity-market economics (capacity credit, ELCC, resource-adequacy obligation). The usual failure mode is to optimise the resource alone — a 0.48 wind capacity factor in Sweetwater County looks like the obvious site — and then discover too late that the cluster study penalises it 18 months of queue time, that the closest 230 kV link is already curtailed 9% of hours, and that three other developers are siting in the same MERRA-2 grid cell so the marginal ELCC is collapsing toward zero.

This workspace gives a siting analyst a deterministic, **choreography-driven** way to walk a candidate portfolio from raw resource through to a buildable, deliverable, dispatchable asset. The methodology borrows from **puppetry movement mechanics**: every portfolio is treated as an articulated body — joints are the assets, linkages are the transmission segments, drives are the control levers (curtailment, storage dispatch, demand response). The technique field is *with capacity planning models* — every commanded walk produces a real capacity-planning number (capacity factor, ELCC, LOLE, EUE, ramp budget), but the *walk itself* is structured by the puppetry vocabulary so that classes of error become visible. Sympathetic motion (correlated ramping across joints in one resource shed). Slack closure (storage cushion exhausted before the next renewable peak). Heartline-vs-track-frame mismatch (asset-frame capacity factor vs. load-frame capacity credit).

The puppetry frame is the methodology, not the metric. Verdicts are anchored to NERC reliability targets (1-day-in-10-years LOLE = 0.1 day/year), ISO interconnection-queue rules (cluster-study schedules, network upgrade allocation), and the geophysical resource (NSRDB, WIND Toolkit, ERA5, MERRA-2). The choreography just makes the walk legible.

## Why This Workspace Exists

Siting analyses tend to live in spreadsheets, PSS/E case files, and engineering memos. That works until the asset misses its commercial operation date, at which point the IPP wants to know: *which* joint, *which* linkage, *which* drive failed? This workspace formalises the articulation graph so each siting verdict carries provenance — `J-3 wind farm, MERRA-2 cell 47.2N-103.1W, CF=0.31, ELCC=13%, transmission L-5 loading 91% pre-contingency, sympathetic-motion correlation ρ=0.78 with J-7 → REWORK` rather than "looks marginal, would build at the right price." It also fits the entropy of the cognitropy daily-build series: capacity planning vocabulary (ELCC, LOLE, capacity credit) and the puppetry vocabulary (joint, linkage, drive, slack, weight transfer, sympathetic motion) don't carry over to any other workspace, which is exactly the point.

## Getting Started

### Prerequisites

- Geophysical resource timeseries for each candidate site — wind speed at hub height, GHI/DNI, hydro inflow, geothermal gradient — with provenance (NSRDB, WIND Toolkit, ERA5, MERRA-2, in-house met-mast). Minimum 5 years of record; 20+ for serious LOLE work.
- Load timeseries for the relevant Balancing Authority or ISO footprint, hourly (or sub-hourly for high-renewables systems). EIA Form 930 at minimum; ISO-published actual load preferred.
- Transmission topology for the relevant footprint — at least line ratings, contingency list, and current queue position for the candidate POIs. WECC TEPPC, MISO MTEP, PJM RTEP, ERCOT regional planning reports are public starting points.
- Familiarity with the relevant ISO capacity-market rules (PJM RPM, ISO-NE FCM, NYISO ICAP, MISO PRA, CAISO RA, ERCOT-ORDC-instead-of-capacity-market) and NERC reliability standards (TPL-001-5, BAL-001-2, BAL-003-2).
- A reasonable production-cost or capacity-expansion model output (PLEXOS, GridView, ReEDS, Aurora, in-house) for the `/load-following-rehearsal` step. If you don't have one, the rehearsal can be run with simplified hourly dispatch logic but the verdict carries lower weight.

### Quick Start

1. Drop the resource timeseries, load timeseries, and candidate-portfolio definition into `outputs/inbox/<project-id>/`.
2. Run `/articulate-portfolio project=<id>` to build the articulation graph. This is the structural pass — joints, linkages, drives, all named with stable IDs that every downstream walk references.
3. Run `/centerline-resource-walk` over each joint to translate raw resource into a per-month capacity-factor verdict tied to the joint's nameplate and assumed power curve / module derate. Reject sites with `REJECT` verdicts before proceeding.
4. Run `/sympathetic-motion-audit` across the surviving joints to quantify how much correlated ramping is hiding in the portfolio. High inter-joint correlation is the silent ELCC killer.
5. Run `/lead-follow-pairing` to pair each variable joint with a firm or storage follower; this is where storage sizing and / or PPA-firming becomes explicit.
6. Run `/weight-transfer-plan` to write the diurnal and seasonal choreography of capacity transfer between joints; the output ties back to NERC BAL-001 ACE-budget compliance.
7. Run `/slack-budget-check` to confirm that no joint's motion depends on a linkage or drive at saturation.
8. Finally, run `/load-following-rehearsal` over a representative historical year (or stress year) and bin the cues where the portfolio loses motion. Cues binned `hold` or `pull-from-service` send the analyst back to step 5 or step 2.

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/articulate-portfolio` | Decomposes a candidate portfolio into joints, linkages, and drives; produces the articulation graph that downstream walks reference. | Once per candidate portfolio, immediately after intake. Re-run after any asset addition or removal. |
| `/centerline-resource-walk` | Walks the site resource timeseries through a capacity-factor envelope decision tree; per-month PASS / REWORK / REJECT. | First analytical pass on each joint, before any portfolio-level work. |
| `/sympathetic-motion-audit` | Quantifies inter-joint ramp correlation and the ELCC penalty it implies. | After centerline walks pass, before paired sizing — sympathetic motion shifts the storage need by 10-40%. |
| `/lead-follow-pairing` | Pairs each variable-renewable joint with a firm or storage follower; emits a pairing table with ELCC contribution per pair. | After sympathetic-motion audit. Required before any RPS / capacity-market bid is finalised. |
| `/weight-transfer-plan` | Plans diurnal and seasonal capacity transfer; ramp schedule with BAL-001 ACE-budget check. | Once pairing is set, to confirm the choreography actually fits the BA's ramp envelope. |
| `/slack-budget-check` | Audits transmission and storage slack across the articulation graph. | Whenever a linkage or storage joint approaches saturation in the rehearsal; rerun after any topology change. |
| `/load-following-rehearsal` | Runs the portfolio against a historical / stress-year load curve; bins cues by severity. | Final integration test before commitment. Stress year (e.g. 2014 polar vortex, 2021 Uri, 2020 heat dome) is non-negotiable. |

## Directory Structure

```
renewable-energy-siting-analysis/
├── CLAUDE.md                 # Agent role, context refs, command list
├── README.md                 # This file
├── .claude/commands/         # Seven bespoke commands for siting walks
├── context/
│   ├── concepts.md           # Capacity factor vs. ELCC, LOLE, articulation vocabulary
│   ├── workflows.md          # The choreography decision trees
│   └── references.md         # Capacity-credit tables, LOLE targets, resource sources
├── prompts/                  # Intake, interconnection positioning, community rehearsal
└── outputs/                  # Articulation graphs, capacity walks, rehearsal binaries
```

## Example Use Cases

### Greenfield wind-plus-storage portfolio in MISO Zone 1
Three candidate wind farms with overlapping resource sheds. `/articulate-portfolio` builds the joints; `/centerline-resource-walk` returns CF=0.41/0.43/0.39 from WIND Toolkit; `/sympathetic-motion-audit` finds ρ=0.81 between the two southern joints, dropping marginal ELCC of the third farm from 18% nameplate to 6%. The pairing step right-sizes storage 30% larger than the naïve nameplate-fraction estimate would have suggested.

### Solar-plus-storage repowering in CAISO RA bucket allocation
The existing PV asset is being augmented with a 4-hour battery. `/lead-follow-pairing` derives the storage-follower contribution to RA System and Flexible buckets under CAISO's ELCC schedule. `/weight-transfer-plan` writes the diurnal choreography that aligns the battery discharge with the CAISO 4-9pm net-load peak — verifying the asset earns Flexible RA, not just System.

### Wind-firm interconnection-queue strategy in PJM
Two POI options at different substations. `/slack-budget-check` exposes that POI-A's 138 kV linkage is at 89% pre-contingency, meaning queue clearance will demand network-upgrade allocation and 3+ years; POI-B is at 61% and clears in cluster. The siting decision flips on linkage slack, not on resource.

### Hydroelectric reservoir rehearsal under a drought year
The hydro joint is the firm follower in a wind-hydro portfolio. `/load-following-rehearsal` re-runs the proposed portfolio against the 2002 Colorado River drought-year inflow curve; the rehearsal flags 14 cues binned `monitor` and 2 binned `hold` — driving the analyst to right-size a battery follower for the hydro joint itself.

### Community-acceptance pre-walk for an offshore wind project
Resource and grid are clean; the host fisheries and coastal communities are not. The `community-acceptance-rehearsal` prompt walks the project's stakeholder objections through the choreography lens — naming which joint's articulation each objection threatens — and produces a structured pre-response document for the public comment period.

## Recommended MCP Servers

- **filesystem MCP** — pull resource/load CSVs from `outputs/inbox/`, push articulation graphs and walks back into `outputs/`.
- **python-exec MCP** (or any sandboxed numeric runner) — `/centerline-resource-walk` needs hourly power-curve mapping, `/sympathetic-motion-audit` needs correlation computation, `/load-following-rehearsal` needs a simplified hourly dispatch loop. Pure-LLM math on 8760-hour series is unreliable.
- **postgres / duckdb MCP** — for portfolios with more than a handful of joints, the resource and rehearsal data should land in a queryable store rather than CSVs on disk.

## Legal & Ethical Considerations

- **Advisory, not approval.** Outputs do not replace the IPP's board-level siting decision, the ISO's interconnection cluster study, NERC TPL-mandated planning studies, NEPA / ESA review, or AHJ permitting. Verdicts are a structured first pass.
- **Resource provenance is non-negotiable.** Reanalysis products (MERRA-2, ERA5) carry siting-specific bias; in-house met-mast data is more accurate but shorter; mixing the two without disclosure is a hidden risk to the verdict. Always name the source and years of record on the face of the output.
- **Cumulative effects, not just project effects.** Sympathetic motion exists between *your* project and *every other developer's* project in the same resource shed. Coordinate ELCC analyses across queue-clustered developers when ISO rules allow; never assume your project's nameplate gets the same capacity credit when filed in a thick queue.
- **Host community acceptance is a first-class constraint.** Siting against a hostile local government via state-preemption statutes is sometimes legally available and almost always operationally bad — communities affect the asset's lifetime through nuisance suits, future re-permitting, and adjacent-parcel development. Treat the township vote as a planning constraint, not a permit detail.
- **Avian, marine mammal, and cultural-resource impacts.** USFWS Eagle Take permits, MMPA take authorisations, ESA Section 7 consultations, and Section 106 cultural-resource reviews can each kill an otherwise-buildable site. Engage the relevant agency early.

## Technical References

- [NREL WIND Toolkit](https://www.nrel.gov/grid/wind-toolkit.html) — 7-year, 5-minute, 2 km resolution wind resource dataset for the contiguous US.
- [NREL NSRDB](https://nsrdb.nrel.gov/) — National Solar Radiation Database, GHI/DNI/DHI at 4 km / 30-minute resolution.
- [NASA MERRA-2 reanalysis](https://gmao.gsfc.nasa.gov/reanalysis/MERRA-2/) — global 40+ year reanalysis used for cross-validating site-level wind resource.
- [ECMWF ERA5 reanalysis](https://www.ecmwf.int/en/forecasts/dataset/ecmwf-reanalysis-v5) — global 1940-present hourly reanalysis on ~31 km grid.
- [NERC Reliability Standards](https://www.nerc.com/pa/Stand/Pages/ReliabilityStandardsUnitedStates.aspx) — TPL-001 (planning), BAL-001 (ACE), BAL-003 (frequency response), TOP/IRO standards.
- [IRENA Renewable Capacity Statistics](https://www.irena.org/Publications) — global renewable capacity factors and trends.
- [EIA Form 860 / 923](https://www.eia.gov/electricity/data/eia860/) — US plant-level nameplate (860) and monthly net-generation (923).
- [PJM Effective Load Carrying Capability documentation](https://www.pjm.com/-/media/markets-ops/rpm/rpm-auction-info/2026-2027/2026-2027-bra-elcc-class-ratings.ashx) — published ELCC class ratings by technology; analogous documents exist for NYISO, MISO, ISO-NE, CAISO.

## Optional plugin

If you have the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, additional global commands (`/workspace-foundational:context-sweep`, `/workspace-foundational:find-template`) are available; the workspace works without it.
