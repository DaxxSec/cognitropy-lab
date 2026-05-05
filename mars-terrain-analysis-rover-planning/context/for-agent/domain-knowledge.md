# Domain Knowledge — Mars Terrain Analysis & Rover Traverse Planning

This document is the substantive reference for the agent. It covers three things in depth: (1) Mars terrain analysis fundamentals, (2) the borrowed analytical framework from jazz composition harmony theory and how it maps onto traverse evaluation, and (3) the peer review workflow structure that governs every uplink decision.

---

## Part 1 — Mars Terrain Analysis Fundamentals

### 1.1 Orbital Datasets

| Instrument | Spacecraft | Resolution | Primary Use |
|------------|------------|------------|-------------|
| HiRISE | MRO | ~25 cm/px (orthoimage), ~1 m posting (DEM) | Tactical-scale hazard mapping; the gold standard for traverse planning |
| CTX (Context Camera) | MRO | ~6 m/px | Strategic look-ahead, landing-site selection, regional context |
| HRSC | Mars Express | 12.5 m/px (nadir), 50 m DEM | Wide-area regional DEMs |
| MOLA | Mars Global Surveyor | 463 m grid (gridded altimetry) | Global topography reference |
| THEMIS VIS / IR | 2001 Mars Odyssey | 18 m / 100 m | Thermal inertia, day/night IR |
| MARCI / CRISM | MRO | wide / hyperspectral | Weather, mineralogy |

**Coordinate systems.** Mars uses a planetocentric latitude / east-positive longitude convention for IAU 2000 / Mars 2000 datum. Local site frames are typically defined in a north-east-down or east-north-up convention rooted at landing. Always confirm which frame a DEM is in before doing slope math.

### 1.2 Deriving a Hazard Map from a DEM

A standard hazard map is a per-pixel score combining:

- **Slope** — first derivative of the DEM. Compute as `slope = atan(sqrt(dz/dx² + dz/dy²))`. Use a ≥ 3×3 window (Horn or Zevenbergen–Thorne method); single-pixel diffs are too noisy.
- **Aspect** — direction of steepest descent; matters for sun exposure (solar rovers) and for determining "downhill" if the rover slips.
- **Roughness** — local height variation at the wheelbase scale. Practical proxy: standard deviation of detrended DEM in a window matched to wheel diameter.
- **Rock abundance** — derived from orthoimage shadow analysis (Golombek et al. methods) and/or thermal inertia. Express as cumulative fractional area covered by rocks ≥ height *h*; the relevant *h* is rover-dependent.
- **Terrain class** — categorical: bedrock, regolith (rocky), regolith (fines), aeolian (ripples / dunes), conglomerate / breccia, mixed.

A useful operational hazard score:

```
hazard = w_s * slope_score
       + w_r * roughness_score
       + w_o * rock_score
       + w_c * class_penalty(terrain_class)
```

…with weights tuned per rover and per phase of mission. Numbers don't substitute for human review; the score is a *prior*, not a decision.

### 1.3 Per-Rover Mobility Capabilities (Reference)

| Rover | Wheel Ø | Max Slope | Top Speed | Notes |
|-------|---------|-----------|-----------|-------|
| Sojourner (1997) | 13 cm | ~30° | ~1 cm/s | Tethered to lander, ~100 m total |
| Spirit / Opportunity (MER, 2004) | 26 cm | ~30° static / 25° dynamic | ~5 cm/s | Solar; both significantly exceeded design life |
| Curiosity (MSL, 2012) | 50 cm | ~30° design / typically held to <20° operationally | ~4 cm/s | RTG; rocker-bogie; AutoNav available |
| Perseverance (M2020, 2021) | 52.5 cm | ~30° design | ~4 cm/s | RTG; enhanced AutoNav; 6 cameras dedicated to mobility |
| Zhurong (2021) | 30 cm | ~20° | ~5 cm/s | Solar; suspended ops 2022 |
| Rosalind Franklin (ExoMars) | ~25 cm | ~25° | varies | Solar; planned drilling to 2 m |

**Operational rule of thumb:** the *operational* slope limit is typically much tighter than the *design* limit. Curiosity, for example, has driven up to ~26° but operational planners hold to ≤ 20° as a routine ceiling. A hazard map's "drivable" pixels should reflect operational, not design, limits.

### 1.4 Common Hazard Categories

- **Steep slope** — exceeding rocker-bogie tilt limits or static stability margin
- **Rock fields** — rocks > ~½ wheel diameter for blind drive, ~⅓ wheel diameter when AutoNav handles avoidance
- **Embedded rocks** — partially-buried rocks that look benign from orbit but high-center the rover
- **Sand / aeolian features** — Spirit was lost in a sand trap (Troy, sol 1900); aeolian terrain is high-risk
- **Wheel damage substrates** — sharp embedded rocks (Curiosity wheel damage in early mission was caused by Hottah-class outcrops)
- **Communication shadows** — terrain that occludes line-of-sight to relay orbiters during planned passes
- **Thermal traps** — north-facing slopes (in southern hemisphere) that impair solar charging or run colder

### 1.5 Tactical Planning Process (Real-Mission Cadence)

For Mars 2020 and Curiosity, the tactical planning loop is roughly:

1. **Downlink** — overnight comms pass returns yesterday's imagery and engineering data
2. **Strategic Operations Working Group (SOWG)** — science team reviews downlink, sets sol N+1 priorities
3. **Tactical Planning** — engineering plus science team turns priorities into a sol plan: drive path, science block, comms windows, contingencies
4. **Uplink Approval Meeting** — the sol plan is reviewed; flight rules are checked; sequence files are generated
5. **Uplink** — sequence files transmitted to rover during the next DTE or relay pass
6. **Execute** — rover runs the sequence, takes new imagery, downlinks, loop repeats

This workspace targets steps 3–4. The peer review workflow (see Part 3) is a tactical-scale adaptation of the Uplink Approval Meeting.

---

## Part 2 — The Jazz Harmony Framework Applied to Traverse Planning

### 2.1 Why a Borrowed Framework?

Traverse planning is a multi-objective trade-off problem with a vocabulary problem. "Risky," "bold," "conservative," "aggressive," "elegant" — these are real planner words but they are imprecise. Jazz harmony is a centuries-mature analytical framework for talking about *how chords move and resolve*, and it has a remarkably clean mapping onto how traverse segments connect and cadence onto safe parking. Borrowing the vocabulary forces planners to be precise about what trade-off they are making.

### 2.2 Chord = Waypoint

A waypoint at coordinates (x, y) has a chord built from three tones:

| Tone | Possible values |
|------|-----------------|
| **Root (terrain class)** | bedrock, regolith-rocky, regolith-fines, aeolian, conglomerate, mixed |
| **Third (slope class)** | flat (< 10°), inclined (10–20°), steep (20–25°), extreme (> 25°) |
| **Fifth (science value)** | none, opportunistic, strategic, priority-1 |

The chord's **quality** comes from how the tones agree:

| Quality | Example | Meaning for traverse |
|---------|---------|----------------------|
| **Major triad** | bedrock + flat + priority-1 | Ideal — drive there, do science, sleep there |
| **Minor triad** | bedrock + flat + opportunistic | Safe stop, modest science |
| **Dominant 7** | bedrock + inclined + strategic | Wants to resolve to a major chord — pause here, but plan a resolution |
| **Half-diminished** | regolith-rocky + steep + opportunistic | Risky stop with low science return; usually not a destination |
| **Fully diminished** | aeolian + extreme + none | Forbidden — never plan a chord here |
| **Suspended** | mixed + inclined + strategic | Ambiguous — needs more data before classification |

**Hard rule:** the *resolution chord* (the final waypoint of any traverse — the safe parking spot) must be a **major** or **minor triad**. Dominant chords resolve; you don't sleep on a dominant chord.

### 2.3 Voice Leading = Segment Smoothness

Between two adjacent chords, each tone moves. A segment has **good voice leading** when those motions are smooth:

- **Slope tone moves smoothly** — slope changes ≤ 5° per metre of segment length, no contour crossings without need
- **Heading tone moves smoothly** — turn rate ≤ 30° per 5 m of segment
- **Terrain class moves stepwise** — bedrock → regolith-rocky is a stepwise motion; bedrock → aeolian is a leap (must be justified)

**Voice crossings to avoid:**
- A segment that crosses a steep slope band without need (going over a ridge when contour-following is feasible)
- A heading reversal in the middle of an unstable terrain class (the hardest place to recover from a stuck rover is the place you were trying to leave)
- A segment that requires the rover to drive *backward* over previously-unverified terrain

### 2.4 Cadence = Resolution

A **cadence** is the closing motion of a phrase. Every traverse must end on a recognized cadence:

| Cadence | Pattern | Use |
|---------|---------|-----|
| **Authentic (V → I)** | Dominant-7 chord (inclined waypoint) → safe major triad (parking) | Standard traverse-to-park |
| **Plagal (IV → I)** | Strategic but flat chord → parking | Used when there is no risky lead-in |
| **Deceptive (V → vi)** | Dominant-7 → unexpected minor (an opportunistic stop where a parking spot was planned) | When new downlink reveals a science target en route to parking |
| **Half cadence (I → V)** | Parking → dominant (next sol's start point) | The sol-N traverse ends on a half-cadence so sol-N+1 has a tension to resolve |
| **No cadence (forbidden)** | Traverse ends on a dim/half-dim chord, or with an unresolved tension | Hard fail at peer review |

### 2.5 Substitutions

When a candidate traverse contains a chord that is too risky or too low-value, substitute it. Two canonical substitutions:

#### Tritone Substitution
Replace a dominant chord with another dominant chord whose root is a tritone away. **Operational meaning:** replace a risky segment with a *different-terrain-class* segment that resolves to the **same waypoint**. Example: a segment that climbs over a rocky ridge can be substituted by a longer segment that contour-follows around it; both end at the same target waypoint.

#### Modal Interchange
Borrow a chord from a parallel "mode" (a parallel plan variant). **Operational meaning:** when the optimistic plan has a risky segment, borrow that segment's slot from the conservative plan variant. The conservative variant typically substitutes a "longer + flatter" segment for "shorter + steeper."

#### Pivot Chords
A chord that functions in two keys at once. **Operational meaning:** a waypoint that is a valid stopping point for *multiple* candidate traverses. Pivot waypoints are gold — they let you commit to a near-term traverse without locking in the medium-term plan. When composing, prefer routes that pass through pivot waypoints.

### 2.6 Tension and Resolution Pattern

Across a full traverse, plot the chord qualities in sequence. Healthy patterns:

```
I  →  ii  →  V7  →  I       (ii–V–I — the classic resolution)
I  →  IV  →  I              (plagal — quiet move)
I  →  V7  →  vi (deceptive) →  ii  →  V7  →  I   (extended phrase)
```

Unhealthy patterns:

```
I  →  vii°  →  vii°  →  vii°  →  ...   (sustained dissonance — no resolution)
I  →  V7  →  V7  →  V7  →  ...         (sustained tension — exhausting)
half-dim  →  dim  →  dim                (dissonance increasing toward end — never)
```

The `/risk-cadence` command is exactly this: walk the sequence, flag any consecutive run of dissonant chords without a resolving major/minor in between.

### 2.7 What the Framework Is *Not* For

- **Not for absolute risk quantification.** The framework structures trade-offs; it does not replace probabilistic risk assessment.
- **Not for autonomous-execution decisions.** This is a *planning* aid, not a *driving* aid.
- **Not a substitute for flight rules.** Flight rules are checked first, hard. Only candidates that pass hard rules get the harmonic analysis.
- **Not a poetry exercise.** When the metaphor obscures rather than clarifies, drop it.

---

## Part 3 — Peer Review Workflow

### 3.1 The Five Reviewer Roles

The reviewer panel is fixed at five roles. Real human reviewers should match the role; in solo / educational use, the planner plays each role in sequence and forces themselves to argue from each perspective.

| Role | Primary concern | Authority |
|------|------------------|-----------|
| **Rover Driver** | Drivability — can I actually drive this? | Hard veto on drivability |
| **Science PI** | Science return per metre / per sol | Veto on "this trades all science for nothing" |
| **Mechanical / Safety** | Slope, tilt, mechanism load, wheel wear | Hard veto on safety |
| **Autonomy Lead** | Whether AutoNav/Hazcam can handle each segment | Veto on autonomy mismatch |
| **Uplink / Comms Lead** | Pass coverage, uplink window, downlink volume | Veto on comms blackout |

### 3.2 The Scoring Rubric

Each reviewer scores the candidate on each of five axes, 1–5 (5 = excellent, 1 = unacceptable). The full rubric is in `resources/reviewer-rubric.md`; summary:

| Axis | What it measures |
|------|------------------|
| Feasibility | Can we drive it as planned? |
| Science return | What science is delivered per sol? |
| Risk profile | What can go wrong, how bad is it? |
| Comms alignment | Do passes line up with planned events? |
| Contingency coverage | Is there a recovery plan if anything goes wrong? |

### 3.3 Quorum and Veto

- **Quorum** is 4-of-5 reviewers participating. A traverse cannot be approved without at least 4 reviewers.
- **Hard fail** = any reviewer scores 1 on **risk** or **feasibility** in their primary domain. A hard fail blocks the candidate regardless of the average score. There is no "average it out."
- **Soft fail** = average score below 3. Returns to revision.
- **Pass** = all hard checks pass and average ≥ 3.5.
- **Strong pass** = average ≥ 4.5 and no individual score below 3.

### 3.4 Dissent Capture

A reviewer who is outvoted but disagrees has their dissent recorded *verbatim* in the decision log:

```
DISSENT — Reviewer: <role>
Position: <candidate approved / rejected> against my recommendation.
My concern: <verbatim>
What would change my position: <verbatim>
```

Dissents are not averaged out. If a future incident relates to a dissent, the dissent is the first thing the post-mortem reads.

### 3.5 The Decision Log Schema

Every `/peer-review` run produces a decision-log entry written to `outputs/decision-log/<sol>-<traverse-id>.md`:

```yaml
sol: <N>
traverse_id: <id>
candidate_path: <hash of waypoint sequence>
reviewers:
  rover_driver: { name: <>, score: { feas: 4, sci: 3, risk: 4, comms: 5, cont: 4 } }
  science:     { name: <>, score: { feas: 4, sci: 5, risk: 3, comms: 4, cont: 4 } }
  mech_safety: { name: <>, score: { feas: 4, sci: 3, risk: 4, comms: 5, cont: 4 } }
  autonomy:    { name: <>, score: { feas: 5, sci: 3, risk: 4, comms: 5, cont: 4 } }
  comms:       { name: <>, score: { feas: 4, sci: 3, risk: 4, comms: 5, cont: 4 } }
quorum: 5/5
hard_fails: []
average: 4.04
decision: PASS
dissents:
  - role: science
    text: "Recommend extending dwell at WP-3 by 30 min for SuperCam raster"
revision_history:
  - rev1: composed (chord sequence: I → ii → V7 → I)
  - rev2: substituted segment 2 (tritone sub: rocky climb → contoured detour)
  - rev3: passed peer review
```

This file is the *sole* source of truth for "why was this traverse uplinked." Future post-mortems and lessons-learned reference it directly.

### 3.6 When the Review Loops

A typical revision loop:

1. `/traverse-compose` produces candidate v1
2. `/risk-cadence` flags an unresolved tension at segment 4
3. `/substitution-search` proposes a tritone substitution; planner accepts → candidate v2
4. `/peer-review` runs on v2; mech/safety scores risk = 2 (soft fail)
5. Planner revises segment 6 — adds a contingency parking waypoint → candidate v3
6. `/peer-review` re-runs on v3; passes 4.2 average, no hard fails → uplink

The decision log captures all three revisions and the reasons for each.
