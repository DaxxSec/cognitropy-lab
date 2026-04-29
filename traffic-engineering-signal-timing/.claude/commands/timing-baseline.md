# /timing-baseline — Characterize Today's Corridor Performance

Pull the existing signal timing and compute today's performance on every dimension that matters before any optimization is attempted.

## Required Inputs
- Intersection list with controller make/model (from `context/for-agent/environment.md`)
- ATSPM URL or controller log export
- Turning movement counts for the study period
- Saturation flow rate measurements OR HCM 7 default `s_o = 1900 vphgpl`
- Fleet-mix percentages

## Procedure

### 1. Pull Programmed Timing
For each intersection:
- Cycle length(s) by time-of-day
- Splits per phase
- Coordinated phase ID and offset
- Min/max green, yellow, red clearance
- Walk + flashing-don't-walk per ped phase
- Detection plan (presence vs. count, dilemma-zone offsets)

Record in `outputs/baseline-{date}/timing-{intersection}.md`.

### 2. Pull Operating Reality (ATSPM)
Where ATSPM exists:
- **Split Monitor:** programmed vs. actual phase duration histogram (last 14 days, this peak only).
- **Purdue Coordination Diagram:** AOG% per coordinated approach.
- **Approach Volume:** detector-derived volumes by 15-minute bin.
- **Pedestrian Delay:** time from call to walk by phase.
- **Yellow + Red Actuations:** safety surrogate.

Save raw exports to `outputs/baseline-{date}/atspm/`.

### 3. HCM 7 Capacity Model
Per critical lane group, compute:
- Adjusted saturation flow `s = s_o * f_w * f_HV * f_g * f_p * f_bb * f_a * f_LU * f_LT * f_RT * f_Lpb * f_Rpb`
- Capacity `c = s * (g/C)`
- v/c ratio
- Uniform delay `d_1 = 0.5 * C * (1 - g/C)^2 / (1 - min(1, X) * g/C)`
- Incremental (Akcelik) delay `d_2 = 900 * T * [(X-1) + sqrt((X-1)^2 + 8 * k * I * X / (c * T))]`
- Total control delay `d = d_1 * PF + d_2 + d_3`
- LOS per Exhibit 19-8

### 4. Field Validation
- Schedule 3+ floating-car runs per direction per peak; record travel time, stops, idle time.
- Compare modeled to observed delay; if > 20% gap, recheck volumes/saturation/coordination assumptions.
- Document any unmodeled effects (illegal parking, double-parked delivery, signal preemption events).

### 5. Baseline Emissions
Hand off to `/emissions-model` with the per-link drive-cycle estimate from the HCM model + observed stops.

### 6. Output Artifacts
Save to `outputs/baseline-{date}/`:
- `summary.md` — per-intersection delay, LOS, AOG%, ped delay; per-corridor totals
- `volumes.csv` — turning movements and ATSPM volumes
- `timing.md` — programmed timing per intersection
- `validation.md` — modeled vs. observed comparison
- `emissions.csv` — baseline pollutant inventory (CO, NOx, VOC, PM2.5, PM10, CO2-eq, fuel gal/hr)

### 7. Log
Append session record to `work-log/{YYYY-MM-DD}.md` with data gaps, validation outcome, and next-step recommendation.
