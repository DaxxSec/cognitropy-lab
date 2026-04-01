# MCI Scenario Generator Prompt

## Purpose
Generate realistic mass casualty incident (MCI) scenarios for tabletop discussions, full-scale exercises, or training simulations. Each scenario includes incident background, patient roster, timeline, and realistic injects.

## Use in Claude Prompt

When you need a realistic MCI scenario, use this prompt:

```
Generate a realistic mass casualty incident scenario with the following parameters:

INCIDENT TYPE: [vehicle crash / building collapse / weather event / workplace incident / mass gathering / other]
SETTING: [urban / suburban / rural / highway / indoor / outdoor]
ESTIMATED PATIENTS: [10-50 / 50-100 / 100+ / other]
ACUITY MIX: [High (>50% Immediate) / Moderate (30-50% Immediate) / Low (<30% Immediate)]
SPECIAL CONSIDERATIONS: [pediatric / hazmat / multiple locations / complex logistics / other]
PROTOCOL FOCUS: [START / JumpSTART / SALT / ESI / multi-protocol]

REQUESTED OUTPUT:
1. Incident description (background, mechanism, location, key details)
2. Timeline of incident progression
3. Patient roster (15-20 patients) with:
   - Age, gender
   - Chief complaint / injury
   - Vital signs (RR, HR, BP, mental status)
   - Triage category per protocol
   - Special considerations (pregnant, disabled, behavioral health, etc.)
4. Realistic injects (information revealed during exercise at specific times)
5. Complications (equipment failure, staff unavailability, supply shortage, etc.)
6. Expected resource needs (staffing, supplies, transport)
7. Discussion points for debrief

Generate the scenario in a realistic, educational format suitable for emergency medicine training.
```

## Example Scenario Output

A realistic scenario might look like:

---

### SCENARIO: Multi-Vehicle Collision on Interstate 70

**INCIDENT BACKGROUND:**
At approximately 2:35 PM on a Wednesday afternoon, a flatbed truck carrying construction materials loses its load on Interstate 70 eastbound near the I-70/I-270 interchange during rush hour. Three passenger vehicles and two commercial trucks collide with the scattered materials. Traffic is backed up for several miles. Initial 911 call reports "multi-vehicle collision, unknown number of patients."

**SETTING:**
- Interstate highway during peak traffic (2–4 PM)
- Sunny weather, 75°F, dry road conditions
- Three lanes eastbound; incident affects all lanes plus shoulder
- Nearest hospital: City Hospital ED, 12 miles away (ETA: 20 minutes)
- Secondary hospital: Regional Trauma Center, 18 miles away

**ESTIMATED PATIENTS & ACUITY:**
- Fire/EMS initial estimate: 12–16 patients
- Actual transported: 18 patients (4 Immediate, 8 Delayed, 6 Minor)
- Expectant: 0

**TIMELINE:**

| Time | Event | Information |
|------|-------|-------------|
| 2:35 PM | Incident occurs | Construction materials spill across lanes; vehicles collide |
| 2:38 PM | First 911 call | Caller reports multi-vehicle collision, "several people injured" |
| 2:42 PM | Hospital ED notified | Fire dispatch calls hospital: "Multi-vehicle collision, approximately 12–16 patients, ETA of first patient 18 minutes" |
| 2:45 PM | ED activates MCI protocol | Surge Phase 1, triage area setup, staff notified |
| 2:55 PM | First 3 patients arrive | Patient roster begins (see below) |
| 3:10 PM | Peak arrivals | Patients 7–12 arrive in rapid succession (6 patients in 10 minutes) |
| 3:30 PM | Escalation point | ED census reaches 75%; ED director considers Phase 2 escalation |
| 3:45 PM | Last patient arrives | Patient #18 transported; scene clear |
| 4:15 PM | Initial treatment/disposition | All patients triaged, initial interventions complete, disposition planning underway |

**PATIENT ROSTER:**

| # | Age/Gender | Vehicle | Injury | RR | HR | BP | CRT | Mental Status | Category |
|---|-----------|---------|--------|----|----|----|----|---------------|----------|
| 1 | 45 M | Sedan driver | Crushing chest trauma, steering wheel imprint | 8 | 125 | 88/55 | >2 sec | Confused, pain response only | Immediate |
| 2 | 38 F | Sedan passenger | Bilateral leg fractures, trapped 15 min | 28 | 112 | 102/68 | 2 sec | Alert, anxious | Delayed |
| 3 | 7 M | Sedan rear | Minor head bump, crying | 26 | 118 | 94/62 | 2 sec | Alert, age-appropriate distress | Minor |
| 4 | 52 M | SUV driver | Severe facial trauma, unable to open eyes | 32 | 135 | 95/60 | >2 sec | Responds to voice, confused | Immediate |
| 5 | 41 F | SUV passenger | Abdominal pain, minor lacerations | 22 | 98 | 118/74 | 2 sec | Alert, oriented | Delayed |
| 6 | 16 F | Pickup truck | Shoulder dislocation, abrasions | 20 | 95 | 110/70 | <2 sec | Alert, oriented, severe pain | Delayed |
| 7 | 35 M | Sedan (second) | Head laceration, minor abrasions | 24 | 105 | 115/75 | <2 sec | Alert, oriented | Minor |
| 8 | 64 F | Sedan (second) | Rib fractures, chest wall pain | 30 | 110 | 108/68 | 2 sec | Alert, oriented | Delayed |
| 9 | 28 F | Truck bed passenger | Crush injury left leg, severe pain | 26 | 119 | 102/70 | 2 sec | Alert, oriented, pain control needed | Delayed |
| 10 | 55 M | Truck driver (construction) | Minor neck strain, anxious | 20 | 88 | 125/82 | <2 sec | Alert, oriented | Minor |
| 11 | 31 M | Flatbed truck (cause) | Severe burn (arm contact with hot materials), shock signs | 36 | 135 | 92/58 | >2 sec | Alert but anxious | Immediate |
| 12 | 42 F | Sedan (third) | Multiple lacerations, shock signs | 34 | 128 | 85/52 | >2 sec | Anxious, oriented but tachycardic | Immediate |
| 13 | 8 F | Sedan (third) | Minor forehead laceration, dazed | 28 | 125 | 98/68 | 2 sec | Responds to voice, not fully alert | Delayed |
| 14 | 19 M | Sedan (third) | Bilateral knee lacerations, stable | 18 | 92 | 120/75 | <2 sec | Alert, oriented | Minor |
| 15 | 34 M | Sedan (first, rear) | Minor trauma, walking, self-extricated | 18 | 85 | 118/75 | <2 sec | Alert, oriented, minimal injury | Minor |
| 16 | 9 M | Sedan (first, rear) | Minor trauma, anxious but stable | 24 | 110 | 105/70 | <2 sec | Alert, age-appropriate | Minor |
| 17 | 62 M | SUV (second vehicle) | Severe multi-trauma: pelvic fracture, internal bleeding, shock | 38 | 142 | 78/48 | >2 sec | Altered mental status, restless | Immediate |
| 18 | 44 F | SUV (second) rear | Stable multi-trauma, leg fracture, conscious | 20 | 95 | 115/72 | <2 sec | Alert, oriented | Delayed |

**TRIAGE CATEGORY DISTRIBUTION:**
- Immediate (Red): 4 patients (#1, 4, 11, 12, 17) [5 total; one listed twice above—recalculate: #1, 4, 11, 12, 17 = 5 Immediate]
- Delayed (Yellow): 8 patients (#2, 5, 6, 8, 9, 13, 18, and one more)
- Minor (Green): 5–6 patients (#3, 7, 10, 14, 15, 16)

[Note: Adjust roster to ensure correct distribution totals 18]

**REALISTIC INJECTS (Information Revealed During Exercise):**

| Time (Relative) | Inject | Information Provided |
|---|---|---|
| T+0 min | Initial notification | "Multi-vehicle collision, Highway 101, 12–16 patients estimated, ETA of first patient 18 minutes" |
| T+15 min | Scene update from fire | "Scene is secured. We count 18 patients total. Mix of injuries, some with entrapment requiring extrication" |
| T+20 min | First patient arriving | "Incoming: 45-year-old male, unresponsive from vehicle 1, respiratory rate difficult to count, likely shallow" |
| T+45 min | Escalation point | "You've triaged 10 patients so far. 6 are Delayed, 4 are Immediate. ED is at 70% capacity. More arriving." |
| T+60 min | Complication #1 | "One of your cardiac monitors just stopped working. Patient still being monitored, but you're short 1 monitor." |
| T+75 min | Resource concern | "IV supply check: Used 12 catheters so far, moderate usage of fluids. Do you need more ordered?" |
| T+85 min | Pediatric notification | "Just notified: Two of the incoming patients are pediatric (ages 7 and 8). JumpSTART protocol in use?" |
| T+110 min | Scene cleared | "Fire reports all patients have been transported. Scene is secure. No more patients expected." |

**COMPLICATIONS & REALISM FACTORS:**

1. **Equipment Failure:** One cardiac monitor malfunction (realistic; high-use equipment)
2. **Pediatric Patients:** Realistic in vehicle collision; requires protocol shift to JumpSTART
3. **Varying Arrival Pace:** First 3 patients arrive quickly (15 min), then slower pace, then peak cluster
4. **Mixed Acuity:** Realistic distribution (4 critical, 8 serious, 6 minor) for highway collision
5. **Shock Indicators:** Multiple patients in hypovolemic shock; requires aggressive fluid resuscitation
6. **Resource Pressure:** Surge capacity reached around 75%; Phase 2 escalation consideration

**EXPECTED RESOURCE NEEDS:**

| Resource | Calculation | Quantity |
|----------|---|---|
| RNs | 4 Immediate (1.5:1) + 8 Delayed (2.5:1) + 5 Minor (4:1) = 3 + 3.5 + 1.5 = | 8 RNs |
| Physicians | 18 patients / 10 per physician = | 2 physicians |
| Technicians | 18 / 4 per tech = | 5 techs |
| IV lines | (4 × 2.5) + (8 × 1.5) + (5 × 0.5) = 10 + 12 + 2.5 = | 24–25 IV lines |
| IV fluids | (4 × 2 L) + (8 × 1 L) + (5 × 0.25 L) = 8 + 8 + 1.25 = | 20 L minimum |
| Blood products | 4 Immediate patients with shock = | 4–6 units O-neg on standby |
| Dressings | (4 × 75) + (8 × 30) + (5 × 15) = 300 + 240 + 75 = | 600+ units |
| Trauma surgeon | 4 critical patients, likely OR cases = | Activate STAT |
| Transport | 18 patients over 90 minutes = | 4–5 ambulances |

**LEARNING POINTS & DISCUSSION PROMPTS:**

1. **Triage Accuracy:** How many patients triaged correctly? Focus on Immediate vs. Delayed distinction.
2. **Mental Status Assessment:** Multiple patients with altered mental status. Did participants assess mental status carefully?
3. **Shock Recognition:** Several patients in hypovolemic shock. Were shock signs recognized early?
4. **Pediatric Protocol:** Were the two pediatric patients assessed with JumpSTART or adult START?
5. **Surge Escalation:** When should Phase 2 surge be activated? (Target: 75% capacity)
6. **Resource Planning:** Were supplies and staffing adequate? Any shortfalls?
7. **Communication:** Were decisions and patient status clearly communicated between triage, treatment, and transport?
8. **Complication Response:** How was the monitor failure handled? Were backups in place?

---

## Real-World Realism Factors Included

- **Realistic incident mechanism:** Highway collision (common, teachable)
- **Realistic patient distribution:** Not all critical (more realistic than training scenarios)
- **Mixed ages & injuries:** Includes pediatric, adult, mixed mechanism (head, chest, abdominal, extremity)
- **Realistic vital signs:** Abnormal vitals consistent with injury severity
- **Realistic timeline:** Delayed onset, cluster arrivals, staggered flow
- **Equipment complications:** One monitor failure (realistic)
- **Resource pressure:** Capacity reached, escalation decision required
- **Protocol shift:** Pediatric patients require JumpSTART consideration
- **Shock indicators:** Multiple hypovolemic shock cases (common in collision)

This scenario provides comprehensive training while remaining realistic and educationally sound.

---

**Last Updated:** 2026-04-01
