# /calibration-audit — Audit a Puppet's Calibration State

Run a structured calibration audit against a puppet's baseline. Treat the puppet as a configuration item; treat divergence from baseline as a config-drift finding.

## Required Inputs

- `--puppet <slug>` — the puppet to audit
- `--reason <text>` — why this audit is happening: `pre-show`, `post-travel`, `post-repair`, `scheduled`

## Steps

### 1. Load Baseline

Read `outputs/baselines/<slug>.yml`. If missing, this is the puppet's first audit — the audit becomes the baseline-establishing audit. Mark the output accordingly.

### 2. Walk the Per-Type Checklist

#### String marionette
- Per-string length measurement (mm). Compare against baseline; record `delta_mm`.
- Per-string tension at rest (in "felt-as" units if no FSR; in newtons if instrumented).
- Hinge friction at each named joint (small spring scale: g of force needed to start motion).
- Rest-pose photo or video frame capture; reference path.

#### Bunraku triple-actor figure
- Per-string and per-rod measurement on each of the three control rigs.
- Costume rig: kimono-mass distribution; weight cue points.
- Head-mech: eye and mouth travel ranges.

#### Wayang shadow puppet
- Per-rod length and rod-to-body anchor security.
- Hide flatness (warp / curl) — critical for screen-distance behavior.
- Backlight calibration: lumens at the screen plane at the dalang's standard distance.

#### Hand / rod (Henson-school)
- Foam-mech mouth travel: max-open and max-closed positions.
- Foam-mech mouth recovery time after 30-cycle stress test (target <1 second to within 0.5 mm of baseline).
- Eye-focus axis check (5° tolerance).
- Rod-arm play / slop measurement.

#### Animatronic
- Per-axis servo offset (commanded zero vs. actual zero, in degrees).
- Per-axis travel range; compare to baseline.
- Per-axis current-draw spectrum at idle (broadband noise above 30 Hz indicates bearing wear).
- Ambient temperature at audit time (servos are temperature-dependent).

#### Stop-motion armature
- Per-joint torque-to-hold (g of force the joint will hold before slipping).
- Surface skin condition (latex tearing, paint loss, hair displacement).

### 3. Compute Drift

For each tracked dimension, compute `delta = current - baseline`. Apply per-dimension tolerance from the baseline file. Produce a finding for each dimension exceeding tolerance:

```yaml
- dimension: right-shoulder-string-length
  baseline: 612.0 mm
  current: 616.4 mm
  delta: +4.4 mm
  tolerance: 3.0 mm
  finding: drift-exceeds-tolerance
  severity: medium
  proposed_action: re-tune via airplane-control adjustment screw
```

### 4. Tag Findings to the Failure-Mode Catalog

Each finding must reference a tactic / technique cell from `resources/puppet-mechanism-failure-modes.md` for traceability into the rule set.

### 5. Write Audit Output

Output to `outputs/audits/<YYYY-MM-DD>-<slug>.md`. Append a one-line summary to `work-log/<date>.md` so the audit is visible in the next `/post-show-report`.

### 6. Decide Next Action

For each finding:
- **No action** — within tolerance after re-measure.
- **Adjust now** — within rigger's adjustment range (e.g. tuning screw); make the adjustment and re-measure.
- **Schedule maintenance** — beyond field adjustment; queue in `planning/<slug>-maintenance.md`.
- **Refresh baseline** — if a deliberate rebuild has occurred (new strings, new servo, etc.), rotate the baseline. The new baseline must be peer-reviewed (`/peer-review --target outputs/baselines/<slug>.yml`).

### 7. If This Is The First Audit (Establishing the Baseline)

Write the baseline to `outputs/baselines/<slug>.yml` with per-dimension tolerances. Tolerances default to:
- String length: 3 mm
- Hinge friction: 5 g
- Servo offset: 1° (hobby-grade) / 0.1° (industrial-grade)
- Foam mouth travel: 1 mm
- Mouth recovery time: 0.2 s

Refine tolerances after 3+ audits using the per-dimension empirical noise floor.

## Output

- `outputs/audits/<date>-<slug>.md` — the audit record
- Updated baseline at `outputs/baselines/<slug>.yml` if applicable
- Findings queued for maintenance in `planning/`

## Failure Modes

- **No measurement instruments at hand.** Audit can run in narrative-only mode; findings carry severity `unmeasured` and warn that baseline-anchored detection rules will not be evaluable.
- **Baseline is over a year old and the puppet has been heavily used.** Recommend a baseline refresh before the audit, peer-reviewed.
