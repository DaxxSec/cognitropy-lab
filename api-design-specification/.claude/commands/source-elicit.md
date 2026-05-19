# /source-elicit

Enumerate and characterise the six intelligence fusion source classes available for a target API surface. First command run on any new surface; refresh quarterly. Outputs the source dossier that every subsequent fusion brief references.

## Inputs

- **Surface identifier** (e.g. `payments-api`, `account-api-v3`, `webhooks`) — the scope of the elicitation.
- **Data-access constraints** — what data systems are off-limits per policy (e.g. raw request bodies in EU regions, customer-name fields in tickets).
- **Time window** — default trailing 90 days for telemetry / tickets; adjust if the surface is newer than that.

## Steps

1. **Direction.** Restate the surface and the decisions the dossier will support (greenfield design, breaking change, audit response, hygiene sweep).
2. **Probe each source class.** For each of the six (`corpus`, `telemetry`, `tickets`, `standards`, `peer-specs`, `stakeholders`): confirm access, identify the *query handle* (file path, dashboard URL, Jira filter, RFC list, peer URL, stakeholder name), and note any access blockers.
3. **Rate reliability (A–F).** Apply the NATO STANAG 2022 reliability axis from `context/concepts.md`. Default starting ratings: standards A, mature peer-spec B, internal corpus B (downgrade if surface is fragmentary), telemetry C (downgrade if sample is sparse), tickets C, stakeholders B in lane / D out of lane.
4. **Note source biases.** What systematically distorts this source for this surface? E.g. "tickets over-represent free-tier customers because enterprise routes via Slack channel"; "telemetry under-represents long-tail enterprise integrations because of sampling rate".
5. **Capture access friction.** What is the time cost of pulling from each source? (Telemetry: 10 min via dashboard X; tickets: 30 min manual triage in Jira filter Y; stakeholders: requires async DM, 1–2 day latency.) The fusion brief budgets against this.
6. **Emit dossier.** Write `outputs/sources/<surface>-<date>.md` with one section per source class containing: access path, rating, biases, access friction, refresh cadence.
7. **Cross-link.** If a previous dossier exists, diff it; flag rating changes (e.g. telemetry upgraded from D to C because the new tracing pipeline backfilled the sample) in a `## Changes since <prior-date>` section.

## Output

`outputs/sources/<surface>-<date>.md` — a one-page-per-source dossier. Schema:

```
# <surface> — Source Dossier (<date>)

## corpus
- Access: <path or repo>
- Rating: <A-F>
- Biases: …
- Friction: …
- Refresh: <cadence>

## telemetry
…
```

This file is read by `/fuse-requirements` to set per-source weights on every claim.

## Notes

- A source with rating E or F that you nonetheless have access to is not useless — it just gets downweighted at fusion time. Don't drop it.
- If three or more source classes come back inaccessible, escalate before drafting; greenfield with two sources is high risk.
- Re-elicit after any major change in tooling: new tracing pipeline, ticket-system migration, corpus refactor.
