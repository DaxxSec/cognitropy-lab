# /interpolate-isofield — Generate Isofield Contours from Spot Measurements

Turn a set of spatial point measurements into a defensible isofield map (lines or surfaces of constant magnitude). Uses kriging or inverse-distance weighting with explicit uncertainty.

## Inputs

- Survey CSV with columns: `x, y, [z], frequency_or_band, magnitude, units`.
- Site outline (PNG / SVG / DXF) for the underlay, registered to the same coordinate system as the survey.
- Choice of interpolation method: ordinary kriging (default), universal kriging (when a deterministic gradient is expected, e.g. distance from a transmitter), or inverse-distance weighting (IDW, fastest, less defensible).
- Target contour levels (e.g. ICNIRP general-public RF level at the surveyed band, 0.5 mT, 5 G, or exposure-quotient contours at 0.1, 0.5, 1.0).
- Optional: a variogram model spec (spherical, exponential, gaussian) if the analyst has prior knowledge of spatial correlation length.

## Steps

1. **Sanity-check the data.** Drop rows with missing position or unit mismatch. Convert all rows to the same field unit (V/m or W/m² typically). If the survey mixes bands, treat each band as a separate map — never average across decades of frequency.
2. **Fit the variogram** if using kriging. Default: empirical variogram with 10 lag bins out to half the site extent, fit a spherical model. Print the nugget / sill / range — a near-zero nugget on noisy field data is a red flag for over-fitting.
3. **Build the prediction grid** matching the site outline. Default cell size is the survey grid spacing divided by 4 (so the map doesn't suggest finer resolution than the data supports). Cap at 200×200 cells.
4. **Run the interpolation** with `pykrige` (kriging) or a NumPy IDW for IDW. Compute both the predicted field and the kriging variance per cell.
5. **Mask uncertain regions.** Cells whose kriging standard error exceeds 50% of the predicted value are stippled or removed — interpolating where you have no data is misleading.
6. **Render contours** at the target levels onto the site underlay. Default style: solid line for the limit, dashed for the watch threshold (0.5 × limit), dotted for the noise floor (0.1 × limit). Use a perceptually-uniform colormap (`viridis`, `inferno`).
7. **Annotate** the map with: survey date, instrument, frequency / band, standard / limit reference, kriging model + parameters, uncertainty band.
8. **Save** to `outputs/maps/<date>-<site>-<band>-isofield.png` and `<...>.svg`. Save the gridded prediction as `outputs/maps/<date>-<site>-<band>-grid.npz` so subsequent runs can re-render without re-interpolating.

## Output

- PNG + SVG isofield map with the site outline underlay, target contours, labels, and uncertainty stippling.
- A `.npz` of the prediction grid (mean + standard error) for reuse.
- A short markdown caption file describing what the map shows, what the colormap means, and where the uncertainty is.

## Notes

- Isofield interpolation extrapolates poorly — never plot the field outside the convex hull of the measurement points. Crop the contour layer to that hull.
- IDW is a presentational tool, not a defensible estimator. For occupational and general-public compliance maps, kriging with reported uncertainty is the standard.
- If the field is dominated by line / surface sources (a busbar, a transformer face) ordinary kriging is biased — use universal kriging with a deterministic trend, or fit per-distance models.
- Above ~1 GHz with multiple sources, the field is interference-dominated and spot-to-spot variation is large; the interpolated map is a smoothed view, not the instantaneous field. State this in the caption.
