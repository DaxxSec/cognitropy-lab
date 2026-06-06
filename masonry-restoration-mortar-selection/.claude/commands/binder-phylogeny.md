# /binder-phylogeny

Place a mortar (or a set) on the binder phylogeny and reason compatibility by relatedness — closeness to the original's clade, distance from the cement clade.

## Inputs

- One or more characterised mortars with Hydraulic Index, binder class, and binder:aggregate.
- The reference original to compare against (the "anchor taxon").
- Optional: aggregate descriptors and vapour/strength data for finer placement.

## Steps

1. Read `context/concepts.md` "Binder taxonomy (the phylogeny)" and `context/references.md` "Binder classes".
2. Position each mortar on the soft→hard cladogram (air lime → pozzolan-gauged → moderately hydraulic → eminently hydraulic → natural cement → Portland) using HI as the primary axis.
3. Compute a relatedness/distance from the anchor original (clade steps + HI delta + strength delta).
4. Apply the compatibility rule: a candidate repair must lie **in or below** the anchor's clade (equal-or-softer). Flag any candidate one or more clades **harder** as incompatible.
5. Hard-flag the **Portland-cement clade** as the distant, near-always-incompatible branch for historic fabric; note the spalling mechanism.
6. Render a small ASCII cladogram with the anchor and candidates marked, plus a verdict per candidate.

## Output

A placement note `outputs/phylogeny-<slug>-YYYY-MM-DD.md`: the cladogram, each mortar's clade + HI, distance from the anchor, and a compatible/incompatible verdict with rationale.

## Notes

- Relatedness here means *behaviour* (strength, permeability), not chemistry for its own sake — a pozzolan-gauged lime can be a "sister taxon" to a feebly hydraulic lime in practice.
- A correct match is equal-or-softer, never harder; if every available product is harder, redesign the aggregate/proportions or shelter the detail rather than climbing the tree.
