# Domain Knowledge — Puppetry Movement Mechanics × Detection Engineering × Peer Review

This file is the agent's substantive reference. Read it before any session that involves authoring rules, reviewing rules, or interpreting movement logs. It covers four bodies of knowledge and how they map onto each other.

## 1. Puppetry Traditions and Their Mechanics

Different traditions stress different mechanisms; failure modes follow.

### 1.1 String Marionettes (Czech, English, French, US-touring)

- **Control rigs.** Two dominant forms: the **airplane control** (a horizontal yoke held parallel to the puppet's shoulder line; used for human-form marionettes; allows independent shoulder, elbow, wrist, knee tilts) and the **paddle control** (a vertical paddle held perpendicular; used for animals, where the spine and head dominate).
- **Typical articulation count.** A full human-form Czech-tradition marionette runs **14–20 control points**: head tilt, head turn, shoulders × 2, elbows × 2, wrists × 2, hips, knees × 2, ankles × 2, plus optional mouth, brow, eye-track.
- **String materials.** Spectra (UHMWPE), braided polyester, monofilament, waxed linen. Each has different stretch / creep behavior under sustained tension. **Spectra creeps under load by ~1–2% over the first 24 hours**, then stabilizes. Polyester relaxes faster but absorbs humidity, which changes effective length by ~0.5–2% across a tour through varying climates.
- **Control-bar drift.** Over a tour, the most common failure mode. Cause: differential string creep across the rig. Detection: compare the puppet's "rest pose" against a calibration baseline (`/calibration-audit`).
- **Pendulum dynamics.** A marionette limb is a forced damped pendulum. The puppeteer's hand input is the forcing function. Natural frequency `f ≈ (1/2π)·√(g/L)` for a simple limb of effective length `L`. For a 30 cm forearm: `f ≈ 0.91 Hz`. Lifelike movement uses controlled phase relationships with this natural frequency; mechanical drift shifts `L` and detunes the relationship.
- **Double-pendulum chaos.** A two-segment limb (upper-arm + forearm) with two independent string controls is a driven double pendulum and exhibits sensitive dependence on initial conditions. Detection rules for "double-pendulum chaos onset" watch for high-frequency wobble in the wrist trace after a settled gesture.

### 1.2 Bunraku / Ningyō Jōruri (Japan)

- **Triple-actor system.** Three puppeteers operate one figure: **omozukai** (head + right arm; dominant performer, often the only one whose face is unhooded), **hidarizukai** (left arm), **ashizukai** (legs / feet, or a sash for female puppets — female bunraku puppets often have no legs, the kimono is manipulated to suggest them).
- **Coordination is the central challenge.** All three puppeteers work blind to each other's full intent; coordination relies on breath, weight cues through the puppet's frame, and decades of trained ensemble habit. A fourteen-second cross-stage move can require ~40 micro-adjustments distributed across the three actors.
- **Typical timing tolerance.** Senior bunraku ensembles target **<50 ms phase lag** between omozukai head-turn and hidarizukai counter-arm. Training ensembles run at 100–200 ms; "unintegrated" feel emerges past ~250 ms.
- **Detection target.** Phase-lag drift between actors; detect by comparing timestamped joint events from the three actors' input channels (or by Laban-tagging video at frame granularity).

### 1.3 Wayang Kulit (Indonesian Shadow Puppetry)

- **The dalang** is puppeteer + narrator + musical director simultaneously, controlling 30–100 puppets in a single performance.
- **Puppet construction.** Buffalo hide, perforated and painted, with horn rods (typically 3 — body rod plus two articulated arms).
- **Screen mechanics.** The puppet is held against a backlit screen (kelir). Critical variable: distance between puppet and screen. **At 0–2 cm, silhouette is sharp; at 5+ cm, the silhouette softens and gains an aura.** Both effects are dramaturgically used. Drift between intent and actuality is a common failure.
- **Detection target.** Screen-distance drift over a long performance. Optical detection from front-of-screen video.

### 1.4 Hand and Rod Puppets (Henson-school, Sesame, Muppet)

- **Mouth mechanism.** Live-hand puppets use a foam-latex mouth driven directly by the puppeteer's thumb against the upper palate; rod-arm puppets have separately-rodded arms. The mouth is the highest-stress mechanism.
- **Foam-latex hysteresis.** Foam latex compresses under repeated cycling and slowly recovers. After ~200 mouth cycles, full recovery to baseline shape takes ~30 seconds. After a tour, baseline shape may have permanently shifted by 1–3 mm.
- **Eye-focus convention.** Henson-school rule: the puppet's eyes converge on the implied audience focal point ~2 m in front of the camera lens; a 5° drift in either eye reads as "dead eyes" or "crossed".
- **Detection target.** Mouth-mech recovery time; eye-focus drift; arm-rod-end positional jitter.

### 1.5 Animatronics (Theme park, film creature)

- **Servo-driven actuators.** RC-style hobby servos for low-force axes; harmonic drives or hydraulic actuators for high-force axes (jaws, large limbs).
- **Servo creep.** Standard hobby-grade servos (e.g. HS-805BB, MG996R class) drift their zero-point by ~1–3° over a 12-hour day under typical theme-park duty cycles. Industrial-grade servos (e.g. Dynamixel Pro, harmonic-drive units) drift <0.1°.
- **Temperature dependence.** Servo offset has a documented temperature coefficient; outdoor figures need temperature-compensated calibration. A 10°C ambient swing typically produces 1–4° offset shift on hobby-grade servos.
- **Detection target.** Per-axis offset drift, jitter spectrum (servo bearing wear shows up as broadband noise above 30 Hz), end-stop overshoot.

### 1.6 Stop-Motion (Aardman, Laika, Coraline-style)

- **Frame rates.** 24 fps is the default; "on twos" (12 fps captured, each frame held for 2) is the default working rhythm; "on ones" (24 fps full animation) reserved for fast action.
- **Arc-of-motion principle.** Joints describe arcs, not straight lines. A "linear" arm move reads as mechanical / robotic. Disney's twelve principles (Thomas & Johnston, *The Illusion of Life*, 1981) codify this.
- **Detection target.** Arc tightness on follow-through, ease-in / ease-out timing, squash-and-stretch ratios.

## 2. Motion Physics Useful for Rule Authoring

### 2.1 Pendulum Equations (Marionettes)

For a simple pendulum of length `L` under gravity `g = 9.81 m/s²`:

- Natural frequency: `f = (1/2π)·√(g/L)`
- Period: `T = 2π·√(L/g)`
- A 50 cm leg swings naturally at ~0.7 Hz (period ~1.4 s).

Implication for detection: a leg whose observed sway frequency drifts more than ~10% from its baseline is showing string-length drift (effective `L` changed) or a hinge friction change (damping changed).

### 2.2 String Tension and Stretch

- Spectra (UHMWPE): Young's modulus ~110 GPa, very low creep at typical marionette tensions (<5 N).
- Polyester braid: lower modulus, higher creep, hygroscopic.
- Stretch under tension: `ΔL = L·F / (E·A)` where `F` = tension, `E` = Young's modulus, `A` = cross-section.
- For a 60 cm Spectra string at 3 N: `ΔL ≈ 0.08 mm` — negligible per-event but accumulates to ~1.5 mm over a tour.

### 2.3 Foam Latex Hysteresis

- Foam latex (the Henson formulation) recovers from compressive strain with two time constants: a fast spring-back (~200 ms) and a slow viscoelastic creep (~10–60 seconds).
- A mouth mechanism cycled at 3 Hz never fully relaxes to baseline; it operates around a partially-compressed equilibrium that drifts over a performance.

### 2.4 Servo Telemetry Primitives

- **Position error** = commanded position − actual position. Drift in error mean indicates calibration drift; drift in error variance indicates bearing wear.
- **Current draw spectrum.** A healthy servo's current spectrum has a clean fundamental at the commanded frequency plus harmonics at <-30 dB. Bearing wear introduces broadband noise above 30 Hz.

## 3. Detection Engineering Methodology (SOC / SIEM)

This section is the practitioner-level summary of the methodology being transplanted.

### 3.1 The Sigma Rule Format

Sigma is the open generic format for SIEM rules ([github.com/SigmaHQ/sigma](https://github.com/SigmaHQ/sigma)). The shape:

```yaml
title:        Short human title
id:           UUID
description:  What this rule detects
status:       experimental | test | stable | deprecated
date:         2026-05-01
author:       name(s)
references:   [URLs / log examples]
logsource:
  product:    (e.g. windows | sysmon | aws-cloudtrail)
  category:   (e.g. process_creation)
detection:
  selection:
    field1:   value
    field2|contains: substring
  filter:
    field3:   benign-value
  condition:  selection and not filter
falsepositives:
  - known benign cause 1
level:        low | medium | high | critical
tags:         [attack.tactic.id, attack.technique.id]
```

**The puppetry adaptation** (full schema in `resources/sigma-rule-template-puppetry.md`) keeps the same shape but renames `logsource.product` to `puppet_type` and `logsource.category` to `event_category` (joint_event, string_tension, manipulator_input, audience_observation, video_annotation).

### 3.2 The MITRE ATT&CK Matrix Shape

ATT&CK ([attack.mitre.org](https://attack.mitre.org/)) is a tactic-by-technique matrix. Tactics are the *why* (e.g. *initial access*, *persistence*); techniques are the *how* (e.g. *spearphishing attachment*).

**The puppetry analogue** (full taxonomy in `resources/puppet-mechanism-failure-modes.md`):

| Tactic | Example Techniques |
|---|---|
| string-system-drift | gradual-stretch, hygroscopic-shrink, knot-slippage |
| servo-axis-drift | zero-point-creep, temperature-offset, bearing-wear-jitter |
| foam-latex-fatigue | mouth-mech-hysteresis, brow-mech-permanent-set, jaw-skin-tear |
| ensemble-sync-loss | handoff-lag, breath-cue-miss, weight-cue-miss |
| screen-geometry-drift | screen-distance-shift (wayang), backlight-flicker |
| arc-of-motion-failure | linear-interpolation-leak (stop-motion), follow-through-clipped |
| performer-fatigue | grip-tremor, off-axis-loading, calibration-skip |
| environment-induced | thermal-shift, humidity-shift, travel-shock-misalignment |

Every detection rule must tag `tactic:<...>` and `technique:<...>` from this taxonomy. New techniques are added via peer review.

### 3.3 Detection Engineering Maturity

After Anton Chuvakin's Detection Engineering Maturity Model (2022–2024), the rule lifecycle is:

1. **Hypothesis** — "I think this pattern keeps recurring."
2. **Draft** — `outputs/rules/draft/<rule>.yml`. Specifies log source, selection, condition, expected false-positive sources.
3. **Peer Review** — red / blue / purple roles; written disposition; `outputs/reviews/<date>-<rule>.md`.
4. **Active** — `outputs/rules/active/<rule>.yml`. Used by `/detect-anomaly`.
5. **Tuned** — version bumped; reviewer-of-record updated.
6. **Retired** — moved to `outputs/rules/retired/<rule>.yml` with a retirement rationale; never deleted (institutional memory).

### 3.4 Backtesting (Regression Testing for Detections)

When a rule is tuned, replay it against the historical `work-log/` corpus and compare which past anomalies it now catches vs. previously caught. This is `/detect-anomaly --backtest`.

## 4. Laban Movement Analysis (LMA)

Rudolf Laban's framework (consolidated by Lisa Ullmann in *The Mastery of Movement*, 4th edition, 1980) is the canonical descriptive vocabulary for human movement and is widely used in puppetry training. Four categories:

- **Body** — what is moving (whole, head, limb, joint).
- **Effort** — *how* it moves, along four "factors":
  - **Weight**: Light ↔ Strong
  - **Time**: Sustained ↔ Sudden
  - **Space**: Indirect ↔ Direct
  - **Flow**: Free ↔ Bound
  - The eight named "Effort Actions" (Float, Punch, Glide, Slash, Dab, Wring, Flick, Press) are the eight corners of the Light/Strong × Sustained/Sudden × Indirect/Direct cube.
- **Shape** — the form the moving body assumes (Spreading, Enclosing, Rising, Sinking, Advancing, Retreating).
- **Space** — pathways through external space (kinesphere, planes, dimensional scale).

**Why the agent uses LMA.** Some failure modes are kinematically subtle but Effort-readable. A puppet whose mouth-mech is slightly degraded reads as Light-Bound where the director called for Strong-Free. The `/laban-tag` command annotates segments with Effort qualities; rules can then fire on Effort-quality drift, not just joint-angle drift.

## 5. Peer Review Workflow

The workspace's peer-review structure transplants directly from cybersecurity detection-engineering practice.

### 5.1 Roles

- **Red** — *try to break the rule*. Construct synthetic logs (or recall real logs) where the rule should fire but does not, or fires but should not.
- **Blue** — *validate the detection covers the failure*. Confirm that on the rule's stated example logs, the rule fires correctly. Confirm tags are correct.
- **Purple** — *collaborative tuning*. Suggest threshold / window / field changes; explicitly named for cross-perspective improvement (puppeteer ↔ rigger; senior ↔ trainee; tradition-bearer ↔ detection-engineer).

### 5.2 Disposition Vocabulary

The `/peer-review` command writes one of:

- `accepted` — rule moves to active.
- `tune <field>` — rule needs change before acceptance; the named field is the one to change.
- `reject` — rule is not the right shape; close the draft, log rationale.
- `escalate` — disposition cannot be reached at this review level; escalates to senior tradition-bearer or company lead.

Full disposition language reference in `resources/peer-review-disposition-language.md`.

### 5.3 The "Two Reviewers, Distinct Roles" Rule

Adapted from Splunk and Elastic detection-engineering practice: every rule needs at least two reviewers, and the two reviewers must be in distinct roles (e.g. puppeteer + rigger, not puppeteer + puppeteer). This is the single most important constraint — it is what prevents the company from accumulating a rule set that only catches the failures one perspective is sensitive to.

## 6. The Crossover Methodology in One Sentence

Capture rehearsals as structured event logs; encode recurring failure patterns as Sigma-style YAML rules with mandatory tags from a MITRE-shaped failure-mode taxonomy; gate every rule through two-reviewer red / blue / purple peer review with written dispositions; backtest tuned rules against the historical log corpus before they re-enter the active set.
