# /triage-sim — Mass Casualty Triage Simulation

## Purpose
Run a realistic mass casualty incident (MCI) simulation with your facility's protocols, patient acuity distribution, and resource constraints. Provides performance feedback and training.

## When to Use
- Staff triage protocol training and competency assessment
- Emergency preparedness drill planning
- Evaluate surge capacity and resource adequacy
- Conduct after-action review on simulated vs. realistic scenarios

## Duration
30–120 minutes depending on simulation scale

## Simulation Parameters

I'll ask you to specify or I can use defaults:

### 1. Scenario Type
- **Vehicle collision** (multi-vehicle crash, highway incident)
- **Building collapse** (structural failure, earthquake aftermath)
- **Transportation** (plane crash, train derailment, bus collision)
- **Weather event** (flood, tornado, extreme heat)
- **Workplace incident** (explosion, fire, chemical exposure)
- **Mass gathering** (crowd crush, explosion at event)
- **Custom:** Describe your scenario

### 2. Patient Volume & Acuity
- Total expected patients (10–1,000+)
- Acuity distribution (e.g., 30% Immediate, 50% Delayed, 20% Minor)
- Pediatric percentage (if any children involved)
- Age distribution details

### 3. Protocol & Assessment Method
- Which triage protocol? (START, JumpSTART, SALT, ESI)
- Single vs. multiple rounds of triage assessment
- Include interventions? (SALT includes airway positioning, hemorrhage control)

### 4. Facility Resources
- Available triage officers and staff
- Equipment available (triage tags, assessment tools, supplies)
- Treatment/transport limitations
- Surge capacity constraints

### 5. Simulation Tempo
- **Fast-track:** 5–10 minute simulation (abbreviated scenario)
- **Realistic:** 30–60 minute simulation (full patient flow)
- **Extended:** 60–120+ minute simulation (prolonged incident with updates)

## How Simulation Works

1. **Scenario Briefing:** I present the incident (type, location, initial report, estimated casualties)

2. **Triage Setup:** You designate triage location, personnel, and begin assessment

3. **Patient Stream:** Patients arrive in waves
   - I present patient data: Age, mechanism of injury, vital signs (RR, HR, BP, mental status)
   - You apply your chosen protocol (START, SALT, etc.)
   - You categorize: Immediate (Red), Delayed (Yellow), Minor (Green), Expectant (Black)
   - I provide feedback on accuracy

4. **Real-Time Challenges:** 
   - Surge updates: "More patients arriving than expected"
   - Resource constraints: "Transport is overwhelmed, only 2 ambulances available"
   - Decision points: "Do you escalate surge protocol? Restrict admissions?"

5. **Progress Tracking:**
   - Patient count by category
   - Triage timing (seconds per patient)
   - Resource utilization
   - Bottleneck identification

6. **Outcome Summary:**
   - Total patients triaged
   - Triage accuracy (% correct categorization)
   - Performance metrics (timing, resource use, decisions)
   - Areas of excellence and improvement

## Example Simulation Flow

```
BRIEFING:
You: "I'm ready to start a triage simulation."
Me: "Vehicle collision on Highway 101, 2 PM. Fire reports 15-20 patients with 
     multiple injuries. ETA: 15 minutes. Your ED is at 60% capacity. How do you 
     prepare your triage area?"

SETUP:
You: "I'll activate the ED triage area in the waiting room, station 2 nurses 
      and a tech to perform rapid assessment."
Me: "Good. Your triage area is set. First patient arriving now."

PATIENT 1:
Me: "Patient A: 35-year-old driver, unresponsive, respirations appear labored 
     at 8 breaths/min, radial pulse present but weak, passenger reports loss 
     of consciousness at scene."
You: "Per START protocol: Check respiration first. RR 8 = Immediate (Red). 
      Also altered mental status, so Immediate. Assign to treatment area."
Me: "Correct per START. Patient A triaged as Immediate (Red). ✓ 
     Next patient arriving..."

[Continue with subsequent patients...]

SURGE UPDATE:
Me: "At 20-minute mark: You've triaged 8 patients so far, 50% Immediate. 
     Fire reports 5 more patients still at scene, ETA 10 minutes. Your 
     treatment areas are filling up. Your ED is now at 80% capacity. 
     Do you escalate surge protocol?"
You: "Yes, activate Phase 1 surge. Call in additional nursing staff, 
      open the observation unit for Delayed patients."
Me: "Good decision. Phase 1 activated at 20 minutes. Continue triage..."

[Simulation concludes when all patients triaged or time limit reached]

SUMMARY:
Me: "Simulation complete. You triaged 18 patients in 35 minutes. 
     Triage accuracy: 16/18 correct (89%). 
     Distribution: 9 Immediate (50%), 7 Delayed (39%), 2 Minor (11%), 0 Expectant.
     Average triage time: 1.9 min/patient.
     Key learning: Two patient misclassifications—both had altered mental 
     status that was initially missed. What would you do differently?"
```

## Feedback & Scoring

**Triage Accuracy:** Percentage of correct categorizations
- Target: 90%+ accuracy for protocol mastery
- 80–89%: Good; some edge cases need review
- 70–79%: Room for improvement; protocol refresher recommended
- < 70%: Significant gaps; remedial training needed

**Timing:** Average seconds per patient assessment
- START/JumpSTART target: 60 seconds per patient (±10%)
- SALT target: 90–120 seconds per patient (includes interventions)
- Faster = more efficient; ensure accuracy isn't sacrificed

**Resource Utilization:**
- Did you escalate surge appropriately?
- Were staff and equipment deployed efficiently?
- Any critical bottlenecks identified?

**Decision Quality:**
- Escalation decisions appropriate and timely?
- Communication to team clear?
- Alternative approaches considered?

## After Simulation Debrief

I'll facilitate discussion:

1. **What Went Well:** Celebrate successes (e.g., rapid triage, accurate protocol application)
2. **Gaps Identified:** Review misclassifications or timing issues
3. **Protocol Review:** If errors found, revisit specific algorithm steps
4. **Recommended Actions:** Remedial training, protocol refresher, process changes

## Advanced Options

### Multi-Participant Simulation
- Multiple triage officers competing on accuracy/speed
- Allows comparison of individual performance
- Team debriefing identifies communication or coordination gaps

### Scenario Variation
- Same patient volume with different acuity distribution
- Tests flexibility and decision-making under varying conditions
- Assesses over-triage vs. under-triage tendencies

### Integration with Facility Surge Data
- Use your facility's historical acuity distribution
- Simulate realistic patient mix for your ED
- Validate forecasting models against actual performance

## Output & Documentation

After simulation:
- I provide summary report (accuracy, timing, resource use)
- Recommend logging exercise in `work-log/session-log.md`
- Identify competency gaps or areas for improvement
- Suggest follow-up actions (remedial training, protocol changes, equipment procurement)

---

**Last Updated:** 2026-04-01
