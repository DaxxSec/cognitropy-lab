# Ornithology Song Spectrogram Analysis — Workflows and Methodology

Procedures and decision trees, framed by today's technique: **taxonomy and classification systems**. Where `concepts.md` says what the characters *are*, this file says what the agent *does* with them. The spine is the systematist's loop: ingest → decompose → measure → key → voucher.

## Workflow 1: Specimen-to-classification pipeline

**Goal:** Turn one unidentified recording into a vouchered, character-backed determination.

### Steps

1. **Ingest** (`/ingest-recording`): render a spectrogram at *both* a wideband (short window) and narrowband (long window) setting; capture provenance (locality, date, recordist, equipment, sample rate, any playback).
2. **Decompose** (`/segment-syllables`): mark element boundaries; group elements into syllables and phrases; assign provisional element-type labels (a, b, c…). Build the element inventory — the acoustic taxonomy's lower ranks.
3. **Measure** (`/measure-acoustic-features`): for each element type, record the standardized character set (peak frequency, bandwidth, duration, FM slope, inter-onset interval, repetition rule).
4. **Key** (`/key-out-species`): descend the dichotomous key, naming the diagnostic character at each branch. Stop at the lowest rank the characters confidently support.
5. **Voucher** (`/voucher-specimen`): commit the determination with spectrogram, measurements, the key path taken, a confidence statement, and the nearest confusable ruled out.

### Decision Points

- If SNR is low or high frequencies are attenuated: down-rank confidence and prefer temporal/structural characters (robust to distance) over absolute frequency bounds (not).
- If the key reaches a cryptic pair the voice can't split: stop at the species-pair / superspecies rank and run `/confusion-audit`; do not force a species.
- If the singer is a known mimic: branch to `/mimicry-trace` before attributing any borrowed phrase to a present species.

## Workflow 2: Building a diagnostic acoustic key

**Goal:** Produce a reusable dichotomous (or polythetic) key for a set of confusable taxa.

### Steps

1. Assemble a vouchered reference set spanning the taxa and their known within-taxon variation (multiple individuals each).
2. For each taxon, tabulate the character set and compute ranges (not just means) — a key built on means alone fails on the tails.
3. Choose split characters by **separation power**: rank candidate characters by how cleanly their ranges divide the taxa with minimal overlap.
4. Write each branch as "character → value range → next node," always with a stated character. Prefer characters robust to recording quality high in the tree.
5. Validate the key against held-out recordings; record misclassifications and revise. A key that has never been tested against held-out data is a hypothesis, not a tool.

### Decision Points

- If two taxa overlap on every single character: the key is monothetic-impossible — switch to a **polythetic** class (membership = "k of n characters") and document the irreducible confusion.

## Workflow 3: Dialect / population classification

**Goal:** Decide whether recordings represent distinct dialects and where the boundary lies.

### Steps

1. Geotag and measure all recordings of the focal species across the region.
2. Cluster on song-structure characters (hierarchical clustering or spectrographic cross-correlation similarity).
3. Test whether acoustic clusters map to geography — a real dialect shows a spatial boundary, not just acoustic clusters.
4. Distinguish **clinal** (gradual) from **dialectal** (stepped) variation by plotting character against distance.
5. Report clusters as *infraspecific* classes; never promote a dialect to a species without independent (genetic/morphological) corroboration.

## Methodology: the rank-by-rank classification descent

Treat identification as **keying a specimen**, descending the biological hierarchy only as far as the acoustic characters license:

### Phase 1 — Coarse placement
Use robust, recording-quality-insensitive structure (song vs call; trill vs warble vs whistle; number of element types) to place the recording into a broad group (family/genus-level acoustic type).

### Phase 2 — Fine determination
Within the group, apply the discriminating frequency/temporal/modulation characters from the key to reach species — citing each character used.

### Phase 3 — Confusion check
Before vouchering, explicitly name the single most similar non-target taxon and the character that rules it out (`/confusion-audit`). An ID without a ruled-out confusable is incomplete.

### Phase 4 — Provenance & voucher
Bind the determination to its evidence and settings so it is reproducible and falsifiable.
