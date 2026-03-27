# Limnology Safety Monitor — Domain Workflows

## Overview

This document defines the core operational workflows for freshwater field science with integrated safety protocol enforcement. Every workflow embeds safety checkpoints — not as afterthoughts, but as gating steps that must be satisfied before proceeding.

The philosophy: **safety protocols are not parallel to the science — they are woven into the science.**

---

## Workflow 1: Pre-Deployment Site Risk Assessment

**Purpose:** Evaluate a field site for hazards BEFORE any personnel or equipment are committed.

### Step 1: Site Intelligence Gathering
Collect the following before visiting the site:

- **Water body type:** Lake, reservoir, river, stream, wetland, pond
- **Access route:** Road condition, distance from vehicle to water, portage requirements
- **Bathymetry:** Maximum depth, mean depth, known drop-offs or submerged hazards
- **Flow conditions (lotic systems):** Current velocity, stage height, recent precipitation
- **Water surface area:** Affects wind fetch, wave development, navigation complexity
- **Historical hazards:** Prior incidents, contamination history, known wildlife conflicts
- **Land use in watershed:** Agricultural (pesticide/nutrient runoff), industrial (effluent), urban (stormwater)

### Step 2: Hazard Classification Matrix

Score each hazard category 1-5 (1=minimal, 5=extreme):

| Category | Factors | Score |
|---|---|---|
| **Drowning** | Depth, current, access to shore, water temp | |
| **Exposure** | UV index, air temp, wind chill, precipitation | |
| **Biological** | HABs (cyanobacteria), pathogens, leeches, wildlife | |
| **Chemical** | Known contamination, pH extremes, H₂S risk | |
| **Mechanical** | Boat traffic, submerged obstacles, equipment entanglement | |
| **Access** | Road condition, cell coverage, distance to emergency services | |
| **Weather** | Forecast stability, lightning probability, wind forecast | |

**Risk Score Interpretation:**
- **7-14:** LOW — Standard precautions, proceed with routine safety gear
- **15-21:** MODERATE — Enhanced PPE, buddy system strictly enforced, check-in schedule
- **22-28:** HIGH — Requires safety officer approval, enhanced emergency plan, shortened field window
- **29-35:** EXTREME — No-go without institutional safety review and additional mitigation

### Step 3: Go/No-Go Decision

Hard no-go triggers (any single factor):
- Lightning within 30 minutes / 10 miles of site
- Sustained winds >20 knots (small craft) or >30 knots (large craft)
- Active HAB advisory with no respiratory PPE available
- Water temperature <4°C without immersion suits
- Solo operator (buddy system violation)
- No communication capability at site
- Risk score ≥29 without institutional safety review

### Step 4: Safety Plan Documentation

Generate a field safety plan including:
- Site-specific hazards and mitigation measures
- Emergency action plan (EAP) with GPS coordinates, nearest hospital, emergency contacts
- Communication schedule (check-in intervals, missed check-in protocol)
- Equipment manifest with safety gear verification
- Personnel qualifications verification (boat operation, first aid, swim capability)

---

## Workflow 2: Water Sampling Campaign Design

**Purpose:** Design a statistically valid and safety-compliant sampling plan for a water body.

### Step 1: Define Objectives
- **Regulatory compliance:** Which parameters, which standards (EPA, state, WHO)?
- **Research question:** What hypothesis or monitoring goal drives the sampling?
- **Temporal scope:** One-time survey, seasonal monitoring, continuous?
- **Spatial scope:** Single point, transect, grid, depth profile?

### Step 2: Station Selection

For lakes and reservoirs:
- **Index station:** Deepest point (typically center of lake) — captures full water column
- **Tributary inflow stations:** Major inlet streams — source characterization
- **Outflow station:** Dam or outlet — what leaves the system
- **Littoral stations:** Near-shore, representative of different land use zones
- **Special stations:** Known discharge points, recreational beaches, drinking water intakes

Station placement safety checks:
- Can each station be safely accessed by the planned watercraft?
- Are any stations near navigation channels, dam intakes, or restricted areas?
- What is the maximum distance from shore for any station?
- Is there a safe order of operations that minimizes open-water transit time?

### Step 3: Parameter Selection

**Core limnological parameters (minimum):**
- Water temperature (°C) — depth profile at 1m intervals
- Dissolved oxygen (mg/L and % saturation) — depth profile
- pH
- Specific conductance (μS/cm)
- Secchi depth (m)
- Total phosphorus (μg/L)
- Total nitrogen (mg/L)
- Chlorophyll-a (μg/L)

**Extended parameters (based on objectives):**
- E. coli or enterococci (recreational waters)
- Microcystin and other cyanotoxins (HAB monitoring)
- Major ions (Ca²⁺, Mg²⁺, Na⁺, K⁺, Cl⁻, SO₄²⁻, alkalinity)
- Metals (Fe, Mn, Cu, Zn — especially near mining or industrial areas)
- Turbidity (NTU)
- Color (Pt-Co units)
- Total suspended solids (mg/L)

### Step 4: Sampling Depth Strategy (Lentic Systems)

**Thermal stratification awareness:**
- During stratification: Sample epilimnion, metalimnion (thermocline), and hypolimnion separately
- During turnover (spring/fall): Single integrated sample may suffice, but verify with temperature profile first
- Under ice: Through-ice sampling requires additional safety protocols (see ice safety workflow)

**Depth profile protocol:**
1. Lower sonde to surface (0.5m), allow 60 seconds equilibration, record
2. Lower in 1m increments through epilimnion
3. At thermocline (>1°C change per meter), switch to 0.5m increments
4. Continue through hypolimnion to 1m above bottom
5. Record bottom depth, note if sonde contacts sediment

### Step 5: QA/QC Integration

Every sampling event requires:
- **Field blank:** DI water processed through sampling equipment — tests for contamination
- **Field duplicate:** 10% of samples collected in duplicate — tests for precision
- **Equipment blank:** Rinse water from cleaned equipment — tests for carryover
- **Calibration log:** Pre-field and post-field calibration readings for all instruments
- **Chain of custody:** Documented from collection through lab receipt

### Step 6: Safety-Integrated Sampling Timeline

Build the sampling day schedule with embedded safety checkpoints:

```
05:00  Weather check #1 (go/no-go for departure)
06:00  Arrive at site — visual hazard scan, deploy wind gauge
06:15  Equipment setup — calibration check, safety gear inspection
06:30  SAFETY CHECKPOINT: confirm comms, log GPS, buddy system check
06:45  Launch watercraft — engine/paddle check, PFD verification
07:00  Transit to Station 1 — begin sampling
       [...]
       HOURLY: Weather re-evaluation (mini go/no-go)
       EVERY STATION: Check sample integrity, log time/GPS, verify chain of custody
       [...]
11:00  Return to shore — target completion before afternoon thermal winds
11:15  SAFETY CHECKPOINT: All personnel accounted for, equipment secured
11:30  Post-field calibration check — log drift
12:00  Sample packaging, chain of custody completion, depart site
```

---

## Workflow 3: Water Quality Analysis and Anomaly Detection

**Purpose:** Interpret water quality data, flag exceedances, and identify patterns that indicate ecological or safety concerns.

### Step 1: Data Validation

Before interpreting any data:
1. Check for impossible values (negative concentrations, DO >200% saturation, pH outside 0-14)
2. Compare field duplicates — RPD (relative percent difference) should be <20% for most parameters
3. Verify calibration drift is within acceptable range (typically <10% for sondes)
4. Check holding times — were samples analyzed within method-specified windows?
5. Review field notes for anything that could affect data quality (weather events, equipment issues)

### Step 2: Threshold Comparison

Compare results against applicable standards:

**EPA Recreational Water Quality Criteria:**
- E. coli (freshwater): Statistical Threshold Value (STV) = 410 CFU/100mL; Geometric Mean = 126 CFU/100mL
- Cyanotoxins: EPA recreational advisory — microcystin-LR ≥8 μg/L (advisory), ≥20 μg/L (do-not-swim)

**Nutrient Criteria (EPA Ecoregion-specific):**
- Total Phosphorus: varies by ecoregion (typically 10-40 μg/L reference condition)
- Total Nitrogen: varies by ecoregion (typically 0.3-1.5 mg/L reference condition)
- Chlorophyll-a: varies (typically 2-8 μg/L reference condition)

**Dissolved Oxygen:**
- Warmwater aquatic life: >5.0 mg/L (acute), >6.0 mg/L (chronic)
- Coldwater aquatic life: >6.0 mg/L (acute), >7.0 mg/L (chronic)
- Hypolimnetic anoxia (<1.0 mg/L) — flag for internal nutrient loading risk

**pH:** Most aquatic life: 6.5-9.0

### Step 3: Trophic State Assessment

Calculate Carlson's Trophic State Index (TSI):
- **TSI(SD)** = 60 - 14.41 × ln(Secchi depth in meters)
- **TSI(CHL)** = 9.81 × ln(Chlorophyll-a in μg/L) + 30.6
- **TSI(TP)** = 14.42 × ln(Total Phosphorus in μg/L) + 4.15

| TSI Range | Classification | Characteristics |
|---|---|---|
| <30 | Oligotrophic | Clear water, low productivity, high DO |
| 30-50 | Mesotrophic | Moderate clarity, moderate productivity |
| 50-70 | Eutrophic | Reduced clarity, high productivity, potential DO problems |
| >70 | Hypereutrophic | Very high nutrients, algal blooms likely, fish kills possible |

**TSI divergences reveal mechanisms:**
- TSI(CHL) > TSI(TP): Phosphorus is efficiently converted to algae (zooplankton grazing is low)
- TSI(TP) > TSI(CHL): Something limits algae despite available P (nitrogen limitation, light limitation, grazing)
- TSI(SD) < TSI(CHL): Non-algal turbidity contributes to reduced clarity (sediment, color)

### Step 4: Anomaly Detection

Flag these conditions automatically:
- **Sudden DO crash:** >2 mg/L decrease over 24 hours at a station — possible fish kill event
- **Chlorophyll-a spike:** >2× previous measurement — potential bloom initiation
- **Conductivity spike:** >20% increase — possible contamination event (salt, industrial discharge)
- **pH excursion >9.0:** Intense photosynthesis driving CO₂ depletion — bloom indicator
- **Temperature inversion:** Surface cooler than subsurface — unusual mixing event, check weather
- **Microcystin detection at any level:** Begin HAB response protocol

### Step 5: Trend Analysis

For long-term datasets:
- Plot seasonal Secchi depth to track clarity trends
- Mann-Kendall test for monotonic trends in annual TP, TN, Chlorophyll-a
- Compare pre/post management intervention periods
- Identify regime shifts (sudden, persistent changes in trophic state)

### Step 6: Safety Implications of Data

Water quality data can reveal field safety issues:
- **Microcystin >8 μg/L** → Issue HAB advisory, require respiratory PPE for sampling, no skin contact
- **E. coli >410 CFU/100mL** → Advise team to avoid water contact, use nitrile gloves, decontaminate equipment
- **pH <4 or >10** → Chemical burn risk, enhanced PPE (face shield, chemical-resistant gloves)
- **H₂S detected (rotten egg odor)** → Toxic gas risk, work upwind, limit exposure time, consider air monitoring
- **Anoxic hypolimnion** → Risk of gas eruption during sampling (rare but documented in volcanic lakes)

---

## Workflow 4: Harmful Algal Bloom (HAB) Response

**Purpose:** Systematic response to suspected or confirmed cyanobacterial blooms, with integrated public safety actions.

### Step 1: Visual Assessment
- Surface scum appearance: paint-like sheen, pea soup color, blue-green streaks
- Spatial extent: localized (cove, windward shore) or lake-wide
- Odor: musty, earthy, or chemical smell associated with cyanotoxins
- Dead fish or wildlife observed?

### Step 2: Field Screening
- Chlorophyll-a reading (in-situ fluorescence if available)
- Phycocyanin fluorescence (cyanobacteria-specific pigment probe)
- Collect samples for lab confirmation: grab sample from within visible bloom, also at 0.5m depth
- Photograph bloom with scale reference and GPS tag

### Step 3: Safety Escalation
Based on initial assessment:

| Indicator | Action Level | Response |
|---|---|---|
| Visual bloom, no lab results | **Caution** | Avoid skin contact, nitrile gloves, notify stakeholders |
| Microcystin 0.3-8 μg/L | **Advisory** | Post warnings at recreational access, enhanced PPE for samplers |
| Microcystin 8-20 μg/L | **Warning** | Close recreational areas, respiratory PPE for fieldwork, limit exposure |
| Microcystin >20 μg/L | **Danger** | Do-not-swim/do-not-contact, minimize field operations, full hazmat PPE |
| Anatoxin-a or cylindrospermopsin detected | **Danger** | Neurotoxin/hepatotoxin risk, immediate health authority notification |

### Step 4: Notification Protocol
- **Internal:** Safety officer, PI, field team
- **External (if thresholds exceeded):** State health department, EPA (if drinking water source), municipal water utility, parks/recreation department
- **Public:** Posted advisories at boat ramps, beaches, park kiosks
- **Documentation:** Date/time of detection, concentrations, spatial extent, advisory level, parties notified

### Step 5: Ongoing Monitoring
During active HAB:
- Increase sampling frequency (2-3× per week minimum)
- Track bloom movement (often wind-driven to downwind shores)
- Monitor for toxin changes (different species produce different toxins)
- Document bloom collapse — toxin release during cell lysis can temporarily increase dissolved toxin levels

---

## Workflow 5: Ice Safety for Winter Limnology

**Purpose:** Safe access to ice-covered water bodies for through-ice sampling, sensor deployment, or under-ice ecology research.

### Minimum Ice Thickness Standards

| Activity | Minimum Clear Ice Thickness |
|---|---|
| Walking (single person) | 10 cm (4 in) |
| Walking with equipment (small group) | 15 cm (6 in) |
| Snowmobile or ATV | 20 cm (8 in) |
| Light vehicle (car/truck) | 30 cm (12 in) |

**Critical modifiers:**
- White (snow) ice is approximately 50% the strength of clear (black) ice — DOUBLE the thickness requirement
- Moving water underneath reduces effective thickness significantly
- Ice near inflows, outflows, springs, and pressure ridges is unreliable
- Late-season "honeycomb" ice is structurally weak regardless of measured thickness

### Ice Assessment Protocol
1. Measure thickness at multiple points along traverse route using ice auger + tape
2. Record ice type (clear, white, layered) at each measurement point
3. Check for cracks, ridges, open water, or discolored areas
4. Assess snow cover (insulates ice, slows growth; heavy snow can depress ice and cause overflow)
5. Check recent temperature history — rapid warming weakens ice without visibly thinning it

### Required Safety Equipment for Ice Operations
- Ice picks (worn around neck)
- Throw rope (20m minimum)
- Ice cleats/crampons
- Dry suit or immersion suit (water temp ≈ 0°C)
- Sled-mounted rescue board
- Hot beverages and dry clothing in vehicle

### Go/No-Go for Ice
- **No-go:** Thickness below minimums, unknown thickness, rain forecast, air temp consistently above 0°C for 48+ hours, visible water on ice surface, audible cracking, any team member uncomfortable

---

## Workflow 6: Field Incident Response

**Purpose:** Immediate response procedures for safety incidents during aquatic fieldwork.

### Incident Categories and Immediate Actions

**Person in Water (unplanned):**
1. Call out — alert all personnel
2. Throw (rope bag, PFD, anything buoyant) — do NOT enter water unless trained rescuer with equipment
3. If victim is conscious: coach them to float, kick toward throw device
4. Once recovered: assess for hypothermia (water temp <15°C = immersion hypothermia possible within minutes)
5. Remove wet clothing, insulate, evacuate if symptomatic (shivering, confusion, loss of coordination)

**Chemical Exposure (from water contact):**
1. Remove from exposure source
2. Flush affected area with clean water for 15+ minutes
3. If eye contact: continuous irrigation, do not rub
4. If ingestion suspected (HAB water): do not induce vomiting, seek medical evaluation
5. Document exposure details: substance, duration, route, time

**Equipment Failure on Water:**
1. Anchor or secure position if possible
2. Signal for assistance (VHF radio, whistle, visual signal)
3. If watercraft is taking water: prioritize personnel safety over equipment
4. Deploy emergency flotation
5. Activate PLB if unable to self-rescue

### Post-Incident Requirements
- Complete incident report within 24 hours (use `/incident-report` command)
- Preserve all physical evidence (photos, samples, equipment condition)
- Notify institutional safety office and PI
- Debrief all team members
- Review and update site-specific safety plan
- Root cause analysis for preventable incidents

---

## Workflow 7: Compliance Audit

**Purpose:** Systematic review of sampling procedures against regulatory and institutional requirements.

### Audit Checklist Categories

1. **Personnel Qualifications**
   - Current first aid / CPR certification
   - Boat operator certification (state-specific)
   - Institutional field safety training completion
   - Swim proficiency documentation

2. **Equipment Maintenance**
   - Calibration records current and complete
   - Safety equipment inspection dates within compliance window
   - Watercraft registration and safety equipment (per USCG or state requirements)
   - Communication equipment tested

3. **Sampling Procedures**
   - Methods match approved QAPP (Quality Assurance Project Plan)
   - Holding times met for all analytes
   - Chain of custody complete and accurate
   - Field blanks and duplicates collected at required frequency

4. **Data Management**
   - Data entered within specified timeframe
   - QA/QC flags applied appropriately
   - Results reported in correct units with correct significant figures
   - Exceedances reported to appropriate authority within required timeframe

5. **Documentation**
   - Field notebooks complete and legible
   - Safety plans current and site-specific
   - Incident reports filed for any events
   - Training records up to date
