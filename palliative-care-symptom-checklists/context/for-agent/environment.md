# Environment

## Where the agent runs

The agent is designed to run inside a compliant environment the deploying organization controls — local machine, organizational workstation, or organization-managed cloud. It does not assume cloud PHI-compliance on its own; that is the deployer's responsibility.

## What it reads

- `context/` — its own role, project context, constraints, domain knowledge, workflows.
- `resources/` — instrument references, scoring rules, escalation thresholds.
- `.claude/commands/` — its slash-command definitions.
- `prompts/` — starter prompt templates.
- `work-log/session-log.md` — its own de-identified session log (append-only).

## What it writes

- `work-log/session-log.md` — one entry per session: timestamp, instrument used, thresholds tripped, draft output filename, session duration. No identifiers.
- `outputs/` — draft notes (de-identified), with a session-scoped placeholder name. The clinician copies into the EHR under the real identity.

## What it does not read or write

- No EHR. No FHIR endpoint. No patient registry.
- No identifiers on disk anywhere.
- No external network calls to fetch patient data.
- No outbound notifications (email, SMS, paging, Slack).

## Tools available

See `tools.md`. The short version: file read / write inside the workspace, Bash for local operations, and — optionally — a local LLM or cloud LLM inference endpoint the deploying organization has pre-approved for PHI handling.

## What the agent should assume about the user's environment

- The clinician has a paper or printed licensed copy of the instrument in front of them (required for IPOS; optional for ESAS-r).
- The clinician has authority to enter the data into the EHR under the patient's real identity.
- The clinician has the team's escalation policy and knows who to call when a flag trips.
