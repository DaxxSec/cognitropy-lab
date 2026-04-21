---
name: design-optical-system
description: Drive a first-pass paraxial + real-ray design layout for the system defined in context/.
---

# /design-optical-system

## Inputs
Read `context/project.md`. If any of {waveband, FOV, f/#, detector/source, environment} is `TBD`, **halt and run /onboard instead**.

## Steps
1. Compute paraxial first-order: EFL, EPD, image height, chief-ray angle per field.
2. From `resources/starting-designs.md`, pick a starting point that matches the system type (e.g., Cooke triplet for visible wide-field, Double-Gauss for f/2 visible, germanium doublet for LWIR).
3. Present **three candidate architectures** with a table:
   | Candidate | Architecture | Element count | Expected RMS WFE | Key risks |
4. For the user's pick, write a preliminary prescription to `outputs/prescription-v1.csv` with columns: Surface, Type, Radius (mm), Thickness (mm), Glass, Semi-Dia (mm), Notes.
5. Plot (ASCII or suggest Python snippet) a quick schematic.
6. **Pair each candidate with ≥3 candidate failure modes** (seed the FMEA).
7. Log the decision in `work-log/YYYY-MM-DD.md`.

## Output
- `outputs/prescription-v1.csv`
- Updated `work-log/`
- Kickoff seed rows in `outputs/fmea-worksheet.csv` with RPN left blank for the /run-fmea pass to fill.

## Exit Criterion
User says "looks good, proceed to FMEA" or equivalent. Do not move to tolerance work without an FMEA pass.
