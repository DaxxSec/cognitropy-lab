# /melt-flux-spec

Specify melt preparation — charge purity, atmosphere, superheat, and fluxing — to suppress heterogeneous nucleation, the single most common destroyer of GFA and therefore of yield and capacity.

## Inputs

- Alloy family and oxygen sensitivity (Zr-based is highly sensitive; Pd-based responds strongly to B₂O₃ fluxing).
- Available melt environment: vacuum level, inert gas (Ar) purity, crucible material.
- Feedstock grades (e.g. Zr sponge vs crystal-bar, oxygen content in ppm) and any recent feedstock/process change.
- The observed symptom, if troubleshooting (yield drop, surface crystallinity, raised Tx scatter).

## Steps

1. Read `context/concepts.md` §7 (failure modes) and §2 (heterogeneous nucleation barrier).
2. Set a **charge-purity spec**: target dissolved oxygen ceiling (Zr-based: keep well below the hundreds-of-ppm regime that degrades Dmax), element purities, and feedstock form (low-O sponge / crystal bar where needed).
3. Specify **atmosphere**: vacuum or high-purity Ar; getter (e.g. Ti sponge) to scavenge residual O₂; leak/backfill protocol.
4. Specify **fluxing** where applicable: B₂O₃ flux for Pd-based alloys (dissolves oxide nucleants, can push Dmax from mm to cm); contact time and temperature; not all families flux usefully — say so.
5. Set **superheat and hold**: enough to dissolve existing nucleants and homogenise, but not so long/hot as to pick up crucible contamination.
6. Build a **nucleation-risk register**: rank the likely heterogeneous-nucleation sources for this setup and the control for each; tie each control to its yield/capacity consequence.

## Output

`outputs/melt-flux-spec-<alloy>-YYYY-MM-DD.md`: charge purity + feedstock spec, atmosphere protocol, fluxing protocol (or "no useful flux for this family"), superheat/hold, and the nucleation-risk register with controls and their capacity impact. If troubleshooting, the most-likely regression and the fix.

## Notes

- For Zr-based alloys, oxygen is usually the dominant lever — a few tens-to-hundreds of ppm of O can seed quasicrystal/crystal nucleation and collapse Dmax with no other change.
- **Safety:** Zr/Ti melts are pyrophoric as fines and O/moisture-reactive; melt under vacuum/inert atmosphere. B₂O₃ fluxing and molten-metal handling are high-temperature hazards. Flag Be-bearing alloys for the beryllium controls.
- A yield drop with no machine change is almost always a melt-prep/feedstock regression — start here before re-cutting molds.
