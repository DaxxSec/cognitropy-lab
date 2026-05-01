# Sigma Rule Template — Puppetry Adaptation

> Adapted from the [Sigma project](https://github.com/SigmaHQ/sigma) generic detection rule format. Use this exact schema in `outputs/rules/draft/<slug>.yml` and `outputs/rules/active/<slug>.yml`.

## Schema

```yaml
title:        # short human title (≤80 chars)
id:           # UUIDv4
description: |
  # one-or-many paragraph rationale
status:       # experimental | test | stable | deprecated
date:         # YYYY-MM-DD
modified:     # YYYY-MM-DD (only on subsequent versions)
version:      # semver; bump on any field change
author:       # name(s); comma-separated for co-authors
references:
  - # work-log/<file>.md (mandatory: at least 2 logs)
  - # external reference (book, article, video URI)
puppet_type:  # marionette | bunraku | wayang | hand-rod | animatronic | stop-motion | *
event_categories:
  # at least one of:
  - joint_event
  - string_tension
  - manipulator_input
  - audience_observation
  - video_annotation
  - imu_event
  - servo_telemetry
detection:
  selection:
    # field-by-field criteria; supports modifiers below
  filter:
    # optional benign-case suppression
  condition: # boolean over named blocks: e.g. "selection and not filter"
falsepositives:
  - # at least one entry; named situations that fire benignly
level:        # informational | low | medium | high | critical
tags:
  - tactic.<id>          # mandatory
  - technique.<id>       # mandatory
  - tradition.<name>     # optional, for tradition-specific rules
```

## Field Modifiers

Sigma's standard modifiers (`|contains`, `|gt`, `|lt`, `|startswith`, `|endswith`, `|all`) plus puppetry-specific extensions:

| Modifier | Operates on | Example |
|---|---|---|
| `\|contains` | string | `note\|contains: "stuck"` |
| `\|gt` | number | `delta_mm\|gt: 3.0` |
| `\|lt` | number | `recovery_seconds\|lt: 0.5` |
| `\|in` | list | `puppet\|in: [prospero, ariel]` |
| `\|drift_from_baseline_gt` | number | `string-length\|drift_from_baseline_gt: 4mm` |
| `\|effort_quality` | LMA code | `effort_observed\|effort_quality: Light-Bound` |
| `\|phase_lag_gt` | duration | `omozukai-hidari\|phase_lag_gt: 100ms` |
| `\|window` | event window | `\|window: { span: 3, unit: events }` |

## Status Lifecycle

- `experimental` — fresh draft; never auto-fires (only fires when `/detect-anomaly --include-experimental` is set explicitly).
- `test` — passed first peer review; fires by default; not yet considered stable.
- `stable` — has spent 30+ days as `test` with no `tune` dispositions in any review.
- `deprecated` — replaced or retired; retained for git history; never fires.

## Level Guidance

| Level | When |
|---|---|
| `informational` | Rule logs an interesting pattern but takes no maintenance action |
| `low` | Worth noting in `/post-show-report`; no immediate action |
| `medium` | Tune mechanism within next maintenance window |
| `high` | Tune before next show |
| `critical` | Do-not-fly; safety-relevant; hold show until resolved |

`critical` rules require unanimous reviewer acceptance plus a tradition-bearer's sign-off.

## Naming Convention

Rule slug = kebab-case `<tactic>-<short-symptom>` — e.g. `string-system-drift--right-shoulder-stretch`. Slugs are stable; if a rule's scope changes substantively, retire and replace rather than rename.

## Example Rule (Right-Shoulder Stretch)

```yaml
title: Right-shoulder support stretches past tuning band
id: 9d3e4a02-f0a1-4f8e-9c1c-1b2a4f5d6e7f
description: |
  On Czech-tradition airplane-control marionettes during 4–6 month tours,
  the right-shoulder support string accumulates Spectra creep beyond the
  per-puppet tuning band, producing a ~3% downward shoulder drop visible
  in the rest pose between scenes. The pattern is bilateral but right
  fires earlier because most performers' dominant pull-side stresses
  the right support more.
status: experimental
date: 2026-05-01
version: 1.0
author: lena
references:
  - work-log/2026-04-15.md
  - work-log/2026-04-22.md
  - work-log/2026-05-01.md
puppet_type: marionette
event_categories: [string_tension, joint_event]
detection:
  selection:
    string-id: right-shoulder-support
    drift_from_baseline_gt: 4mm
    rest-pose-context: true
  filter:
    note|contains: "deliberate slack"
    OR puppet_metadata.baseline_age_lt: 2 days
  condition: selection and not filter
falsepositives:
  - "Director-called slack pose, not yet logged in cue list"
  - "Recently restrung; baseline not refreshed"
level: medium
tags:
  - tactic.string-system-drift
  - technique.gradual-stretch
  - tradition.czech-marionette
```

## Linting

Recommended `yamllint` config in `.yamllint.yml`:

```yaml
extends: default
rules:
  line-length: { max: 120 }
  truthy: { check-keys: false }
  document-start: disable
```

## Reference

- [SigmaHQ/sigma](https://github.com/SigmaHQ/sigma) — schema and modifier reference
- [Elastic detection-rules](https://github.com/elastic/detection-rules) — exemplar of detection-as-code peer review against this schema family
- [Panther Sigma support](https://docs.runpanther.io/) — alternate dialect; cross-check before adopting modifiers not in upstream Sigma
