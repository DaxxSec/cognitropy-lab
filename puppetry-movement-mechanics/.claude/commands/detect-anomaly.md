# /detect-anomaly — Replay Rules Against a Movement Log

Walk a movement log against the active rule set and surface every firing, in detection-engineering shape.

## Required Inputs

- One of:
  - `--log <path>` — single log file (default: most recent under `work-log/`)
  - `--backtest <rule>` — single rule replayed against all historical logs
  - `--all-active` — every active rule against every historical log (slow; full corpus replay)

## Steps

### 1. Load the Active Rule Set

Walk `outputs/rules/active/` and parse each YAML rule using the schema in `resources/sigma-rule-template-puppetry.md`. A rule fails to load → log the failure, skip the rule, and continue. Never run a rule that didn't parse.

### 2. Load the Target Log(s)

Parse `work-log/*.md` files into the canonical event stream:

```
event = { timestamp, puppet, category, fields... }
```

Where `category` ∈ {`joint_event`, `string_tension`, `manipulator_input`, `audience_observation`, `video_annotation`, `imu_event`, `servo_telemetry`}.

### 3. Replay

For each rule × log pair, evaluate the rule's `selection` and `filter` clauses against the event stream. Apply `condition`. Emit a firing record:

```yaml
- rule_id: <uuid>
  rule_slug: <slug>
  rule_version: 1.0
  log_path: work-log/2026-05-01.md
  matched_events:
    - timestamp: 02:14
      puppet: prospero-marionette
      category: joint_event
      joint: right-shoulder
      observation: felt loose on the rising sequence
  tactic: string-system-drift
  technique: gradual-stretch
  confidence: high
  suggested_next_step: tune-threshold | escalate-to-review | no-action
```

### 4. Per-Firing Disposition

For each firing, ask the user:
- **No action** — fire is expected; record in log.
- **Tune** — open a `/peer-review --tune` pass on the rule.
- **Escalate** — escalate to senior reviewer.
- **Real anomaly** — open a maintenance ticket / rigging note in `outputs/reports/`.

### 5. Backtest Mode (`--backtest`)

When invoked with `--backtest <rule>`, replay the rule against every `work-log/*.md` file. Report:

| Metric | Value |
|---|---|
| Total logs scanned | n |
| Firings | n |
| New firings (not in any earlier active set) | n |
| Missed firings (logs that hand-review flagged anomaly, but rule did not fire) | n |
| Estimated false-positive rate | percent |

If false-positive rate exceeds 30%, refuse to recommend acceptance — the rule needs tuning before it ships.

### 6. Output

Write the firing report to `outputs/reports/<YYYY-MM-DD>-detect-<log-or-rule>.md`. Reference the rule version at the time of replay for full reproducibility.

## Failure Modes

- **No active rules yet.** The first time the workspace is used, `outputs/rules/active/` is empty; report "rule set empty — run `/rule-author` to draft your first rule" and exit cleanly.
- **Log is narrative-only.** Some rules may not be evaluable; emit "rule skipped — log lacks <category> data" and continue. Do not block the run.
- **Rule references a baseline that does not exist.** The rule needs `outputs/baselines/<puppet-slug>.yml`; emit "rule skipped — no baseline for <slug>; run `/calibration-audit`".

## Example Invocations

```
/detect-anomaly                                   # most recent log against active rules
/detect-anomaly --log work-log/2026-05-01.md      # specific log
/detect-anomaly --backtest right-shoulder-stretch # one rule, full corpus
/detect-anomaly --all-active                      # full replay; slow
```
