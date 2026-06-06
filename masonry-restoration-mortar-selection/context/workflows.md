# Masonry Restoration Mortar Selection — Workflows and Methodology

Step-by-step procedures, all framed through the engine's technique — **predictive maintenance scheduling** — and the borrowed mycology-taxonomy methodology. Identification feeds selection; selection plus monitoring feeds the forecast.

## Workflow 1: Keying out an unknown mortar (provisional ID)

**Goal:** Place an unknown original mortar in a binder class quickly, from cheap field + simple-lab characters, before committing to lab work.

### Steps
1. Sample correctly: take loose fragments from a *raked joint*, not the units; multiple locations; record provenance (elevation, height, drawing reference) for every fragment.
2. Field characters: colour, hardness (scratch with a brass pick / fingernail / steel), friability, lime lumps visible, aggregate visible to a hand lens, set behaviour, presence of grey cement haze.
3. Simple-lab characters: acid (dilute HCl) reaction vigour (fizz = carbonate binder; sluggish + grey residue suggests cement/hydraulic), approximate binder:aggregate after digestion, aggregate grading by sieve.
4. Run the dichotomous key (`/mortar-key`) couplet by couplet to a binder class (air lime / pozzolan-gauged / moderately hydraulic / eminently hydraulic / natural cement / Portland).
5. Record the *determination confidence* and the characters that drove each couplet — like annotating a key, so a second analyst can audit it.

### Decision points
- Calcareous aggregate suspected (limestone sand) → flag that acid digestion will overstate binder; require petrography to confirm.
- Key terminates ambiguously between two clades → escalate to the two-track identification (Workflow 2); do not force a determination.
- Cement haze present on a "lime" building → likely a later repointing campaign; trigger `/delimit-mix`.

## Workflow 2: Two-track identification (morphology + chemical barcode)

**Goal:** Confirm the binder class and assign a binomial name, using the mycology two-track model — petrographic "morphology" plus chemical "barcode."

### Steps
1. **Morphology track — petrography.** Prepare a thin-section; under PLM record binder character, hydraulic phases, lime lumps, aggregate mineralogy/provenance/roundness, grading, voids and shrinkage cracks. Point-count for binder:aggregate by volume.
2. **Barcode track — chemistry.** Acid digestion → binder:aggregate by mass + insoluble-residue grading (cross-check petrography to catch carbonate aggregate). Oxide analysis (SEM-EDS / XRF) → **Hydraulic Index**. XRD → mineral phases. TGA → bound water / portlandite / CaCO₃ steps.
3. **Reconcile the two tracks.** Concordance raises confidence (mirrors morphology-vs-ITS concordance in GCPSR species recognition). Disagreement (e.g. petrography says air lime, chemistry says HI 0.25) → re-examine; one track is mis-sampled or contaminated.
4. **Assign the binomial name** (Workflow 3 naming convention) and a determination confidence.
5. Write the identification report (`prompts/mortar-identification-report.md`) to `outputs/`.

### Decision points
- Only one track available → state the name as *provisional* and list the missing confirmatory character.
- Contamination (gypsum from later plaster, soluble salts) detected in XRD/TGA → separate "decay products" from "original binder" before naming.

## Workflow 3: Naming and accessioning a type specimen

**Goal:** Give the mortar a stable binomial name and deposit it as a type specimen so future buildings match against the collection (the "fungarium" model).

### Naming convention (binomial + qualifier)
`<Genus = binder class> <species = binder:aggregate ratio> (<aggregate descriptor>)`
e.g. `Calx aerius 1:3 (fine siliceous)`, `Calx hydraulica-moderata 1:2.5 (coarse calcareous)`, `Calx pozzolanica 1:1:6 (cocciopesto)`. Append the determination author and date, like an authority citation.

### Steps
1. Assign an **accession number** (e.g. `MRT-2026-073-01`) — one number = one holotype = one name.
2. Record holotype data: provenance (building, elevation, height, date sampled), photographs with scale, thin-section image, the two-track character set, HI, binder:aggregate, aggregate grading curve, determination confidence, author.
3. Store the physical fragment reference (box/location) and digital record (`/specimen-accession` writes the JSON/markdown record).
4. Register in the collection index so `/mortar-key` and `/match-compatible-mortar` can retrieve known regional "species."

### Decision points
- A new sample matches an existing accession within tolerance → record as *additional material* of that taxon, not a new holotype.
- A sample differs beyond tolerance → new accession; consider whether it is a genuinely new taxon or a delimitation question (Workflow 5).

## Workflow 4: Designing the compatible repair mortar (the deliverable)

**Goal:** Specify a repair mix that is softer, more porous and more vapour-open than the substrate and the original, and durable for the exposure.

### Steps
1. Retrieve the characterised original (name, HI, binder:aggregate, aggregate grading).
2. **Match aggregate first** — replicate the original grading and mineralogy/colour; aggregate controls porosity, shrinkage and appearance more than the binder.
3. **Choose the binder one notch *no harder* than the original**, never harder. Air-lime original → air lime (putty or hot-mixed) or, only if exposure demands, a feebly hydraulic/pozzolan gauge. NHL original → match or undershoot the NHL class.
4. Check the proposed mix on `/binder-phylogeny`: it must sit in or below the original's clade. Reject if it lands in the cement clade.
5. Set proportions (by volume), water demand, and any pozzolan/gauge; specify batching, mixing (knock-up), and application.
6. Specify performance acceptance: 28/90-day compressive & flexural strength (EN 1015-11) **below** the unit, capillary absorption (EN 1015-18) **above** a dense substrate, vapour resistance μ (EN 1015-19) **at or below** the unit, frost/salt resistance for the exposure.
7. Specify **curing**: protect from frost, rapid drying and rain; keep damp; respect lime carbonation time. This constraint feeds the maintenance calendar.
8. Output the specification (`prompts/repair-mortar-specification.md`) to `outputs/`.

### Decision points
- Severe exposure (parapet, chimney, sea front) tempts a harder mix → prefer better detailing/sheltering and a sacrificial render over a harder, incompatible mortar.
- Original is itself a damaging later cement repair → the "compatible" target is the *units and any surviving original*, not the cement.

## Workflow 5: Delimiting mixes (one taxon or several?)

**Goal:** Decide whether sampled variation across a building is intraspecific variation of one mortar or several distinct mixes/phases — the species-delimitation analog.

### Steps
1. Plot every sample's characters (HI, binder:aggregate, aggregate grading, colour) on the elevation map.
2. Look for *discontinuities*, not gradients: clustered character sets separated by gaps suggest distinct taxa (campaigns), while a continuum suggests one mortar with natural variation.
3. Cross-check with documentary/archaeological phasing (build campaigns, known repairs).
4. Apply a tolerance rule (see references) for "same mix": within tolerance → one taxon; beyond → delimit a new mix and accession it.
5. Map each delimited mix to its own repair recipe and its own conservation decision (retain / repair / carefully remove later cement).

### Decision points
- Cryptic case: two mixes look identical by eye but differ in HI → trust the chemical barcode (cryptic "species").
- Gradient with no clear gap → resist over-splitting; one recipe with tolerances is more conservable than many bespoke patches.

## Workflow 6: Biodeteriogen survey (literal mycology as bioindication)

**Goal:** Identify the colonising organisms and read them as indicators of the moisture/exposure regime.

### Steps
1. Map colonisation by elevation/height: photograph, estimate coverage %, note growth form (filamentous alga, crustose lichen, black MCF crust, moss).
2. Identify to genus where possible using morphology + a field key; sample for lab/ITS confirmation where it changes the diagnosis.
3. Interpret as bioindicators: *Trentepohlia* / persistent algal greening → chronic wetting (failed detail, splash, run-off); endolithic lichens on calcareous stone → long undisturbed wet exposure; black MCF → repeated wet-dry stress.
4. Relate distribution to the decay map and the suspected moisture source.
5. Recommend *cause-first* action (fix the water) before any biocide; flag protected/slow-growing lichens.

### Decision points
- Heavy biofilm over sound, dry-after-rain masonry → may be cosmetic; monitor, don't treat.
- Colonisation tracking a defect line (coping, sill, downpipe) → the biology has localised the leak for you.

## Workflow 7: Monitor → forecast → schedule (predictive maintenance)

**Goal:** Turn monitored decay indicators and colonisation growth into a remaining-useful-life estimate and a scheduled intervention.

### Steps
1. `/decay-monitor`: at each epoch record joint recession, hardness/drilling resistance, capillary absorption, salt content, biofilm coverage, crack width — per elevation/zone, with method and date.
2. Require ≥3–4 epochs before trending; fit a decay trajectory per indicator (linear recession, exponential capillarity rise, logistic biofilm growth; lichenometry growth curve as a colonisation clock).
3. Estimate **RUL** = time for the governing indicator to reach its failure threshold, with a confidence band.
4. Rank zones by RUL × exposure (driving-rain) × consequence (visible/structural).
5. Schedule the intervention inside the P-F interval **and** inside a lime-curing-compatible weather window; sequence repointing, biocide (cause-first), and sheltering/detailing fixes.
6. Output the maintenance plan (`prompts/repointing-maintenance-plan.md`) to `outputs/` and set the next inspection date.

### Decision points
- Accelerating (non-linear) recession or capillarity → shorten inspection cadence; the P-F interval is collapsing.
- A change-point in an indicator coinciding with a weather/works event → attribute and re-baseline, don't extrapolate across the break.
- RUL band wide due to few epochs → schedule a re-inspection rather than a premature campaign; say "monitor," not "intervene."
