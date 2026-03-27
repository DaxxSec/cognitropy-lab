# /dyno-plan — Dyno Session Planning

Generate a structured, safe dyno session plan before you load the car on the rollers.

---

## When to Use This Command
- Before any scheduled dyno session
- When planning a road tune pass
- To create a structured pull protocol after a significant tune change
- To document target metrics and go/no-go criteria ahead of time

---

## What to Tell Me

Provide context for this specific session:
1. **Session goal:** (e.g., baseline pull / testing new turbo / final tune / diagnosis)
2. **Current tune state:** Is this the same tune as last time or has something changed?
3. **Any new parts since last session:** (affects expected behavior)
4. **Fuel for the session:** (octane, ethanol content, fresh tank?)
5. **Dyno type:** (Mustang / Dynojet / Hub / Other)
6. **Ambient conditions:** (temperature, humidity if known)
7. **Target power:** (realistic expectation, not just hope)

---

## What Gets Generated

### Pre-Session Checklist
A complete go/no-go list to check before the first pull (references `resources/dyno-prep-checklist.md`).

### Pull Protocol
- **Gear recommendation:** (typically highest gear providing sufficient load)
- **RPM range:** Start RPM → Pull-through RPM → Brake point
- **Number of pulls:** (recommended sequence)
- **Cooldown period:** (minimum time between pulls)
- **Fan protocol:** (use shop fans during cooldown — yes/no, placement)

### Target Metrics
- Expected peak power range (WHP / WTQ)
- Expected peak boost
- Target AFR at WOT
- IAT budget (max acceptable before skipping a pull)
- Coolant temp budget

### Go / No-Go Criteria
Explicit conditions that mean STOP and investigate:
- Knock retard threshold that aborts the session
- AFR lean limit that aborts the session
- Boost spike limit
- Thermal limits

### Data to Capture
- Channels to confirm are logging before the first pull
- Screenshots to take of each pull
- Specific things to watch for given current tune state

### Post-Session Protocol
- What to log in work-log/ after the session
- How to save and label the tune file post-session
- Cool-down / trailer-load procedure if applicable

---

## Output

The completed plan is saved to `planning/dyno-session-YYYY-MM-DD.md` for reference during the session.

---

## Safety Reminders (Always Included)
- Wideband must be reading before ANY pull
- Fire extinguisher accessible at dyno
- Operator briefed on abort signal
- Coolant and oil levels checked pre-session
- No pulls within first 2 minutes of engine operation (proper warm-up)
- If ANY unexpected noise occurs — abort immediately
