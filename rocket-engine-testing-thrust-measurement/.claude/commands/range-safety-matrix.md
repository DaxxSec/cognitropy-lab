# /range-safety-matrix

Score proximity hazards for personnel positions against AFSPCMAN 91-710 / NFPA 55 / KSC-DE-512 standoffs by walking the `S-*` tree (`context/workflows.md` §5). Emits a per-position matrix cell and an aggregate NO_GO_LAYOUT / GO_LAYOUT disposition.

## Inputs

- `test_id` — test identifier.
- `stand_layout_path` — map / drawing of the test stand and surrounding facilities, with named personnel positions (control room, observation point, fire department staging, etc.).
- `propellant_inventory` — per-propellant mass at fire time. Includes propellants in tanks, lines, and ancillary stores within hazard distance.
- `stand_structural_geometry` — blast walls, deflector geometry, fragment containment specs, slope-of-pad.
- `engine_failure_mode_likelihoods` — pulled from the `T-*` matrix output (chamber breach, pump rotor uncontainment, plumbing leak).
- `weather_constraints_policy` — wind direction / speed limits, plume dispersion model parameters.

## Steps

1. Run `S-0` intake. Reject if stand layout, propellant inventory, or engine FMEA-derived likelihoods are missing.
2. Compute TNT-equivalent per propellant at `S-1`. Use NFPA 55 / DoD 6055.09-M factors per propellant combination. LOX/RP-1 and LOX/CH4 typical 0.10–0.25 unconfined-liquid-mix; LOX/LH2 lower bulk TNT-eq with larger fireball. Cite source per row.
3. Compute overpressure standoffs at `S-2` (1 psi, 2.3 psi, 5 psi) using AFMAN 91-201 / Kingery-Bulmash equations from the TNT-eq result. Plot each personnel position against the iso-overpressure contours.
4. Compute fragmentation footprint at `S-3`. Worst-credible fragment mass × velocity from chamber breach or pump rotor uncontainment. Apply stand geometry (containment walls, blast deflector) to scope the angular spread.
5. Compute fire-spread footprint at `S-4`. Cryo pool spread radius from spill volume + slope geometry; combustible inventory within radius drives propagation severity.
6. Compute plume / toxicity footprint at `S-5`. Downwind product concentration using site-approved dispersion model. For hypergolics (MMH/NTO), reference AEGL/ERPG tables. For LOX/HC, primary concern is CO and stand-material decomposition products.
7. Apply likelihood overlay at `S-6`. For each hazard, use the FMEA-derived likelihood of the failure mode that produces it (chamber breach: B–C development, D–E flight-heritage).
8. Plot per-position matrix cells at `S-7`. Any position with cell ≥ SERIOUS → NO_GO_LAYOUT with reposition / evacuation recommendation. MEDIUM cells require ALARP justification with documented mitigation. All LOW → routine.
9. Write the matrix and aggregate disposition to `outputs/range-safety/<test_id>-range-<YYYYMMDD>.md`.

## Output

Markdown file containing:
- Test ID, propellant inventory, stand geometry hash.
- TNT-equivalent computation per propellant with cited factors.
- Overpressure standoff table: 1 psi / 2.3 psi / 5 psi distances; personnel positions plotted against them.
- Fragmentation footprint diagram (textual: angular spread, max range, blocking geometry).
- Fire-spread footprint diagram.
- Plume / toxicity downwind concentration vs. distance at the planned wind envelope.
- Per-personnel-position matrix table: position name, hazard contributions, worst-cell, band, mitigation if applicable.
- Aggregate disposition (GO_LAYOUT / NO_GO_LAYOUT) with binding cells.
- Recommended layout adjustments if NO_GO_LAYOUT.
- Reproducibility footer: layout hash, inventory snapshot, wind envelope.

## Notes

- TNT-eq factors vary widely in the literature. Cite your source (NFPA 55, DoD 6055.09-M, NASA-STD-5018) per row. Site-specific factors may bind.
- Stand-survivability is not the same as personnel-survivability. A blast wall that saves the control room from 5 psi may still let 2.3 psi reach an unprotected observation point.
- Plume modeling is wind-direction-sensitive. If the campaign uses a wind-window go/no-go, document the window in the test card and check actual conditions at T-30 minutes.
- For hypergolic propellants, the plume-toxicity term is often more binding than the overpressure or fragmentation terms. Run plume *first* if the propellants are hypergolic.
- Re-run `/range-safety-matrix` on every change to: propellant inventory, personnel positions, stand structural geometry, or wind constraints. The matrix is not portable across configurations.
- Range-safety officer signs the range-safety-matrix; the test conductor signs the `T-*` readiness matrix. Both signatures required for fire.
