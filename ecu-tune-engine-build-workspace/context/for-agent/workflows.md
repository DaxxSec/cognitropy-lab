# Agent Workflows & Decision Trees

> This file defines how the agent should approach each domain task. Read this before executing any command beyond /onboard.

---

## General Principles

1. **Context First:** Always read project.md, constraints.md, and role.md before giving any technical advice. Generic advice without vehicle context is low value.

2. **Safety Over Power:** When there is any ambiguity, default to the conservative recommendation. Detonation and lean conditions can destroy engines in seconds.

3. **Ask Before Assuming:** If critical context is missing (e.g., fuel type, current boost level, injector size), ask before proceeding. Do not assume.

4. **One Change at a Time:** Always recommend incremental changes. Never suggest changing multiple parameters simultaneously without logging between changes.

5. **Log Everything:** Encourage the user to log every meaningful session in work-log/ with date, changes made, observations, and next steps.

---

## Workflow: /analyze-tune

### Purpose
Evaluate ECU calibration data (maps, tables, scalars) for safety issues, inefficiencies, and tuning opportunities.

### Inputs Required
- Map/table data (pasted text, screenshot description, or file via filesystem MCP)
- Fuel type being used
- Current boost target
- Injector size and type

### Process
1. **Identify the platform** — confirm ECU type and ROM version if provided
2. **Safety audit first:**
   - Fuel map / VE table — check for lean cells at WOT (AFR targets < 11.5:1 on gasoline = danger zone)
   - Ignition timing table — check for aggressive timing at low RPM / high load
   - Boost control — verify target doesn't exceed stated constraints
   - Rev limiter / fuel cut — confirm it's set appropriately
3. **Performance review:**
   - Identify areas where timing could potentially be advanced (low-load cruise cells)
   - Check for fuel trim compensation
   - Evaluate cold start enrichment if reported issues exist
4. **Output:**
   - Summarize findings in a table: [Parameter | Current Value | Assessment | Recommendation]
   - Flag any CRITICAL items at the top in bold
   - Suggest a prioritized list of changes (conservative first)

### Decision Tree: Is This Tune Safe to Pull On?
```
Is AFR target at WOT >= 11.2:1 (gasoline) or 10.5:1 (E30+)? → NO → STOP, rich up fuel first
Is timing within known-safe window for platform? → NO → STOP, pull timing before test
Is boost target within constraints.md hard limits? → NO → STOP, address boost control
All checks pass → Proceed with caution, monitor datalog on first pull
```

---

## Workflow: /review-datalog

### Purpose
Analyze a logged run or session for anomalies, knock events, lean conditions, and thermal issues.

### Inputs Required
- Datalog data (CSV paste, channel descriptions, or file)
- Fuel used during the log
- Type of run (WOT pull / street drive / cold start / idle)

### Process
1. **Identify channels present** — confirm what was logged (check environment.md)
2. **Critical channel review (in order):**
   a. **Knock / Knock Retard** — any non-zero value is a flag; >2° retard = investigate immediately
   b. **AFR / Lambda** — WOT targets should be within calibrated range; lean excursions = serious
   c. **Boost** — compare to target; overboost = investigate wastegate; underboost = possible leak
   d. **Coolant Temp** — WOT above 100°C / 212°F is concerning; above 105°C = abort condition
   e. **IAT** — high IAT degrades knock resistance; note if intercooler is heat-soaked
   f. **Injector Duty Cycle** — above 85% = injectors running out of headroom
3. **RPM / Load correlation** — check if issues cluster at specific RPM/load zones
4. **Output:**
   - Summary table of key metrics (min, max, average at WOT)
   - Flagged events with timestamps/RPM
   - Recommended action items in priority order

### Red Flag Decision Guide
| Finding | Severity | Action |
|---------|----------|--------|
| Knock retard > 4° at any point | CRITICAL | Do not pull again. Investigate fuel, timing map |
| AFR > 13.5:1 at WOT (gasoline) | CRITICAL | Fix fueling before any WOT run |
| AFR > 12.0:1 sustained WOT (boosted) | WARNING | Investigate — acceptable range is 11.0–11.8:1 |
| Injector duty > 90% | WARNING | Injectors near limit — upgrade or reduce boost |
| Boost spike > 3 psi over target | WARNING | Check wastegate, boost controller |
| Coolant > 102°C at WOT | WARNING | Check cooling system before next run |
| Any channel shows erratic/implausible data | INFO | Check sensor / wiring before trusting the log |

---

## Workflow: /build-log

### Purpose
Record and retrieve modification history, parts installed, and build milestones.

### Add Entry Flow
1. Ask for: date, what was done, parts used (brand/part number if known), who performed the work
2. Note the vehicle's current odometer reading
3. Ask if any baseline measurements were taken before/after (compression, leakdown, dyno)
4. Record any observed changes post-install
5. Save entry to work-log/ as `YYYY-MM-DD-[descriptor].md`

### Review Flow
1. Load all entries from work-log/
2. Summarize chronologically: what was changed and when
3. Identify last known-good configuration
4. Flag any mods without documented install notes

---

## Workflow: /dyno-plan

### Purpose
Create a structured, safe dyno session plan before going to the dyno.

### Required Context
- Current tune state (read project.md)
- Session goal (power baseline / pull on new tune / diagnosis / final numbers)
- Fuel to be used day-of
- Any new parts installed since last dyno

### Plan Structure to Generate
1. **Pre-dyno checklist** (see resources/dyno-prep-checklist.md)
2. **Pull strategy:** gear, RPM range, hold time, number of pulls
3. **Target metrics:** expected power, AFR range, boost curve
4. **Safety criteria:** go/no-go decision points
5. **Data to capture:** channels to log, screenshots to take
6. **Cooldown protocol:** between-pull wait time, fan usage
7. **Post-session documentation:** what to record in build-log

---

## Workflow: /parts-research

### Purpose
Evaluate parts for a specific application — compatibility, expected gains, reliability, and sourcing.

### Process
1. Confirm the vehicle and current configuration from project.md
2. Identify the performance gap or goal driving the parts search
3. For each candidate part:
   - **Fitment:** Is it plug-and-play or does it require supporting mods?
   - **Expected performance delta:** HP/TQ gain, flow improvement, reliability change
   - **Known issues:** Common failure modes, fitment problems, quality control concerns
   - **Supporting mods required:** What else needs to change for this part to work safely?
   - **Budget check:** Does this fit within constraints.md budget?
4. Rank options by value (performance per dollar) and safety
5. Note any research sourced from forums, manufacturer specs, or community data

---

## Workflow: /diagnose

### Purpose
Systematically diagnose a problem from symptoms, OBD codes, or observed behavior.

### Process
1. **Collect symptoms:**
   - What is the car doing? (misfires, power loss, rough idle, smoke, CEL, noise)
   - When does it occur? (cold start, warm idle, WOT, specific RPM range)
   - How long has it been happening?
   - Any recent changes to the vehicle or tune?
2. **Build differential diagnosis list** — ranked by probability
3. **Suggest diagnostic tests** in order (cheap/easy first):
   - Live data checks (OBD reader)
   - Visual inspection points
   - Specific mechanical tests (compression, leakdown, fuel pressure)
   - Software checks (check for fault codes, review recent tune changes)
4. **Cross-reference known issues** for the platform
5. Explicitly note if the symptom could indicate an unsafe condition before further driving

---

## Workflow: /tune-diff

### Purpose
Document and explain differences between two tune states.

### Process
1. Collect two tune states (described, pasted maps, or file-based via MCP)
2. Identify what parameters changed
3. For each change:
   - Describe what the table/map controls
   - What direction did it change (more aggressive / more conservative)?
   - What effect should this have on performance and safety?
4. Summarize the intent of the revision
5. Flag any changes that approach hard limits in constraints.md
6. Save the diff summary to outputs/ for reference

---

## Session Wrap-Up Protocol

At the end of any work session where changes were discussed or made, the agent should:
1. Summarize what was decided / recommended
2. List any open questions or items needing follow-up
3. Remind the user to log any physical changes in work-log/
4. Note the next step or upcoming milestone
