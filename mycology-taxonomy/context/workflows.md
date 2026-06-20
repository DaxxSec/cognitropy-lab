# Mycology Taxonomy — Workflows and Methodology

Two interlocking loops: the **determination chain** (move one specimen to a valid name) and the **capacity loop** (keep the pipeline that runs the chain on schedule). The technique anchor for this workspace is **capacity-planning models**, so the capacity loop is woven through, not bolted on.

---

## Loop A — The determination chain (per specimen)

```
accession → morphology → marker choice → barcode ID → [phylogeny if ambiguous] → nomenclature check → publish/label
```

### Phase 1 — Accession (`/accession-specimen`)
1. Capture collection metadata: collector, date, locality (lat/long + datum), substrate/host, habitat, permit reference (Nagoya / park permit), field notes, photos.
2. Assign an accession number and a fungarium barcode. Record drying/storage state.
3. Classify the specimen's **expected difficulty tier** (see capacity loop) — this drives queue routing, not just bookkeeping.
4. Enqueue: add to the determination backlog with a timestamp so arrival rate `λ` can be measured.

### Phase 2 — Morphological keying (`/morphology-key`)
1. Macro characters: pileus, lamellae/pores/teeth, stipe, ring/volva, spore print colour, odour, staining/bruising reactions, chemical spot tests (KOH, Melzer's/amyloid reaction).
2. Micro characters: spore size/shape/ornamentation, basidia, cystidia (cheilo-/pleuro-), pileipellis structure, clamp connections, hyphal system.
3. Run the relevant key (regional flora, genus monograph). Record the path taken and where the specimen is ambiguous.
4. Output a **candidate taxon** (genus confident, species provisional) with the characters supporting and contradicting it.

### Phase 3 — Marker selection & barcode ID (`/barcode-id`)
1. Default to **ITS** first. If the candidate genus is in the low-ITS-resolution list (*Fusarium*, *Trichoderma*, *Cladosporium*, *Penicillium*, *Aspergillus*), plan a **secondary marker** (TEF1-α, RPB2, BenA) up front.
2. QC the read: check trace quality / trim primers, confirm length, screen for chimeras and contamination.
3. Query UNITE (Species Hypotheses) **and** GenBank. Prefer SH assignment and ex-type / curated references over raw GenBank hits.
4. Apply threshold intuition (≥99% same species; 97–99% genus; <97% genus/novel) **as a prior, not a verdict** — weight by reference reliability.
5. Emit a provisional determination with explicit confidence and the disagreements between morphology and barcode.

### Phase 4 — Phylogenetic escalation (`/phylogenetic-placement`) — only if needed
Trigger when: barcode is ambiguous (ties between named species), the genus is a known cryptic complex, morphology and barcode conflict, or the specimen may be undescribed.
1. Assemble a reference set (ex-type sequences + close UNITE SHs) for the candidate genus.
2. Align within-genus (MAFFT); trim for protein-coding markers.
3. Infer ML tree (IQ-TREE, ModelFinder, ≥1000 UFBoot) and/or place onto a fixed backbone with EPA-ng.
4. For species-boundary questions, build single-locus trees for ITS + ≥1 secondary marker and apply **GCPSR**: concordant, supported monophyly across loci = a species.
5. Record support values and any locus conflict (possible hybridization).

### Phase 5 — Nomenclature check (`/nomenclature-check`) — mandatory before publishing
1. Look up the proposed binomial in MycoBank and Index Fungorum.
2. Confirm current status: accepted / synonym / illegitimate / invalid; resolve to the **correct** name by priority.
3. Verify authorship and basionym format; flag dual (anamorph/teleomorph) names that violate 1F1N.
4. Confirm registration identifier exists (required for post-2013 names).
5. Output the validated name, authorship, current status, and the synonymy you collapsed.

### Integrative-taxonomy decision tree (when evidence disagrees)
- Morphology ✓ + barcode ✓ concordant → **publish** at species confidence.
- Morphology ✓ + barcode ambiguous → secondary marker; if still ambiguous → phylogeny.
- Morphology ✗ + barcode strong (curated ref) → trust barcode, re-examine morphology for cryptic/plastic characters; report `cf.`
- Both weak / conflicting across supported loci → report at genus (`sp.`) and flag as candidate novel taxon or hybrid. **Do not force a binomial.**

---

## Loop B — The capacity-planning loop (per pipeline, recurring)

Run this weekly/monthly and before any deadline commitment. It treats Loop A's stages (accession, sequencing, curation) as queues.

### Step 1 — Measure (inputs for every model)
- Arrival rate `λ` (specimens/week) and its variability `C_a²`.
- Service rate `μ` and variability `C_s²` **per stage and per difficulty tier** (an *Agaricus* and a *Cortinarius* are different service distributions).
- Current WIP / backlog `L` per stage; current mean turnaround `W`.
- Server counts `c`: curators per group, sequencer slots/plates per cycle.

### Step 2 — Forecast the backlog (`/backlog-forecast`)
1. Compute utilization `ρ = λ / (c·μ)` per stage. Any stage with ρ ≥ ~0.85 is the danger zone; ρ ≥ 1 means the backlog grows without bound.
2. Identify the **bottleneck** stage (highest ρ) — this sets total throughput (Theory of Constraints).
3. Project backlog clearance: with current ρ, when does the pile clear? Use M/M/c (Erlang-C) for expected wait, Kingman's approximation when variability is high.

### Step 3 — Size the sequencing batches (`/sequencing-capacity-plan`)
1. Given plate format (96 / 384 well) and per-run setup cost, find the batch size that meets the turnaround SLA at acceptable per-unit cost.
2. Model the wait-to-fill: small backlog + large plate = specimens wait for the plate to fill (raises `W`); compute the crossover where partial plates are worth running.
3. Plan multiplexing/indexing capacity if amplicon (Illumina) rather than Sanger.

### Step 4 — Allocate curator capacity (`/curator-allocation`)
1. Weight demand by **difficulty-adjusted service time**, not raw specimen count.
2. Assign expert hours to taxonomic groups to balance utilization (avoid one group at ρ=0.98 while another idles).
3. Hold a **safety-capacity buffer** sized to arrival/service variability (Kingman) — never plan a key reviewer to 100%.

### Step 5 — Set and audit the SLA (`/turnaround-sla`)
1. Use Little's Law (`W = L/λ`) and Erlang-C to derive a defensible per-tier turnaround promise.
2. Set SLA targets per difficulty tier (fast for routine, longer for cryptic complexes).
3. Audit actuals vs SLA; when a tier breaches, trace it to the bottleneck stage and loop back to Step 2.

### Capacity decision heuristics
- Backlog growing? → the bottleneck stage has ρ ≥ 1. Add capacity *there* (more curator hours / an extra plate cycle), not elsewhere.
- Turnaround too long but ρ < 0.85? → variability is the culprit; reduce batch-induced waiting or smooth arrivals.
- Cost over budget but SLA met? → batches too small / plates underfilled; raise batch size toward the SLA-binding limit.
- Deadline-driven project? → compute takt (available time ÷ specimens due) and staff the bottleneck to beat it, with a buffer.
