# /scenario-test — Perturbation Scenarios on a Planned Form

Take a form spec produced by `/form-sim` and stress-test it against a catalog of realistic studio perturbations. The output is a per-scenario verdict, a recovery plan for any survivable failure, and a "do not proceed" flag for any that cannot be recovered safely.

## Required Inputs
- A form spec file from `planning/form-<slug>-v<n>.md` (or run `/form-sim` first if none exists)
- A scenario set — defaults to the standard seven below; the user may supply additional studio-specific scenarios

## Standard Scenario Catalog

Each scenario is run as a what-if: "the plan as written, but at step N, X happens. What now?"

### 1. Glory Hole Crash (Loss of Reheat)
- **Insult:** Glory hole loses temperature mid-session (gas pressure drop, electrical fault); soak temp falls 200 °C and won't recover for 15 minutes
- **Check:** Is there a safe parking position for the in-progress piece? Can the lehr accept a partial form for slow cool, or will sudden cool from working temp shatter it?
- **Verdict logic:** Green if piece can be parked in lehr at >450 °C and recovered; red if mid-gather phase with thin walls

### 2. Color Rod Break
- **Insult:** A color rod fractures during pickup or application; fragment ejects or lodges in the gather
- **Check:** Does the form tolerate marvering off the contamination, or does the cane application define the piece (e.g., reticello, incalmo)?
- **Verdict logic:** Green for surface color application; yellow if fragment is buried (cord risk); red for cane-defined pieces (restart)

### 3. Punty Failure
- **Insult:** Punty doesn't seat or releases prematurely after transfer
- **Check:** Is the piece geometry forgiving of an asymmetric punty mark? Is there time for a re-punty before the lip work cools below working point?
- **Verdict logic:** Green for pieces with thick foot; red for pieces where punty mark is on a visible flat (e.g., flat plate bottom)

### 4. Cool Curve Crash (Lehr Failure)
- **Insult:** Lehr loses power or controller crashes mid-anneal cycle
- **Check:** At which segment did it crash? If during the hold-at-anneal (~480 °C for soda-lime), how long can the piece sit at room temp before strain becomes unrecoverable?
- **Verdict logic:** Green if caught during ramp-down (re-fire to anneal point and restart); yellow if caught during hold (try recovery anneal); red if caught during fast-ramp-up (likely thermal shock crack already)

### 5. Devitrification Onset
- **Insult:** Glass surface develops crystalline haze due to extended time in the devit window (typically 700–900 °C for soda-lime, much higher for borosilicate)
- **Check:** Does the planned step sequence keep the glass below or above the devit window between heats? Long marvering or fancy bench work with no reheat is the typical trigger
- **Verdict logic:** Green if all bench operations are < 60 s; yellow if any operation is 60–120 s; red if any step is > 120 s without reheat

### 6. COE Mismatch (Slow Cracker)
- **Insult:** A color rod assumed compatible turns out to be from a different COE family (lot mix-up, mislabeled stock)
- **Check:** Hard stop. Compatibility cannot be recovered after the fact
- **Verdict logic:** Always red. Force a documented compatibility test on a small dummy piece before committing the full plan

### 7. Gather Over-Mass
- **Insult:** A gather comes out 30–50% heavier than planned (typical for tired or new gaffers)
- **Check:** Does the form tolerate over-mass without exceeding the gravity-sag threshold from `/form-sim`? Is the mass budget per gather such that one heavy gather still leaves headroom for the next?
- **Verdict logic:** Green if total mass budget has > 20% slack; yellow if < 20%; red if over-mass would push the sag check over threshold

## Procedure

### 1. Load Form Spec
Open `planning/form-<slug>-v<n>.md`. If it doesn't exist, refuse and prompt `/form-sim` first.

### 2. Run Each Scenario
For each scenario in the standard set (and any user-added):
- Identify the latest plan step at which the perturbation could plausibly occur
- Check the piece's state at that step (in-glory-hole / on-marver / on-bench / pre-transfer / post-transfer / lehr)
- Apply the scenario logic above, noting any glass-family-specific overrides (borosilicate has a wider working window than soda-lime; flag this)

### 3. Compose Recovery Plans
For yellow scenarios, write a short recovery plan: what action the artist takes, in what time window, with what fallback. Recovery plans must be physically realistic (no "magically reheat to 1100 °C in 5 seconds").

### 4. Aggregate Verdict
Compose a scenario-test summary:
- All-green → proceed, but log scenarios as part of the batch record's pre-flight notes
- Any yellow → proceed only if user explicitly accepts the risk; log the acceptance in the batch record
- Any red → block. Surface the failing scenario(s); user must rework the plan or explicitly override

### 5. Save and Cross-Link
Append the scenario-test result to the form spec under a `## Scenario Test` section. Link it from the day's batch record. Save a standalone copy to `outputs/scenario-tests/<slug>-v<n>.md` for historical querying.
