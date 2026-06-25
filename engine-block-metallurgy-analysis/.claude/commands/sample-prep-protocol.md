# /sample-prep-protocol

Produce a metallographic sectioning, mounting, grinding, polishing, and etching plan that preserves the evidence and yields artefact-free micrographs (per ASTM E3 / E407).

## Inputs

- Part and the feature to capture (crack origin, bore wall, defect, general microstructure)
- Material family (cast iron vs. aluminium — dictates abrasives, etchant, and care against graphite/Si pull-out)
- What must be preserved (fracture surface, as-received geometry)

## Steps

1. **Document before cutting** — photograph, dimension, and (if a fracture is present) locate the origin so the section is taken *near but not through* it, preserving the origin for fractography.
2. Plan sectioning: orientation (transverse vs. longitudinal to the crack), abrasive cut-off with coolant to avoid thermal damage, and an archive piece set aside untested.
3. Mounting: hot-compression or castable epoxy; note edge-retention needs for surface/chill zones.
4. Grinding/polishing ladder: SiC 120→1200 grit, then diamond 9→3→1 µm, final 0.05 µm colloidal silica — light pressure on cast iron to avoid graphite pull-out and on Al-Si to avoid Si smearing.
5. Etch selection from `context/references.md` (2% Nital for iron matrix; Stead's for P segregation; Keller's or dilute HF for aluminium) — and always read **as-polished first** for graphite/porosity before etching.

## Output

`outputs/<case-id>/prep-protocol.md`: the section map (with origin-preservation note), the abrasive/polish ladder, etchant choice, and the as-received documentation checklist.

## Notes

- Over-aggressive polishing produces graphite "comet tails" and pull-out that masquerade as porosity — light final steps matter.
- Never section through a fracture origin; cut adjacent and keep the mating face intact for SEM.
