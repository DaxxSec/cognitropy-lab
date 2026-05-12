# Tools & Data Pipelines

## Geospatial / DEM Processing

### GDAL command line
- **gdal_translate** — Format conversion, reprojection of HiRISE/CTX orthoimages and DEMs.
- **gdaldem** — Built-in slope/aspect/hillshade/roughness/TPI/TRI computation. Example:
  - `gdaldem slope <input.dem> <output.slope> -compute_edges -alg ZevenbergenThorne`
  - `gdaldem aspect <input.dem> <output.aspect> -trigonometric -zero_for_flat`
  - `gdaldem TRI <input.dem> <output.tri>`  (Terrain Ruggedness Index — Riley/Wilson)
- **gdalwarp** — Reprojection, mosaicking, clipping to a planning AOI.

### Python: rasterio + numpy
- `rasterio` — Read/write GeoTIFF DEMs and orthoimages while preserving CRS.
- `numpy` / `scipy.ndimage` — Local statistics for roughness, dilations / erosions to grow hazard footprints by half-wheelbase margin.
- `scipy.signal.convolve2d` — Custom kernels for direction-of-travel hazard projection.

### Python: networkx
- Build a graph where nodes = waypoints (chord positions), edges = candidate segments with cost = drive-time + harmonic penalty.
- `networkx.shortest_path` for naïve shortest path; `networkx.all_simple_paths` for enumerating candidate progressions; `networkx.k_shortest_paths` (via `nx.shortest_simple_paths`) for top-k.

### QGIS / JMARS / ArcGIS Pro
- **JMARS** — Free JPL/ASU tool for Mars-specific overlays (HiRISE, CTX, THEMIS); excellent for visual review of candidate traverses on top of context imagery.
- **QGIS** — Open-source GIS, good for inspecting hazard rasters and exporting plots for the peer review meeting.
- **ArcGIS Pro** — Commercial; supported at JPL and many universities.

## Mars Mission Tooling (External)

### RSVP — Rover Sequencing and Visualization Program
- The actual NASA/JPL flight tool for tactical sequence generation and visualization. **Not open source.**
- This workspace produces *human-readable* sol plans intended for handoff into RSVP (or its successor) by an authorized planner; it does not generate flight sequences directly.

### ROAMS / ROVERSW
- Rover dynamics simulation. Useful for analog field tests where you want to validate a candidate before driving.
- Open-source equivalents: rover-sim packages from various university programs (e.g., MIT-RAS, ETH Zurich Mars Yard).

### USGS ISIS
- The Integrated Software for Imagers and Spectrometers — used for HiRISE/CTX product processing. Most planners consume PDS-released products; ISIS is needed if you're processing raw EDRs.

## File Format Reference

| Extension | Format | Use |
|-----------|--------|-----|
| `.IMG` | PDS-3 image | Raw HiRISE/CTX EDRs (rare in tactical planning) |
| `.JP2` | JPEG2000 | HiRISE released ortho/DEM products |
| `.tif` / `.tiff` | GeoTIFF | Standard processed DEM/ortho |
| `.shp` / `.gpkg` | Shapefile / GeoPackage | Vector overlays (planned waypoints, hazard polygons) |
| `.csv` | Tabular | Waypoint lists, scoring tables |
| `.md` | Markdown | Plan files, decision logs, handoff documents |
| `.mmd` | Mermaid | State / chord-progression diagrams |

## Internal Workspace Tooling

### Hazard map score formula (reference)

```
hazard_score = (
    0.40 * normalized(slope) +
    0.20 * normalized(roughness_at_wheelbase) +
    0.25 * normalized(rock_abundance_above_h_threshold) +
    0.15 * class_penalty[terrain_class]
)
```

Where `class_penalty` defaults to `{ bedrock: 0.0, regolith_rocky: 0.3, regolith_fines: 0.5, aeolian: 0.8, conglomerate: 0.2, mixed: 0.5 }`.

### Voice-leading penalty (reference)

```
voice_leading_penalty(seg) = (
    abs(slope_change_per_metre) / 5.0  +     # ≤5°/m is fine
    abs(heading_change_per_5m) / 30.0 +      # ≤30°/5m is fine
    leap_penalty(terrain_class_change)       # stepwise ≤ 0.2; leap >= 0.6
)
```

### Scoring during `/peer-review`

- Each axis (feasibility, science, risk, comms, contingency) scored 1–5 by each reviewer.
- Hard fails: any reviewer scoring 1 on **risk** or on their primary-domain axis.
- Average = mean of all (reviewer, axis) scores excluding hard fails.

## Data Sources

- **PDS Geosciences Node — MRO HiRISE/CTX:** https://pds-imaging.jpl.nasa.gov/volumes/mro.html
- **HiRISE catalog (browse):** https://www.uahirise.org/hiwish/
- **MOLA gridded products:** https://pds-geosciences.wustl.edu/missions/mgs/mola.html
- **NASA Trek (Mars):** https://trek.nasa.gov/mars/
- **Mars QuickMap:** https://mars.quickmap.io/

## Optional Integrations

- **MCP filesystem** — for reading large GeoTIFFs out-of-process.
- **MCP shell** — for running GDAL/gdaldem pipelines.
- **MCP python** — for running rasterio + networkx scoring routines.
- **GitHub Issues** — for asynchronous peer review on educational / analog projects.
