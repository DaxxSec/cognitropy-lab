# Boundaries & Constraints

*Populated by `/onboard`. The agent reads this on every operating session and respects every line as a hard constraint, not a suggestion.*

## Specimen Provenance (HARD)

- Every observation must reference a specimen ID. Specimens without an institutional accession or unambiguous field number are **insufficient evidence** — record observations but flag the conclusion as preliminary.
- Locality records are recorded at the precision the user provides. **Do not infer or geocode below user-supplied precision.** Sensitive taxa: defer to user; default is to redact precise locality from any output destined for distribution.

## Nomenclature

- The convention listed in `role.md` is **primary**. Secondary citations are allowed in parens. **Do not silently mix conventions** — if a structure is unnamed in the primary, say so and propose a parenthetical reference to the convention you're borrowing from.
- Latin names: italicize species; do not italicize higher ranks. Authority + year on first use of a binomial in any output document.

## Homology vs. Analogy vs. Homoplasy

- **Never assert homology without grounding.** Required justification: (a) topology / position relative to invariant landmarks, (b) ontogenetic correspondence where data exists, (c) phylogenetic congruence where a tree exists.
- When grounding is incomplete, use the language of *putative homology* and flag what evidence would resolve it.
- Convergent / parallel similarity is **homoplasy**, not homology — never blur the distinction in trait-matrix character definitions.

## Quantitative Standards

- Linear measurements: SI units (mm preferred for vertebrate work; µm for histology). Imperial conversions only on user request.
- Counts: integer with the structure named (e.g. "12 caudal vertebrae" not "many caudal vertebrae").
- Angles: degrees, with reference plane / axis explicitly defined.
- Ratios: numerator ÷ denominator with both quantities defined; provide raw values alongside ratio.
- Significant figures: match measurement precision (e.g. caliper to 0.05 mm = report to 0.1 mm; estimated from photo = report to 1 mm).
- **Do not invent ranges.** If a published range is cited, attach the citation.

## Specimen Care & Animal Ethics

- This workspace assumes specimens are **dead, preserved, fossilized, or imaged-only**. Live-animal work requires IACUC (US) or equivalent — workspace will refuse methodology requiring live procedures unless the user attaches an active approval.
- Photographs of specimens must respect institutional terms; never publish without holding-institution permission.
- Indigenous/culturally significant material: agent will halt and request explicit consultation evidence before proceeding with descriptive work.

## Data Sharing & Embargo

- Default: outputs in `outputs/` are **not** for distribution until the user marks them as cleared.
- If `context/project.md` notes an embargo, agent flags it on every output.
- Specimen photos: never include in agent-authored outputs unless user pastes them in or supplies a path under user-controlled storage.

## What This Workspace Does NOT Do

- Phylogenetic tree inference (use IQ-TREE, RAxML, MrBayes, BEAST in your environment).
- Statistical morphometric analysis beyond descriptive summaries (use geomorph, Morpho, R/Python).
- Histological interpretation requiring stain-specific expertise (defer to a histology specialist).
- Identification beyond the user's claimed taxonomic competence (will not assign a binomial without supporting key + image confirmation by the user).
- Live animal procedure planning.

## Failure Modes — Halt and Report

The agent halts and asks the user to resolve, rather than proceeding, when:

1. A specimen has no provenance.
2. A homology claim cannot be grounded in topology or ontogeny.
3. The user requests a measurement the agent cannot derive from supplied data.
4. The output would identify a sensitive taxon's precise locality.
5. Ethical sourcing of the specimen is unclear.
