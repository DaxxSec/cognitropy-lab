# /rule-author — Draft a Sigma-Style Movement-Detection Rule

Author a new draft rule for a recurring failure pattern. Output is a YAML file in `outputs/rules/draft/`. The rule is **not** active until peer-reviewed.

## Required Inputs

- A pattern observed in **at least two** distinct movement logs (the agent enforces this).

## Steps

### 1. Establish the Hypothesis

Ask the author:
- "Describe the recurring pattern in one sentence."
- "Which two-or-more `work-log/` files motivated this rule?" Refuse to proceed with fewer than two.
- "Which puppet types does this apply to? (one, several, or *)"

### 2. Choose the Schema Anchors

Walk through the schema in `resources/sigma-rule-template-puppetry.md`. The author specifies:

- `title:` — short human title
- `id:` — agent generates a UUIDv4
- `description:` — paragraph
- `status:` — always `experimental` for new drafts
- `date:` — today
- `author:` — username
- `references:` — list of work-log paths and any external references
- `puppet_type:` — `marionette` / `bunraku` / `wayang` / `hand-rod` / `animatronic` / `stop-motion` / `*`
- `event_categories:` — list of categories the rule reads (`joint_event`, `string_tension`, `imu_event`, etc.)

### 3. Define the Detection

Sigma-style:

```yaml
detection:
  selection:
    <field>: <value or list>
    <field>|gt: <number>     # greater-than
    <field>|window:
      span: 3
      unit: events
  filter:
    <field>: <benign value>
  condition: selection and not filter
```

Common puppetry-side modifiers:

- `|drift_from_baseline_gt: <millimeters | degrees | newtons>` — anything that compares an observed value against `outputs/baselines/<slug>.yml`.
- `|effort_quality:` — Laban Effort qualifier (`Light-Bound`, `Strong-Free`, etc.) for rules that key off `/laban-tag` annotations.
- `|phase_lag_gt: <ms>` — for ensemble-sync rules between named manipulators.

### 4. Tag the Rule

Mandatory tags from `resources/puppet-mechanism-failure-modes.md`:

```yaml
tags:
  - tactic.<id>
  - technique.<id>
```

If the author cannot find a fitting tactic / technique, do **not** invent a free-form tag — instead, draft a tactic / technique addition in `outputs/reviews/<date>-taxonomy-proposal.md` to be reviewed alongside the rule.

### 5. State False-Positive Sources

Mandatory. List at least one situation in which the rule will fire on a benign condition. If the author cannot name any, the rule is too narrow or the author has not thought hard enough — push back.

### 6. Backtest the Draft

Run `/detect-anomaly --backtest <draft-rule>` immediately after writing. Capture firing rate. If the rule fires on 30% or more of historical logs, warn — likely too broad.

### 7. Write the Draft

Output to `outputs/rules/draft/<rule-slug>.yml`. Use the schema from `resources/sigma-rule-template-puppetry.md` exactly. The agent never edits a rule in place once written; tunings happen via `/peer-review --tune`.

### 8. Open a Peer Review

`/rule-author` always ends by opening `/peer-review --target outputs/rules/draft/<rule-slug>.yml`. The rule cannot move to active otherwise.

## Output

- `outputs/rules/draft/<slug>.yml` — the draft rule, schema-conformant.
- A backtest summary appended to the rule's references section as a comment.
- A `/peer-review` pass open against the draft.

## Failure Modes

- **Single example log.** Refuse. Tell the author: "A rule needs at least two logs as evidence — wait until you see this pattern again."
- **Tag not in catalog.** Draft a taxonomy proposal alongside the rule; never pass a non-catalog tag.
- **Description too vague.** Push back: "What specific event-stream pattern fires this? Be concrete enough that a reviewer can construct a counter-example."

## Example Skeleton

```yaml
title: Right-shoulder support stretches past tuning band
id: 9d3e4a02-...
description: |
  On Czech-tradition airplane-control marionettes (4–6 month tour), the
  right-shoulder support string accumulates Spectra creep beyond the
  per-puppet tuning band, producing a ~3% downward shoulder drop visible
  in the rest pose between scenes.
status: experimental
date: 2026-05-01
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
  condition: selection and not filter
tags:
  - tactic.string-system-drift
  - technique.gradual-stretch
falsepositives:
  - "Director-called slack pose, not yet logged in cue list"
  - "Recently restrung; baseline not refreshed"
level: medium
```
