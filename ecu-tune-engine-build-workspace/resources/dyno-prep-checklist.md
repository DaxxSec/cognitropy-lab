# Dyno Day Preparation Checklist

Complete this checklist before your first pull. No shortcuts — dyno fires and engine failures happen when basics are skipped.

---

## The Night Before

### Fluids
- [ ] Engine oil checked — at the correct level, no signs of milky appearance (coolant contamination)
- [ ] Coolant level checked — full, no recent loss
- [ ] Transmission / differential fluid checked
- [ ] Power steering fluid (if applicable)
- [ ] Windshield washer fluid (for trailer trip)
- [ ] Brake fluid level

### Visual Inspection
- [ ] No boost hose cracks or splits — squeeze every intercooler pipe and check clamps
- [ ] Intercooler end tanks checked for cracks
- [ ] No fuel smell anywhere in engine bay or cabin
- [ ] No oil leaks that could drip onto hot exhaust
- [ ] All engine bay covers, brackets, and hoses secured
- [ ] Air filter clean and properly seated
- [ ] Intake path unobstructed

### Electrical
- [ ] Wideband sensor working — check reading at idle (should show ~14.7 AFR on unloaded engine)
- [ ] Data logging software connected and logging — do a test log
- [ ] ECU interface cable confirmed communicating
- [ ] Battery terminals clean and tight
- [ ] No check engine lights (or understand any that are present)

### Tune Verification
- [ ] Confirm correct tune file is loaded (check revision / filename)
- [ ] Rev limiter set appropriately for planned RPM range
- [ ] Boost target confirmed in ECU
- [ ] Wideband AFR correction enabled / disabled as intended
- [ ] Knock sensitivity confirmed — will the ECU pull timing if needed?

---

## Morning of Dyno Day

### Fuel
- [ ] Fresh tank of the fuel type your tune is calibrated for
- [ ] Confirm ethanol content if running E-blend (use flex sensor or test kit)
- [ ] No old or suspect fuel in the tank

### Transport
- [ ] If trailering: straps secure, correct tie-down points used
- [ ] Coolant and oil checked again after transport (especially if car is on a tilt)

### Safety Equipment
- [ ] Fire extinguisher at the dyno (confirm with shop or bring your own ABC type)
- [ ] Know the emergency stop procedure for the dyno facility
- [ ] Briefed the dyno operator on abort signal (knock on window / wave off)

---

## At the Dyno — Pre-Pull Protocol

### Warm-Up
- [ ] Engine fully up to operating temperature before any WOT run
  - Coolant: ≥ 85°C / 185°F
  - Oil: ≥ 80°C / 175°F (higher is better for consistent results)
- [ ] IAT checked — note the reading before the first pull (baseline for heat soak tracking)
- [ ] No WOT pulls in the first 2 minutes of operation

### First Pull Preparation
- [ ] Wideband confirmed reading (check live AFR before starting)
- [ ] Data logging confirmed active — verify channels are recording
- [ ] Boost controller set to intended target
- [ ] Operator briefed on: gear, RPM start, RPM brake point, abort signal
- [ ] Any gauges you're monitoring: note baseline readings

### Go / No-Go Decision
Only proceed if:
- [ ] Wideband is reading a plausible idle AFR
- [ ] Coolant temp is in operating range
- [ ] Oil temp is in operating range
- [ ] No CEL (or known, non-critical codes only)
- [ ] No boost leak noises at idle
- [ ] No fuel smell

---

## Between Pulls

- [ ] Minimum cooldown time: [set in dyno-plan — typically 5–10 min]
- [ ] Check IAT — if above [X°C], wait longer before next pull
- [ ] Check coolant temp — if above 100°C, full cool-down before next pull
- [ ] Review previous pull datalog before authorizing next pull
- [ ] Note any changes between pulls clearly before making them

---

## Abort Criteria (STOP THE PULL)

Stop immediately if:
- **Any knock retard** above your stated threshold
- **AFR leans out** beyond your stated limit at WOT
- **Boost spike** more than 3 psi above target
- **Coolant temp** above hard limit
- **Any unusual noise** during pull — metallic knock, boost hiss, banging
- **Any vibration** not present in baseline
- **Smoke** from engine bay, exhaust, or wheelwells

---

## Post-Session

- [ ] Save all pull datalogs with consistent naming: `YYYY-MM-DD-pull-[N]-[description]`
- [ ] Screenshot dyno graph for each pull
- [ ] Note best power number and conditions
- [ ] Note any issues observed and next steps
- [ ] Log the session in work-log/ when you get home
- [ ] Check for any new leaks after cooling down

---

## Emergency Procedures

**If the car catches fire:**
1. Dyno operator hits emergency stop immediately
2. Operator or spotter discharges fire extinguisher at base of fire
3. Do NOT open hood if fire is in engine bay — oxygen feeds it
4. Evacuate bystanders from the building
5. Call fire department if not immediately extinguished

**If engine makes a loud noise / failure sound:**
1. Abort pull immediately
2. Let car coast to a stop on the dyno
3. Shut engine off
4. Do not restart until visually inspected
