# /scenario-compare — Plan-vs-Plan Delta

Side-by-side comparison of two or more timing plans on every dimension that matters: delay, fuel, CO2, NOx, PM2.5, noise, pedestrian/bike service.

## Required Inputs
- Two or more plans, each with HCM 7 capacity output and emissions output (CMEM or MOVES).
- A common study period (AM, MD, PM, off-peak) — never compare different periods.
- A common demand vector (volumes, fleet mix) — never compare under different demand.

## Procedure

### 1. Build the Comparison Matrix
Rows = scenarios; columns = metrics. Required columns:
- Cycle length (s)
- v/c max
- Control delay per veh (s) — corridor average
- LOS — corridor and worst-intersection
- Stops per vehicle — corridor average
- Vehicle hours of delay (VHD) — corridor total per peak hour
- Fuel (gal/hr)
- CO2-eq (kg/hr)
- NOx (g/hr)
- VOC (g/hr)
- PM2.5 (g/hr)
- PM10 (g/hr)
- Noise Leq dB(A) — at sensitive receptors if any
- Pedestrian average delay (s)
- AOG % (coordinated approaches)
- Transit delay (s/bus) — if TSP modeled

### 2. Annualize
Convert peak-hour numbers to annual estimates using time-of-day factors and operating-day count (typically 250 weekdays for commute corridors, 365 for retail).

### 3. Sensitivity Sweep
Recompute the matrix under:
- ±10% volume
- +5 yr fleet (model-year roll-forward; lowers per-veh emissions ~10–15%)
- +1°F summer temp (NOx sensitive)

### 4. Equivalent Metrics
Translate the comparison into stakeholder-friendly equivalents:
- CO2 → "passenger cars off the road for a year" (≈ 4.6 t-CO2-eq each, EPA 2024)
- Fuel → annual fuel cost @ local gas price
- NOx → fraction of corridor NAAQS exposure standard
- Delay → annual person-hours saved × VOT ($/hr)

### 5. Recommendation Block
Pick the recommended plan; document why (constraint-driven, knee-point, stakeholder priority).
Mark explicitly any worsened dimension and explain the trade-off.

### 6. Output
Save to `outputs/scenario-compare-{date}/`:
- `matrix.csv` — full numeric matrix
- `summary.md` — narrative comparison with chart references
- `sensitivity.csv` — sweep results
- `chart-pareto.png` — recommended plan plotted on the Pareto frontier
- `chart-stack.png` — pollutant stack chart by scenario

### 7. Log
Append to `work-log/{YYYY-MM-DD}.md`.
