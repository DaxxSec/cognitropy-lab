# /after-action — Post-Movement Debrief

Capture what actually happened on the leg, calibrate the matrix against reality, and feed forward into the next cycle's threat baseline.

## Required Inputs
- Movement brief (`outputs/<window>/operational-brief-<YYYY-MM-DD>.md`)
- The actual route used (deviations from primary if any)
- Detail leader's incident log
- Driver and CAT (if used) observations
- Counter-surveillance team's indicator log

## Procedure

### 1. Reconstruct What Happened
Walk the leg in chronological order. For each segment:
- Did the actual residual match the predicted residual?
- Were any indicators of the dominant hazard observed?
- Were any mitigations *unable* to be applied (e.g. advance team got pulled, route closure didn't materialize)?
- Were any new hazards observed that weren't in the survey?

Capture deviations from the planned timing, route, or composition with the reason.

### 2. Incidents and Near-Misses
For each:
- Time (relative T+) and segment
- What happened
- What was the response (against the drill or improvised)
- What was the outcome
- Was the principal aware?
- Did host-nation / liaison respond as expected?

### 3. Calibration Check
For each High+ residual segment that was crossed:
- Predicted band vs observed exposure (Low / Moderate / High actually felt)
- If overscored: note for re-tuning
- If underscored: note for re-tuning AND elevate it for the next baseline

### 4. Lessons & Forward-Looking Items
- What changes for the next leg in this window?
- What changes for the next baseline (new actor signal? new indicator type?)
- What changes in the workspace (a new drill type? a new criterion in `/route-compare`?)
- Any contracting-office reportable events?

### 5. Output
Write `outputs/<window>/after-action-<YYYY-MM-DD>-<leg>.md`:

```
# After-Action — <window codename> — <leg> — <YYYY-MM-DD>

## Summary
- Result: [uneventful / minor deviation / incident / near-miss]
- Primary route used: yes / no — if no, which alternate
- Time-on-route vs predicted: [+/− N min]

## Segment-by-segment reality vs prediction
[table]

## Incidents
[list]

## Calibration deltas
[bullets]

## Lessons forward
- For next leg: ...
- For threat baseline: ...
- For workspace: ...

## Contracting office reporting
[required / not required] — [if required, what was reported and to whom]
```

Update `cognitropy-history.json`-style internal "movement history" file at `planning/movement-log.md` (append a row).

Log to `work-log/<YYYY-MM-DD>-aar-<leg>.md`.

## Decision Rules

- If an incident occurred: AAR is mandatory and reviewed by the contracting office before the *next* movement.
- If three consecutive movements show predicted-vs-actual residual drift > ±1 band: trigger a recalibration of the matrix anchors and document in `planning/calibration-log.md`.
- If an unforeseen hazard appeared mid-leg and no drill matched: write a new drill template into `outputs/<route-codename>/contingencies/` and propagate it to the workspace's resources for future use.
- If pattern-of-life convergence is happening (the principal's actual movements look more predictable than the workspace assumed): flag it for the principal's chief of staff and re-design the next window for unpredictability.
