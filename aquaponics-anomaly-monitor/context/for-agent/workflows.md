# Aquaponics Anomaly Detection — Domain Workflows

## Overview

This document defines the expert-level workflows the agent follows for aquaponics monitoring, anomaly detection, root cause analysis, and intervention planning. It draws from aquaculture best practices, water treatment engineering, and systems monitoring methodology.

---

## Workflow 1: Automated Anomaly Scan (`/scan`)

### Purpose
Systematically evaluate all current sensor readings against established baselines and thresholds to identify anomalies, rate-of-change violations, and compound event patterns.

### Inputs Required
- Current readings for all available parameters
- Previous reading (for rate-of-change calculation) — optional but recommended
- System baseline from `context/project.md`

### Step-by-Step Protocol

**Step 1: Parameter Validation**
Before analysis, sanity-check incoming data for sensor error signatures:
- pH < 4.0 or > 10.0 → likely probe error (swap/recalibrate)
- DO > 14 mg/L → probe error or supersaturation event
- NH3 = 0.000 exact → colorimetric test may have been read wrong
- Temperature step-change > 5°C/hour → probe fault or equipment failure
Flag suspect readings as `[SENSOR CHECK REQUIRED]` and continue with caveat.

**Step 2: Threshold Check (Tier 1)**
Compare each parameter against species-specific thresholds from `resources/species-profiles.md`:

```
For each parameter P:
  if P > critical_max OR P < critical_min:
    alert = CRITICAL
  elif P > warn_max OR P < warn_min:
    alert = WARNING
  else:
    status = OK
```

Standard threshold table (generic — override with system baselines if available):

| Parameter | OK Range | Warning | Critical |
|---|---|---|---|
| pH | 6.8–7.4 | 6.5–6.8 or 7.4–7.8 | <6.5 or >7.8 |
| NH3 total | <0.1 ppm | 0.1–0.25 ppm | >0.25 ppm |
| NO2- | <0.1 ppm | 0.1–0.25 ppm | >0.25 ppm |
| NO3- | <80 ppm | 80–160 ppm | >160 ppm |
| DO | >6 mg/L | 5–6 mg/L | <5 mg/L |
| Temp (tilapia) | 26–30°C | 24–26 or 30–32°C | <22°C or >34°C |
| EC | 300–1500 μS/cm | >1500 μS/cm | >2500 μS/cm |

**Step 3: Rate-of-Change Check (Tier 2)**
If previous reading available, calculate Δ/hour for key parameters:

```
delta_pH_per_hour = (current_pH - prev_pH) / hours_elapsed
delta_DO_per_hour = (current_DO - prev_DO) / hours_elapsed
delta_NH3_per_hour = (current_NH3 - prev_NH3) / hours_elapsed
delta_temp_per_hour = (current_temp - prev_temp) / hours_elapsed
```

Rate-of-change alert thresholds:
- pH: ±0.3/hr = WARNING, ±0.5/hr = CRITICAL
- DO: -0.5 mg/L/hr = WARNING, -1.0 mg/L/hr = CRITICAL
- NH3: +0.1 ppm/hr = WARNING, +0.2 ppm/hr = CRITICAL
- Temp: ±1.5°C/hr = WARNING, ±2.5°C/hr = CRITICAL

**Step 4: Compound Event Detection (Tier 3)**
Cross-correlate parameter states to identify compound events:

```
# Biofilter crash pattern
if NH3 > WARNING AND NO2 > WARNING AND pH is FALLING:
    compound_event = "BIOFILTER CRASH — CRITICAL"

# Oxygen depletion pattern
if DO < WARNING AND NH3 is RISING AND fish_behavior == "surfacing":
    compound_event = "OXYGEN CRISIS — CRITICAL"

# Overfeeding / overcrowding
if NH3 > WARNING AND NO2 OK AND NO3 RISING AND DO OK:
    compound_event = "NITROGEN LOADING — HIGH"

# Acidification (CO2 or organic acid buildup)
if pH FALLING rapidly AND NH3 OK AND DO OK:
    compound_event = "ACIDIFICATION EVENT — MEDIUM/HIGH"

# Mineral imbalance
if EC > WARNING AND pH stable AND NH3 OK:
    compound_event = "MINERAL BUILDUP — MEDIUM"
```

**Step 5: Output Report**
Format output as:
1. System Status banner (ALL CLEAR / WARNING / CRITICAL)
2. Parameter table with status indicators
3. Rate-of-change flags (if previous reading provided)
4. Compound event alerts (if detected)
5. Prioritized action list (immediate → short-term → routine)

---

## Workflow 2: Alert Triage (`/triage`)

### Purpose
When multiple anomalies are present simultaneously, determine the correct intervention order to avoid making things worse.

### Triage Priority Hierarchy

**Tier 1 — Life Safety (fish)**
Address before anything else:
1. Dissolved oxygen < 4 mg/L — fish are dying right now
2. NH3 > 1.0 ppm — acute toxicity
3. pH < 5.5 or > 9.0 — enzyme/gill damage
4. Temperature > 4°C from species maximum

**Tier 2 — System Stability**
Address within 1–4 hours:
1. Biofilter compromise (NH3 + NO2 both elevated)
2. Pump/flow failure
3. Rapid pH change (even if still in range)

**Tier 3 — Quality Concerns**
Address within 24–72 hours:
1. Elevated nitrate (>80 ppm)
2. EC drift
3. Plant deficiency signs

### Triage Decision Tree

```
START: Multiple alerts present
         │
         ▼
Is DO < 5 mg/L? ──YES──→ PRIORITY 1: Emergency aeration
         │                            (all other actions pause)
        NO
         │
         ▼
Is NH3 > 0.5 ppm? ──YES──→ PRIORITY 1: Partial water change (max 30%)
         │                              Identify source before correcting
        NO
         │
         ▼
Is pH < 6.0? ──YES──→ PRIORITY 1: Slow buffer addition (sodium bicarbonate)
         │                         Investigate cause in parallel
        NO
         │
         ▼
Are NH3 AND NO2 both elevated? ──YES──→ Biofilter event workflow (see below)
         │
        NO
         │
         ▼
Single parameter anomaly ──→ Standard diagnosis workflow
```

---

## Workflow 3: Root Cause Analysis (`/diagnose`)

### Ammonia Spike — Differential Diagnosis

**Possible Causes (ranked by frequency):**
1. **Overfeeding** — most common cause in established systems
2. **Dead fish** — check entire system thoroughly; one rotting fish poisons the tank
3. **New fish addition** — biofilter not yet scaled to new bioload
4. **Biofilter damage** — cleaning with chlorinated water, medication, pH crash
5. **Temperature drop** — slows bacterial metabolism
6. **pH < 6.5** — Nitrosomonas bacteria fail below this pH
7. **Oxygen depletion in biofilter** — bacteria are aerobic
8. **Chemical contamination** — medications, algaecides, cleaning products

**Confirmatory Questions:**
- Any recent system changes? (fish, food, cleaning, chemicals)
- What is NO2 reading? (rising NO2 = bacteria alive but overloaded; falling NO2 = bacteria dead)
- What is pH? (low pH → bacterial inhibition)
- What is DO in filter zone? (low DO → anaerobic conditions)
- Any fish deaths? (if yes, remove immediately)
- When was the filter last disturbed?

**Decision Matrix:**
```
NH3 ↑, NO2 ↑, pH normal → Biofilter overloaded (more fish/feed than bacteria can handle)
NH3 ↑, NO2 ↓/normal, pH dropping → Biofilter failing (bacterial die-off)
NH3 ↑, NO2 normal, NO3 normal → New loading event (recent fish or feed increase)
NH3 ↑, NO2 ↑, NO3 ↑ → System overwhelmed — immediate partial WC needed
NH3 ↑ sudden, everything else normal → Dead fish; search immediately
```

### Dissolved Oxygen Crash — Differential Diagnosis

**Possible Causes:**
1. **Warm water** — O2 saturation decreases with temperature
2. **Aeration equipment failure** — pump, air stone, venturi blockage
3. **Algae crash** — overnight photosynthesis reversal in heavily planted/algae systems
4. **Overfeeding + bacterial bloom** — BOD spike consumes O2
5. **Power outage** — pumps and aerators offline
6. **Biofilm overgrowth** — excessive organic matter in system

**Confirmatory Questions:**
- Time of reading? (DO naturally lowest pre-dawn in planted systems)
- Temperature? (high temp = lower O2 saturation ceiling)
- Any new organic matter added? (feed, plant trimmings)
- Aeration system operational? (listen for pump, check air stones)
- Any algae bloom visible?

### pH Crash — Differential Diagnosis

**Possible Causes:**
1. **CO2 accumulation** — most common overnight; aeration resolves it
2. **Organic acid production** — uneaten feed, decaying matter
3. **High stocking density + low buffering capacity**
4. **Acid dose accident** — pH Down product added incorrectly
5. **Rainwater intrusion** — especially in outdoor systems with low-pH precipitation
6. **Biofilter acid byproducts** — nitrification produces H+ ions; needs alkalinity

**Alkalinity (KH) Context:**
- KH > 100 ppm = good buffering capacity (pH stable)
- KH 50–100 ppm = moderate buffering (pH can drift under load)
- KH < 50 ppm = poor buffering (sudden pH crashes possible)

**Critical Relationship: pH ↔ Ammonia Toxicity**
- NH3 (toxic form) vs NH4+ (non-toxic) depends on pH
- At pH 7.0: ~1% of total ammonia is toxic NH3
- At pH 8.0: ~10% is toxic NH3 — TEN TIMES more toxic at same test kit reading
- At pH 6.5: ~0.3% is toxic NH3
- Always calculate free NH3 fraction, not just total ammonia

```
NH3 fraction = 1 / (1 + 10^(pKa - pH))
pKa at 25°C ≈ 9.25 (adjust for temperature)
```

---

## Workflow 4: Baseline Establishment (`/baseline`)

### Purpose
Derive system-specific thresholds that account for your actual system's behavior, rather than relying on generic textbook values.

### Requirements
- Minimum 7 consecutive days of stable operation (no events)
- Readings at consistent times each day (same time of day)
- At least 2 readings/day (morning and evening) preferred

### Statistical Method

For each parameter:
1. Collect all stable-period readings
2. Calculate: mean (μ), standard deviation (σ)
3. Set thresholds:
   - Normal range: μ ± 1.5σ
   - Warning threshold: μ ± 2σ
   - Critical threshold: μ ± 3σ (or species hard limit, whichever is more restrictive)

### Seasonal Adjustment
Note: Baselines should be recalculated seasonally for outdoor systems as temperature and photoperiod affect:
- Oxygen saturation (temperature-dependent)
- Plant nutrient uptake rate
- Feeding rates
- pH diurnal swing (photosynthesis CO2 consumption)

---

## Workflow 5: Biofilter Health Assessment (`/biofilter`)

### Nitrogen Cycle Efficiency Score

Calculate using:
```
Nitrification Efficiency = NO2_today / NH3_added_estimate
(If efficiency < 0.8, biofilter is lagging)

Full Cycle Score:
  Stage 1 (NH3 → NO2): NH3 removal rate
  Stage 2 (NO2 → NO3): NO2 removal rate
  
If Stage 1 lagging: Nitrosomonas under stress
If Stage 2 lagging: Nitrobacter/Nitrospira under stress
If both lagging: System-wide crash, investigate pH + DO + temperature
```

### Biofilter Recovery Protocol
After a biofilter crash, recovery sequence:
1. **Stop adding stress** — reduce feeding by 50–75%
2. **Optimize conditions** — pH 7.0–7.5, DO >6 mg/L, Temp in optimal range
3. **Do NOT clean biofilter** — you will remove surviving bacteria
4. **Partial water changes** — reduce NH3/NO2 to non-lethal levels without crashing
5. **Consider bacterial supplement** — Nitrifying bacteria products (e.g., Tetra SafeStart) can accelerate recovery
6. **Monitor every 12 hours** — expect 7–21 days for full recovery
7. **Resume feeding only after** — NH3 < 0.1 ppm AND NO2 < 0.1 ppm for 3 consecutive days

---

## Workflow 6: Water Chemistry Analysis (`/chemistry`)

### Full Chemistry Panel Interpretation

**Nitrogen Compounds:**
- NH3 total: target < 0.1 ppm in mature systems
- NO2-: target < 0.1 ppm; any elevation = biofilter stress
- NO3-: target 10–80 ppm for plant uptake; below 10 = underfed; above 160 = partial water change

**Buffering Chemistry:**
- KH (carbonate hardness / alkalinity): target > 100 ppm for stability
- GH (general hardness / minerals): target 100–250 ppm
- If KH low: add potassium bicarbonate or calcium carbonate (not baking soda in high-Na systems)

**Mineral Balance:**
- Iron (Fe): target 2–4 mg/L for plant health — deficiency causes yellowing
- Calcium (Ca): target 40–70 mg/L
- Magnesium (Mg): target 10–25 mg/L
- Potassium (K): target 20–40 mg/L

**Phosphorus:**
- Naturally provided by fish waste
- Rarely deficient in properly loaded systems
- If algae bloom present, phosphorus may be excess

### Chemistry Adjustment Protocols

**To raise pH:** Potassium hydroxide (KOH) or calcium hydroxide (Ca(OH)2) — dilute first, dose slowly
**To lower pH:** Phosphoric acid — use sparingly in food systems; CO2 injection preferred
**To raise KH/alkalinity:** Potassium bicarbonate (preferred — adds K for plants) or calcium carbonate
**To add iron:** Chelated iron (Fe-EDTA or Fe-DTPA) — dose weekly to maintain 2–4 mg/L
**To raise GH:** Calcium/magnesium sulfate blend (cal-mag products)

**Dose calculation framework:**
```
Volume to treat (V) in liters
Target concentration (C_target) in ppm
Current concentration (C_current) in ppm
Product concentration (C_product) as decimal

Dose (mL) = V × (C_target - C_current) / (C_product × 1000)
```

---

## Workflow 7: Health Report Generation (`/report`)

### Report Structure

1. **Executive Summary** (1 paragraph — overall system health, key issues)
2. **Parameter Table** — all parameters with current value, baseline, status, trend arrow
3. **Alert Summary** — active alerts with severity and duration
4. **7-Day Trend Analysis** — if log data available
5. **Nitrogen Cycle Health** — efficiency score and stage assessment
6. **Maintenance Recommendations** — prioritized action list
7. **Upcoming Milestones** — scheduled tasks, feed adjustments, crop harvest windows

### Trend Indicators
- ↑ Rising (consistently higher than baseline)
- ↓ Falling (consistently lower than baseline)
- → Stable (within ±0.5σ of baseline)
- ⚡ Volatile (high variance, coefficient of variation > 15%)

### Severity Tags
- 🔴 CRITICAL — Act immediately
- 🟠 HIGH — Act within hours
- 🟡 MEDIUM — Act within 24–72 hours
- 🟢 ROUTINE — Schedule for next maintenance window
- ℹ️ INFO — Observation, no action required
