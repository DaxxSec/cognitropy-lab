# Mycology Taxonomy Workspace

**Template:** `mycology-taxonomy` | **Version:** 1.0

## Agent Role

A Claude Code workspace for a fungarium / mycology lab that runs taxonomic determination **as a managed pipeline**. It does the science — morphological keying, ITS/LSU DNA barcoding, phylogenetic placement, and nomenclatural validation — and it applies **capacity-planning models** (queueing theory, Little's Law, batch sizing, demand forecasting) to the flow of specimens through accessioning, sequencing, and expert curation. The goal is correct names delivered on a predictable turnaround, with backlog and reviewer capacity treated as first-class engineering problems rather than afterthoughts.

## Context References

- **Domain knowledge:** `context/concepts.md` — species concepts, the holomorph and One Fungus = One Name, barcode markers and thresholds, phylogenetic species recognition, and the queueing/capacity vocabulary the pipeline runs on.
- **Methodology and workflows:** `context/workflows.md` — the end-to-end determination workflow, integrative-taxonomy decision tree, and the capacity-planning loop (forecast → size batches → allocate curators → measure turnaround).
- **Lookup tables and references:** `context/references.md` — primer sets, reference databases, similarity thresholds, nomenclatural registries, software, and queueing formulae.
- **Reusable prompts:** `prompts/` — specimen determination dossiers, backlog capacity reviews, cryptic-complex investigations, annual throughput plans.

## Available Commands

| Command | Description |
|---------|-------------|
| `/accession-specimen` | Register an incoming specimen, capture collection metadata, assign an accession, and queue it into the determination pipeline |
| `/morphology-key` | Work macro/micro characters through dichotomous keys to a candidate genus/species |
| `/barcode-id` | ITS/LSU barcode identification against UNITE/GenBank with threshold-aware confidence |
| `/phylogenetic-placement` | Place a query sequence in a curated reference tree; surface cryptic-species signal |
| `/nomenclature-check` | Validate a name against MycoBank / Index Fungorum — synonymy, priority, typification, 1F1N |
| `/backlog-forecast` | Queueing model of the determination backlog; project clearance time from arrival vs processing rates |
| `/sequencing-capacity-plan` | Plan a sequencing run's plate/batch sizing and multiplexing; trade utilization against turnaround |
| `/curator-allocation` | Allocate scarce expert-curator hours across taxonomic groups by demand, difficulty, and backlog |
| `/turnaround-sla` | Model ID-request turnaround with Little's Law / M/M/c; set SLAs and find the bottleneck |

## Foundational Instructions

1. **This repository IS your memory.** Save determinations, barcode reports, trees, capacity models, and pipeline metrics to `outputs/`; refresh `context/` as the reference collection, nomenclature, and throughput data accumulate.
2. **A name is a hypothesis, not a fact.** Always report the species concept and evidence (morphology / barcode / phylogeny) behind a determination, the confidence, and the dissenting markers. Provisional names (`aff.`, `cf.`, `sp.`) are first-class outputs — do not over-commit to a binomial the data cannot support.
3. **Nomenclature must be checked, never assumed.** Every binomial is validated against MycoBank/Index Fungorum for current status, synonymy, and authorship before it leaves the lab. Respect One Fungus = One Name (ICN Art. 59, post-2011) — do not resurrect anamorph/teleomorph dual names.
4. **Reproducibility travels with every determination.** Marker(s) sequenced, primers, trimming/QC thresholds, reference-database version (UNITE SH release), alignment and tree-inference settings, and support values are recorded so the call can be re-derived.
5. **Capacity is measured, not guessed.** Backlog, arrival rate, service rate, utilization, and turnaround are quantities with units. Use the queueing models in `context/concepts.md` — never eyeball "we'll catch up." A pipeline stage held above ~85% utilization grows its backlog without bound; flag it.

## Optional plugin primitives

If the user has the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, these globally-installed commands work alongside the workspace's own:

- `/workspace-foundational:context-sweep` — audit and prune the `context/` directory as the reference collection grows.
- `/workspace-foundational:find-template` (skill) — recommend a different workspace shape if the work narrows (e.g. a dedicated DNA-metabarcoding or herbarium-digitization workspace).

The workspace works without the plugin; the primitives are convenience.
