# Roller Coaster Forces — Decision-Tree Workflows

These are the named decision trees the workspace runs on. Every command in `.claude/commands/` walks one of these trees and produces a traced verdict. Trees are named with a single-letter prefix (F, R, J, I, B); nodes are numbered (F-1, F-2, ...) with sub-branches (F-1-a, F-1-b). When a command outputs a verdict, it cites the terminal node so the path is reproducible.

## 1. Force-Envelope Triage Tree (`F-*`)

Used by `/force-envelope-check`. Walks each axis independently, then a combined-vector node, then aggregates to a single verdict.

```
F-0 INTAKE
 ├─ frame == "track" or "heartline"? -- if unknown → REJECT, request frame.
 ├─ sample rate ≥ 50 Hz? ------------ if no → REJECT, request resample.
 └─ standard == F2291 or EN13814 or in-house? -- if in-house, swap limit table.

F-1 VERTICAL (+z, eyeballs-down)
 ├─ peak(+z) ≤ limit_peak? --- if no → REJECT(node F-1-a, value, time)
 └─ sustained(+z, 2s window) ≤ limit_sustained? -- if no → REWORK(F-1-b)

F-2 VERTICAL (-z, airtime)
 ├─ peak(-z) ≥ limit_peak_neg? --- if no → REJECT(F-2-a)
 └─ sustained(-z, 2s) ≥ limit_sustained_neg? -- if no → REWORK(F-2-b)

F-3 LATERAL (±y)
 ├─ peak(|y|) ≤ limit_peak_lat? --- if no → REJECT(F-3-a) AND route to /banking-curvature-tune
 └─ duration(|y| > 0.5g) ≤ 1.5s? -- if no → REWORK(F-3-b)

F-4 LONGITUDINAL (±x)
 ├─ launch event present? ----- if yes, apply launch limit table.
 └─ brake event present? ------ if yes, apply brake limit table.

F-5 COMBINED VECTOR
 └─ peak(|a|) ≤ limit_peak_vec? -- if no → REJECT(F-5)

F-6 VERDICT
 └─ all nodes PASS → PASS
    any REJECT → REJECT
    any REWORK, no REJECT → REWORK
    within 5% of any limit → PASS_WITH_NOTE
```

Each verdict carries: node id, axis, measured value, duration, limit, frame.

## 2. Restraint-Class Decision Tree (`R-*`)

Used by `/restraint-class-decide`. Ordered, top-down — stop at first match.

```
R-0 INTAKE
 └─ inversions list, -z floor, lateral peak — all required.

R-1 INVERSIONS PRESENT?
 ├─ yes → at least OTSR class (route to R-3 to refine OTSR vs. soft-vest).
 └─ no → continue to R-2.

R-2 -z FLOOR
 ├─ -z ≥ 0g       → R-2a: candidate class = none/lap-bar (refine via R-4).
 ├─ -z in [-0.5, 0g) → R-2b: candidate class = lap-bar single.
 ├─ -z in [-1.0, -0.5g) → R-2c: candidate class = lap-bar individual ratchet.
 └─ -z < -1.0g    → R-2d: individual ratchet minimum; if -z < -1.5g, consider soft-vest.

R-3 OTSR REFINEMENT (only reached if R-1 = yes)
 ├─ lateral peak ≥ 1.2g sustained > 0.5s → R-3a: soft-vest (head-bang mitigation).
 ├─ launch present > 4g forward         → R-3b: individual hydraulic.
 └─ else                                → R-3c: OTSR fixed yoke.

R-4 LATERAL REFINEMENT (only when no inversions)
 ├─ lateral peak ≥ 1.0g  → upgrade candidate class by one tier.
 └─ lateral peak < 1.0g  → keep candidate class from R-2.

R-5 OUTPUT
 └─ class = highest minimum from R-2/R-3/R-4, plus operator override field.
```

## 3. Jerk-Budget Audit Tree (`J-*`)

Used by `/jerk-budget-audit`. Operates over **transition windows** — the time bands between named elements (e.g. the 0.6 s between pullout-end and airtime-hill-crest).

```
J-0 INTAKE
 ├─ smoothed force trace (low-pass at 30 Hz to suppress sensor noise; do NOT smooth more aggressively).
 └─ window list — defaults to auto-detected (zero-crossing of d²a/dt²).

J-1 LATERAL JERK
 ├─ peak(|d(ay)/dt|) ≤ 1.5 g/s? -- if no → REJECT(J-1-a) AND route to /banking-curvature-tune.
 └─ sustained(|d(ay)/dt|, 0.3s) ≤ 1.0 g/s? -- if no → REWORK(J-1-b)

J-2 VERTICAL JERK
 ├─ peak(|d(az)/dt|) ≤ 5 g/s? -- if no → REJECT(J-2-a)
 └─ sustained(|d(az)/dt|, 0.3s) ≤ 2 g/s? -- if no → REWORK(J-2-b)

J-3 LONGITUDINAL JERK
 └─ peak(|d(ax)/dt|) ≤ 3 g/s? -- if no → REWORK(J-3-a)

J-4 TRANSITION QUALITY
 ├─ any axis jerk-direction-flip within 0.2 s window? -- if yes → REWORK(J-4-a, whiplash candidate)
 └─ multi-axis jerk co-occurrence > 2 axes simultaneously? → REWORK(J-4-b, vestibular hazard)

J-5 VERDICT
 └─ aggregate as in F-6.
```

## 4. Incident Triage Tree (`I-*`)

Used by `/incident-triage`. Routes a complaint or sensor event to a queue.

```
I-0 INTAKE
 ├─ complaint type (head-bang, lateral-strike, restraint-bruise, vestibular, eject-event, hardware)
 ├─ rider position (front car / mid / back) — back-car amplifies negative-g; front amplifies launch.
 ├─ sensor data available? (yes/no)
 └─ injury reported? (yes/no)

I-1 INJURY GATE
 ├─ injury reported → HOLD (pull from service pending review). Skip to I-5 with HOLD outcome.
 └─ no injury → continue.

I-2 HARDWARE OR FORCE?
 ├─ hardware (wheel chunk, restraint malfunction, fastener loss) → route to maintenance; bin = HOLD until cleared.
 └─ force-related (head-bang, lateral-strike, vestibular, eject) → continue.

I-3 SENSOR DATA AVAILABLE?
 ├─ yes → run /force-envelope-check + /jerk-budget-audit on the relevant window, return here with their verdicts.
 │       ├─ both PASS → bin = MONITOR (track frequency; ≥3 events / week of similar type promotes to HOLD).
 │       ├─ either REWORK → bin = HOLD.
 │       └─ either REJECT → bin = PULL_FROM_SERVICE.
 └─ no → continue to I-4.

I-4 PATTERN MATCH
 ├─ first reported event of this type on this element? → bin = MONITOR, prompt for sensor instrumentation.
 ├─ 2nd–4th matching event → bin = MONITOR, escalate priority for sensor pass.
 └─ 5+ matching events → bin = HOLD pending sensor pass and force review.

I-5 OUTPUT
 └─ bin ∈ {NUISANCE, MONITOR, HOLD, PULL_FROM_SERVICE} + reasoning trail.
```

## 5. Banking / Curvature Tuning Loop (`B-*`)

Used by `/banking-curvature-tune`. This is a loop, not a one-shot tree.

```
B-0 INTAKE
 ├─ failing segment from /force-envelope-check (must be lateral-axis fail).
 └─ current banking profile θ(s) and curvature κ(s) along arc length s.

B-1 IDEAL BANK ANGLE
 └─ θ_ideal(s) = atan(v(s)² · κ(s) / g) — banking that zeros lateral-g at the heartline.

B-2 DELTA
 ├─ Δθ(s) = θ_ideal(s) - θ(s)
 └─ if |Δθ(s)| > 30° anywhere → flag B-2-a: structural change likely required, not a tune.

B-3 SMOOTHING
 └─ propose θ'(s) = θ(s) + α · Δθ(s), with α ∈ [0.4, 0.7] for one iteration (avoid over-correcting).

B-4 SECONDARY EFFECTS
 ├─ does proposed bank change height profile? → flag for re-survey.
 └─ does proposed bank change train clearance to support columns? → STOP, require engineering review.

B-5 RECOMMEND
 └─ output: new banking profile, expected lateral-g after change (linear approximation), recommend re-simulate.
```

After applying B-5, re-run `/force-envelope-check`. If still failing, iterate B-1..B-5 with α at the upper end of [0.4, 0.7]; if iteration 3 still fails, the geometry change is mandatory.

## How the trees compose

- `/force-envelope-check` walks `F-*`. On a lateral failure, it auto-suggests `/banking-curvature-tune`.
- `/restraint-class-decide` walks `R-*`. It pulls `-z` floor and lateral peak from a prior `F-*` walk if available; otherwise demands them inline.
- `/jerk-budget-audit` walks `J-*`. It is usually run **after** `F-*` flags PASS_WITH_NOTE or any REWORK — peaks pass, slopes don't.
- `/incident-triage` walks `I-*`. Inside the tree it may invoke `/force-envelope-check` and `/jerk-budget-audit` for sensor-equipped events.
- `/banking-curvature-tune` walks the `B-*` loop and is iterated until `F-3` passes or B-2-a fires (structural change required).
- `/heartline-analysis` is the pre-processor: if a sim reports track-frame, run heartline-analysis first to project to heartline frame, then feed those forces into `F-*`.

## Phases of a full ride review

### Phase 1 — Frame & data quality (F-0, J-0)
Confirm frame, sample rate, smoothing. Reject the data, not the ride, if these fail.

### Phase 2 — Element-by-element envelope (F-*)
Walk every named element through the envelope tree. Produce a per-element verdict table.

### Phase 3 — Transition audit (J-*)
For every transition between elements (and every PASS_WITH_NOTE element from Phase 2), walk the jerk tree.

### Phase 4 — Restraint lock (R-*)
With Phase 2/3 results in hand, run restraint-class-decide once per train configuration. Restraint class is global to the ride, not per element.

### Phase 5 — Tune-and-resimulate loop (B-*)
For every REWORK from Phases 2/3, run the banking/curvature loop. Iterate until PASS or geometry change is mandated.

### Phase 6 — Sign-off package
Concatenate all decision-tree walks into the outputs/ ride review folder. The package is the audit trail; do not summarise away the node ids.
