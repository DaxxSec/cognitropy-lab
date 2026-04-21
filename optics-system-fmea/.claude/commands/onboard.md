---
name: onboard
description: Initialize the optics-system-fmea workspace by interviewing the user and populating context/ files.
---

# /onboard — Optics System FMEA Workspace Initialization

You are starting a new project in the optics-system-fmea workspace. Walk the user through a structured interview and populate these files:

- `context/role.md`
- `context/project.md`
- `context/constraints.md`
- `context/for-agent/environment.md`

## Interview Script

### Part 1 — About the User
1. What is your background (optical engineer, physicist, EE, hobbyist, student)?
2. What's your comfort level with: paraxial math, aberration theory, tolerancing, FMEA?
3. Is this for research, product, teaching, or a personal build?

### Part 2 — The System
4. In one sentence, what does this system do?
5. System type: imaging / illumination / spectrometer / laser / fiber / metrology / other?
6. Waveband (nm or µm)?
7. Field of view? (full angle, degrees, or linear)
8. f/# or NA?
9. What's the detector (pixel pitch, format, QE) OR source (power, etendue)?
10. What's the **environment** (temp range, vibration spec, shock, humidity)?
11. Size/mass/cost envelope?

### Part 3 — Standards & Safety
12. Does this fall under any of: ISO 10110, MIL-STD, IEC 60825 (lasers), IEC 60601 (medical), FDA, ITAR/EAR, AS9100?
13. If laser: what class are you targeting, and is there eye/skin exposure potential?

### Part 4 — Tooling
14. What optical design software do you have (Zemax, Code V, FRED, OSLO, LightTools, none)?
15. Python libraries you can run?
16. Any existing design files or a starting prescription?

### Part 5 — Deliverables
17. What does "done" look like? (design review deck, FMEA worksheet, prescription file, all of above)
18. Deadline?

## After the Interview

1. Fill out all four context files with the gathered information. Use tables where the template provides them.
2. Write a **project kickoff entry** to `work-log/YYYY-MM-DD.md`.
3. Create `planning/plan.md` with a three-phase outline: (1) first-order design, (2) FMEA, (3) tolerance + stray light + thermal review.
4. Summarize what you learned back to the user in <10 bullets and propose the next command to run.

## Output Style
- Ask ONE question at a time. Do not dump the whole interview at once.
- When the user gives a vague answer, probe once for a number or unit.
- If the user is a novice, offer defaults (e.g., "most visible imagers use f/2.8 — sound OK?").
