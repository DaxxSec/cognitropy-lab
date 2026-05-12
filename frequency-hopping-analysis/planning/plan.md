# Active Analysis Plan

> Updated by `/onboard` and after each engagement. Pivots go in `planning/pivots/`.

## Current Status

- **Engagement:** (none yet — run `/onboard`)
- **Calibration:** not run
- **Workflow phase:** PERSONALIZE (awaiting `/onboard`)

## Calibration Plan

Mandatory before any unknown-signal analysis. See `prompts/bluetooth-classic-calibration.md`.

| Step | Status | Output |
|------|--------|--------|
| Phone in BT pairing mode | pending | — |
| 80 MS/s, 1 s, 2.441 GHz capture | pending | `outputs/calibration-<date>/calibration.iq` |
| `/hop-detect` | pending | `outputs/calibration-<date>/hop-detect.json` |
| `/hop-set-prior --system bluetooth-classic` | pending | `outputs/calibration-<date>/hop-set-prior.json` |
| `/dehop-bayes` | pending | `outputs/calibration-<date>/dehop/` |
| `/sequence-id --system bluetooth-classic` | pending | `outputs/calibration-<date>/sequence-id.json` |
| Cross-validate against gr-bluetooth | pending | `outputs/calibration-<date>/calibration-report.md` |

Pass criteria:
- P(hopping) > 0.95
- Hop rate posterior peaked in [1590, 1610] hops/s with > 0.9 mass
- K = 79 with > 0.9 posterior mass
- Sequence type = "table" with > 0.7 mass
- LAP recovered
- > 90% per-dwell agreement with gr-bluetooth ground truth

## Engagement Plan

(populated by `/onboard`)

## Open Questions

- Q1: ?
- Q2: ?

## Next Action

Run `/onboard`.
