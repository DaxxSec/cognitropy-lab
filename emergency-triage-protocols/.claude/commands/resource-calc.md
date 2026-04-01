# /resource-calc — Staffing, Supply & Transport Calculations

## Purpose
Calculate detailed staffing, supply, and transport resource requirements for a given patient volume, acuity mix, and facility model. Supports resource planning and surge preparation.

## When to Use
- Planning for anticipated surge or MCI response
- Validating surge protocol staffing requirements
- Calculating supply chain needs
- Transport resource planning
- Budget justification for additional resources

## Duration
15–30 minutes depending on complexity

## Input Required

I'll request:

### 1. Patient Volume & Acuity
- **Total patient count:** Expected or actual
- **Acuity breakdown:**
  - By ESI level (1, 2, 3, 4, 5) — for ED surge
  - By triage category (Immediate, Delayed, Minor) — for MCI
  - If unsure, I can use your facility's typical distribution

### 2. Facility Model
- **ED bed capacity:** Total beds available
- **Surge bed capacity:** Additional beds available during surge
- **Treatment areas:** Trauma resus, acute care beds, waiting area, fast track
- **Equipment availability:** Monitors, ventilators, IV pumps, etc.

### 3. Average Length of Stay (LOS)
- **By acuity level:** How long does average ESI-2 patient stay?
- **Or by category:** Average time in ED for Immediate, Delayed, Minor
- **Processing time:** Time from arrival to bed assignment

### 4. Calculation Type
- **Staffing:** RNs, physicians, technicians needed
- **Supply:** IV fluids, medications, dressings per patient
- **Transport:** Ambulances, personnel, transport time
- **All of above:** Complete resource picture

## How Calculations Work

### 1. Staffing Calculations

**Nurse-to-Patient Ratio:**
- ESI-1 (Immediate): 1 nurse per 1–2 patients
- ESI-2 (High-acuity): 1 nurse per 2–3 patients
- ESI-3 (Moderate): 1 nurse per 3–4 patients
- ESI-4/5 (Low-acuity/fast track): 1 nurse per 5–6 patients

**Example:**
- 18 patients: 2 ESI-1, 8 ESI-2, 8 ESI-3
- ESI-1: 2 patients ÷ 1.5 ratio = 1.3 RNs (round up to 2)
- ESI-2: 8 patients ÷ 2.5 ratio = 3.2 RNs (round up to 4)
- ESI-3: 8 patients ÷ 3.5 ratio = 2.3 RNs (round up to 3)
- **Total RN staffing needed: 9 nurses**

**Physician Staffing:**
- 1 physician per 8–12 patients (depending on acuity and training level)
- 18 patients ÷ 10 = 1.8 physicians (round up to 2 physicians or 1 MD + 1 NP)

**Support Staff (Technicians, Aides):**
- 1 tech per 4–6 patients
- 18 patients ÷ 5 = 3.6 techs (round up to 4)

### 2. Supply Calculations

**IV Access & Fluids:**
- ESI-1 patients: 2–3 IV lines per patient
- ESI-2 patients: 1–2 IV lines per patient
- ESI-3 patients: 0–1 IV line per patient
- Average IV fluid consumption: 500 mL–2 L per patient depending on acuity

**Medications:**
- Pain medications: ~60% of patients require analgesics
- Antiemetics: ~40% require
- Antibiotics: ~20% of acuity ≥2
- IV medications: 2–3 doses per patient average

**Dressings & Supplies:**
- Minor injuries: 5–10 dressing units per patient
- Moderate injuries: 20–40 dressing units
- Major/critical: 50–100+ dressing units

**Example for 18 patients:**
- IV lines needed: (2 × 2.5) + (8 × 1.5) + (8 × 0.5) = 5 + 12 + 4 = 21 IV lines
- IV catheters (16–20 G): 21 catheters + 25% backup = ~26
- IV fluids (LR): 5 L × 1.5 avg + 12 L × 1 avg + 4 L × 0.5 avg = 27.5 L (round to 30 L)
- Dressings: (8 × 30) + (8 × 20) + (2 × 75) = 240 + 160 + 150 = 550 dressing units

### 3. Transport Calculations

**Ambulance Requirements:**
- Average transport time: 15 minutes each direction = 30 minutes round-trip
- Each ambulance can handle 1–2 patients per hour depending on destination distance
- For 18 patients over 2 hours: 18 patients ÷ 2 hrs ÷ 2 patients/hr/rig = 4.5 rigs (5 ambulances minimum)

**Personnel:**
- 2 paramedics per ambulance
- Additional supervisory/coordination staff

## Example Complete Resource Calculation

```
SCENARIO: Mass Casualty Incident — 18 Patients

PATIENT DISTRIBUTION:
- Immediate (Red): 2 patients
- Delayed (Yellow): 8 patients
- Minor (Green): 8 patients
- Expectant (Black): 0 patients

FACILITY BASELINE:
- ED capacity: 20 beds
- Surge capacity: 25 beds (add observation area)
- Available physicians: 2
- Available RNs: 8
- Available techs: 3

STAFFING CALCULATION:

Immediate (2 patients) - Trauma resus
- Requirement: 1 RN per 1–1.5 patients = 2 RNs
- Physician time: High intensity; dedicated surgeon on standby

Delayed (8 patients) - Acute care beds
- Requirement: 1 RN per 2–3 patients = 3–4 RNs
- Physician time: Regular evaluation, procedures

Minor (8 patients) - Fast track
- Requirement: 1 RN per 4–5 patients = 2 RNs
- Physician time: Limited, basic evaluation

Support staff:
- Technicians: 1 tech per 4–5 patients = 4 techs (charge + 3)
- Unit clerk: 1 per 10 patients = 2

STAFFING SUMMARY:
| Role | Needed | Available | Shortfall | Call-In |
|------|--------|-----------|-----------|---------|
| Physician | 2 | 2 | 0 | None |
| RN | 7–8 | 8 | 0 | None |
| Technician | 4 | 3 | 1 | 1 tech |
| Unit Clerk | 2 | 0 | 2 | 2 clerks |
| Trauma Surgeon | On standby | 0 | 1 | Call trauma surgeon |

SUPPLY CALCULATION:

IV Lines & Access:
- Immediate: 2 patients × 2.5 lines = 5 lines
- Delayed: 8 patients × 1.5 lines = 12 lines
- Minor: 8 patients × 0.3 lines = 2.4 lines
- Total: 19.4 IV lines (order 24 with backup)
- IV catheters: 24 catheters (mix of 18–20 G)

IV Fluids:
- Immediate: 2 × 2 L = 4 L
- Delayed: 8 × 1 L = 8 L
- Minor: 8 × 0.3 L = 2.4 L
- Total: 14.4 L crystalloid (order 20 L = 4 × 5L bags)

Medications:
- Analgesics (60% of 18): 11 doses (morphine, fentanyl)
- Antiemetics (40%): 7 doses
- Antibiotics (ESI-2+, ~10 patients): 10 doses
- Sedatives (immediate care): 3 doses
- Other: estimate +20%

Dressings & Supplies:
- Immediate: 2 × 75 units = 150 units
- Delayed: 8 × 30 units = 240 units
- Minor: 8 × 10 units = 80 units
- Total: 470 units (order 500 with backup)

Blood Products (if anticipated):
- Estimated need: O-negative whole blood (2–4 units on standby)
- Type-specific if time permits: Crossmatched units for known injuries

SUPPLY SUMMARY:
✓ IV catheters: 24 units
✓ IV fluids (LR/NS): 20 L
✓ Dressings: 500 units
✓ Medications: As calculated above
✓ Blood: 2–4 units O-neg on standby
✓ Other: Airway supplies, monitors, medications, consumables

TRANSPORT CALCULATION:

Patient Distribution Over Time:
- First 15 min: 3 patients arrive
- 15–30 min: 5 patients arrive
- 30–45 min: 6 patients arrive
- 45–60 min: 4 patients arrive
- Total: 18 patients over ~50 minutes

Transport Requirements:
- Scene location: Highway 101, ~20 min transport time
- Receiving facility: City Hospital (baseline), Regional Trauma Center (as needed)
- Ambulances needed:
  - 4–5 ambulances to handle 18 patients (1–2 patients per rig per hour)
  - Average turnaround: 30 min (15 min transport each way)
  - Peak load: 6 patients in 15 minutes requires 3 rigs available
  
TRANSPORT SUMMARY:
✓ Ambulances: 5 (4 primary, 1 backup)
✓ Paramedic crews: 10 paramedics (2 per rig)
✓ Transport Supervisor: 1
✓ Alternative transport: If ambulance shortage, request mutual aid from neighboring EMS
✓ Receiving facility coordination: Notify Regional Trauma Center, secondary hospitals for Delayed/Minor patients

RESOURCE SUMMARY TABLE:
| Category | Resource | Quantity | Status | Notes |
|----------|----------|----------|--------|-------|
| Staffing | Physicians | 2 | OK | Trauma surgeon on standby |
| | RNs | 8 | OK | May need per-diem from pool |
| | Technicians | 4 | CALL 1 | Currently have 3 |
| | Clerks | 2 | CALL 2 | Need for triage/documentation |
| Supplies | IV catheters | 24 | CHECK | Verify stock |
| | IV fluids | 20 L | CHECK | Request additional 10 L |
| | Dressings | 500 | CHECK | Request restock if low |
| | Medications | Per calc | CHECK | Verify critical meds stock |
| | Blood | 2–4 units | STANDBY | O-neg on emergency hold |
| Transport | Ambulances | 5 | Coordinate | EMS mutual aid if needed |
| | Personnel | 10 + supervision | Coordinate | Per EMS call-out protocol |

ACTIVATION TIMELINE:
✓ T+0: Incident call received (2:38 PM)
✓ T+5: Hospital notified, surge protocol activated
✓ T+8: ED prepares triage area, surge staffing notified
✓ T+22: First patient arrives, triage begins
✓ T+55: All 18 patients have arrived and been triaged
✓ T+90: Initial treatment/stabilization complete, disposition planning

RECOMMENDATIONS:
1. Activate surge protocol Phase 1 immediately (have capacity)
2. Call in 1 additional tech and 2 unit clerks within 15 minutes
3. Alert trauma surgeon; prepare OR standby
4. Request additional dressing supplies (current stock may be insufficient)
5. Coordinate with Regional Trauma Center for potential ICU admits
6. Brief all staff on incident and resource allocation plan
7. Monitor resource consumption in real-time; escalate if needed
```

## Advanced Calculation Options

### Staffing by Skill Level
- **Attending Physicians:** For critical cases
- **Resident/Fellow:** For moderate acuity
- **Nurse Practitioner/PA:** For ESI-3 and some ESI-2
- **Registered Nurse:** Core staffing
- **Licensed Vocational Nurse:** Support for stable patients
- **Medical Technicians:** Blood draws, ECGs, vital signs
- **Patient Care Assistants:** Patient transport, positioning

### Supply Reorder Point Analysis
When does current supply run low?
- Calculate consumption rate (units per patient)
- Estimate when current stock depleted
- Trigger reorder at 80% consumption (leave 20% buffer)

### Cost Analysis (Optional)
- Staffing cost: Hours × rate
- Supply cost: Units × unit cost
- Transport cost: Per-call, per-mile, fuel
- Total estimated cost for incident response

### Multi-Facility Coordination
If surge exceeds single facility capacity:
- Calculate resource gap (patients exceeding capacity)
- Identify receiving hospitals with available capacity
- Calculate transport requirements for patient diversion
- Coordinate mutual aid and resource sharing

## Output

I'll provide:
1. **Staffing requirements:** By role and acuity level
2. **Supply calculations:** Specific quantities for all materials
3. **Transport plan:** Ambulance needs and coordination
4. **Resource availability:** Compare needs vs. current availability
5. **Activation recommendation:** Surge protocol phase and timing
6. **Action checklist:** Specific steps to activate and execute
7. **Cost estimate:** Optional, if budget important

---

**Last Updated:** 2026-04-01
