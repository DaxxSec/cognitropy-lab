# Mycology Taxonomy — Reference Tables

Compact lookup data for determination and capacity work. Prose lives in `concepts.md`; this is the cheat-sheet.

## Barcode markers & standard primers

| Marker | Primers (common) | Resolves to | Notes |
|---|---|---|---|
| ITS (full) | ITS1F / ITS4 | species (most groups) | Primary barcode; ITS1F is fungal-biased |
| ITS2 | fITS7 / ITS4 | species | Common in metabarcoding |
| ITS1 | ITS1F / ITS2 | species | Shorter amplicon |
| LSU (D1/D2) | LROR / LR5 (LR0R/LR3) | genus–family | Backbone placement |
| SSU (18S) | NS1 / NS4 | order–class | Deep phylogeny only |
| TEF1-α | EF1-983F / EF1-2218R | cryptic species | Secondary barcode |
| RPB2 | fRPB2-5F / fRPB2-7cR | species–genus | Single-copy, strong signal |
| BenA (β-tub) | Bt2a / Bt2b | species | *Aspergillus*, *Penicillium* |

## ITS identity → confidence (prior, not verdict)

| % identity to a *reliable* reference | Read as |
|---|---|
| ≥ 99% | Likely same species |
| 97–99% | Genus confident; species uncertain → secondary marker |
| 94–97% | Genus likely; possibly novel |
| < 94% | Family/order only; novel candidate |

Prefer **UNITE Species Hypothesis (SH)** assignment over a fixed %. Groups where ITS under-resolves and a secondary marker is **required**: *Fusarium*, *Trichoderma*, *Cladosporium*, *Penicillium*, *Aspergillus*, *Colletotrichum*.

## Reference databases & registries

| Resource | URL | Use |
|---|---|---|
| UNITE | https://unite.ut.ee/ | Fungal ITS + DOI-cited Species Hypotheses |
| NCBI GenBank / BLAST | https://www.ncbi.nlm.nih.gov/ | Broad reference (uncurated — verify hits) |
| MycoBank | https://www.mycobank.org/ | Name registration, status, synonymy |
| Index Fungorum | https://www.indexfungorum.org/ | Names, authorship, basionyms |
| GBIF | https://www.gbif.org/ | Occurrence/distribution data |
| MycoPortal | https://mycoportal.org/ | North American fungarium specimen records |
| Catalogue of Life | https://www.catalogueoflife.org/ | Accepted-name backbone |
| RefSeq Targeted Loci (ITS) | NCBI BioProject PRJNA177353 | Curated type-derived ITS |

## Nomenclatural quick-reference

- **ICN** = International Code of Nomenclature for algae, fungi, and plants (Shenzhen Code 2018; Madrid Code in progress).
- **Art. 59** — One Fungus = One Name (since 2011): no separate anamorph/teleomorph names.
- **Post-2013** — new names need a MycoBank/Index Fungorum registration ID to be valid.
- Type ranks: holotype > isotype/syntype > lectotype > neotype > epitype (incl. ex-type **sequence**).
- Name format: `Genus species Author` or recombination `Genus species (BasionymAuthor) CombiningAuthor`.
- Status terms: *validly published* / *legitimate* / *correct* are independent checks.

## Software

| Tool | Role |
|---|---|
| MAFFT | Multiple sequence alignment |
| trimAl / Gblocks | Alignment trimming |
| IQ-TREE (+ModelFinder, UFBoot) | ML phylogeny + model selection |
| RAxML / RAxML-NG | ML phylogeny |
| MrBayes / BEAST | Bayesian phylogeny |
| EPA-ng / pplacer | Phylogenetic placement on a fixed tree |
| Biopython / scikit-bio | Sequence handling, QC |
| DADA2 / VSEARCH | Amplicon denoise / chimera detection |
| Geneious / SeqTrace | Sanger trace editing |

## Capacity-planning formulae (cheat-sheet)

| Quantity | Formula | Meaning |
|---|---|---|
| Little's Law | `L = λ · W` | WIP = arrival rate × time-in-system |
| Utilization | `ρ = λ / (c · μ)` | Stable only if ρ < 1; danger at ρ ≳ 0.85 |
| Takt time | `available time / demand` | Pace you must hit to meet demand |
| Throughput | departures / time | Capped by the bottleneck stage |
| Kingman (mean wait) | `Wq ≈ (ρ/(1−ρ)) · ((C_a²+C_s²)/2) · (1/μ)` | Variability inflates waiting below ρ=1 |
| Erlang-C | `P(wait)` for M/M/c | Probability an arrival queues; sizes server pools |
| Batch wait-to-fill | `≈ (batch−1)/(2λ)` | Mean wait for a plate to fill at rate λ |

Symbols: `λ` arrivals/time · `μ` per-server service rate · `c` servers (curators / plate slots) · `C_a²,C_s²` squared coefficients of variation of inter-arrival / service times.

## Difficulty tiers (example routing weights)

| Tier | Example genera | Rel. service time | Default marker plan |
|---|---|---|---|
| Routine | *Agaricus*, *Pleurotus*, common polypores | 1× | ITS only |
| Moderate | *Russula*, *Lactarius*, *Amanita* | 2–3× | ITS + morphology emphasis |
| Hard / cryptic | *Cortinarius*, *Inocybe*, *Fusarium*, *Trichoderma* | 4–8× | ITS + secondary marker + phylogeny |
