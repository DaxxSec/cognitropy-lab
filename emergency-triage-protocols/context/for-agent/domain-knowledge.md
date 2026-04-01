# Domain Knowledge: Triage Protocols, MTBF Models & Forecasting

## Triage Protocol Fundamentals

### Purpose of Triage
Triage is the process of sorting patients by urgency and acuity to allocate limited resources appropriately. In mass casualty incidents and surge scenarios, triage determines the sequence of patient assessment, treatment, and transport when resources cannot serve all patients simultaneously.

**Core Principle:** Save the maximum number of lives with available resources.

### Triage Categories (Universal)
All major protocols use variants of these categories:

| Category | Color | Priority | Definition |
|----------|-------|----------|-----------|
| **Immediate** | Red | 1 (Urgent) | Life-threatening, salvageable with immediate intervention |
| **Delayed** | Yellow | 2 (Urgent) | Serious injury, but can wait for treatment |
| **Minor** | Green | 3 (Walking Wounded) | Minor injuries, can self-care or minimal intervention |
| **Expectant** | Black | 4 (Comfort care only) | Non-salvageable injuries in resource-constrained setting |

---

## START (Simple Triage and Rapid Treatment)

**Use for:** Adults in mass casualty scenes  
**Developed by:** Newport Beach Fire Department, CA (1983)  
**Assessment time:** 60 seconds per patient

### START Algorithm — Step-by-Step

**STEP 1: RESPIRATION (Airway Assessment)**
- Respirations < 10 or > 30? → **IMMEDIATE (Red)**
- If normal respirations, proceed to Step 2

**STEP 2: PERFUSION (Circulation Assessment)**
Assess radial pulse and capillary refill (CRT):
- Radial pulse absent OR CRT > 2 seconds? → **IMMEDIATE (Red)**
- Radial pulse present AND CRT ≤ 2 seconds? → Proceed to Step 3

**STEP 3: MENTAL STATUS (Neurological Assessment)**
Ask patient to follow a simple command (e.g., "Open your eyes" or "Squeeze my hand"):
- Unable to follow command? → **IMMEDIATE (Red)**
- Able to follow command? → **DELAYED (Yellow)**

**Special Cases:**
- Patient not breathing after airway repositioning → **EXPECTANT (Black)**
- Patient walking and alert → likely **MINOR (Green)**, still apply Step 1–3
- Respiratory distress or severe injury → start at **IMMEDIATE (Red)**

### START Decision Tree

```
START TRIAGE ALGORITHM

Patient encountered
    ↓
RESPIRATION
├─ < 10 or > 30 breaths/min → IMMEDIATE (Red)
└─ Normal → Continue to PERFUSION
    ↓
PERFUSION
├─ No radial pulse OR CRT > 2 sec → IMMEDIATE (Red)
└─ Radial pulse present AND CRT ≤ 2 sec → Continue to MENTAL STATUS
    ↓
MENTAL STATUS
├─ Cannot follow commands → IMMEDIATE (Red)
└─ Follows commands → DELAYED (Yellow)

RULE: All walking patients → at least MINOR (Green)
RULE: Respiratory arrest after airway positioning → EXPECTANT (Black)
```

---

## JumpSTART (Pediatric START)

**Use for:** Children ages 1–8 years  
**Developed by:** Schmitz et al., 1999  
**Assessment time:** 60 seconds per patient

### JumpSTART Modifications to START

| Step | START (Adults) | JumpSTART (Peds 1–8) |
|------|----------------|----------------------|
| Respiration | < 10 or > 30 | < 15 or > 40 |
| Perfusion | Radial pulse, CRT | Palpate brachial/femoral pulse, assess for weak or absent pulse |
| Mental Status | Follow command | Appropriate play or behavioral response (age-adjusted) |
| Special | N/A | If normal respirations but no appropriate behavior → assess for airway positioning |

### JumpSTART Algorithm — Step-by-Step

**STEP 1: RESPIRATION**
- Respiratory rate < 15 or > 40 breaths/min? → **IMMEDIATE (Red)**
- Normal respirations? → Proceed to Step 2

**STEP 2: PERFUSION**
- Palpate brachial or femoral pulse
- Weak or absent pulse? → **IMMEDIATE (Red)**
- Strong pulse present? → Proceed to Step 3

**STEP 3: MENTAL STATUS (Age-Appropriate Behavior)**
- Does child demonstrate age-appropriate behavior or play? (Can follow commands, responds appropriately)
- No appropriate response? → **IMMEDIATE (Red)**
- Appropriate behavior? → **DELAYED (Yellow)**

**STEP 4: AIRWAY POSITIONING (If Normal Respirations But No Appropriate Behavior)**
- If child has normal respiration but abnormal behavior, attempt airway positioning (head tilt/chin lift)
- After positioning, does respirations improve or behavior normalize? → **DELAYED (Yellow)**
- No improvement? → **IMMEDIATE (Red)**

### Pediatric Modifications
- **Behavioral response** used instead of command-following (children < 3 may not follow commands)
- **Respiratory rate thresholds** adjusted for faster pediatric metabolism
- **Pulse assessment** uses brachial (arm) or femoral (groin) instead of radial (wrist)
- **Airway positioning** as therapeutic intervention in triage

---

## SALT (Sort, Assess, Lifesaving Interventions, Treatment/Transport)

**Use for:** Comprehensive mass casualty triage with interventions  
**Developed by:** CDC/Emergency Preparedness and Response  
**Assessment time:** 90–120 seconds per patient (longer due to intervention phase)

### SALT Algorithm — Four Phases

**PHASE 1: SORT (Initial Wave Assessment)**
Rapidly identify patients who can walk or require immediate help:
- **All affected area:** Patients walk toward designated area ("walking wounded")
- **Unable to walk:** Assess individually in place
- **No spontaneous movement:** Assess last

Categorize as:
- **Likely salvageable:** Proceed to individual assessment (Phases 2–4)
- **Clearly deceased or non-salvageable:** Expectant (Black)

**PHASE 2: ASSESS (Vital Sign Assessment)**

For each patient:

| Finding | Triage Level |
|---------|--------------|
| **No breathing after 10-second airway maneuver** | **Expectant** |
| **Radial pulse absent** | **Immediate** |
| **Respiratory rate ≥ 30** | **Immediate** |
| **Altered mental status** | **Immediate** |
| **Non-compressible truncal hemorrhage** | **Expectant** |

If none of above → **DELAYED** or reassess in Phase 3

**PHASE 3: LIFESAVING INTERVENTIONS**
Apply immediate life-saving measures:
- Airway positioning (head tilt/chin lift, remove obstructions)
- Hemorrhage control (direct pressure, elevation, tourniquets)
- Decompression (needle thoracostomy for tension pneumothorax if trained)
- Repositioning (recovery position if safe)

After intervention, reassess:
- Has status improved? → May downgrade triage category
- No improvement? → Maintain assigned level

**PHASE 4: TREATMENT/TRANSPORT**
- Route patients to appropriate transport or treatment area
- Document triage decision and any interventions applied

### SALT Decision Tree

```
SALT TRIAGE ALGORITHM

PHASE 1: SORT
├─ Walking → Proceed to individual assessment
├─ Not walking → Assess individually
├─ No movement → Assess last
└─ Clearly dead/non-salvageable → EXPECTANT (Black)

PHASE 2: ASSESS
├─ No breathing after airway maneuver → EXPECTANT
├─ No radial pulse → IMMEDIATE
├─ RR ≥ 30 → IMMEDIATE
├─ Altered mental status → IMMEDIATE
├─ Non-compressible truncal hemorrhage → EXPECTANT
└─ None of above → Continue to PHASE 3

PHASE 3: LIFESAVING INTERVENTIONS
├─ Apply: airway positioning, hemorrhage control, decompression
└─ Reassess after intervention

PHASE 4: TREATMENT/TRANSPORT
└─ Route to appropriate destination
```

---

## ESI (Emergency Severity Index)

**Use for:** Emergency department triage (routine and surge)  
**Developed by:** Gilboy, Tanabe, Travers, Rosenau (ANA 2007)  
**Assessment time:** 2–5 minutes (more comprehensive than START/JumpSTART)

### ESI Decision Algorithm

**ESI-1 (Emergent) — Does patient require immediate life-saving intervention?**
- Requires immediate aggressive intervention (intubation, resuscitation, hemodynamic support, etc.)
- Examples: Cardiac arrest, severe respiratory distress, altered mental status
- **Action:** Immediate placement in acute care bed

**ESI-2 (Emergent) — Is this a high-risk situation requiring immediate evaluation?**
- Risk of clinically unstable deterioration (chest pain, sepsis, severe pain, overdose)
- Altered mental status, severe headache, unexplained hypotension
- **Action:** Immediate physician/provider evaluation

**ESI-3 (Urgent) — Can patient wait for treatment?**
- Stable with complaint that requires resources (IV, imaging, procedures)
- Examples: Fracture, laceration requiring sutures, fever in child, mild asthma
- **Action:** Evaluation in queue based on acuity

**ESI-4 (Less Urgent) — Minor problem, minimal resources needed**
- Stable, single complaint, minimal ED resources
- Examples: Sore throat, simple laceration needing adhesive strip, cold
- **Action:** Routine queue

**ESI-5 (Least Urgent) — Stable, minimal or no resources**
- No acute complaint, preventive care, minor complaints
- Examples: Medication refill, follow-up exam, minor wound check
- **Action:** May be diverted to fast track

### ESI Application in Surge
During ED surge, ESI allows rapid identification of:
- **ESI-1 & 2 patients:** Require immediate acute care bed (highest priority)
- **ESI-3 patients:** Can accommodate reasonable wait if holding area available
- **ESI-4 & 5 patients:** May be diverted to alternate care sites, urgent care, or observation

---

## MTBF (Mean Time Between Failures) Models

### What is MTBF?

**Mean Time Between Failures (MTBF)** is the average operating time between equipment failures requiring repair or maintenance.

**Formula:** MTBF = Total Operating Hours / Number of Failures

**Example:** Ventilator used 10,000 hours with 5 failures = MTBF of 2,000 hours

### MTBF Application to Equipment

| Equipment | Typical MTBF | Failure Modes | Maintenance Interval |
|-----------|--------------|---------------|----------------------|
| **Ventilator** | 4,000–8,000 hrs | Valve failure, circuit leak, battery | 500 hrs or 3 months |
| **Cardiac Monitor** | 3,000–6,000 hrs | Display failure, electrode connector wear | 400 hrs or 6 months |
| **Infusion Pump** | 5,000–10,000 hrs | Battery, calibration drift, motor wear | 500 hrs or 1 year |
| **Defibrillator** | 2,000–5,000 hrs | Battery depletion, pad degradation, circuit | 6 months (per standard) |
| **Portable Suction** | 2,000–4,000 hrs | Motor wear, canister seal, tubing | 300 hrs or 6 months |

### Predictive Failure Scoring

**Risk Score = (Operating Hours / MTBF) × 100**

- **Risk Score 0–50:** Low risk (Green) — Normal operation, routine maintenance
- **Risk Score 50–75:** Medium risk (Yellow) — Schedule preventive maintenance soon
- **Risk Score 75–90:** High risk (Orange) — Prioritize maintenance, consider backup unit
- **Risk Score 90–100:** Critical risk (Red) — Immediate maintenance or replacement

### Example Calculation

**Cardiac Monitor with MTBF of 5,000 hours:**
- Operating hours to date: 3,500 hours
- Risk Score = (3,500 / 5,000) × 100 = 70%
- **Action:** Schedule maintenance within 2 weeks, order replacement if lead time > 3 months

### Maintenance Schedule Recommendation Algorithm

```
EQUIPMENT MAINTENANCE SCHEDULING

Input: Equipment type, operating hours, MTBF baseline, last maintenance date

Calculate Risk Score = (Operating Hours / MTBF) × 100

IF Risk Score < 50:
  Action: Log routine operation, no maintenance needed
  Review: In 6 months or 500 hours

ELSE IF Risk Score 50–75:
  Action: Schedule preventive maintenance
  Timeline: Within 2–4 weeks
  Monitor: Increase monitoring frequency

ELSE IF Risk Score 75–90:
  Action: Prioritize maintenance scheduling
  Timeline: Within 1 week
  Contingency: Identify backup unit or procure replacement

ELSE IF Risk Score ≥ 90:
  Action: Immediate maintenance or replacement
  Timeline: Within 24–48 hours
  Contingency: Activate backup unit immediately
  Supply Chain: Order replacement parts/unit if not in stock

AFTER MAINTENANCE:
  Reset: Operating hours counter = 0
  Document: Service date, hours serviced, issues found, parts replaced
  Next Review: Per maintenance schedule

FAILURE PREDICTION:
  IF Risk Score ≥ 85 AND no maintenance scheduled:
    Alert: High probability of failure within 1 week
    Recommend: Preemptive replacement or intensive monitoring
```

---

## ED Surge Capacity Forecasting

### Forecasting Models

**1. Time-Series Analysis (ARIMA)**
Uses historical ED census to predict future demand:
- **Daily patterns:** Account for day-of-week effects (Mondays higher, Sundays lower)
- **Weekly patterns:** Variations across weeks
- **Seasonal patterns:** Winter flu, summer trauma, etc.
- **Trend:** Overall growth/decline in volume

**Formula:** ED Census(t) = Baseline + Seasonal Effect + Trend + Error

**Example:**
- Baseline ED census: 100 patients/day
- Winter flu season adds: 20–30 patients/day
- Forecast Jan 15: 100 + 25 = 125 patients expected

**2. Case Mix Analysis**
Predicts resource needs based on patient acuity:
- Categorize patients by ESI level or DRG
- Estimate resource consumption per category (bed hours, staff hours, supplies)
- Calculate aggregate staffing and supply needs

**Example:**
- If 20% of surge patients are ESI-2 (high-acuity)
- ESI-2 requires average 4 bed-hours and 2 RN-hours
- 100 patients × 20% ESI-2 = 20 high-acuity patients
- Staffing need: 20 × 2 RN-hours = 40 additional RN-hours

**3. Surge Ratio Method**
Uses proportional relationship between normal and surge volume:
- **Normal ED capacity:** 100 beds, 80 patients/day, 20 nurses
- **Surge trigger:** 150 patients (1.5x normal)
- **Staffing surge:** 20 nurses × 1.5 = 30 nurses (10 additional)
- **Supply surge:** Multiply baseline supplies by surge ratio

### Surge Capacity Tiers

| Tier | Trigger | Capacity | Staffing | Description |
|------|---------|----------|----------|-------------|
| **Green** | 0–80% | Normal | Normal | Routine operations |
| **Yellow** | 80–100% | Phase 1 surge | +20% staff | Activate contingency beds, flexible scheduling |
| **Orange** | 100–120% | Phase 2 surge | +40% staff | All surge beds open, call-in staff, limit admissions |
| **Red** | 120%+ | Phase 3 surge | +60%+ staff | Divert transfers, critical inventory, mutual aid |

### Forecasting Accuracy Factors

**Factors Improving Accuracy:**
- Longer historical dataset (12+ months)
- Stable baseline patterns (no major changes in facility operations)
- Inclusion of special events (holidays, flu season, local disasters)
- Real-time adjustment based on current census trends

**Factors Reducing Accuracy:**
- Novel events not in historical data (pandemic, major disaster)
- Seasonal changes in patient population
- Changes in referral patterns or facility capacity
- External events (weather, transportation disruptions, community events)

---

## Combined Risk Scoring (Triage + Equipment + Staffing)

### Multi-Factor Risk Assessment

During an MCI or surge event, assess overall system risk:

```
OVERALL SYSTEM RISK SCORE = (Triage Burden + Equipment Reliability + Staffing Capacity)

TRIAGE BURDEN:
- % of patients triaged as IMMEDIATE (red)
- High triage burden = > 40% Immediate patients
- Multiplier: 1.0–2.0x (baseline to double)

EQUIPMENT RELIABILITY:
- Average risk score of critical equipment
- Equipment at high risk = < 30% time until failure
- Multiplier: 1.0–1.5x

STAFFING CAPACITY:
- % of available staff already deployed
- High staffing utilization = > 85% deployed
- Multiplier: 1.0–2.0x

OVERALL RISK = Base Capacity × Triage Burden × Equipment Reliability × Staffing Capacity

IF OVERALL RISK > 1.5x:
  Action: Escalate surge protocol, activate mutual aid, restrict admissions
  Recommendation: Consider patient diversion, transfer, or discharge

IF OVERALL RISK > 2.0x:
  Action: Maximum surge activation, declare internal disaster, external resources
  Recommendation: Activate mutual aid, request state/federal assistance
```

---

## Continuous Improvement Framework

### Data Collection & Analysis
1. **Session Logging:** Record every exercise, simulation, and real event
2. **Performance Metrics:** Triage accuracy, timing, resource utilization
3. **Equipment Tracking:** Maintenance compliance, failure rates, replacement cycles
4. **Staffing Analysis:** Surge activation timeliness, staff utilization, competency gaps

### After-Action Review (AAR)
Conduct within 48 hours of any major event:
1. **What happened?** Objective review of events
2. **Why did it happen?** Root cause analysis
3. **What will we do better?** Specific improvement actions
4. **Who is responsible?** Assign owners for improvements
5. **When will we know it worked?** Define success metrics

### Competency & Training
- Annual protocol training for all clinical staff
- Quarterly competency assessments (protocol knowledge, decision accuracy)
- Simulation-based training with feedback
- Remedial training for staff scoring < 80% on assessments

---

## Key References

- American College of Surgeons. (2020). *ATLS: Advanced Trauma Life Support* (11th ed.)
- CDC Emergency Preparedness and Response. *SALT Triage Algorithm*
- Gilboy, N., Tanabe, P., Travers, D., & Rosenau, A. M. (2007). *Emergency Severity Index (ESI): A Triage Tool for Emergency Department Care* (Version 4)
- Schmitz, G. R., et al. (1999). *JumpSTART Pediatric Triage Algorithm*
- Reliability and Maintainability Center. (Various). *Equipment MTBF Standards & Best Practices*

---

**Last Updated:** 2026-04-01
