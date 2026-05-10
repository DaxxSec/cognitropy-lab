# Soil Microbiome Management Workspace

**Template:** `soil-microbiome-management` | **Version:** 1.0

## Agent Role

A Claude Code workspace for managing agricultural soil microbiomes through longitudinal monitoring — applying **time-series trend analysis** to amplicon (16S/ITS), metagenomic, qPCR functional-gene, and soil-health sensor records so growers and agronomists can spot shifts in diversity, functional capacity, and disturbance recovery before they hit yield.

## Context References

- **Domain knowledge:** `context/concepts.md` — microbiome composition, diversity metrics, compositionality, functional capacity, time-series methods, disturbance / recovery patterns, sampling design.
- **Methodology and workflows:** `context/workflows.md` — sample-design planning, normalisation, trend testing, decomposition, change-point detection, treatment comparison.
- **Lookup tables and references:** `context/references.md` — primer sets, reference databases, R/Python packages, standards, public catalogues.
- **Reusable prompts:** `prompts/` — longitudinal trend assessment, post-disturbance recovery curves, seasonal decomposition.

## Available Commands

| Command | Description |
|---------|-------------|
| `/sample-design` | Plan replication, cadence, depth, compositing, storage for a study question |
| `/clr-transform` | CLR/ILR-normalise a relative abundance table; flag low-prevalence taxa |
| `/trend-test` | Run Mann-Kendall + Theil-Sen on a series; report monotonic trend with magnitude |
| `/seasonal-decompose` | STL decomposition on a time series to isolate trend from seasonal cycle |
| `/changepoint-detect` | Detect community-level shifts using PELT or Bayesian online change-point detection |
| `/disturbance-recovery` | Quantify recovery trajectory after a disturbance event (tillage, fumigation, drought) |
| `/treatment-compare` | Mixed-effects model with `time × treatment` for replicated plot trials |

## Foundational Instructions

1. **This repository IS your memory.** Save trend reports, change-point detections, recovery summaries, and recommendations to `outputs/`; refresh `context/` as new sequencing runs and seasons accumulate.
2. **Microbiome counts are compositional.** Apply CLR/ILR or use compositional-aware tools (ALDEx2, ANCOM-BC, MaAsLin2 with appropriate transforms) before fitting linear time-series models. Never read relative abundance shifts as absolute biology without an anchor (qPCR total 16S, flow cytometry, or spike-ins).
3. **One time point is a snapshot, not a trend.** Insist on ≥4 time points across a relevant season before declaring a "shift," and prefer ≥6 when the cadence allows.
4. **Always log batch metadata.** Sequencing run, primer set (515F/806R, ITS1F/ITS2), DNA extraction kit, read-depth threshold, and pipeline version travel with every analysis. Batch effects masquerade as biology.
5. **Capture covariates every visit.** Temperature, moisture, pH, EC, total C/N, prior management. Without covariates, time-series trends are uninterpretable.

## Optional plugin primitives

If the user has the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, these globally-installed commands work alongside the workspace's own:

- `/workspace-foundational:context-sweep` — audit and prune the `context/` directory as new runs accumulate.
- `/workspace-foundational:find-template` (skill) — recommend a different workspace shape if the project narrows (e.g. dedicated nitrogen-cycling or root-microbiome work).

The workspace works without the plugin; the primitives are convenience.
