# /post-show-report — Generate a Performance Incident-Shape Report

After every public performance, produce a structured report in incident-response shape. Borrows from cybersecurity post-incident write-ups (Google SRE postmortem, AWS post-event summary, Atlassian incident report).

## Required Inputs

- `--date <YYYY-MM-DD>` — performance date (defaults to today)
- `--production <id>` — production identifier
- Optional: `--include-rehearsals` — include rehearsal logs since the last performance

## Steps

### 1. Gather Inputs

- The performance's `work-log/<date>.md`
- All `/detect-anomaly` firings against that log
- `/calibration-audit` findings since the last performance
- Any new draft rules opened during this performance cycle
- Free-form post-show notes (collected in step 4 if not already present)

### 2. Build the Report Skeleton

```markdown
# Post-Show Report — <production> — <date>

## Summary
<one paragraph>

## Timeline
<chronological scene-by-scene events; flag rule firings inline>

## Detected Anomalies
<table: rule, firing-count, disposition>

## Calibration Findings
<table: puppet, dimension, delta, severity, action>

## What Went Well
<free-form>

## What Surprised Us
<free-form — the new patterns that motivate new rules>

## Action Items
<table: action, owner, deadline, peer-review-required?>

## Rules Affected
<list of draft / active / retired rules touched by this report>
```

### 3. Walk the Timeline

Scene by scene, summarize:
- Manipulator inputs noted in the log
- Rule firings, with the rule slug and version
- Audience-side observations
- Calibration findings that touched this scene's puppets

### 4. Capture Free-Form Notes

If post-show notes were not already collected in `work-log/<date>.md`, prompt the user to dictate them. Cover:
- What went well (so the company can preserve it)
- What surprised us (so the company can investigate)
- What broke (so the company can fix it)

### 5. Action Items

Each action item gets:
- A short title
- An owner (named person, not a role)
- A deadline (calendar date, not "soon")
- Whether peer review is required (yes for any new draft rule, any rule tuning, any baseline refresh)

### 6. Open Peer Review on the Report

Every post-show report goes through `/peer-review` before it lands as a `stable` artifact. SLA: 48 hours. Reviewers must include at least one role distinct from the report's author.

### 7. Write the Report

Output to `outputs/reports/<YYYY-MM-DD>-<production>.md`.

### 8. Update the Rule-Affected List

For every rule referenced in the report, append a back-reference to the rule file's `references:` section as a comment indicating the report path.

## Output

- `outputs/reports/<date>-<production>.md` — the report
- A `/peer-review` pass open against the report
- Action items mirrored into `planning/action-items.md`

## Failure Modes

- **No anomalies fired.** Still write the report — "nothing broke" is data. The report serves training and continuity even on quiet shows.
- **Calibration was skipped today.** Note the skip in the report; flag a higher priority for tomorrow's audit.

## Quality Bar

A useful report can be written in 20–30 minutes. Reports that consistently take >60 minutes are a sign that the workspace's data capture is too coarse — either lift instrumentation tier, or simplify the templates.
