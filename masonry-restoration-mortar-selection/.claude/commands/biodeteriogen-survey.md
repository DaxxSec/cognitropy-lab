# /biodeteriogen-survey

Taxonomically identify the organisms colonising the masonry and read their distribution as a bioindicator of the moisture / exposure regime.

## Inputs

- Photographs of colonised surfaces by elevation/height, with scale.
- Field observations: growth form, colour, coverage %, texture (filamentous, crustose, crust, moss).
- Optional lab/ITS results for confirmation of ambiguous taxa.
- The elevation map and any known moisture defects (copings, sills, downpipes).

## Steps

1. Read `context/concepts.md` "Biodeteriogens and bioreceptivity" and `context/references.md` "Biodeteriogen genera".
2. Map colonisation: coverage % and growth form per zone; photograph with scale.
3. Identify to genus where possible (morphology + field key); sample for lab/ITS confirmation only where it changes the diagnosis.
4. Interpret as bioindicators: *Trentepohlia* / persistent greening → chronic wetting; endolithic lichens on calcareous stone → long undisturbed wet exposure; black microcolonial fungi → repeated wet–dry stress.
5. Overlay colonisation distribution on the decay map and the suspected moisture source — the biology often localises the leak.
6. Recommend **cause-first** action (fix the water) before any biocide; flag protected or slow-growing lichens and friable surfaces.

## Output

A survey record `outputs/biosurvey-<building>-YYYY-MM-DD.md`: the colonisation map (zone, taxa, coverage, growth form), the moisture-regime interpretation, the localised likely source, and cause-first recommendations with biocide caveats.

## Notes

- Heavy biofilm over masonry that dries soundly after rain may be cosmetic — monitor, don't treat.
- Bioreceptivity rises as fresh lime weathers (pH falls, surface roughens); time biocide/repointing accordingly.
- Identification feeds `/decay-monitor` (biofilm coverage %) and `/maintenance-forecast` (colonisation growth as a clock).
