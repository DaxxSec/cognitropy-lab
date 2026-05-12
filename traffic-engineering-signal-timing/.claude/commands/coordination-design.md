# /coordination-design — Eco-Weighted Green-Wave Coordination

Design a coordinated timing plan across 3+ adjacent signals with an emissions-augmented bandwidth objective.

## Required Inputs
- Per-intersection optimized cycle/splits from `/eco-optimize` (must share a common cycle).
- Inter-signal distances and speed limits.
- Field-measured 85th-percentile speed per segment.
- Directional volumes (inbound vs. outbound).
- Platoon dispersion factor (TRANSYT default = 35; calibrated per corridor preferred).

## Procedure

### 1. Common Cycle Selection
- The longest critical-intersection cycle from Workflow 2 controls.
- If two intersections fall into different time-of-day plans (e.g., one runs free at midday), re-cluster the corridor.

### 2. Identify Coordinated Phase
- Usually the heaviest through movement.
- Verify with an O-D survey, Bluetooth re-ID travel-time data, or ATSPM detector volumes.

### 3. Compute Eco-Target Speed
- Posted speed (start point).
- 85th-percentile (better).
- For CO2 minimization, target 5–7 mph below the lower of those — Barth & Boriboonsomsin (2009) found this is where deceleration severity drops.

### 4. Solve Offsets — Eco-Weighted Multiband
Objective:
```
maximize  sum_d  (vol_d * BW_d) - alpha * sum_d (vol_d * stops_d * CO2_per_stop)
```
where:
- `BW_d` = bandwidth seconds for direction d
- `stops_d` = expected stops on direction d (function of offset choice)
- `alpha = SC_CO2 / VOT_per_second` (≈ 9.5e-3 s/g with $190/t and $20/hr defaults)

Implementation:
- LP via PuLP, with bandwidth and stops both linear in the offset decision variables.
- Or invoke TRANSYT-7F with a custom Performance Index extension.

### 5. Time-Space Diagram
Plot bands inbound + outbound, mark each intersection's coordinated phase. Verify both directions get ≥ 30% bandwidth (typical target).

### 6. Stress Test
- Vary platoon dispersion factor ±20% and verify bandwidth survives.
- Insert simulated TSP green-extension events; verify cross-street recovery within next cycle.
- Insert preemption (rail/EVP) events; verify graceful return to coordination.

### 7. Cross-Street Check
- For every cross-street, verify v/c < 0.9 with the new offsets.
- If a cross-street is pushed over capacity, reduce the bandwidth weight on that segment or carve out a longer split.

### 8. Emissions Delta
- Run `/emissions-model --cmem` on uncoordinated baseline AND the new coordinated plan.
- Document corridor-level CO2/NOx/fuel deltas.
- For finalist coordination plan, re-run with `--moves`.

### 9. Output
Save to `outputs/coordination-{date}/`:
- `offsets.md` — per intersection: coordinated phase, offset (s), reference point.
- `time-space.png` — visualization both directions.
- `bandwidth.csv` — direction × period bandwidth, percent of cycle.
- `stress-test.md` — sensitivity results.
- `emissions-delta.md` — CO2 / NOx / fuel before vs. after.

### 10. Log
Append to `work-log/{YYYY-MM-DD}.md`.
