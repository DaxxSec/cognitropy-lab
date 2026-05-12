# /movement-log — Capture a Rehearsal as a Structured Event Log

Convert a just-finished rehearsal or performance into a timestamped event log that downstream commands (`/detect-anomaly`, `/post-show-report`, `/peer-review`) can read.

## Required Inputs

- Date (defaults to today)
- Production identifier
- Scene IDs covered in the session
- Puppets in scope
- Optional: video file path or URI; cue-list reference; IMU / servo telemetry export path

## Steps

### 1. Header Block

Write the log frontmatter:

```yaml
date: 2026-05-01
production: <id>
session_type: rehearsal | performance | tech | dress
puppets: [<slug>, ...]
video_uri: <uri or omit>
telemetry_path: <path or omit>
manipulators: [<name : role>, ...]
```

### 2. Scene-by-Scene Walkthrough

For each scene the user names, prompt for events in four categories:

#### Joint events
- Timestamp (HH:MM:SS or scene:beat)
- Puppet slug
- Joint (e.g. `right-shoulder`, `mouth`, `eye-track-l`)
- Observation: what happened, how the puppeteer felt it, and a free-text qualifier (e.g. "lagged", "snagged", "felt loose").

#### String-tension samples (marionettes / rod)
- Timestamp
- String identifier (which line on which control)
- Sample qualifier: tight / slack / normal / off-baseline
- Estimated tension if the puppeteer can give one (in "felt-as" terms — light / nominal / heavy)

#### Manipulator inputs
- Timestamp
- Manipulator name
- Cue / beat / breath note
- Free-text input description

#### Audience-side observations
- Timestamp
- Observer (dramaturg / director / AD / house manager)
- Free-text observation

### 3. Free-Form Notes

After the structured walk, allow free-form rehearsal-room notes. These are not used by detection rules but are preserved for the post-show report and for future training.

### 4. Telemetry Ingestion (Tier 3 only)

If `telemetry_path` is set, attempt to ingest:
- IMU events as `imu_event` rows (timestamp, sensor, axis, value).
- Servo telemetry as `servo_telemetry` rows (timestamp, axis, commanded, actual, current).
- FSR string-tension as `string_tension` rows (timestamp, string-id, force-newtons).

If telemetry is absent, skip silently.

### 5. Run a Quick Detection Pass

After saving the log, immediately offer to run `/detect-anomaly --log work-log/<file>` so the user sees what fires before the institutional context fades.

## Output

`work-log/<YYYY-MM-DD>.md` (or `work-log/<YYYY-MM-DD>-<n>.md` for multiple sessions in one day) containing:
- Header frontmatter
- Per-scene event tables (one table per category that has events)
- Free-form notes section

## Schema Example

```markdown
---
date: 2026-05-01
production: tempest-tour
session_type: rehearsal
puppets: [prospero-marionette, ariel-marionette]
video_uri: s3://company/rehearsals/2026-05-01.mov
manipulators: [Lena : prospero-airplane, Mateo : ariel-airplane]
---

## Scene 2.1 — Storm

### Joint events
| Time     | Puppet               | Joint           | Observation                                |
|----------|----------------------|-----------------|--------------------------------------------|
| 02:14    | prospero-marionette  | right-shoulder  | felt loose on the rising sequence          |
| 02:31    | ariel-marionette     | left-elbow      | snagged on cape; recovered within a beat   |

### String-tension samples
| Time     | String                    | Sample      | Notes                          |
|----------|---------------------------|-------------|--------------------------------|
| 02:14    | prospero-r-shoulder       | off-baseline | felt heavier than normal       |
```

## Failure Modes

- **User has no time for full structured walk.** Offer compact mode: free-form notes only; the agent will return at the next session and offer to retro-structure them.
- **No video and no telemetry.** Run pure-narrative; downstream rules limited to manipulator-input + audience-observation categories.
