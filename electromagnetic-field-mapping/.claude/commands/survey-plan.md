# /survey-plan — Design an EM Field Survey

Produce a frequency-aware, standard-aware survey plan: measurement grid, probe + detector + RBW table, dwell budget, and a written scope.

## Inputs

- Site description (indoor / rooftop / substation / chamber / bench) and a layout sketch or floor plan in `outputs/site/`.
- Survey objective: occupational compliance, general-public compliance, EMC pre-screen, TSCM, fringe-field mapping, or environmental baseline.
- Frequency range(s) of interest (or "unknown — sweep wide" for baseline).
- Standard the survey must satisfy (ICNIRP 2020, IEEE C95.1-2019, FCC OET-65, IEC 62232, CISPR 32, IEC 61786, IEC 60601-2-33, or "informational only").
- Available probes / antennas / instruments and their calibration status.
- Time and access budget on site.

## Steps

1. **Classify the survey type** by walking the top of the triage tree in `context/workflows.md` — this fixes the standard, the relevant frequency split (DC/ELF, 100 kHz – 6 GHz, 6 GHz – 300 GHz), and the detector mode (RMS, peak, quasi-peak).
2. **Choose the probe set** from `context/references.md` against the frequency split: E-field, H-field, or isotropic broadband for survey-grade; horn / log-periodic / biconical with calibrated antenna factors for spectrum-analyser work; 3-axis ELF for power frequency. Reject any probe whose calibration is older than the survey program allows.
3. **Build the measurement grid.** Default spacings: 1 m (general-public RF safety), 0.5 m (occupational), 5 – 10 cm (near-field / EMC), and isofield-target spacing (where the standard specifies, e.g. 0.5 mT for MRI). Mark exclusion zones (energized cabinets, antenna near-field volumes). For rooftop telecom: respect the compliance perimeter — points beyond the exclusion radius are routine, points inside are PPE-controlled.
4. **Set instrument parameters.** RBW chosen to resolve the narrowest expected emission and to satisfy any standard-mandated bandwidth (CISPR 32 uses 120 kHz QP from 30 – 1000 MHz; ICNIRP integrates over averaging time, not RBW). Dwell ≥ 2× the longest expected duty cycle, or 6 minutes for time-averaged RF, or 30 minutes where required.
5. **Plan polarization sweeps.** Above 1 GHz at telecom sites, at least horizontal + vertical + 45° captures per point. For broadband isotropic probes, polarization is folded in — note it explicitly.
6. **Budget time and storage.** `total = points × (dwell + travel) + setup + calibration verification`. Add 20% contingency. Estimate raw-data volume if logging IQ or spectrum traces.
7. **Write the scope document.** Save as `outputs/plans/<date>-<site-slug>-survey-plan.md` with: objective, standard, exclusion zones, probe table with calibration IDs, grid coordinates, parameter table, dwell budget, sign-off line.

## Output

A scope file at `outputs/plans/<date>-<site-slug>-survey-plan.md` and a printable grid sheet at `outputs/plans/<date>-<site-slug>-grid.csv`. Both committed to the workspace.

## Notes

- A wider grid produces a plot you cannot defend — always check that the grid resolves the strongest expected lobe by at least 4 samples across.
- If the user can't name the standard, ask before generating the plan. Default to ICNIRP 2020 for RF safety in non-US jurisdictions and IEEE C95.1-2019 + FCC OET-65 for US sites.
- Recalibration of probes near survey day, not "we'll check it later" — a probe with a lapsed cert invalidates the entire report.
