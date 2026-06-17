# Endpoint Detection & Response — Reconstruction Workspace

> Investigate endpoint intrusions the way a conservator reconstructs a historical garment — provenance, anachronism, stratigraphy, and material analysis — with geographic/spatial mapping of how the attack spread.

## What This Workspace Does

This is a Claude Agent workspace for **EDR analysts, threat hunters, and incident responders**. It reframes an endpoint investigation as a *reconstruction problem*: telemetry arrives fragmentary, layered, and partly tampered — exactly the condition of an extant garment recovered from a dig or estate. So it imports the disciplines that keep historical costume reconstruction honest — **provenance research, anachronism detection, material analysis, stratigraphic layering, comparative typology, and a strict evidence-vs-conjecture boundary** — and applies them to process, file, registry, and network events.

The distinctive technique threaded through every command is **geographic/spatial analysis**. Costume historians map regional dress and the trade routes that carried dyes and patterns between workshops; this workspace maps the spatial structure of an intrusion: where endpoints sit, how the compromise diffused across sites, login geovelocity, and the geolocation/ASN topology of command-and-control infrastructure.

The result is an investigation that produces an *authenticated, defensible, reproducible* account of what happened — not a plausible story. Every claim carries a confidence tag and the telemetry that backs it.

## Why This Workspace Exists

Endpoint investigations fail in predictable ways: an analyst's plausible inference hardens into a "fact," a single backdated timestamp is trusted, C2 geolocation gets mistaken for actor nationality, and the first artifact *found* is assumed to be the first *deposited*. Textile conservation faced the identical failure modes a century earlier and built explicit disciplines to defeat them — the evidence/conjecture rule, anachronism authentication, stratigraphic ordering. This workspace ports those disciplines into EDR so the same mistakes stop happening, and adds a geospatial layer so multi-host incidents are understood as the diffusion processes they actually are.

## Getting Started

### Prerequisites

- An EDR/telemetry source you are **authorized** to investigate (Microsoft Defender for Endpoint, CrowdStrike, SentinelOne, Elastic, or Sysmon + Windows Event Log / auditd / macOS ES).
- Claude Code (or any agent runtime that reads `CLAUDE.md` + `.claude/commands/`).
- Optional: a GeoIP/ASN data source (MaxMind GeoLite2, IPinfo) for the geospatial commands.
- Optional: [Sigma](https://github.com/SigmaHQ/sigma) tooling to convert drafted rules to your platform's query language.

### Quick Start

1. Clone this workspace and open it with your agent.
2. Drop the telemetry export, alert, or suspicious artifact into the conversation (or point the agent at an outputs path).
3. Run `/anachronism-sweep` or `/artifact-provenance` to authenticate and source the fragments before you trust them.
4. Run `/geo-spread-map` if more than one host is involved, then `/reconstruct-timeline` to assemble the confidence-tagged whole.
5. Close out with `/condition-report` → `/pattern-draft` → `/custody-dossier`.

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/artifact-provenance` | Trace an artifact's lineage and find-context | You have a suspicious file/process and need to know where it came from |
| `/anachronism-sweep` | Hunt timestomping, backdating, version mismatch | Before trusting any artifact's chronology |
| `/reconstruct-timeline` | Assemble a confidence-tagged super-timeline | Once fragments are authenticated and ordered |
| `/layer-stratigraphy` | Order intrusion strata by deposition | To map dropper → loader → implant → C2 |
| `/material-fingerprint` | Fingerprint tooling for attribution | When you need an actor hypothesis from the tooling itself |
| `/geo-spread-map` | Geospatial analysis of the spread | Multi-host incidents, lateral movement, geovelocity |
| `/campaign-typology` | Match TTPs to known campaign families | To produce ranked attribution hypotheses |
| `/condition-report` | Compromise assessment + containment | To stabilize hosts and brief responders |
| `/pattern-draft` | Draft Sigma / EDR detection rules | To make the find reproducible for the SOC |
| `/custody-dossier` | Assemble the evidentiary package | At write-up / handoff / potential legal referral |

## Directory Structure

```
endpoint-detection-and-response/
├── CLAUDE.md                 # Agent role, context refs, command list
├── README.md                 # This file
├── .claude/commands/         # 10 bespoke domain commands
├── context/
│   ├── concepts.md           # EDR + the costume-reconstruction mapping + geospatial
│   ├── workflows.md          # The eleven-phase reconstruction methodology
│   └── references.md         # ATT&CK, telemetry sources, anachronism tells, geo data
├── prompts/                  # 5 reusable prompt templates
└── outputs/                  # Generated reconstructions, condition reports, dossiers
```

## Example Use Cases

### Authenticating a "trusted" system binary
A signed-looking binary in `System32` is flagged. `/anachronism-sweep` compares its `$SI`/`$FN` timestamps and Amcache first-execution against its PE compile time — the chronology is impossible, exposing a planted implant masquerading as a system file.

### Untangling a multi-site ransomware incident
Three offices report alerts within an hour. `/geo-spread-map` plots affected hosts on the site topology, models lateral movement as diffusion to find patient-zero, and runs geovelocity on the VPN logons — revealing one compromised account driving the spread.

### Building a defensible handoff to counsel
After reconstruction, `/custody-dossier` assembles a package with a confidence-tagged timeline, provenance chains, anachronism findings, a geospatial annex, and a full chain-of-custody log with acquisition hashes — defensible because evidence and conjecture never blur.

### Turning one find into durable detection
The intrusion used a distinctive parent-child process pattern. `/pattern-draft` converts the most stable IOA into a Sigma rule plus the native EDR query, with its false-positive surface documented.

## Recommended MCP Servers

- **Filesystem MCP** — read large telemetry/EVTX exports and write reconstructions into `outputs/`.
- **A SIEM/EDR query MCP** (Sentinel/Defender, Elastic, Splunk) — pull live telemetry for provenance and geovelocity checks.
- **HTTP/fetch MCP** — resolve ASN/WHOIS/passive-DNS for the C2 supply-line map and check ATT&CK technique pages.

## Legal & Ethical Considerations

- **Authorized scope only.** Investigate solely endpoints you are contracted or employed to defend.
- **PII in telemetry.** Usernames, IP addresses, and geolocation are personal data under GDPR/CCPA — handle, store, and share accordingly.
- **Chain of custody.** Preserve order of volatility (RFC 3227), hash on acquisition, and document every transfer if the work may become evidence.
- **Geolocation is a lead, not a verdict.** Never attribute actor identity or nationality on GeoIP/ASN alone.

## Technical References

- [MITRE ATT&CK](https://attack.mitre.org/) — the shared TTP typology used throughout.
- [NIST SP 800-86](https://csrc.nist.gov/publications/detail/sp/800-86/final) — integrating forensic technique into incident response.
- [RFC 3227](https://www.rfc-editor.org/rfc/rfc3227) — evidence collection and order of volatility.
- [Sigma](https://github.com/SigmaHQ/sigma) — portable detection-rule format for `/pattern-draft`.
- [LOLBAS](https://lolbas-project.github.io/) — living-off-the-land binaries catalogue.

## Optional plugin

If you have the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, additional global commands (`/workspace-foundational:context-sweep`, `/workspace-foundational:find-template`) are available; the workspace works without it.
