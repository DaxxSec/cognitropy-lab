---
description: Propose a map design — layers, symbology, projection — for a stated analytical or operational goal.
---

# /map — Map Design Proposal

Invoke when the user needs a map for a report, dashboard, field crew briefing, executive summary, or operational display. Grid Spatial Analyst proposes a design; the user builds it in their GIS of choice.

## Required inputs (agent should prompt if missing)

1. **Purpose of the map.** Is it for a decision, a briefing, a public-facing report, or an operational dashboard? Different audiences need different designs.
2. **The single question the map must answer.** A good map answers one question well; a mediocre map tries to answer five.
3. **Geographic scope.** Service territory, corridor, state, substation neighborhood.
4. **Audience.** Executives / field crews / regulators / public / the analyst themselves.
5. **Medium.** Printed (letter/tabloid), slide, web dashboard, large-format (E-size, wall).
6. **Available layers.** What the user actually has.

## Output shape

1. **Purpose statement** — one sentence. The agent should restate the map's job.
2. **Projection & CRS** — pick a projected CRS appropriate to the scope. For a single state in the US, state plane or a local UTM zone. For a service territory in a single ISO region, a Lambert Conformal Conic works well. Web maps: EPSG 3857 with the caveat that distances/areas are distorted.
3. **Layer stack** — ordered bottom-up, with each layer's role and recommended styling:
   - Basemap (subdued; light gray canvas is the default for operational maps)
   - Reference features (boundaries, water, relief as needed — not competing with data)
   - Context features (service territory, substations as subtle markers)
   - Data layers (the actual analytical content; highest visual weight)
   - Callouts / annotations (labels, scale bar, legend, north arrow, date)
4. **Symbology** — recommended color ramps and classification:
   - Diverging ramp for signed deviations (above/below target)
   - Sequential ramp for single-sign quantities (risk score, load, outage count)
   - Qualitative palette for categorical layers (feeder ID, asset owner)
   - Quantile vs. equal-interval vs. Jenks classification — pick based on whether the tail matters
5. **Accessibility** — recommend a color-blind-safe palette (ColorBrewer 2.0 sequential ramps are a safe default). Avoid red/green as the sole distinguishing cue.
6. **What to leave out** — the design's restraint. Anything that doesn't serve the map's one question comes off.

## Common map types the agent should recognize

- **Outage density map** — sequential ramp over hex or grid, not dots (dots misrepresent density for reporting)
- **Vegetation exposure map** — overlay of canopy height / change detection with ROW buffer, often sequential by exposure score
- **Feeder health map** — categorical or sequential by health index, usually on a primary network geometry
- **Contingency impact map** — sequential by customers-affected or load-lost for an N-1 scenario
- **Wildfire risk corridor map** — multiband composite of fire-weather, fuel, ignition history, and assets
- **Critical asset map** — CIP-sensitive; redact to share publicly; keep assets symbolized, not geocoded precisely

## What the agent should NOT do

- Do not propose designs that expose CIP-protected asset locations to a public audience. Flag the sensitivity and offer a redacted variant.
- Do not specify an ESRI/QGIS/Mapbox-only workflow unless the user said they use that stack.
- Do not invent specific symbol libraries or basemap IDs the user may not have.
