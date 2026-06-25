# /fracture-surface-read

Interpret a fracture surface (visual + SEM) to determine the fracture mode, the initiation site, and the crack-progression history.

## Inputs

- Macro photos of the fracture and SEM fractographs (state magnification)
- Part and location; whether the surface is as-found or was cleaned (note any contamination)
- Operating context: cyclic loading, thermal cycling, single overload event

## Steps

1. **Macro first** — locate the origin from radial marks / chevrons pointing back to it and from beach marks (cyclic) vs. a single shear lip (overload). Map the crack-propagation direction.
2. SEM mode ID: fatigue striations (HCF), intergranular (hot tear, temper embrittlement, creep), transgranular cleavage (brittle overload in gray iron), microvoid coalescence/dimples (ductile overload).
3. Inspect the origin for an initiating feature — casting pore, inclusion, machining mark, graphite cluster — and EDS any inclusion at the origin.
4. Read the surface condition: oxidation/heat tint (thermal involvement), corrosion product, secondary cracking.
5. Convert mode + origin into a likelihood ratio across the hypotheses (striations from a pore origin → fatigue initiated at a casting defect) and pass to `/bayes-evidence-update`.

## Output

`outputs/<case-id>/fractography.md`: mode, origin location and initiating feature, propagation map, oxidation/secondary findings, annotated images, and the LR contribution.

## Notes

- Never wire-brush or solvent-blast a fracture before SEM — it destroys the origin and any initiating inclusion.
- Beach marks indicate variable cyclic loading (start/stop); their spacing hints at the load history but is not a striation count.
