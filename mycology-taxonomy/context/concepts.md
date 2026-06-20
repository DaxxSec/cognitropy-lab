# Mycology Taxonomy — Working Concepts

Background the agent should read before any determination or capacity task. Two halves: the taxonomy (how to name a fungus correctly) and the capacity model (how to keep the naming pipeline on schedule). Optimised for fast recall, not exhaustive theory.

## The shape of the fungal kingdom (orientation)

Knowing roughly *where* a specimen sits speeds every later step. Major lineages a curator routes by:

- **Ascomycota** — sac fungi; the largest phylum. Cup fungi, morels, truffles, most lichen fungi, *Aspergillus/Penicillium*, yeasts (Saccharomycotina), and the huge Sordariomycetes/Dothideomycetes. Many pleomorphic (anamorph/teleomorph) — the 1F1N flashpoint.
- **Basidiomycota** — club fungi; mushrooms, boletes, polypores, puffballs, rusts (Pucciniomycotina), smuts (Ustilaginomycotina), jelly fungi.
- **Mucoromycota & Zoopagomycota** — the former "zygomycetes," now split; bread moulds, AMF relatives, insect/animal-associated.
- **Glomeromycota** — arbuscular mycorrhizal fungi; obligate plant symbionts, notoriously hard to culture/barcode.
- **Chytridiomycota & allies** — zoosporic, mostly aquatic; includes the amphibian pathogen *Bd*.

Trophic guild also routes work (saprotroph / mycorrhizal / pathogen / lichenised / endophyte); tools like **FUNGuild** assign guild from taxonomy and sharpen ecological interpretation.

## What "naming a fungus" actually involves

A determination is a *hypothesis* that a specimen belongs to a named taxon, supported by evidence and bounded by a confidence. The chain: **specimen → characters → candidate taxon → valid name**. Each link can fail, and the failure modes are different (a good barcode against a bad reference; a correct phylogeny against an invalid name). Treat the binomial as the *last* step, not the first.

### Species concepts (which "kind" of species are we recognising?)

- **Morphological species recognition (MSR)** — based on observable structure. Cheap, fast, and the historical default; blind to cryptic species and misled by convergence and phenotypic plasticity.
- **Biological species recognition (BSR)** — interfertility / mating compatibility. Rigorous but rarely practical (most fungi won't mate in culture).
- **Phylogenetic species recognition — GCPSR** (Genealogical Concordance Phylogenetic Species Recognition, Taylor et al. 2000): a species boundary is where **multiple independent gene genealogies become concordant**. The modern gold standard; it is what separates true cryptic species from intraspecific variation.
- **Integrative taxonomy** — combine MSR + molecular + ecological + geographic evidence; the practical working standard for a modern fungarium.

### The holomorph and One Fungus = One Name (1F1N)

Many fungi are pleomorphic — they have a sexual stage (**teleomorph**) and one or more asexual stages (**anamorph**), historically named *separately* (e.g. *Aspergillus* anamorph vs *Emericella* teleomorph). The whole organism is the **holomorph**. Since the 2011 Melbourne Code (ICN Art. 59), dual nomenclature is **abolished**: one fungus gets one name, chosen by priority. Do **not** resurrect retired dual names. This is the single most common nomenclatural error in legacy datasets.

## Nomenclature essentials

- **Type specimen** — the physical anchor of a name. **Holotype** (the original), **isotype** (duplicate), **lectotype** (chosen later from original material), **neotype** (new type when original is lost), **epitype** (interpretive supplement, increasingly an *ex-type sequence*).
- **Basionym** — the original name on which a recombination is based; carries the original author. Format: `Genus species (OrigAuthor) NewAuthor`.
- **Priority** — the earliest validly published legitimate name wins (with conservation exceptions). Synonymy resolution is mostly a priority question.
- **Valid vs legitimate vs correct** — *validly published* (meets ICN publication rules) ≠ *legitimate* (not a later homonym / superfluous) ≠ *correct* (the accepted name for a circumscription). Check status, don't assume.
- **Registration** — since 2013, new fungal names require a registration identifier (MycoBank or Index Fungorum) to be validly published.

## Molecular markers and barcode thresholds

| Marker | What it is | Use |
|---|---|---|
| **ITS** (ITS1–5.8S–ITS2) | nuclear ribosomal internal transcribed spacer | **Primary fungal barcode** (Schoch et al. 2012). First marker, broadest reference coverage |
| **LSU** (28S, D1/D2) | large ribosomal subunit | Genus/family-level placement; complements ITS |
| **SSU** (18S) | small ribosomal subunit | Deep phylogeny; poor at species |
| **TEF1-α** | translation elongation factor 1-α | Secondary barcode; resolves many cryptic complexes |
| **RPB1 / RPB2** | RNA polymerase II subunits | Single-copy; strong for species/genus phylogeny |
| **BenA / β-tubulin** | beta-tubulin | Standard secondary marker in *Aspergillus*, *Penicillium* |

**Threshold intuition (ITS, not a hard rule):** ≥99% identity → likely same species; 97–99% → genus confident, species uncertain (check secondary marker); <97% → genus only, possibly novel. UNITE's **Species Hypotheses (SH)** replace fixed thresholds with dynamically clustered, DOI-citable units at multiple distance levels — prefer SH assignment over a raw % identity. ITS barcoding fails in groups with low ITS variation (*Fusarium*, *Cladosporium*, *Trichoderma*) — those **require** a secondary marker.

### Barcode pitfalls the agent must guard against

- **Reference-database error** — GenBank is full of misidentified sequences. A 100% match to a wrong name is still wrong. Prefer curated references (UNITE SH, ex-type sequences) and treat unverified GenBank hits skeptically.
- **Chimeras & contamination** — PCR chimeras and co-amplified contaminants masquerade as taxa; check read quality and run chimera detection on amplicon data.
- **Paralogy / intragenomic ITS variation** — multiple divergent ITS copies in one genome can split a single species.
- **Numt/pseudogene artifacts** — for protein-coding markers, watch for stop codons / frameshifts indicating non-functional copies.

## Phylogenetic placement basics

1. **Alignment** — MAFFT (L-INS-i for small accurate sets); trim ambiguous regions (trimAl/Gblocks) for protein-coding markers; ITS alignment across distant taxa is unreliable — align within a genus.
2. **Model selection** — ModelFinder (in IQ-TREE) picks the substitution model.
3. **Inference** — Maximum likelihood (IQ-TREE, RAxML) with ≥1000 ultrafast bootstraps, or Bayesian (MrBayes, BEAST) with posterior probabilities. Support guideline: ML bootstrap ≥70 / ≥95 ultrafast, BI posterior ≥0.95 = supported.
4. **Concordance (GCPSR)** — build single-locus trees; a clade that is **monophyletic and supported across independent loci** is a species. Conflict between well-supported loci signals reticulation/hybridization, not a species.
5. **Placement tools** — EPA-ng / pplacer place a query onto a fixed reference tree without re-inferring it (fast, ideal for routine ID against a curated backbone).

## Capacity-planning vocabulary (the technique)

The fungarium is a queueing system: specimens **arrive**, wait in a **backlog**, get **served** (determined), and **depart** with a name. The math that governs it:

- **Little's Law:** `L = λ · W`. Work-in-progress `L` = arrival rate `λ` × average time-in-system `W`. The single most useful identity — given any two, you get the third. To cut turnaround `W`, cut WIP `L` or raise throughput.
- **Utilization:** `ρ = λ / (c · μ)`, where `μ` = per-server service rate and `c` = number of servers (curators / sequencer slots). **Stability requires ρ < 1.** As ρ → 1, queue length and wait time blow up nonlinearly — a stage run steadily above ~0.85 will accumulate an unbounded backlog.
- **M/M/c queue** — Poisson arrivals, exponential service, `c` parallel servers. Erlang-C gives the probability an arrival waits and the mean wait `Wq`. Use it to size curator pools and predict turnaround.
- **Variability matters (Kingman's formula):** mean wait ≈ `(ρ/(1−ρ)) · ((C_a² + C_s²)/2) · (1/μ)`. High variability in arrivals (`C_a`) or service times (`C_s`) — and taxonomic difficulty is *extremely* variable — inflates waiting even below full utilization. Buffer with safety capacity, not just average capacity.
- **Throughput, WIP, lead time, takt** — throughput = departures/time; takt = available time ÷ demand (the pace you must hit). Theory of Constraints: total throughput is set by the **bottleneck**; optimise the bottleneck, subordinate everything else.
- **Batching** — sequencing has setup cost per run, so it batches (a 96- or 384-well plate). Larger batches raise utilization/lower per-unit cost but *increase* waiting (a specimen waits for the plate to fill). The batch-size sweet spot trades cost against turnaround.

## Common failure modes

- **Naming before checking** — publishing a binomial without a MycoBank/Index Fungorum status check; resurrecting synonyms or dual names.
- **Over-trusting a single barcode** — calling a species off one ITS hit in a group known for cryptic species or low ITS resolution.
- **Ignoring the reference-database error rate** — a confident match to a mislabelled reference.
- **Eyeballing capacity** — "we'll catch up" with no arrival/service-rate model; running a stage at ρ ≈ 0.95 and being surprised the backlog grows.
- **Batching blind** — sizing sequencing plates for cost alone and blowing the turnaround SLA, or running half-empty plates and wasting reagent budget.
- **Treating difficulty as uniform** — allocating curator hours by specimen *count* rather than by difficulty-weighted *service time* (a *Cortinarius* is not an *Agaricus*).
