# /emissions-model — MOVES- or CMEM-Style Emissions Estimate

Run a project-level emissions estimate from per-link delay, queue, and idle time. CMEM is the default fast inner-loop; MOVES4 is the regulatory mode.

## Modes

- **`--cmem`** (default): seconds-fast lookup using `resources/cmem-modal-fuel-rates.md`. Use during Pareto search.
- **`--moves`**: invokes EPA MOVES4 project-level scale. Use for the regulatory deliverable on finalist plans.
- **`--emfac`**: California-only; invokes CARB EMFAC2021. Required for any CA conformity submittal.

## Required Inputs
- Link table: per intersection movement, with length, average speed, source-type fraction, road-type code (per MOVES `roadTypeID`).
- Drive cycle: per-link average delay, stops/vehicle, idle time. (For MOVES microsimulation drive-schedule, second-by-second speed traces from Vissim/SUMO.)
- Fleet mix: % LDV / LDT / SU truck / Combo truck / Bus / MC by model year (or county-default if unavailable).
- Meteorology: county-month T (°F), RH (%), barometric pressure.

## CMEM Procedure (default)

### 1. Modal Time Fraction Per Link
From HCM/HCS output:
- `t_idle = ped_calls + queue_clearance` (controller-derived)
- `t_accel ≈ S * (v_target / a_avg)` where S = stops/veh, a_avg = 5 ft/s² typical
- `t_decel ≈ S * (v_target / d_avg)` where d_avg = 5 ft/s² typical
- `t_cruise = link_travel_time - (t_idle + t_accel + t_decel)`

### 2. Apply Modal Rates
For each pollutant `p` and source-type `j` with fleet weight `w_j`:
```
E_p_link = sum_j w_j * (
    t_idle * r_idle_p_j +
    t_accel * r_accel_p_j +
    t_cruise * r_cruise_p_j +
    t_decel * r_decel_p_j
) * vehicles_link
```
Coefficients `r_*` from the lookup table.

### 3. Aggregate
Sum to per-intersection, then per-corridor, then peak-hour totals.

### 4. Output
`emissions-cmem-{peak}-{date}.csv` with columns:
```
intersection, movement, peak, vehicles, CO_g, NOx_g, VOC_g, PM25_g, PM10_g, CO2_kg, fuel_gal
```

## MOVES4 Procedure (regulatory)

### 1. Build the MOVES Project Database
- Use the MOVES4 GUI's project-level wizard OR an XML run-spec.
- Tables to populate: `roadType`, `link`, `linkSourceTypeHour`, `linkAverageSpeed`, `meteorology`, `sourceTypeYear`, `fuelType`, `operatingModeBin` (if drive-schedule provided).

### 2. Drive Schedule From Microsim
If Vissim/SUMO traces are available:
- Bin second-by-second speed × VSP (vehicle specific power) into MOVES operating-mode bins (1–40).
- Replaces the link-average-speed approach with a richer modal description.
- Yields ~10–20% better accuracy for stop-and-go conditions.

### 3. Run MOVES4
- GUI for one-off; CLI batch via `MOVESLooper` for sensitivity.
- Verify outputs in the `MOVESOutput` database.

### 4. Aggregate
Sum across source-types, processes (running, start, idle, evap), and links to corridor-level totals per pollutant.

### 5. Document Methodology
Critical for SIP/CMAQ submittal — record:
- MOVES version (e.g., 4.0.1, 2024 release)
- Input year used
- Fleet source (HPMS year, MPO submittal)
- Drive-schedule source (microsim model + scenario)
- Meteorology source (NOAA station, year)

### 6. Output
`emissions-moves-{peak}-{date}/` with:
- `summary.md` — corridor totals per pollutant
- `byLink.csv` — link-level emissions
- `methodology.md` — inputs and assumptions for the regulatory record
- `runspec.xml` — the MOVES run specification used (for reproducibility)

## Cross-Check
For finalist plans, compute both CMEM and MOVES; expect agreement within ±15% at the corridor level. If divergence > 25%, debug the link-table inputs (most often a fleet-mix or operating-mode-bin mistranslation).
