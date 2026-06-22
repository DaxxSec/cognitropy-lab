# Pyrotechnics Choreography Timing — Core Concepts

Background to read before acting. Two halves fused: **display choreography** (the timed, safety-critical artifact) and **formal verification** (how we argue it correct). Optimised for fast recall, not exhaustive theory. Scope is planning/verification for licensed operators firing manufactured devices — no chemistry, no manufacture.

## The Cue as the Atomic Unit

A **cue** is one scheduled firing event. The canonical model used throughout this workspace pins these fields per cue:

- `id` — stable identifier (e.g. `F1-12`).
- `t_fire` — absolute fire time from show T0, the instant the e-match is energized.
- `device` / `effect` — the product and what it does (see taxonomy below).
- `position` / `rack` — where it sits on the site (x, y) and which mortar/rack/angle.
- `channel` — firing-module address (module, pin) that energizes the e-match.
- `lift` / `tof` — time-of-flight: delay from `t_fire` to the visible effect (break/ignition).
- `t_effect = t_fire + tof` — when the audience sees it. **The number that matters artistically.**
- `duration` — how long the effect is visibly "live" in the air or on the ground.
- `t_clear` — when fallout/debris has descended below the danger height (≈ `t_effect + descent_time`).
- `radius` — fallout/effect radius used for separation (drifts downwind).

Two timelines coexist: the **firing timeline** (`t_fire`, what the system commands) and the **visual timeline** (`t_effect`, what the crowd sees). Conflating them is the #1 bug.

## Effect Taxonomy (timing-relevant properties)

| Class | Examples | Lift / ToF | Notes for timing |
|---|---|---|---|
| Aerial shells (mortars) | peony, chrysanthemum, willow, ring | 2–5 s rise, breaks at apogee | ToF scales with bore; willows hang ~6–8 s |
| Multishot / cakes | 25–500 shot "cakes" | per-tube internal delay | internal fuse fixes inter-shot timing; you cue the *start* only |
| Mines / fronts | gerbs, mine bags | ~0 s (ground-up) | effect is immediate; short ToF, near-zero |
| Comets / shots | single rising stars | 0.5–2 s | low ToF; common music accents |
| Set pieces / lances | ground portraits, wheels | ignition spread | long duration; treated as one long-lived cue |
| Flame / proximate | flame projectors, gerbs, close shells | immediate | NFPA 1126 regime; tight distances, indoor air |

## Time-of-Flight and Pre-Fire Compensation

To make an aerial effect break **on** a musical beat at time `b`, you must fire it **early**:

```
t_fire = b − tof(device)        # fire ahead by the time of flight
```

Time-of-flight rises roughly with shell bore. Rule-of-thumb apogee/ToF (see references): a 3" shell ~ 2.5 s to break; 6" ~ 4 s; 12" ~ 6 s. Software like Finale 3D models this, but exported cue lists vary in whether `t_fire` or `t_effect` is the listed time — **always confirm which timeline the export uses** before verifying.

## Safety Distances and Fallout Geometry

The dominant *spatial* constraint. Outdoor display (NFPA 1123) minimum spectator separation is commonly summarized as **≥ 70 ft per inch of shell bore** (so a 6" shell ⇒ ≥ 420 ft radius), with the AHJ permit potentially stricter. Fallout (spent stars, casing) descends and **drifts downwind**; the effective danger footprint is the break point shifted by `wind_vector × descent_time`. Proximate pyrotechnics (NFPA 1126) uses far smaller, product-rated distances and adds overhead/clearance and indoor-air constraints. Two effects are **separation-safe** iff their (possibly drifted) danger footprints do not overlap *while either is still live*.

## Firing Systems and Channel Budgets

- **E-match / igniter:** one-shot electric initiator; one per cue (or paralleled within current limits).
- **Firing module / rail:** addressable box with N pins; cues map to (module, pin). A pin fires once.
- **Time code:** shows run on an internal clock or SMPTE timecode locked to the audio (so video/lighting/pyro share T0).
- **Current budget:** a module sourcing many simultaneous e-matches has a max simultaneous-fire count / current ceiling. Firing K matches within the module's settle window must satisfy `K ≤ max_simultaneous`. Violating it ⇒ some matches don't fire (duds) — a *resource* obligation, not just a timing one.
- **Chain / hard-wired finale:** dense finales often parallel many tubes on few channels; the allocation must respect both the current budget and the separation geometry.

## The Show as a Timed System (formal-methods half)

We model the schedule as a **timed system** and the rules as **specifications** to discharge:

- **Timed automaton / trace model.** Cues are timed events on a shared clock; the verifier reasons over the trace `{(id, t_fire, t_effect, t_clear, position, channel)}`. Tools: **UPPAAL** (timed automata, native clock constraints), **TLA+/TLC** (bounded checking of a discrete-time model), **Z3/SMT** (encode intervals + geometry as constraints and check `unsat` = no violation).
- **Proof obligation.** A named property the schedule must satisfy. Each is `discharged` (proved), `refuted` (counterexample found), `open` (not yet checked), or `assumed` (taken as a premise, e.g. "wind ≤ 15 mph"). The set of obligations is the **spec catalog**; tracking their status over revisions is the **proof ledger**.
- **Counterexample.** A concrete witness to a violation: *"cue F1-07 (`t_clear`=64.8 s) and F1-09 (`t_fire`=63.1 s) overlap in the SW position by 1.7 s; fallout footprints intersect at the crowd line under 12 mph SW wind."* A counterexample is actionable; a bare "unsafe" is not.
- **Temporal logic.** Express timed properties compactly. **MTL/STL** allow timed operators — e.g. *globally, between any two cues at the same position, `t_fire(next) − t_clear(prev) ≥ 0`*; STL adds a **robustness margin** (how much slack), which is exactly the "we cleared the window by 1.4 s" number you want to report.
- **Invariant vs. liveness.** Most obligations here are **safety/invariant** properties ("nothing bad ever happens" — no overlap, no over-current). The artistic ones are bounded-time properties ("the hero shell breaks within ±80 ms of the beat").

## Canonical Proof Obligations (the recurring catalog)

| ID | Obligation | Type | Discharged by |
|---|---|---|---|
| SEP | No two live effects' danger footprints overlap | safety / geometry+interval | `/separation-proof` |
| REUSE | A mortar/position is not re-cued before its previous shell clears | safety / interval | `/verify-schedule` |
| CURR | Simultaneous e-match count per module ≤ current budget | resource | `/rack-allocation` |
| CHAN | No firing channel is double-booked | resource | `/rack-allocation` |
| RUNTIME | Total show time ≤ music/track length (+ permitted tail) | bounded-time | `/verify-schedule` |
| SYNC | Each hero cue's `t_effect` within ±τ of its beat | bounded-time / STL | `/beat-sync-check` |
| FALLOUT | All drifted footprints stay outside the spectator line & no-fire zones | safety / geometry | `/separation-proof`, `/weather-gate` |
| DENSITY | ≤ N effects live simultaneously (sky-clutter / visibility) | invariant | `/verify-schedule` |

## Common Failure Modes

- **Fire-time / effect-time conflation** — comparing a beat to `t_fire` instead of `t_fire + tof`; the accent lands a full time-of-flight late.
- **Uncompensated time-of-flight** — bigger shells need more pre-fire; a mixed-bore accent chain breaks raggedly if each isn't compensated by its own ToF.
- **Reuse-before-clear** — re-firing a position while the previous shell's fallout is still descending into it.
- **Wind-shift fallout** — a separation that holds in still air fails when fallout drifts downwind toward the crowd; verify the worst-case forecast vector, not nominal.
- **Channel double-book / over-current** — finale chains that exceed the module's simultaneous-fire budget produce silent duds.
- **Runtime overrun** — the show outlasts the music; the last 6 seconds fire to silence.
- **Sky clutter** — too many effects live at once; individually safe, collectively unreadable (and harder to spot a malfunction).
- **Assuming instead of proving** — marking an obligation "fine" without a discharge; the ledger must distinguish `assumed` from `discharged`.

## Operating Constraints

- Licensed operator + AHJ permit + manufactured devices assumed throughout. NFPA 1123 (outdoor) / NFPA 1126 (proximate) set the safety floor; the permit may be stricter and always governs.
- All distances/times carry units and a cited source table; the model is only as trustworthy as its inputs (device ToF, fallout radius, wind forecast).
- Verification results are *modeling* statements — they inform, never replace, the on-site judgment of the licensed shooter and the AHJ.
