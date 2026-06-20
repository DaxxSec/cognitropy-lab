# Mycology Taxonomy Workspace

> Determine fungal specimens correctly — morphology, DNA barcode, and phylogeny — and run the determination pipeline like a capacity-planned production line.

## What This Workspace Does

This workspace equips a Claude Code agent to act as the working core of a small mycology lab or fungarium. On the **science** side it carries the full determination chain: accessioning a specimen, working it through morphological keys, identifying it by ITS/LSU DNA barcode against UNITE and GenBank, placing it in a reference phylogeny when the barcode is ambiguous, and validating the resulting name against the nomenclatural registries (MycoBank, Index Fungorum) before it is published.

On the **operations** side it treats that chain as a queueing system. Specimens arrive faster than experts can name them — every herbarium on earth has a determination backlog measured in years. So this workspace folds **capacity-planning models** into the work: Little's Law and M/M/c queues for turnaround, batch-sizing and plate-utilization math for sequencing runs, demand forecasting for arrival rates, and curator-hour allocation across taxonomic groups. The point is to deliver correct names on a *predictable* schedule instead of an open-ended one.

The combination is the whole idea: a determination is only useful if it arrives before the grant report, the regulatory deadline, or the field season closes. Naming fungi and planning the throughput of naming fungi are the same job here.

## Why This Workspace Exists

Fungal taxonomy has a structural bottleneck. There are an estimated 2.2–3.8 million fungal species and only ~155,000 formally described; meanwhile expert mycologists — the people who can actually key a *Cortinarius* or untangle an *Aspergillus* section — are scarce and retiring faster than they are replaced. Specimens pile up in fungaria; sequencing capacity is lumpy (you run a plate or you don't); and "we'll get to it" is not a turnaround anyone can plan around.

This workspace codifies both halves of the solution: rigorous, reproducible determination practice **and** the queueing/capacity discipline to keep the pipeline from silently diverging. It encodes the species concepts, marker thresholds, and nomenclatural rules an expert relies on, alongside the throughput math a lab manager needs, so the agent can move a specimen from box to name to MycoBank-checked binomial — and tell you when the backlog is going to win.

## Getting Started

### Prerequisites

- Sanger or amplicon sequencing access (in-house or a service) for ITS/LSU markers, or existing sequence files (`.ab1`, `.fasta`).
- Python 3 with Biopython, plus an aligner (MAFFT) and a tree builder (IQ-TREE or RAxML) if you intend to run `/phylogenetic-placement` locally.
- Internet access to UNITE, GenBank/BLAST, MycoBank, Index Fungorum, and GBIF (or local mirrors / cached datasets).
- A specimen intake spreadsheet or accessions log (CSV) and, for the capacity commands, a record of arrivals and processing times.

### Quick Start

1. Clone this workspace and skim `context/concepts.md` (species concepts, markers, queueing vocabulary) and `context/workflows.md` (the determination and capacity loops).
2. Run `/accession-specimen` to log an incoming collection — metadata, accession number, and queue placement land in `outputs/accessions/`.
3. Run `/morphology-key` and `/barcode-id` to produce a candidate determination with evidence and confidence.
4. If markers disagree or a cryptic complex is suspected, run `/phylogenetic-placement`, then `/nomenclature-check` to settle the valid name.
5. Run `/backlog-forecast` and `/turnaround-sla` on your arrivals log to see whether the current pipeline keeps up — and `/sequencing-capacity-plan` + `/curator-allocation` to fix it if it doesn't.

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/accession-specimen` | Register a specimen, capture collection metadata, assign accession, queue it | At intake, before any analysis |
| `/morphology-key` | Work macro/micro characters through dichotomous keys to a candidate taxon | First-pass determination from the physical specimen |
| `/barcode-id` | ITS/LSU identification vs UNITE/GenBank with threshold-aware confidence | Once a marker is sequenced |
| `/phylogenetic-placement` | Place the query in a reference tree; surface cryptic-species signal | When the barcode is ambiguous or a complex is suspected |
| `/nomenclature-check` | Validate the name against MycoBank / Index Fungorum (synonymy, priority, 1F1N) | Before any determination is published or labelled |
| `/backlog-forecast` | Queueing model of the backlog; project clearance time | When the unprocessed pile is growing or a deadline looms |
| `/sequencing-capacity-plan` | Plan plate/batch sizing and multiplexing; trade utilization vs turnaround | Before committing a sequencing run |
| `/curator-allocation` | Allocate expert-curator hours across taxonomic groups | Weekly/monthly planning, or when a group's backlog spikes |
| `/turnaround-sla` | Model ID-request turnaround (Little's Law / M/M/c); set SLAs, find bottlenecks | When promising or auditing a turnaround commitment |

## Directory Structure

```
mycology-taxonomy/
├── CLAUDE.md                 # Agent role, context refs, command list
├── README.md                 # This file
├── .claude/commands/         # Bespoke domain commands
├── context/
│   ├── concepts.md           # Species concepts, markers, nomenclature, queueing theory
│   ├── workflows.md          # Determination chain + capacity-planning loop
│   └── references.md         # Primers, databases, thresholds, registries, formulae
├── prompts/                  # Reusable prompt templates
└── outputs/                  # Determinations, barcode reports, trees, capacity models
```

## Example Use Cases

### Name an unknown agaric from a foray
A box of dried gilled mushrooms arrives from a bioblitz. Accession them, key the macro/micro characters, sequence ITS, run `/barcode-id`, and where the genus is notorious for cryptic species (e.g. *Cortinarius*, *Russula*) escalate to `/phylogenetic-placement` before settling a name with `/nomenclature-check`.

### Clear a digitization backlog before a grant deadline
A digitization grant requires 1,200 specimens determined in 9 months. `/backlog-forecast` shows the current arrival vs service rates miss the deadline by 4 months; `/sequencing-capacity-plan` and `/curator-allocation` redesign batch sizes and reviewer assignments to close the gap, and `/turnaround-sla` sets a defensible per-specimen SLA.

### Resolve a suspected cryptic complex
A morphospecies keeps coming back with 99% ITS matches to *two* named species. `/phylogenetic-placement` plus a multi-locus tree (ITS + TEF1 + RPB2) under GCPSR tests whether you are looking at one variable species or two cryptic ones — and the dossier prompt writes it up.

### Audit a name before publication
A draft species list is going into a regulatory report. `/nomenclature-check` flags three names that are now synonyms, one with a basionym authorship error, and one anamorph name that must be replaced under One Fungus = One Name.

## Recommended MCP Servers

- **Filesystem** — read/write accession logs, sequence files, trees, and capacity models in `outputs/`.
- **Fetch / HTTP** — query UNITE, GBIF, MycoBank, Index Fungorum, and NCBI E-utilities for reference data and nomenclatural status.
- **SQLite / database** — back the accessions register and pipeline-metrics tables for the capacity commands.

## Legal & Ethical Considerations

- **Collection permits & access.** Many fungi are collected under permits (national parks, protected areas, foreign jurisdictions); the Nagoya Protocol governs access to genetic resources and benefit-sharing. Record permit and provenance metadata at accessioning.
- **Toxic and regulated taxa.** Determinations are not eating advice. Never present a name as edibility guidance; lethal lookalikes (e.g. *Amanita phalloides* vs edible *Volvariella*/*Agaricus*) make this a safety issue. Flag any determination touching toxic, hallucinogenic, or quarantine-regulated taxa.
- **Data deposition.** Sequences underpinning a name should be deposited (GenBank/ENA) and the voucher cited; UNITE Species Hypotheses are DOI-citable. Don't publish a determination on data you won't share.

## Technical References

- [Schoch et al. 2012, *Nuclear ribosomal ITS as a universal DNA barcode for Fungi* (PNAS)](https://doi.org/10.1073/pnas.1117018109) — establishes ITS as the primary fungal barcode.
- [UNITE database — fungal ITS + Species Hypotheses](https://unite.ut.ee/) — DOI-versioned reference sequences and dynamic clustering thresholds.
- [MycoBank](https://www.mycobank.org/) and [Index Fungorum](https://www.indexfungorum.org/) — registries of fungal names, authorship, and synonymy.
- [International Code of Nomenclature for algae, fungi, and plants (Shenzhen Code, 2018)](https://www.iapt-taxon.org/nomen/main.php) — the governing nomenclatural rules, incl. Art. 59 (1F1N).
- [Taylor et al. 2000, *Phylogenetic species recognition and species concepts in fungi* (Fungal Genet. Biol.)](https://doi.org/10.1006/fgbi.2000.1228) — GCPSR, the basis for `/phylogenetic-placement`.
- [Little's Law and queueing fundamentals (Hopp & Spearman, *Factory Physics*)](https://factoryphysics.com/) — the throughput/WIP/lead-time relationships the capacity commands use.

## Optional plugin

If you have the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, additional global commands (`/workspace-foundational:context-sweep`, `/workspace-foundational:find-template`) are available; the workspace works without it.
