# /porosity-defect-map

Quantify casting porosity and inclusions and classify each by origin (gas vs. shrinkage vs. slag/dross/sand), so casting-quality evidence enters the posterior with a calibrated weight.

## Inputs

- As-polished micrographs and/or radiographs/CT of the defect region
- Defect location relative to section geometry (junction, hot spot, cope surface, last-to-freeze region)
- For inclusions: EDS spectra if available

## Steps

1. Quantify the void/inclusion population — area fraction, size distribution, and spatial clustering (ASTM E1245 image analysis; E2422/E505 radiographic reference grades for aluminium).
2. Classify each void by morphology: gas (smooth, round, subsurface), shrinkage (jagged, dendritic, interconnected, in last-to-freeze zones), cold shut (smooth fused boundary).
3. Classify inclusions by EDS chemistry: sand (Si/O), dross/oxide film (Al-Mg-O in aluminium), slag/refractory.
4. Tie location to mechanism — shrinkage at a thick junction, gas distributed subsurface, dross at a turbulent gate — to point at the casting process step.
5. Express the defect finding as a likelihood ratio (origin-coincident shrinkage pore → strong LR for casting-defect cause) and pass to `/bayes-evidence-update`.

## Output

`outputs/<case-id>/defect-map.md`: defect inventory with area fraction and size stats, per-defect origin classification, process-step attribution, and the LR contribution.

## Notes

- Distinguish gas vs. shrinkage by morphology under SEM, not by size alone — they overlap in dimension.
- Polishing pull-out and graphite drop-out mimic porosity; verify against the etched image and the as-cast surface before counting.
