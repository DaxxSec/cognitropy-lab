# Phishing Kit Analyzer

A Claude Agent Workspace for dissecting, reverse-engineering, and extracting threat intelligence from phishing kits.

## What Is This?

Phishing kits are the pre-packaged toolkits that attackers deploy on compromised web servers to harvest credentials. They typically contain HTML login page clones, PHP credential-handling scripts, JavaScript for form validation and evasion, and exfiltration mechanisms (email, Telegram bots, dead drops, remote APIs). Analyzing these kits yields rich threat intelligence: IOCs, actor attribution, infrastructure mapping, and victim targeting patterns.

This workspace turns Claude Code into a phishing kit analysis assistant. Drop in a kit, run `/triage`, and get structured intelligence back — no sandbox required because all analysis is purely static.

## Who Is This For?

- **DFIR analysts** triaging phishing incidents
- **Threat intelligence teams** cataloging actor TTPs
- **SOC analysts** who need quick IOC extraction from reported phishing
- **Security researchers** studying phishing ecosystem evolution
- **Email security teams** building detection signatures

## Getting Started

1. Clone this repository
2. Run `/onboard` to configure your analyst profile, preferred output formats, and tool environment
3. Place phishing kit archives in `outputs/incoming/` (or reference them by path)
4. Run `/triage` to begin

## Command Reference

| Command | Purpose | Typical Input | Output |
|---------|---------|---------------|--------|
| `/onboard` | Initialize workspace | Interactive interview | Populated `context/` files |
| `/triage` | Quick kit assessment | Path to ZIP/archive | Threat level, kit type, exfil summary |
| `/deep-dive` | Full static analysis | Path to extracted kit | Complete analysis with deobfuscated code |
| `/ioc-extract` | Pull all indicators | Path to kit or analysis | IOC list in STIX 2.1 / CSV / JSON |
| `/attribution` | Actor identification | Kit path + optional context | Attribution assessment with confidence |
| `/report` | Formal write-up | Completed analysis | Markdown report for stakeholders |
| `/compare` | Kit comparison | Two or more kit paths | Overlap matrix, shared IOCs, code diff |
| `/deobfuscate` | Decode obfuscation | Obfuscated file or snippet | Decoded source with annotations |

## Directory Structure

```
phishing-kit-analyzer/
├── CLAUDE.md                    # Agent configuration (lightweight)
├── README.md                    # This file
├── context/
│   ├── project.md               # Project scope (populated by /onboard)
│   ├── role.md                  # Analyst role (populated by /onboard)
│   ├── constraints.md           # Boundaries (populated by /onboard)
│   └── for-agent/
│       ├── environment.md       # Tool & environment details
│       └── workflows.md         # Analysis methodology
├── work-log/                    # Session-by-session analysis logs
├── planning/                    # Investigation plans and pivot tracking
├── user-docs/                   # Analyst reference documentation
├── .claude/commands/
│   ├── onboard.md               # Workspace initialization
│   ├── triage.md                # Quick kit assessment
│   ├── deep-dive.md             # Full static analysis
│   ├── ioc-extract.md           # IOC extraction & formatting
│   ├── attribution.md           # Kit attribution workflow
│   ├── report.md                # Report generation
│   ├── compare.md               # Kit comparison
│   └── deobfuscate.md           # Code deobfuscation
├── prompts/
│   ├── php-backdoor-analysis.md # Prompt for analyzing PHP backdoors in kits
│   ├── telegram-bot-extraction.md # Prompt for extracting Telegram exfil configs
│   └── evasion-technique-catalog.md # Prompt for cataloging anti-analysis tricks
├── resources/
│   ├── common-kit-signatures.md # Known kit family signatures
│   ├── exfil-methods-reference.md # Exfiltration method taxonomy
│   └── ioc-format-templates.md  # Output format templates (STIX, CSV, MISP)
├── outputs/                     # Generated reports and IOC files
└── .mcp.json                    # Optional MCP server configs
```

## Example Use Cases

### Incident Response Triage
A user reports a phishing email. Your email gateway captured the kit URL. Download the kit, run `/triage` to get an instant threat assessment, then `/ioc-extract` to feed indicators into your SIEM and blocklists.

### Threat Intel Production
You're tracking a phishing actor group. Run `/deep-dive` on their latest kit, then `/attribution` to correlate with known campaigns. Use `/compare` to map kit evolution over time. Generate a `/report` for your threat intel platform.

### Detection Engineering
Use `/deobfuscate` to understand evasion techniques, then build detection signatures for your email gateway, WAF, or proxy based on the decoded patterns.

### Campaign Tracking
When you find multiple kits on a single compromised server, run `/compare` to determine if they're from the same actor, repackaged kits, or distinct campaigns sharing infrastructure.

## Recommended MCP Servers & Tools

- **VirusTotal MCP** — Enrich IOCs with VT reputation data
- **URLScan MCP** — Check live phishing URLs safely
- **MISP MCP** — Push extracted IOCs directly to your MISP instance
- **Shodan MCP** — Investigate hosting infrastructure
- **File system tools** — For navigating extracted kit contents

## Ethical & Legal Considerations

- **Never deploy or host phishing kit code** — analysis only
- **Handle victim data responsibly** — kits often contain harvested credentials; treat as PII
- **Responsible disclosure** — report compromised hosting infrastructure to abuse contacts
- **Chain of custody** — if kit is part of a legal investigation, document handling carefully
- **Credential exposure** — if analysis reveals active credential harvesting, follow your org's incident response procedures

## Credits

Built on the [Claude Agent Workspace Model](https://github.com/danielrosehill/Claude-Agent-Workspace-Model) by Daniel Rosehill. Inspired by the [COSINT workspace](https://github.com/DaxxSec/COSINT).
