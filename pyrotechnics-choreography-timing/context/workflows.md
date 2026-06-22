# Pyrotechnics Choreography Timing — Workflows and Methodology

How the agent actually works. The spine is the **verification loop**; today's technique — **decision-tree triage workflows** — drives three trees: the weather go/no-go gate, the misfire runbook, and constraint-violation triage. `concepts.md` says *what things are*; this file says *what to do with them*.

## Workflow 1: The Verification Loop (model → specify → verify → triage → repair → sign-off)

**Goal:** Turn a draft show into one whose every safety and artistic obligation is discharged and recorded.

### Steps

1. **Model.** Build the canonical cue sheet (`/cue-sheet-build`): every cue with `t_fire`, `tof`, `t_effect`, `t_clear`, `position`, `channel`, `radius`. Confirm which timeline the source export uses and normalize to both.
2. **Specify.** Generate the proof-obligation catalog (`/timing-spec`) for the safety framework (1123 vs 1126), the site geometry, the firing hardware, and the artistic goals. Each obligation gets an ID, a formal statement, and a tolerance.
3. **Verify.** Discharge the catalog (`/verify-schedule`, plus `/separation-proof`, `/rack-allocation`, `/beat-sync-check` for the heavy ones). Each obligation returns `discharged` (+ robustness margin), `refuted` (+ counterexample), `open`, or `assumed`.
4. **Triage.** For each refuted obligation, run the **constraint-violation triage tree** (Workflow 4) to decide the repair class.
5. **Repair & re-verify.** Apply the minimal cue-sheet edit, then re-run only the obligations the edit could affect (and a full pass before sign-off). Repairs can introduce new violations — never trust a local fix without a re-check.
6. **Sign-off.** Snapshot the ledger (`/proof-ledger`): all safety obligations `discharged` or explicitly `assumed` with the assumption named; artistic obligations discharged or accepted-with-deviation. Tie the snapshot to the cue-sheet revision.

### Decision Points

- If the export's time column is ambiguous (fire vs. effect): **stop and resolve** before modeling — do not guess.
- If any **safety** obligation is `open` at sign-off: the show is **not** signed off. Open ≠ safe.
- If a safety obligation is `assumed` (e.g. "wind ≤ 12 mph"): the assumption becomes a **show-day gate condition** in the weather tree.

## Workflow 2: Time-of-Flight Compensation & Beat Sync

**Goal:** Make hero effects break *on* the beat and prove they do.

### Steps

1. Extract beat/downbeat times `{b_i}` from the music map (DAW markers or `librosa`/`madmom`); pick the **hero cues** that must hit them.
2. For each hero cue, set `t_fire = b_i − tof(device)` using the bore-specific ToF from `references.md`.
3. Recompute `t_effect = t_fire + tof` and the sync error `e_i = t_effect − b_i` (≈0 by construction, but quantization, shared-channel constraints, and ToF uncertainty reintroduce error).
4. Discharge **SYNC**: `|e_i| ≤ τ` for every hero cue (typical τ = 50–100 ms). Report the robustness margin `τ − |e_i|`.
5. Flag cues that *can't* be compensated (e.g. two hero shells of different bore sharing one beat from one channel) as constraint-violation triage inputs.

### Decision Points

- If ToF uncertainty (wind, lift variance) exceeds τ: widen τ for that cue or downgrade it from "hero" to "ambient" — and record the deviation.
- If two hero cues collide on a shared channel at the same beat: re-rack (Workflow 4 → re-rack branch).

## Workflow 3: Separation & Fallout Proof under Wind

**Goal:** Prove no live effect's danger footprint reaches the crowd or another live effect, in the **worst-case forecast wind**.

### Steps

1. For each cue compute the danger footprint: a disc of `radius` centered on `position`, shifted by `wind_vector × descent_time` (downwind drift) over `[t_effect, t_clear]`.
2. **FALLOUT:** check every footprint against the spectator line and no-fire-zone polygons. Any intersection ⇒ counterexample.
3. **SEP:** for every pair of cues whose live intervals `[t_effect, t_clear]` overlap in time, check footprint disc intersection. Any overlap ⇒ counterexample with the two ids, the overlap distance, and the time.
4. Re-run for the **worst-case** forecast wind vector (max speed, direction toward the crowd), not nominal.
5. Report discharge + minimum clearance margin (the smallest gap across all pairs/lines — the show's spatial "slack").

### Decision Points

- If FALLOUT fails: the position or the wind gate must change (no timing edit fixes geometry). Escalate to the weather tree and/or re-position.
- If SEP fails on time-overlap only (footprints fine if staggered): push the later cue to `t_fire ≥ t_clear(prev)` — a timing repair.

## Workflow 4: Constraint-Violation Triage Tree (technique core)

When `/verify-schedule` refutes an obligation, classify the repair before touching the cue sheet:

```
Refuted obligation
├─ Is it a SAFETY obligation (SEP / FALLOUT / REUSE / CURR / CHAN)?
│  ├─ Geometry-rooted (SEP/FALLOUT)?
│  │   ├─ Caused by wind drift only → tighten WEATHER GATE (cap wind), re-verify
│  │   └─ Static overlap → RE-POSITION / RE-RACK the cue, re-verify SEP+FALLOUT
│  ├─ Time-rooted (REUSE / time-only SEP)?
│  │   └─ DELAY the later cue to ≥ t_clear(prev); if that breaks SYNC → drop or re-rack
│  └─ Resource-rooted (CURR / CHAN)?
│      └─ RE-ALLOCATE channels / split across modules (/rack-allocation), re-verify
└─ Is it an ARTISTIC obligation (SYNC / DENSITY / RUNTIME)?
   ├─ SYNC miss within slack → micro-adjust t_fire by −Δtof; else downgrade hero→ambient
   ├─ DENSITY exceeded → thin or stagger non-hero cues
   └─ RUNTIME overrun → trim tail cues or compress gaps (never compress at the cost of SEP)
```

**Rule:** safety branches always dominate artistic branches. Never resolve a SYNC/DENSITY/RUNTIME violation with an edit that opens a SEP/FALLOUT/REUSE/CURR/CHAN obligation. After any repair, re-verify the affected obligations *and* their neighbors.

## Workflow 5: Weather Go/No-Go Gate (decision tree)

**Goal:** A show-day tree that turns the `assumed` weather premises into a firm go/no-go. Built by `/weather-gate`.

```
Weather call (T-minus window)
├─ Wind speed > permit/NFPA max (e.g. >20 mph sustained)? → NO-GO
├─ Wind direction toward crowd AND fallout margin < threshold? → NO-GO (or reduce max bore / shift positions)
├─ Lightning within X miles / storm forecast in window? → HOLD, re-poll
├─ Visibility / ceiling below min for max bore apogee? → reduce max bore or HOLD
└─ All within assumed bounds? → GO, log the actual readings against the assumptions
```

Each leaf cites the assumption it discharges from the ledger; a GO is only valid while the readings stay within the assumed envelope.

## Workflow 6: Misfire / Hangfire Triage Runbook (decision tree)

**Goal:** The shooter's live contingency card. Built by `/misfire-triage`. (Operational decision logic only — no device handling chemistry.)

```
Anomaly observed at a cue
├─ No fire (no effect, no report)?
│   ├─ Electric system: verify module status; do NOT re-fire blindly
│   └─ Treat as live → wait the mandated interval before any approach; safe the module
├─ Low break / partial (fired but abnormal)?
│   └─ Hold any dependent downstream chain on that position; flag position as suspect
├─ Hangfire (delayed initiation suspected)?
│   └─ NEVER approach; electrically disconnect/safe; wait the full mandated stand-off time
└─ Continue/abort decision
    ├─ Isolated, downstream unaffected → continue, annotate cue as failed in the as-fired log
    └─ Safety-relevant or cascading → execute show ABORT per site plan
```

The runbook defers all stand-off intervals and approach rules to the operator's permit, NFPA, and product guidance — it sequences the *decision*, not the physical handling.

## Methodology note — the as-fired ledger

Every run, whether rehearsal or live, updates the **proof ledger** with as-fired reality: which obligations held, which assumptions were exercised (actual wind vs. assumed), and any failed cues. Over revisions this becomes the audit trail that makes the next show's verification faster and the deviations explainable.
