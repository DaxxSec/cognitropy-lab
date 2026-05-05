# /terrain-assess — Per-Tile Hazard Map

Generate a hazard raster + terrain-class raster for a planning AOI, from an orthoimage + DEM pair.

## Required Inputs

- DEM file (HiRISE 1 m posting preferred for tactical; CTX 12 m posting for strategic)
- Orthoimage file (same projection as DEM)
- Planning AOI (bounding box in same CRS, or a GeoJSON polygon)
- Rover platform (used to set `wheel_diameter`, `slope_limit`, `tilt_limit`)
- Output directory (default: `outputs/hazard-maps/<sol>-<aoi-id>/`)

## Procedure

### 1. Sanity-Check Inputs

- Verify DEM and orthoimage share a CRS and overlap the AOI.
- Confirm DEM units are metres (HiRISE DEMs typically are; some derived products are not).
- Confirm Mars 2000 datum / planetocentric latitude convention.
- Re-derate the assessment confidence if posting is coarser than wheel diameter (e.g., CTX 12 m posting cannot detect a 30 cm rock).

### 2. Compute Slope and Aspect

Use `gdaldem` or `rasterio` + Horn (default) or Zevenbergen–Thorne (preferred for non-square cells):

```
gdaldem slope <dem> <slope.tif> -compute_edges -alg ZevenbergenThorne
gdaldem aspect <dem> <aspect.tif> -trigonometric -zero_for_flat
```

Save both to the output directory.

### 3. Compute Roughness

Local detrended-DEM standard deviation in a window matched to the rover's wheelbase (e.g., Curiosity wheelbase ~1.9 m → 2 × 2 m window). Save as `roughness.tif`.

### 4. Estimate Rock Abundance

If the orthoimage is high-enough resolution (HiRISE), use shadow analysis (Golombek et al. methods) or, if a project-specific rock-abundance product exists, use that. Output as `rock_abundance.tif` representing cumulative fractional area of rocks above a threshold height set to `0.5 * wheel_diameter`.

### 5. Classify Terrain

Per-pixel categorical assignment using a combination of:
- Orthoimage texture / brightness
- Slope and roughness
- Project-supplied terrain unit map (if available)

Output as `terrain_class.tif` with codes: `bedrock=1, regolith_rocky=2, regolith_fines=3, aeolian=4, conglomerate=5, mixed=6`.

### 6. Compute Composite Hazard Score

```
hazard = 0.40 * normalized(slope, max=slope_limit)
       + 0.20 * normalized(roughness, max=0.3 * wheel_diameter)
       + 0.25 * normalized(rock_abundance, max=0.2)
       + 0.15 * class_penalty[terrain_class]
```

Save as `hazard.tif` (continuous 0–1) and `drivable.tif` (binary, threshold = 0.6 by default; document the threshold in the report).

### 7. Generate Visual Summary

Render a single PNG with:
- Hillshade base (from `gdaldem hillshade`)
- Hazard overlay (red = high, transparent = low)
- AOI bounding box
- Current rover position (if known)
- Strategic target waypoint(s)

Save to `<output>/hazard_summary.png`.

### 8. Document the Assessment

Write `<output>/README.md` capturing:
- Input DEM and orthoimage IDs (PDS product IDs)
- Date of assessment, sol of assessment
- Posting / resolution, derated confidence
- Composite-hazard formula weights used (do *not* leave defaults silent)
- Threshold for `drivable.tif` and rationale
- Known limitations (e.g., shadow analysis can't see rocks in shadow)

### 9. Log to Work-Log

Append to `work-log/<YYYY-MM-DD>.md`: which tile assessed, output path, any anomalies encountered.

## Output

The set of GeoTIFFs (`slope`, `aspect`, `roughness`, `rock_abundance`, `terrain_class`, `hazard`, `drivable`), the visual summary PNG, and the README. Subsequent commands (`/traverse-compose`, `/risk-cadence`) consume these directly.
