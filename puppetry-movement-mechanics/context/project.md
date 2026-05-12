# Project Context

> Populated by `/onboard`. The agent reads this on every session to understand which puppets, productions, and review roster it is working with.

## Production / Company

- **Company name:**
- **Production(s) currently in scope:** (e.g. "*The Tempest* — touring marionette production, six-month run")
- **Performance cadence:** (e.g. four shows / week, plus two rehearsals)
- **Tour or resident:** (touring shows accumulate travel-induced drift faster; resident shows accumulate fixture-related drift)

## Puppet Inventory

For each puppet in scope, record:

| Field | Example |
|---|---|
| Slug / call-name | `prospero-marionette` |
| Type | string marionette / hand / rod / bunraku-style / shadow / animatronic / stop-motion |
| Materials | maple body, basswood limbs, foam-latex face, Spectra strings |
| Articulation count | 18 control points (head, shoulders × 2, elbows × 2, wrists × 2, hips, knees × 2, ankles × 2, mouth, brow × 2, eye-track) |
| Control rig | airplane-bar control / paddle control / triple-actor / glove / multi-rod |
| Mass | g or kg, including rigging |
| Calibration baseline file | `outputs/baselines/<slug>.yml` |
| Known failure-mode aliases | `string-system-drift / shoulder-stretch / mouth-mech-hysteresis` |

## Peer-Review Roster

The `/peer-review` command always asks for at least two distinct reviewers with distinct roles. Populate the roster here:

| Reviewer | Role | Strengths | Default review color |
|---|---|---|---|
| (name) | puppeteer | timing, phrasing | blue (validate detection) |
| (name) | rigger | mechanism, materials | red (try to break the rule) |
| (name) | dramaturg | dramatic intent | purple (tune for art-side impact) |

## Performance Context

- **Venue type(s):** proscenium / black-box / outdoor / theme-park / film studio / TV studio
- **Audience proximity:** (changes which detection rules matter — close-up reveals different drifts than long-throw)
- **Lighting cue density:** (high-cue-density shows shift Effort qualities and stress mechanisms differently)
- **Climate exposure:** (foam latex behaves very differently in tropical climates; servo offsets drift with temperature)

## Goals For This Workspace

- (e.g. "build a starter rule set we can carry to next year's tour")
- (e.g. "formalize the bunraku training-handoff review process")
- (e.g. "stop rediscovering the same mouth-mech wear pattern every six weeks")
