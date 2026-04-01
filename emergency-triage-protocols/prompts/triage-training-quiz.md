# Triage Training Quiz Generator Prompt

## Purpose
Generate interactive triage training quizzes with patient scenarios, questions, answer keys, and feedback. Supports competency assessment and protocol training.

## Use in Claude Prompt

When you need a training quiz, use this prompt:

```
Generate a triage training quiz with the following specifications:

PROTOCOL: [START / JumpSTART / SALT / ESI / combination]
DIFFICULTY: [Beginner / Intermediate / Advanced]
QUESTION_COUNT: [5 / 10 / 20 questions]
SCENARIO_TYPE: [Multiple choice / Case study / Step-by-step decision tree / Mixed]
FOCUS_AREA: [Mental status assessment / Perfusion evaluation / General protocol / Edge cases / Pediatric considerations / All]

CONTENT:
- Each question should present a realistic patient scenario
- Include vital signs (RR, HR, BP, CRT, mental status) as applicable
- Provide mechanism of injury and chief complaint
- For each question, provide:
  1. Patient scenario (2–3 sentences)
  2. Vital signs/assessment findings
  3. Multiple choice options (4 options, labeled A–D)
  4. Correct answer with full explanation
  5. Common mistakes / misconceptions
  6. Protocol citations (algorithm step reference)

FORMAT: [Interactive quiz / PDF / Text document]
ANSWER_KEY: [Included / Separate document]
FEEDBACK_LEVEL: [Basic / Detailed with learning points]
TARGET_AUDIENCE: [ED nurses / Physicians / Paramedics / Mixed team / Trainees]

Generate quiz in educational format suitable for staff competency assessment.
```

## Example Quiz Structure

### START Triage Protocol Quiz — Intermediate Level (10 Questions)

---

**QUESTION 1: Respiratory Assessment**

**Scenario:**
45-year-old male, motor vehicle collision, unresponsiveness reported by bystanders. You approach to assess. Patient does not respond to verbal stimuli but opens eyes to painful stimuli and appears to be breathing, though respirations appear shallow.

**Vital Signs / Assessment:**
- Respiratory rate: Shallow, difficult to count but appears <10 breaths/min
- Heart rate: 120 bpm (palpable at radial artery)
- Blood pressure: Palpable systolic at wrist (~90 mmHg estimated)
- Mental status: Eyes open to pain only, not following commands

**Question:**
Per START triage, what is the appropriate triage category for this patient?

A) Delayed (Yellow) — stable respiratory rate, alert
B) Immediate (Red) — respiratory rate <10, abnormal vital signs
C) Minor (Green) — patient is breathing, appears stable
D) Expectant (Black) — unresponsive, poor prognosis

**CORRECT ANSWER: B) Immediate (Red)**

**Explanation:**
Per START Step 1 (Respiration Assessment), any respiratory rate <10 or >30 breaths/min = Immediate category. This patient's respiratory rate is shallow and <10, which immediately designates them as Immediate (Red), regardless of other findings. The abnormal mental status (not following commands) would also be an Immediate finding per Step 3, providing additional confirmation.

**Protocol Citation:** START Algorithm, Step 1: "Respirations <10 or >30 = Immediate (Red)"

**Common Mistakes:**
- Assuming "patient is breathing" automatically = stable (NOT true; need to count respiratory rate)
- Focusing on other abnormalities instead of following START sequence (should assess respiration FIRST)
- Underestimating severity of shallow respirations (shallow breathing may indicate deterioration, not stability)

**Learning Point:**
START is a sequential algorithm: Respiration → Perfusion → Mental Status. A single abnormal finding in Respiration immediately categorizes patient as Immediate; no need to continue to other steps (though you can confirm).

---

**QUESTION 2: Perfusion Assessment (Capillary Refill)**

**Scenario:**
8-year-old child trapped in vehicle for 10 minutes, extricated and brought to triage. Small lacerations on forehead and left arm, blood soaked into clothing from arm wound. You're applying JumpSTART protocol.

**Vital Signs / Assessment:**
- Respiratory rate: 20 breaths/min (normal for age 8)
- Brachial pulse: Palpable, but pulse rate 138 bpm
- Capillary refill: >2 seconds on sternum
- Mental status: Crying, responding to caregivers' voices, age-appropriate behavior after calming

**Question:**
Per JumpSTART, what is the appropriate triage category for this child?

A) Delayed (Yellow) — respiratory rate normal, child responding to voice
B) Immediate (Red) — prolonged capillary refill indicates poor perfusion / shock
C) Minor (Green) — child is crying and responding, alert
D) Expectant (Black) — excessive blood loss, non-salvageable

**CORRECT ANSWER: B) Immediate (Red)**

**Explanation:**
Per JumpSTART Step 2 (Perfusion Assessment), abnormal perfusion = Immediate. This child has:
- Prolonged capillary refill (>2 seconds) indicating poor perfusion
- Tachycardia (HR 138 for age 8; normal ~80–100) suggesting shock compensation
- Significant blood loss (blood-soaked clothing)

These signs indicate hypovolemic shock (hemorrhagic shock) from blood loss, warranting Immediate category for rapid fluid resuscitation and hemorrhage control.

**Protocol Citation:** JumpSTART Algorithm, Step 2: "Absent/weak pulse OR prolonged capillary refill = Immediate (Red)"

**Common Mistakes:**
- Assuming "normal respiratory rate" + "responding appropriately" = Delayed (Incorrect; perfusion abnormality overrides)
- Not recognizing that tachycardia + delayed CRT = shock signs requiring Immediate categorization
- Underestimating danger of blood loss in small child (children compensate well until abrupt decompensation)

**Learning Point:**
Perfusion assessment is critical in pediatrics. Shock compensation allows children to maintain mental status even when significantly blood-lost. Tachycardia + delayed CRT = RED FLAG for shock, even in alert child.

---

**QUESTION 3: Mental Status Assessment (START Step 3)**

**Scenario:**
32-year-old female, building collapse scenario, buried under rubble for 45 minutes. Extricated with leg fracture and minor lacerations. Respirations 24, radial pulse present with normal capillary refill. When you ask her to "open your eyes," "squeeze my hand," she does not respond to these commands.

**Vital Signs / Assessment:**
- Respiratory rate: 24 breaths/min
- Radial pulse: Strong, rate 98 bpm
- Capillary refill: <2 seconds
- Mental status: Does NOT follow commands (does not open eyes, does not squeeze hand when asked)

**Question:**
Per START protocol, what is the appropriate triage category?

A) Delayed (Yellow) — respirations and perfusion are normal
B) Immediate (Red) — inability to follow simple commands indicates altered mental status / Immediate
C) Minor (Green) — no critical vital sign abnormalities besides leg fracture
D) Expectant (Black) — buried for 45 minutes, likely severe internal injuries

**CORRECT ANSWER: B) Immediate (Red)**

**Explanation:**
Per START Step 3 (Mental Status Assessment): "Able to follow commands = Delayed; Unable to follow commands = Immediate."

This patient cannot follow simple commands (open eyes, squeeze hand), which per START = Immediate category. This could indicate:
- Neurological injury (head trauma, intracranial bleed)
- Hypoxia (during entrapment or now)
- Shock (hypovolemic from internal bleeding)
- Altered consciousness from sedation, blood loss, or trauma

Any inability to follow commands = Immediate category, regardless of other vital signs.

**Protocol Citation:** START Algorithm, Step 3: "Unable to follow commands = Immediate (Red)"

**Common Mistakes:**
- Assuming normal respiratory rate + normal perfusion = Delayed (Incorrect; any abnormal finding = abnormal category)
- Confusing "unresponsive" with "unconscious" (patient may respond to pain or commands, or neither)
- Underestimating mental status findings (altered mental status is a critical sign requiring immediate intervention)
- Assuming entrapment duration predicts final outcome (prognosis uncertain; triage for salvageability, not expected outcome)

**Learning Point:**
START Step 3 is the discriminator for many patients. If respiration and perfusion are normal but mental status abnormal = Immediate. Mental status abnormality signals potential neurological or systemic compromise.

---

## Quiz Answer Key Format

**Complete Answer Key for Training Quiz:**

| Q# | Patient | Correct Answer | Rationale | Protocol Step | Common Error |
|----|---------|---|-----------|--------------|------|
| 1 | 45M MVC, RR<10 | Immediate (Red) | RR <10 = Immediate Step 1 | START Step 1 | Assuming "breathing" = stable |
| 2 | 8F child, CRT>2 | Immediate (Red) | CRT >2 = abnormal perfusion | JumpSTART Step 2 | Missing shock signs |
| 3 | 32F collapse, no command follow | Immediate (Red) | Cannot follow commands = Immediate | START Step 3 | Ignoring mental status |
| ... | ... | ... | ... | ... | ... |

## Competency Scoring

**Score Interpretation:**
- **90–100%:** Advanced competency — Protocol mastery demonstrated
- **80–89%:** Proficient competency — Adequate protocol knowledge; minor gaps
- **70–79%:** Developing competency — Needs protocol review before independent triage
- **60–69%:** Below competency — Requires remedial training and reassessment
- **<60%:** Insufficient competency — Cannot perform triage without supervision; mandatory retraining

**Remedial Training Recommendations:**
- Scores 70–79%: Protocol quick-reference review + self-study
- Scores 60–69%: Focused training on missed question areas + supervised practice
- Scores <60%: Comprehensive protocol retraining + competency reassessment before return to triage duty

---

**Last Updated:** 2026-04-01
