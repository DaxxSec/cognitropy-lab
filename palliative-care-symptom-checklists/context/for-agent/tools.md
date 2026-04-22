# Tools

The agent uses a minimal tool surface on purpose. Fewer moving parts = fewer PHI-handling failure modes.

## File operations
- **Read** — read any file under the workspace (`context/`, `resources/`, `.claude/`, `prompts/`, `work-log/`, `outputs/`).
- **Write / Edit** — write to `outputs/` and append to `work-log/session-log.md`. Do not write identifiers.

## Bash
- For local operations: formatting, de-identification checks, simple trend computation.
- Do not use Bash to reach the network for patient data.
- Do not use Bash to ingest a live EHR export unless the deploying team has signed off on a specific workflow and the input has been de-identified.

## LLM inference
- If a local LLM or organizational cloud LLM is configured, prefer it for any generation that might involve patient-adjacent text.
- If no PHI-approved inference endpoint is available, the agent refuses to process any input that looks like PHI and asks the clinician to either redact or switch to a placeholder.

## What the agent must not do with its tools

- No network fetches of patient data.
- No writing PHI to disk.
- No calling external APIs that would log request bodies.
- No sending email / SMS / paging. Escalation surfaces in the current session; the clinician acts on it.
- No autonomous EHR writes.

## Prompt-level discipline

Every tool call involving patient-relevant content must:
1. Use the session-scoped placeholder ("Patient A", etc.) rather than real identifiers.
2. Be logged (tool, target, byte count, timestamp) to `work-log/session-log.md` without the payload content.
3. Respect the constraints in `context/constraints.md`.
