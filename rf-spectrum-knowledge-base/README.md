# RF Spectrum Analysis — Knowledge Base Workspace

> Stop running spectrum surveys you forget by next week. Turn every sweep into a durable, citable, FAQ-driven knowledge base — and keep it honest.

## What This Workspace Does

Most spectrum analysis produces a waterfall screenshot and a paragraph of prose that nobody can find six months later. This workspace treats the radio spectrum as a **knowledge-management problem**: it turns each sweep, emitter identification, and analyst question into structured entries in a searchable corpus, generates a grounded FAQ on top, and continuously scans for what's missing, duplicated, contradictory, or stale.

The defining technique is **knowledge base and FAQ generation** — classic knowledge engineering (entry schemas, provenance, controlled vocabulary, retrieval grounding, gap analysis) applied to RF. The agent ingests `hackrf_sweep`/`rtl_power` captures into entry drafts, authors schema-compliant canonical entries with mandatory citations, reconciles them against authoritative band plans, answers questions **grounded only in the KB** (with a strict abstain path), and mines the query log to keep a FAQ current.

The non-negotiable discipline: **cite or abstain.** When the KB doesn't cover a question, the agent says so and logs a gap — it never fills the silence with a confident guess. That single rule is what makes the corpus trustworthy enough to brief a stakeholder from.

## Why This Workspace Exists

Spectrum knowledge decays in two directions at once: new emitters appear faster than they're logged, and logged emitters silently change or disappear. An RF team without a maintained KB re-discovers the same signals every quarter and can never answer "is this band getting more congested?" with evidence. Knowledge engineering solved this for other domains — provenance, controlled vocabulary, retrieval grounding, staleness review — and this workspace ports that machinery onto the spectrum so that what one analyst learns on Tuesday is citable by the whole team on Friday.

## Getting Started

### Prerequisites

- An SDR for capture (RTL-SDR, HackRF, USRP, Airspy) and a sweep tool (`hackrf_sweep`, `rtl_power`), **or** existing capture CSVs / survey notes to ingest
- An authoritative band-plan reference for your region (ITU table; FCC/NTIA, Ofcom, etc. — links in `context/references.md`)
- Optionally the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin for `/workspace-foundational:*` conveniences

### Quick Start

1. Clone this workspace and open it as your Claude project.
2. Capture (or drop in) a spectrum sweep with full settings, then run `/kb-ingest-sweep` to turn detections into entry drafts in `outputs/kb/_drafts/`.
3. Promote drafts with `/emitter-entry-author` and add a `/signature-card` to each — that's your first canonical entries in `outputs/kb/`.
4. Run `/band-plan-sync` and `/kb-audit` to reconcile and QA, then `/faq-generate` to publish `outputs/faq.md`.
5. Ask questions with `/kb-query` (grounded + cited), and run `/gap-scan` to get the priority frequencies for your next sweep.

## Command Reference

| Command | When to use |
|---------|-------------|
| `/kb-ingest-sweep` | After a capture — convert a raw sweep/log into structured entry drafts |
| `/emitter-entry-author` | Promote a draft (or update an entry) into a canonical, cited entry |
| `/band-plan-sync` | Periodically — reconcile entries against an authoritative allocation table |
| `/faq-generate` | After an ingest or a wave of questions — refresh the grounded FAQ |
| `/kb-query` | Answer one spectrum question from the KB, with citations or an abstain |
| `/gap-scan` | Weekly — find dark bands, unknowns, stale entries; rank the backlog |
| `/entry-dedup-merge` | After large ingests — collapse duplicate entries, link variants |
| `/signature-card` | Build the recognition card that tops each emitter entry |
| `/kb-audit` | Before sharing — QA schema, citations, contradictions, staleness |
| `/glossary-build` | Maintain the controlled vocabulary so the corpus speaks one language |

## Directory Structure

```
rf-spectrum-knowledge-base/
├── CLAUDE.md                 # Agent role, commands table, foundational rules
├── README.md                 # This file
├── .claude/commands/         # 10 bespoke knowledge-engineering commands
├── context/
│   ├── concepts.md           # Spectrum measurement + knowledge-engineering concepts
│   ├── workflows.md          # The ingest → identify → author → curate → publish → maintain loop
│   └── references.md         # Entry schema, band tables, fingerprint cheat-sheet, sources
├── prompts/                  # 5 reusable prompt templates
└── outputs/                  # The KB itself: kb/ entries, faq.md, glossary.md, audits, backlogs
```

## Example Use Cases

1. **Standing spectrum survey.** Sweep a site monthly, ingest, and watch occupancy trend per band with cited evidence instead of vibes.
2. **Unknown-emitter triage.** A bursty 433 MHz signal appears — intake it, rule out artifacts, rank candidate identities, and queue the cheapest decode to confirm.
3. **Compliance briefing.** Answer "are we compliant in the aeronautical band?" with a KB-grounded briefing that cites every claim and names the gaps.
4. **Team onboarding.** A new analyst asks "what's on 868 MHz here?" and gets a grounded answer + signature cards instead of a week of rediscovery.
5. **Coverage planning.** `/gap-scan` turns the KB's dark bands into the next sweep's priority frequencies — the survey aims itself.

## Recommended MCP Servers / Tools

- **Filesystem MCP** — read/write the `outputs/kb/` corpus and capture CSVs
- **Fetch / web MCP** — pull band-plan tables and Signal Identification Wiki entries for citations
- SDR tooling outside the agent: GQRX, SDRangel, Universal Radio Hacker (decode), Inspectrum (burst inspection)

## Legal & Ethical Considerations

Receiving and *analyzing* signals is regulated differently across jurisdictions, and **decoding or acting on certain transmissions (cellular, encrypted, emergency services) may be illegal** even where mere reception is not. Only document signals you are authorized to monitor, record the legal basis in each entry's provenance, and treat the KB as a record of *authorized* observation — not a tool for intercepting communications. When in doubt, log the frequency and behavior, not the content.

## Technical References

- ITU Radio Regulations & Table of Frequency Allocations — https://www.itu.int/pub/R-REG-RR
- ITU-R SM-series (spectrum monitoring) — https://www.itu.int/rec/R-REC-SM/en
- US frequency allocation chart (NTIA) — https://www.ntia.gov/page/2011/united-states-frequency-allocation-chart
- Ofcom UK Frequency Allocation Table — https://www.ofcom.org.uk/spectrum/information/uk-fat
- Signal Identification Wiki — https://www.sigidwiki.com/wiki/Signal_Identification_Guide
- RadioReference database — https://www.radioreference.com/

---

*Part of the [Cognitropy](https://github.com/DaxxSec/cognitropy-lab) daily agent-workspace experiment — one new entropy-seeded workspace per build. Today's seed: **RF/SDR/Signals → RF spectrum analysis**, with knowledge base and FAQ generation.*
