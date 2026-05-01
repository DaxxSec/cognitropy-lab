# Work Log Template

> Copy this template to `work-log/<YYYY-MM-DD>.md` (or `<YYYY-MM-DD>-<n>.md` for multiple sessions in one day) at the start of each rehearsal or performance log. The `/movement-log` command will guide you through filling it in.

```markdown
---
date: YYYY-MM-DD
production: <id>
session_type: rehearsal | performance | tech | dress
puppets: [<slug>, ...]
video_uri: <uri or omit>
telemetry_path: <path or omit>
manipulators: [<name : role>, ...]
---

# <Production> — <Session Type> — <Date>

## Scene <id> — <Scene Title>

### Joint events
| Time | Puppet | Joint | Observation |
|------|--------|-------|-------------|
|      |        |       |             |

### String-tension samples
| Time | String | Sample | Notes |
|------|--------|--------|-------|
|      |        |        |       |

### Manipulator inputs
| Time | Manipulator | Cue / Beat / Breath | Description |
|------|-------------|---------------------|-------------|
|      |             |                     |             |

### Audience-side observations
| Time | Observer | Observation |
|------|----------|-------------|
|      |          |             |

### Video annotations (if any)
| Time | Body | Effort observed | Effort called | Shape | Space | Notes |
|------|------|-----------------|---------------|-------|-------|-------|
|      |      |                 |               |       |       |       |

## Free-form Notes

(Rehearsal-room conversation, director's calls, anything that doesn't fit the structured tables.)

## Detection-Anomaly Run

(Filled by `/detect-anomaly`. Lists rule firings against this log.)

## Action Items

| Action | Owner | Deadline | Peer-review required? |
|--------|-------|----------|-----------------------|
|        |       |          |                       |
```
