# /diagnose — Problem Diagnosis

Systematically diagnose mechanical and electrical issues using symptoms, OBD codes, and observed behavior.

---

## When to Use This Command
- Check engine light is on
- The car is behaving unexpectedly (rough idle, misfires, power loss, unusual noise)
- After a tune change that introduced a problem
- When you have a list of OBD fault codes and want interpretation
- Pre-purchase inspection research for known platform issues

---

## What to Tell Me

Provide as much of the following as you can:

1. **Symptoms:** What is the car doing? (be specific — e.g., "misfire at idle that goes away above 2000 RPM," not just "runs rough")
2. **When it occurs:** Cold start / warm idle / WOT / specific RPM range / constant
3. **Fault codes:** List any OBD codes with freeze frame data if available
4. **Recent changes:** Any mods, tune changes, or maintenance done recently?
5. **When it started:** Did this just appear or has it been building gradually?
6. **Any unusual readings:** AFR, boost, coolant temp anomalies visible in logs or gauges
7. **Sounds or smells:** Knocking, ticking, hissing, burning smell, fuel smell, exhaust smell
8. **Any fluids:** Oil consumption, coolant loss, water in oil

---

## Diagnosis Process

1. **Interpret fault codes** — explain what each code means, likely triggers, and false-positive risks
2. **Build a differential diagnosis list** ranked by probability
3. **Suggest diagnostic tests** in order (cheapest/easiest first):
   - Live OBD data checks
   - Visual inspection points
   - Specific tests (compression, leak-down, fuel pressure, vacuum test)
   - Software checks (review datalogs, check for tune anomalies)
4. **Cross-reference known platform issues** for your specific engine/ECU
5. **Safety assessment** — is it safe to drive while investigating, or should it be parked?

---

## Output Format

**Summary of Symptoms:**
[Brief restatement of what you described]

**Fault Codes Interpreted:**
| Code | Description | Common Cause on Your Platform |
|------|-------------|-------------------------------|

**Differential Diagnosis (Most to Least Likely):**
1. [Most likely cause] — [Reasoning]
2. [Second possibility] — [Reasoning]
3. [Less likely but worth ruling out] — [Reasoning]

**Recommended Diagnostic Sequence:**
1. [Cheapest/easiest check first]
2. [Next check]
3. ...

**Safe to Drive?** [Yes / Limited / No — with reasoning]

**Red Flags to Watch For:**
[Any symptoms that would escalate urgency]

---

## Common Platform Fault Code Reference

For platforms with known issues, I'll cross-reference your codes against:
- Subaru (EJ/FA): common cam/crank sensor, AVCS, boost codes, coolant temp sensor issues
- Mitsubishi (4G63/4B11): boost codes, cam position sensor, MAP sensor failures
- Honda K/B: VTEC codes, cam sensor, idle relearn requirements
- GM LS: common MAF, O2, and cam sensor issues
- Nissan RB/SR: AFM/MAF sensitivity, CAS issues, boost codes
- Ford EcoBoost: carbon buildup symptoms, charge pipe failures, HPFP codes

---

## Escalation Protocol

If any of the following appear in symptoms, flag immediately as HIGH PRIORITY before continuing:
- **Knocking / pinging noises** — potential detonation → do not drive under load
- **White smoke from exhaust** — possible head gasket → stop driving, check coolant and oil
- **Oil or water in intake / intercooler** — possible ring failure or HG leak
- **Sudden power loss + lean code** → do not make WOT pulls until resolved
- **Fuel smell in cabin** → park immediately, fire risk
