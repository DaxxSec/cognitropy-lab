# Tools and Integrations — CI Motive Analysis

> Most of the "tools" of CI motive analysis are analytic frameworks, not software. The integrations below are optional aids; the workspace works in plain markdown.

## Structured Analytic Technique (SAT) Tooling

| Tool | Role | Notes |
|---|---|---|
| ACH Matrix (markdown table or Excel) | Force enumeration of competing hypotheses; rate each indicator against each | Heuer 1999. The dominant hypothesis is the one with the fewest *inconsistencies*, not the most consistencies. |
| Mermaid `timeline` / `gantt` | Visual chronology of indicators and life events | Embeds in markdown; renders in any modern viewer. |
| Mermaid `flowchart` | State diagram of recruitment vector progression | Useful for `recruit-vector-assessment` outputs. |
| Markdown checklist | The 5-domain inspection itself | Canonical instrument lives in `resources/indicator-taxonomy.md`. |
| Confidence-calibration table | Tracks how analyst's stated confidence has matched outcomes over time | Personal calibration habit; not a workspace requirement. |

## Source-Reliability Rating

The legacy NATO Admiralty Code (also used in US doctrine) rates source reliability and information credibility on independent axes:

| Source Reliability | Information Credibility |
|---|---|
| A — Completely reliable | 1 — Confirmed by other independent sources |
| B — Usually reliable | 2 — Probably true |
| C — Fairly reliable | 3 — Possibly true |
| D — Not usually reliable | 4 — Doubtful |
| E — Unreliable | 5 — Improbable |
| F — Reliability cannot be judged | 6 — Truth cannot be judged |

A B-2 indicator is the working baseline; an A-1 indicator is rare and significant; anything below C-3 should be flagged for corroboration before contributing to a motive finding.

## Recommended MCP Integrations

- **filesystem** — Read source packets, write finding drafts, manage case folder structure. Required.
- **sqlite** or **postgres** — Optional but useful for indicator storage with audit trail. One row per indicator: `id, subject_ref, domain, item_id, source, source_date, observation_date, classification, reliability, credibility, status (possible/corroborated/refuted)`.
- **memory (Anthropic)** — Short-term cross-session continuity within a single case. Do **not** use for classified content; the memory store is not classification-aware.

## Open-Source Research Aids

Where the analyst is authorized to perform open-source research and the host environment permits:

- **Public court records** (PACER for federal US, state/local equivalents) for documented life events
- **OFAC / SDN list** for any name in a foreign-contact field
- **PERSEREC unclassified archive** for case-pattern reference (`https://www.dhra.mil/PERSEREC/`)
- **DNI ICD library** (`https://www.dni.gov/index.php/who-we-are/organizations/ic-cio/ic-cio-related-menus/ic-cio-related-links/ic-technical-specifications/intelligence-community-directives`)

The workspace does **not** invoke:
- Social-media scraping services
- Data brokers
- Facial-recognition services
- Surveillance-grade aggregation tools

## Tool-Free Path

Every command in this workspace is designed to work with nothing more than a text editor and the markdown files in this directory. The integrations above are conveniences, not dependencies. A senior analyst with a notebook and these checklists produces the same finding as one with the full integration stack — slower, but with identical analytic rigor.

## Output Formats

| Output | Format | Location |
|---|---|---|
| Indicator checklist (per case, per inspection) | Markdown table | `outputs/<date>-indicator-checklist.md` |
| Motive profile draft | Markdown structured doc | `outputs/<date>-motive-profile-draft.md` |
| Timeline | Markdown table + Mermaid | `outputs/<date>-timeline.md` |
| ACH matrix | Markdown table | `outputs/<date>-ach.md` |
| Recruit-vector assessment | Markdown structured doc | `outputs/<date>-recruit-vector.md` |
| Final CI finding | ICD-203-compliant markdown | `outputs/<date>-finding.md` |
| Session log | Append-only log | `work-log/session-log.md` (or `work-log/<date>.md` per session) |

All outputs are markdown. They convert losslessly to whatever format the cognizant CI office requires (PDF, agency-specific formats) without losing the analytic chain.
