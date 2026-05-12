# Escalation MDT Brief

## Purpose

When a spectrum issue crosses an organisational boundary — RF analyst alone can't fix it, ownership now sits with SecOps, facilities, compliance, or a business sponsor — generate the multidisciplinary-team brief that lets the meeting actually decide something. This is the prompt that produces the artefact `/spectrum-mdt-handoff` writes; use it directly when you need a brief without running the full command.

## Prompt Template

```
Generate an MDT escalation brief for the spectrum subject below. This will be read in a 30-minute cross-team meeting whose attendees are listed in [AUDIENCE]. The meeting must leave with the listed decisions made or escalated.

- **Subject:** [CHANNEL_OR_EMITTER]
- **Latest symptom record:** [PATH]
- **Latest control chart:** [PATH]
- **Latest trajectory plot:** [PATH]
- **Latest capability report (if applicable):** [PATH]
- **Audience disciplines present:** [E.g. "RF eng, SecOps, facilities, clinical engineering, business sponsor"]
- **Decisions required at this meeting:** [BULLETED]
- **Constraints:** [E.g. "no antenna relocation possible this quarter due to building works"]

Please:
1. Open with a two-paragraph case summary in language an audience without RF training can parse. Define inline any term that doesn't appear in everyday business vocabulary.
2. Show the severity trajectory and annotate the prior interventions.
3. Quantify business impact: convert RF measurements into things the audience cares about (packet-loss → user-visible outages; capability index → SLA breach probability; etc.).
4. Generate a differential of 2–4 candidate causes with evidence weight per cause. Be honest about uncertainty.
5. Present an options table: action, intervention rung, owner discipline, cost, expected duration, business risk if not done.
6. State the recommended path explicitly, tied to measurable success criteria.
7. Surface the decisions required as yes/no questions for the meeting. Name a decision-maker for each.
8. End with a sign-off table that each discipline can initial post-meeting.
```

## Expected Output

- A standalone Markdown brief readable in 5 minutes.
- Plain-language case summary.
- Annotated trajectory plot reference.
- Business-impact paragraph.
- 2–4 row differential table.
- Options table.
- Recommended path with success criteria.
- Decisions list (yes/no, owner per question).
- Sign-off table.
