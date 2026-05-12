# Environment

> Populated and refined by `/onboard`. Describes the company's stage / studio / shop environment and what motion data the agent can rely on.

## Instrumentation Tier

The workspace runs at four ascending tiers — pick what your company has, the agent adapts the workflows to it.

### Tier 0 — Notebook Only

- No video, no sensors. Logs are entirely free-text observations.
- `/movement-log` works in pure-narrative mode; the puppeteer dictates events the agent timestamps.
- Detection rules in this tier are restricted to "manipulator-input" + "audience-observation" event categories.
- Suitable for: small marionette troupes, traditional puppetry studios without budget for instrumentation.

### Tier 1 — Video

- Two camera angles minimum (front + side; or front + above for marionettes).
- Frame-accurate timecode (drop-frame timecode-burned video, or mux-locked SMPTE).
- `/laban-tag` operates against the video; the agent guides frame-by-frame Effort annotation.
- Detection rules can read a `video_annotation` event category.

### Tier 2 — Video + Manual Calibration Logs

- Tier 1 plus periodic measurement sessions (`/calibration-audit`) that record string lengths, hinge friction (with a small spring scale), servo offsets, foam-mech mouth travel.
- Detection rules can compare against a per-puppet baseline.

### Tier 3 — Video + Sensors

- IMUs (e.g. MetaMotion R, X-IMU3) on rigging or puppeteer's hands.
- Force-sensitive resistors on string anchors (Spectra strings can be cyanoacrylate-bonded to a small FSR pad without affecting performance).
- Servo telemetry from animatronic figures (Dynamixel, Robotis OpenRB-150 line, or theme-park standard buses).
- Detection rules at this tier are quantitative across `joint_event`, `string_tension`, `servo_telemetry`, `imu_event`.

## Stage / Studio Layout

Record per the company's spaces:

- **Rehearsal room dimensions and lighting** — affects shadow-puppet (wayang) detection rule baselines.
- **Performance venue range** — touring vs. resident affects expected travel-shock failure rate.
- **Climate** — humidity range affects foam latex hysteresis rules; temperature range affects servo offset rules.
- **Network** — entirely offline workspaces are supported; the workspace has no required network calls.

## Filesystem Layout

This repo lives at the company's standard project location. Recommended:

```
~/companies/<company>/<production>/puppetry-movement-mechanics/
```

`work-log/`, `outputs/rules/active/`, `outputs/reviews/` are version-controlled with `git`. `outputs/baselines/` is also tracked. Raw video is **not** stored in this repo — videos live in the company's media storage and logs reference them by URI.

## Operating System and Tooling

- Linux, macOS, Windows — the workspace is OS-agnostic.
- Required: `git`, a markdown-aware editor.
- Optional: `python3` (for small DSP scripts in `outputs/`), `ffmpeg` (for video timestamp extraction), `yamllint` (for rule schema linting).
