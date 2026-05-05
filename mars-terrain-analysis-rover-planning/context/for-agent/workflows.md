# Core Workflows — Mars Terrain Analysis & Rover Traverse Planning

Three workflows cover the bulk of the agent's work: the **per-sol tactical planning loop**, the **replan-on-anomaly loop**, and the **strategic look-ahead loop**.

---

## Workflow 1: Per-Sol Tactical Planning Loop

**Goal:** Turn yesterday's downlink and today's strategic priorities into tomorrow's reviewed sol plan.

### Steps

1. **Ingest downlink artifacts.** Read the latest hazard map, end-of-drive rover state (position, heading, attitude, mechanism health), and any new orbital coverage. Update `planning/state.md` with current rover state.
2. **Read strategic priorities.** Read `planning/plan.md` for the current campaign target. Confirm sol-N target waypoint with the science PI / strategic team if priorities have shifted.
3. **Run `/terrain-assess`** on the current tile if not already assessed. Output is a hazard raster + terrain-class raster, both saved under `outputs/hazard-maps/`.
4. **Run `/traverse-compose`** to build 1–3 candidate traverses from current rover position to the sol-N target. Each candidate is recorded as a chord progression in `planning/candidates/<id>.md`.
5. **Run `/risk-cadence`** on each candidate. Reject candidates with unresolved-dissonance stretches; for those with isolated risky segments, mark them for substitution search.
6. **Run `/substitution-search`** on flagged segments. Each successful substitution produces a new candidate revision; old revision is preserved in the planning history.
7. **Select top candidate(s)** for review — at most 2 to avoid reviewer fatigue.
8. **Run `/peer-review`** on the top candidate. If it fails, revise and re-review (max 3 cycles before escalating).
9. **Run `/sol-plan`** on the approved candidate to produce the final sol plan with science block, comms passes, contingencies.
10. **Hand off** the sol plan from `outputs/sol-plans/<sol>.md` to the uplink team. Log the session in `work-log/<YYYY-MM-DD>.md`.

### Decision Points

- **If no candidate passes flight-rule check:** escalate — the strategic target may be unreachable from current position with the available terrain. Recommend the strategic team consider an alternate target.
- **If `/risk-cadence` finds a deceptive cadence is *desired* (en-route science target):** explicitly tag it in the candidate and ensure science PI signs off in `/peer-review`.
- **If `/peer-review` reaches 3 revision cycles without consensus:** escalate to the SOWG (Strategic Operations Working Group) for the next sol; uplink a "stay in place" or "minimum drive" plan today.

---

## Workflow 2: Replan-on-Anomaly Loop

**Goal:** When the rover hits an unexpected condition (stuck wheel, unexpected terrain class, comms anomaly), produce a recovery plan within the planning shift.

### Steps

1. **Triage the anomaly.** Read fresh downlink, classify: mobility (wheel stuck, high tilt) / sensing (camera fault, hazcam glitch) / comms (missed pass, low SNR) / terrain (unmodeled hazard).
2. **Snapshot the current state** to `planning/anomaly/<sol>-<id>/state.md`. Include rover pose, mechanism health, energy state, comms state, planned vs actual progress.
3. **Re-run `/terrain-assess`** at higher resolution / smaller tile around the rover; the previous assessment may have missed the responsible feature.
4. **Compose a *recovery* candidate** with `/traverse-compose --mode recovery`. Recovery mode prefers:
   - Short segments (≤ 5 m) so each can be incrementally verified
   - Bedrock or known-safe terrain only
   - Resolution chord at every segment end (no built-up tension)
   - Cadence on a verified safe parking spot
5. **Run `/risk-cadence`** with stricter thresholds (no half-diminished chords allowed in recovery mode).
6. **Run `/peer-review`** with **mech/safety as the chair** for recovery plans (normal cadence rotates the chair).
7. **Output** the recovery plan to `outputs/recovery/<sol>-<id>.md` with a section explicitly comparing the *as-planned* vs *as-executed* states and what changed.
8. **Lessons-learned hook.** Update `resources/flight-rules-quickref.md` if the anomaly revealed a flight rule that needs tightening.

### Decision Points

- **If the anomaly is a wheel stuck in fines:** absolutely do not re-attempt the same heading; substitute around it (Workflow 1 step 6 with stricter substitution rules).
- **If comms anomaly:** plan with reduced data-volume budget until the comms issue is resolved.
- **If mechanical:** mech/safety reviewer has hard veto on any plan that re-stresses the affected mechanism.

---

## Workflow 3: Strategic Look-Ahead Loop

**Goal:** Plan 3–10 sols ahead toward a high-value strategic target, identifying branch points and pivot waypoints.

### Steps

1. **Define the strategic horizon.** Read the campaign plan; identify the strategic target and the rough sol budget to reach it.
2. **Coarse traverse with CTX.** Use lower-resolution CTX terrain to compose a coarse traverse covering the full horizon. Each chord here represents ~10–50 m, not a single drive.
3. **Identify pivot waypoints.** Mark waypoints that work in multiple traverse keys — places where the medium-term plan can branch without re-planning the whole horizon.
4. **HiRISE-refine the next 1–2 sols.** Re-run `/terrain-assess` at HiRISE resolution for the immediate-future tiles. Coarse plan must be consistent with refined plan.
5. **Compose tactical candidates** for sol N (Workflow 1) within the strategic chord progression. Reject candidates that don't honor the medium-term progression.
6. **Run `/risk-cadence`** at *both* scales — tactical (per-segment) and strategic (per-sol). A traverse can have great tactical cadence but a poor strategic cadence (e.g., every sol ends on a half-cadence with no plagal cadence anchored on a science target).
7. **`/peer-review`** on the strategic plan happens at SOWG cadence (typically weekly), not per-sol.
8. **Update the campaign plan** in `planning/campaign.md` with the look-ahead, marked-up pivot waypoints, and any newly-identified strategic risks.

### Decision Points

- **If the strategic chord progression includes a forbidden-terrain segment:** propose a re-routing campaign to the strategic team; do not paper over with tactical heroics.
- **If the look-ahead horizon is too uncertain (e.g., new HiRISE coverage hasn't arrived):** explicitly cap the plan at the last well-known waypoint and flag the rest as "speculative — re-plan when HiRISE arrives."
- **If two strategic candidates differ only in pivot waypoint choice:** prefer the one with more pivot waypoints — it preserves replan optionality.

---

## Cross-Workflow Patterns

### When to invoke `/substitution-search` vs accept and review the original

- **Substitute first** when the flagged segment has a viable lower-risk alternative within ~15% drive-time penalty.
- **Accept and review** when the original is the only path within budget; let `/peer-review` adjudicate the trade-off explicitly.

### When the harmonic vocabulary is helping vs hurting

- **Helping:** when the planner can describe a trade-off as "I want to substitute the tritone here" and the reviewer immediately understands the move (terrain class swap, same destination).
- **Hurting:** when reviewers spend time arguing about whether something is a true ii-V-I or a deceptive cadence rather than about whether it's safe. When that happens, drop the metaphor and revert to plain rover-driver vocabulary.

### Weekly retrospective

Each week, review the decision logs in `outputs/decision-log/`. Look for:

- Patterns in dissents (the same reviewer raises the same concern repeatedly → flight rule may need updating)
- Substitutions that *should* have been used but weren't (post-hoc identification)
- Hard-rule failures that revealed a gap in `resources/flight-rules-quickref.md`

Capture the retrospective in `work-log/retros/<YYYY-WW>.md`.
