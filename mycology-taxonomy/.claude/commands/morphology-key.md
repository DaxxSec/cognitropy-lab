# /morphology-key

Work a specimen's macro- and micro-morphological characters through the appropriate dichotomous key to a candidate genus and provisional species.

## Inputs

- Accession number (record from `/accession-specimen`).
- Macro characters: pileus, hymenophore (lamellae/pores/teeth), stipe, ring/volva, spore-print colour, odour, bruising/staining, chemical spot tests (KOH, Melzer's amyloid reaction).
- Micro characters: spore dimensions/shape/ornamentation, basidia, cystidia, pileipellis, clamp connections, hyphal system.
- The relevant key or monograph (regional flora, genus revision).

## Steps

1. Read `context/concepts.md` "Species concepts" and `context/workflows.md` "Phase 2".
2. Tabulate the observed characters; note which were unmeasurable (immature, damaged).
3. Walk the key couplet by couplet, recording the path taken and every couplet where the specimen is ambiguous or forces a guess.
4. Produce a candidate taxon: genus (confidence) + provisional species, with the characters that support it and those that contradict it.
5. Decide the marker plan: if the candidate genus is a low-ITS-resolution group, flag a secondary marker for `/barcode-id` now.

## Output

- `outputs/determinations/<accession>-morphology.md` — character table, key path, candidate taxon, supporting/contradicting characters, recommended marker plan, and a morphology-only confidence.

## Notes

- Record measurements with units and sample size (e.g. spores "8.5–10.5 × 5–6 µm, n=20"), not adjectives alone.
- Morphology is the first hypothesis, not the verdict — phenotypic plasticity and cryptic species mean it must be reconciled with the barcode in `/barcode-id`.
- Never present a determination as edibility guidance (see CLAUDE.md / README legal notes).
