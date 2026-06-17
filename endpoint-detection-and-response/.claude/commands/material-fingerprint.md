# /material-fingerprint — Characterize the Tooling's "Materials"

Fingerprint the materials and construction of the adversary's tooling — compiler, packer, code reuse, naming conventions — the way textile analysis identifies fiber, dye, weave, and stitch to attribute a garment to a workshop.

## Inputs

- The malicious/suspect binaries or scripts (hashes + samples), and any C2 infrastructure details.
- Optional access to a sandbox / static-analysis tooling and a code-reuse/YARA corpus.

## Steps

1. **Static "fiber" analysis**: PE Rich header, compiler/linker version, language/runtime, section names, entropy (packing), import hash (imphash).
2. **Construction technique**: packer/obfuscator signatures, anti-analysis tricks, error-handling and string-building idioms — the "stitch style."
3. **Dye/source markers**: hard-coded strings, language artifacts, build paths, PDB paths, mutex names, infrastructure-naming conventions.
4. **Separate commodity from bespoke**: commodity materials (off-the-shelf RAT, public packer) are weak attribution signal; bespoke materials (custom loader, unique mutex/protocol) are strong — weight them accordingly.
5. **Match against the corpus**: compute code-reuse / imphash / YARA overlaps with known toolsets and record similarity scores.

## Output

`outputs/material-fingerprint-<sample>-<date>.md`: a materials table (marker · value · commodity-or-bespoke · attribution weight), code-reuse matches with scores, and a short "workshop hypothesis" with explicit confidence.

## Notes

- Commodity tooling is shared by many actors — never attribute on it alone, just as undyed linen names no workshop.
- Feed bespoke markers into `/campaign-typology` as discriminating features.
