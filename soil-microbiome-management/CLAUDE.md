# Soil Microbiome Management Workspace

**Template:** `soil-microbiome-management` | **Version:** 1.0

A Claude Code workspace for managing agricultural soil microbiomes through longitudinal monitoring — applying time-series trend analysis to amplicon (16S/ITS), metagenomic, qPCR functional-gene, and soil-health sensor records so growers and agronomists can spot shifts in diversity, functional capacity, and disturbance recovery before they hit yield.

## Layout

- `context/` — domain knowledge the agent should read before acting: microbiome concepts, time-series methods tuned for compositional ecological data, and reference standards / catalogues.
- `prompts/` — reusable prompts for recurring workflows: longitudinal trend assessment, post-disturbance recovery curves, seasonal decomposition of community signals.
- `outputs/` — generated artifacts: trend reports, change-point summaries, decomposition plots, recovery indices, agronomic recommendations.

## Relevant plugin primitives

Provisioned by the `workspace-foundational` plugin model. Useful commands once that plugin is installed:

- `/workspace-foundational:context-sweep` — audit and prune the `context/` directory as new sequencing runs and seasons accumulate.
- `/workspace-foundational:find-template` (skill) — ask if a more specific workspace type now suits an offshoot project (e.g. dedicated nitrogen-cycling or root-microbiome work).

## How to use

1. Drop sample manifests, ASV/OTU tables, qPCR exports, and agronomic covariates into `context/` (or `outputs/raw/` for large derived data).
2. Use prompts in `prompts/` to bootstrap a session — they parameterise inputs, they don't replace judgement.
3. Save trend reports, change-point detections, and recovery summaries to `outputs/` and reference them in the next iteration.

## Operating reminders

- Microbiome counts are compositional — apply CLR/ILR or rarefaction before fitting linear time-series models, or use compositional-aware tools (ALDEx2, ANCOM-BC, MaAsLin2 with appropriate transforms).
- A single time point is a snapshot, not a trend; insist on >=4 time points across a relevant season before declaring a "shift".
- Always log the sequencing run, primer set (e.g. 515F/806R, ITS1F/ITS2), DNA extraction kit, and read-depth threshold alongside the data — batch effects masquerade as biology.
