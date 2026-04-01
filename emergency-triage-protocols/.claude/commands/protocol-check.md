# /protocol-check — Triage Decision Validation

## Purpose
Validate a patient's triage categorization against START, JumpSTART, SALT, or ESI protocol criteria. Provides immediate feedback and protocol citations.

## When to Use
- Confirm triage category assignment during training
- Resolve uncertainty or disagreement about categorization
- Real-time decision support during exercises or drills
- Quality assurance review of documented triage decisions

## Duration
2–5 minutes per patient assessment

## Input Required

I'll ask you to provide:

### 1. Patient Presentation
- **Age:** (specify for JumpSTART vs. START distinction)
- **Mechanism of injury:** (e.g., motor vehicle collision, fall, blunt force)
- **Vital signs:**
  - Respiratory rate (breaths/min)
  - Heart rate (beats/min)
  - Blood pressure (systolic/diastolic)
  - Capillary refill time (seconds) if available
  - Temperature (if relevant)
- **Chief complaint / Injury:** (e.g., chest pain, crush injury to left leg, head trauma)
- **Mental status:** (alert, responds to voice, responds to pain, unresponsive; follows commands yes/no)
- **Other findings:** (e.g., visible bleeding, severe distress, shock signs)

### 2. Your Proposed Categorization
- Your triage category: Immediate (Red), Delayed (Yellow), Minor (Green), Expectant (Black)
- Your reasoning (brief)

### 3. Protocol Context
- Which protocol are you using? (START, JumpSTART, SALT, ESI, or facility-specific)
- Is this a mass casualty scenario (START/SALT) or ED surge (ESI)?
- Any facility-specific protocol variations to consider?

## How Protocol Check Works

1. **You describe the patient** with vital signs and presentation
2. **You state your proposed category** and how you arrived at it
3. **I apply the protocol step-by-step:**
   - For START: Walk through respiration → perfusion → mental status assessment
   - For JumpSTART: Apply pediatric-specific thresholds and behavioral assessment
   - For SALT: Sort phase → assess vital signs → consider interventions
   - For ESI: Walk through decision algorithm (immediate intervention? high-risk? resources needed?)
4. **I validate your decision:**
   - Correct? I confirm and provide protocol citation
   - Incorrect? I explain why, cite the correct algorithm step, and discuss the learning
5. **I provide alternatives:**
   - Edge cases? I discuss clinical considerations and any ambiguity in protocol
   - Protocol conflicts? I note where clinical judgment may override algorithm

## Example Protocol Checks

### START Protocol Example
```
You: "I have a patient: 45-year-old driver, respiratory rate 28, radial pulse 
      present, cap refill 2 seconds, alert and follows commands. Triage?"
Me: "Let's check using START protocol:
     STEP 1 - Respiration: RR 28 = normal (>10 and <30). Continue.
     STEP 2 - Perfusion: Radial pulse present + CRT 2 seconds = normal. Continue.
     STEP 3 - Mental Status: Alert, follows commands = normal.
     Per START: No abnormal findings = DELAYED (Yellow). ✓
     Citation: START Algorithm, Step 3 - patient with normal respiration, 
     perfusion, and mental status = Delayed category."
```

### JumpSTART Pediatric Example
```
You: "Child age 4, struck by car, respiratory rate 36, brachial pulse weak, 
      not responding to voice but cries to pain. Triage?"
Me: "Using JumpSTART (pediatric START, ages 1-8):
     STEP 1 - Respiration: RR 36 = normal for age 4 (thresholds: <15 or >40). 
     Continue.
     STEP 2 - Perfusion: Weak brachial pulse detected. Per JumpSTART, weak or 
     absent pulse = IMMEDIATE (Red). Stop.
     Citation: JumpSTART Algorithm - abnormal perfusion (weak pulse) = Immediate.
     Note: Even though RR is normal, abnormal perfusion takes priority."
```

### SALT Protocol Example
```
You: "Patient found lying down, not moving, respiratory rate 6. Triage?"
Me: "Using SALT protocol:
     PHASE 1 - Sort: Patient not ambulating, cannot walk. Assess individually.
     PHASE 2 - Assess: Respiration: RR 6 = CRITICAL. No breathing after airway 
     positioning attempt? Per SALT, no breathing after 10-second airway maneuver 
     = EXPECTANT (Black).
     If breathing improves with airway positioning, reassess: If RR now adequate 
     and other vital signs normal, may be DELAYED.
     Citation: SALT Algorithm, Phase 2 - no breathing after airway maneuver = 
     Expectant."
```

### ESI Protocol Example
```
You: "ED patient: chest pain, anxiety, blood pressure 160/95, heart rate 110. 
      Alert, oriented. Triage level?"
Me: "Using ESI algorithm:
     ESI-1 decision: Does patient require immediate life-saving intervention? 
     No (not intubating, hemodynamically unstable by vital signs alone but alert).
     ESI-2 decision: High-risk situation requiring immediate evaluation? 
     YES. Chest pain is high-risk regardless of vital signs; may be ACS. 
     Also abnormal vital signs (elevated BP, tachycardia).
     Per ESI: High-risk situation = ESI-2 (Emergent).
     Citation: ESI Algorithm - chest pain is a high-risk presenting problem 
     requiring immediate provider evaluation."
```

### Edge Case / Ambiguous Example
```
You: "Adult patient, respiratory rate 31, cap refill 2 seconds, alert but 
      confused. START triage?"
Me: "Let's analyze this carefully:
     STEP 1 - Respiration: RR 31 = ABNORMAL (>30). Per START, any RR <10 or >30 
     = IMMEDIATE (Red).
     At this point, the decision is IMMEDIATE regardless of other findings.
     However, let's note the other findings for completeness:
     - Altered mental status (confusion) also = IMMEDIATE by Step 3
     - Perfusion (CRT 2 sec) is normal
     
     Final: IMMEDIATE (Red) - clearly indicated by RR alone.
     
     Learning point: START algorithm goes top-to-bottom. First abnormal finding 
     determines category. No need to continue assessing if already determined 
     to be Immediate by respiration."
```

## When to Over-Triage vs. Under-Triage

**Safe Practice: When Uncertain, Over-Triage**

```
Rule: Patient Safety First

If you're uncertain about respiration rate:
  - Is it 28 or 30? → Treat as Immediate if unsure
  
If you're uncertain about mental status:
  - Is patient alert or confused? → If any doubt, assume altered = Immediate
  
If you're uncertain about mechanism/severity:
  - Could be Delayed or Immediate? → Assign Immediate initially; 
    can be reassessed if patient stable
  
Rationale: Over-triage (higher acuity) ensures patient gets rapid assessment. 
Under-triage (lower acuity) may delay critical care and worsen outcome.
```

## Common Protocol Misapplications & Corrections

### START Misapplication #1: Respiratory Rate Threshold
```
WRONG: "RR 30 = normal, continue to next step"
RIGHT: "RR 30 = ABNORMAL (threshold is <10 or >30, so 30 is the boundary). 
         RR ≥30 = IMMEDIATE. Stop here."
Lesson: RR of exactly 30 is abnormal per START; triage as Immediate.
```

### START Misapplication #2: All Walking Patients Green
```
WRONG: "Patient is walking, so automatically Minor (Green)"
RIGHT: "Patient walks, but still assess all three steps of START. 
         If walking but RR abnormal or perfusion poor = Immediate or Delayed."
Lesson: Walking doesn't mean Minor; must assess vital signs completely.
```

### JumpSTART Misapplication: Wrong Age Cutoff
```
WRONG: "10-year-old child, use JumpSTART"
RIGHT: "JumpSTART is for ages 1-8 ONLY. Age 10 = use adult START."
Lesson: Know age cutoffs precisely. Children 1-8 = JumpSTART. Age 9+ = START.
```

### ESI Misapplication: Forgetting High-Risk
```
WRONG: "Chest pain patient, normal vital signs, ESI-3"
RIGHT: "Chest pain = high-risk situation per ESI algorithm, ESI-2 
         (Emergent) regardless of vital sign stability."
Lesson: ESI-2 includes high-risk situations (chest pain, sepsis, unexplained 
        hypotension) even if vital signs appear stable.
```

## Advanced Considerations

### Conflicting Findings
When different vital signs point to different categories:
- Abnormal respiration + normal perfusion + normal mental status = Immediate (respiration abnormal takes priority)
- Normal respiration + weak perfusion + altered mental = Immediate (perfusion abnormal takes priority)
- All findings abnormal = Immediate (clearly)
- All findings normal = Delayed (or Minor if no injury mechanism)

### Interventions & Reassessment (SALT)
After lifesaving interventions:
- Airway positioning improves respiration? Reassess category (may downgrade)
- Hemorrhage control achieves hemostasis? Reassess (may downgrade)
- No improvement after intervention? Maintain assigned category

### Pediatric vs. Adult Differences
- Respiratory rate thresholds different (JumpSTART < START)
- Behavioral assessment more important in young children
- Capillary refill may be slower in cold environments (consider context)
- Pediatric shock signs more subtle than adult signs

## Output

After protocol check, I provide:
1. **Validation:** Your decision is correct or incorrect with explanation
2. **Protocol Citation:** Specific algorithm step(s) referenced
3. **Alternative Considerations:** Other valid approaches or edge cases
4. **Learning Point:** Key takeaway for future decisions
5. **Improvement Recommendation:** If errors found, suggest remedial review

## Using Protocol Check for Quality Assurance

You can use this command to:
- **Review past incidents:** Describe patient from incident report, check if triage was appropriate
- **Analyze misclassifications:** If error occurred, understand why using protocol
- **Resolve team disagreements:** Neutral protocol application settles ambiguous cases
- **Train new staff:** Use real or realistic patient examples to teach protocol

---

**Last Updated:** 2026-04-01
