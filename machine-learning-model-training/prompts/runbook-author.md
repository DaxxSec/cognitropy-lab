# New Runbook Author

## Purpose

Author a new runbook for a *novel* training failure class that the existing commands don't cover — typically an action item out of a postmortem. Produces a file ready to drop into `.claude/commands/`.

## Prompt Template

```
You are codifying hard-won incident knowledge into a reusable runbook for a training-run reliability workspace.

I need a runbook for a new failure class:

- **Failure class / name:** [E.G. "expert-imbalance collapse in MoE training"]
- **Detection signals:** [WHAT METRICS/LOGS REVEAL IT]
- **Typical root causes:** [KNOWN CAUSES]
- **Known mitigations:** [WHAT HAS WORKED, SMALLEST-CHANGE-FIRST IF POSSIBLE]
- **Recovery procedure:** [HOW TO GET A HEALTHY RUN BACK]
- **Severity guidance:** [WHEN IS THIS SEV-1 vs SEV-2 vs SEV-3]

Please produce a runbook in the workspace's command format:
1. A slash-command name (domain-specific, kebab-case, NOT generic).
2. A one-sentence purpose.
3. `## Inputs`, `## Steps` (numbered, stabilise-before-diagnose), `## Output` (an `outputs/` artifact), `## Notes` (gotchas).
4. The symptom→runbook router row to add to `context/references.md`.
```

## Expected Output

- A complete `.claude/commands/<name>.md` runbook in the workspace's house style
- A matching router-table row for `references.md`
- A suggested alert threshold to pair with it, if applicable
