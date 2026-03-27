# /onboard — Workspace Initialization

Welcome to the ECU Tune & Engine Build Workspace. This command walks you through setting up your personalized tuning environment.

---

## What This Command Does

This onboarding process will:
1. Gather your vehicle, engine, and ECU details
2. Capture your goals and experience level
3. Document your safety limits and constraints
4. Record your workshop and software environment
5. Populate all `context/` files so Claude can be your personalized tuning assistant

The entire interview takes about 10–15 minutes. You can skip sections and fill them in later.

---

## Onboarding Interview

Run through each section below. For each question, provide as much detail as you know — it's okay to say "unknown" or "TBD" for things you haven't determined yet.

---

### Section 1: Vehicle Identity

Ask the user:
1. What is the year, make, and model of the vehicle?
2. What is the chassis code (if known)?
3. What is the primary use for this vehicle? (Street / Track / Drag / Show / Daily)
4. What is the approximate current odometer reading?

Save to: `context/project.md` → Vehicle Details section

---

### Section 2: Engine & Build Configuration

Ask the user:
1. What is the engine code and displacement?
2. Is the block stock, sleeved, or a full aftermarket unit? Any internal work done?
3. What is the current compression ratio (if known)?
4. Are the rotating internals stock or forged? What brand/spec?
5. Any head work? (head gasket, porting, cams, valve springs)

Save to: `context/project.md` → Engine Configuration section

---

### Section 3: Forced Induction & Fueling

Ask the user:
1. What turbo or supercharger is fitted? (OEM or aftermarket — spec if known)
2. What intercooler setup is running?
3. What boost target are you running at peak?
4. What fuel type do you typically use?
5. What injectors and fuel pump are fitted?
6. Do you have a flex fuel sensor?

Save to: `context/project.md` → Forced Induction / Intake and Fuel System sections

---

### Section 4: ECU & Tuning Platform

Ask the user:
1. What ECU is fitted? (OEM or standalone — brand and model)
2. What tuning software do you use?
3. What wideband O2 sensor do you have and where is it installed?
4. Do you have a current tune file, or is this a fresh start?
5. Are you working with a professional tuner, or are you self-tuning?

Save to: `context/project.md` → ECU & Tuning Platform section

---

### Section 5: Goals & Experience Level

Ask the user:
1. How would you rate your tuning experience? (Beginner / Intermediate / Advanced / Professional)
2. What is the primary goal for this build? (e.g., reliable 400whp street car, sub-12s quarter mile)
3. Do you have a timeline or upcoming dyno session booked?
4. How detailed do you want explanations — brief summaries or full technical depth?

Save to: `context/role.md`

---

### Section 6: Safety Limits & Constraints

Ask the user:
1. What is the maximum safe boost limit for your setup?
2. What is your acceptable AFR range at WOT on your fuel?
3. Is there a transmission or drivetrain torque limit you're aware of?
4. What is your remaining budget for mods?
5. Are there any modifications you've decided against? (e.g., no E85, no water-meth)
6. Do you have any emissions or registration requirements to maintain?

Save to: `context/constraints.md`

---

### Section 7: Workshop & Environment

Ask the user:
1. Do you have access to a dyno? What type?
2. What tuning and logging software is installed on your computer?
3. What ECU interface cable/device do you use?
4. What data channels are you able to log? (list them)
5. What is your rough altitude? (affects boost and fuel calculations)

Save to: `context/for-agent/environment.md`

---

## After Collecting All Answers

1. Populate `context/project.md` with vehicle, engine, ECU, and build details
2. Populate `context/role.md` with experience level and goals
3. Populate `context/constraints.md` with all safety limits and constraints
4. Populate `context/for-agent/environment.md` with workshop and software details
5. Create an initial entry in `work-log/` named `YYYY-MM-DD-onboard.md` documenting:
   - The build baseline as captured
   - Current known power output (if any)
   - First focus area / immediate next step

6. Confirm completion with a summary:
   > "Your workspace is set up! Here's a quick summary of your build:
   > [Vehicle + Engine summary]
   > [Current power / target power]
   > [Next recommended action]
   >
   > Available commands: /analyze-tune, /review-datalog, /build-log, /dyno-plan, /parts-research, /diagnose, /tune-diff"
