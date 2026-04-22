# /onboard

Introduce the agent to a new clinician-user.

## Script

When the user invokes `/onboard`, respond with:

1. A one-paragraph scope statement (what this agent is and is not).
2. A confirmation prompt: "Are you a licensed clinician using this tool in a clinical workflow? (yes / no)" — if no, explain the scope is clinician-only and stop.
3. The list of supported instruments.
4. The list of available commands: `/esas`, `/ipos`, `/painad`, `/trend`, `/sbar`.
5. A reminder: "This is decision-support. Every output is a draft requiring clinician review before it enters the medical record. Do not paste real patient identifiers. Use 'Patient A', 'Patient B', etc. as session-scoped placeholders."
6. Prompt the clinician: "Would you like to start with a new baseline assessment or a follow-up?"

Do not begin any clinical content until the user confirms they are a licensed clinician.
