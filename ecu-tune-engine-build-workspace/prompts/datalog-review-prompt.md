# Prompt Template: Datalog Review Request

Use this template when asking Claude to review a datalog. Fill in the bracketed sections before submitting.

---

## Template

```
I need help reviewing a datalog from [DATE]. Here's the context:

**Vehicle:** [Year Make Model — from project.md]
**Fuel used:** [Octane and ethanol content]
**Type of run:** [WOT pull / street drive / dyno session / cold start]
**Conditions:** [Ambient temp, IAT at pull start if known]
**Any observations during the run:** [What you felt, heard, or noticed]
**Specific concern (if any):** [What you're worried about]

Here is the datalog data:
[PASTE CSV OR DESCRIBE KEY VALUES]

Key channels I have logged:
- RPM: [yes/no]
- TPS: [yes/no]
- MAP/Boost: [yes/no]
- AFR/Lambda (wideband): [yes/no]
- Knock/Knock Retard: [yes/no]
- Coolant Temp: [yes/no]
- IAT: [yes/no]
- Injector Duty: [yes/no]
- Other: [list]

Please review for safety issues first, then give me a full assessment.
```

---

## Quick Version (Minimal Context)

```
Review my datalog from today's pull. [VEHICLE from context]. Running [FUEL].
Key values: peak boost [X]psi, AFR held at [X.X], saw [X] counts knock retard
at approximately [XRPM]. Full WOT pull in [GEAR], [XRPM] to [XRPM].
Flag anything concerning and give me recommended actions.
```

---

## When to Include Full CSV

Always paste full CSV data when:
- You observed any knock events
- You're seeing a power loss or AFR anomaly
- This is the first pull on a new tune or new part
- You want an accurate peak/min/average analysis
