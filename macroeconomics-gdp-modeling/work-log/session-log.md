# Work Log Template

Each session day produces a file `work-log/<YYYY-MM-DD>.md` using this shape.

## Suggested Sections

### Header
- Date (UTC).
- Operator (user identity or `claude-code`).
- Workspace state at session start (latest manifest entry id, latest model id, latest forecast id).

### Activities
- Bullet list of slash commands run with their key parameters.
- For each command, link to the produced artifact path and its hash.

### Data anomalies
- Any indicator surprises ≥ 1σ.
- Any source schema drift.
- Any embargo events.

### Decisions
- Bullet list of decisions taken (refit, hold, escalate).

### Next session
- One or two bullets stating the planned next command and trigger.

## Why This Format

Work-logs are scanned by the agent on the next session as the recent operating history. A consistent shape lets the agent locate the prior decision quickly without re-reading the whole file.
