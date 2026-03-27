# Firmware Reverse Engineering Workspace

> A Claude Agent Workspace for systematic firmware extraction, analysis, vulnerability research, and reporting on embedded device firmware images.

---

## What Is This?

The Firmware RE Workspace transforms Claude Code into a purpose-built assistant for embedded firmware reverse engineering. Whether you're doing IoT security research, DFIR investigations involving embedded devices, bug bounty hunting on hardware targets, or just satisfying curiosity about how a router or smart appliance works — this workspace gives you a structured, repeatable methodology backed by an AI co-analyst.

It follows the [Claude Agent Workspace Model](https://github.com/danielrosehill/Claude-Agent-Workspace-Model) pattern: a repository that acts as the agent's memory, with context files that persist across sessions and slash commands that define repeatable workflows.

---

## Why This Workspace Exists

Firmware reverse engineering is notoriously fragmented. Analysts juggle binwalk, Ghidra, radare2, strings, file, hexdump, qemu, and a dozen other tools with no standard workflow. Important findings get lost in terminal history. Reports take hours to write from scratch. Context gets rebuilt from memory every new session.

This workspace solves that by:
- Giving Claude persistent memory through the repo structure
- Defining proven workflows for each analysis stage
- Providing reusable prompt templates for common RE tasks
- Maintaining a running work log so nothing is forgotten between sessions
- Generating professional reports from structured analysis notes

---

## Getting Started

### Prerequisites
- Claude Code installed and configured
- At least one of: binwalk, file, strings, hexdump (basic analysis)
- Recommended: Ghidra, radare2/Cutter, or Binary Ninja for disassembly
- Recommended: qemu-user-static for emulation
- A firmware image to analyze (`.bin`, `.img`, `.trx`, `.hex`, etc.)

### Quick Start

```bash
# 1. Clone or download this workspace
git clone <your-repo> firmware-re-workspace
cd firmware-re-workspace

# 2. Open in Claude Code
claude .

# 3. Run onboarding to set up your profile and target
/onboard

# 4. Start your first analysis
/analyze-firmware
```

---

## Slash Command Reference

| Command | Purpose | Typical Output |
|---|---|---|
| `/onboard` | First-run setup: collect your profile, environment, and target | Populated `context/` files |
| `/analyze-firmware` | Full structured analysis of a firmware binary | Analysis notes in `outputs/` |
| `/extract-fs` | Step-by-step filesystem extraction from firmware blob | Extracted filesystem in `outputs/` |
| `/identify-target` | Determine architecture, endianness, OS, compression | Identification report |
| `/find-secrets` | Hunt hardcoded credentials, keys, certs, tokens | Secrets inventory |
| `/vuln-hunt` | Systematic vulnerability discovery workflow | Vulnerability findings |
| `/map-attack-surface` | Enumerate all services, interfaces, entry points | Attack surface map |
| `/write-report` | Generate formal firmware analysis report | `outputs/report-[target]-[date].md` |
| `/toolchain-setup` | Get toolchain recommendations for your target | Setup guide |

---

## Directory Structure

```
firmware-re-workspace/
├── CLAUDE.md                    # Agent role, commands, memory protocol
├── README.md                    # This file
├── context/
│   ├── project.md               # Current target/project context
│   ├── role.md                  # Your role and experience level
│   ├── constraints.md           # Legal/ethical boundaries, tool preferences
│   └── for-agent/
│       ├── environment.md       # Your toolchain and OS environment
│       └── workflows.md         # Detailed analysis methodology
├── work-log/                    # Session-by-session analysis log
│   └── .gitkeep
├── planning/                    # Investigation plans and pivot notes
│   └── .gitkeep
├── user-docs/                   # Agent-written reference docs for you
│   └── .gitkeep
├── .claude/
│   └── commands/                # Slash command definitions
│       ├── onboard.md
│       ├── analyze-firmware.md
│       ├── extract-fs.md
│       ├── identify-target.md
│       ├── find-secrets.md
│       ├── vuln-hunt.md
│       ├── map-attack-surface.md
│       ├── write-report.md
│       └── toolchain-setup.md
├── prompts/                     # Reusable prompt templates
│   ├── binary-analysis.md
│   ├── code-review.md
│   └── report-sections.md
├── resources/                   # Reference materials
│   ├── architecture-reference.md
│   ├── common-vulns-checklist.md
│   └── tool-cheatsheet.md
└── outputs/                     # All analysis artifacts go here
    └── .gitkeep
```

---

## Example Use Cases

### IoT Device Security Assessment
Analyze a consumer router firmware for vulnerabilities before reporting to the vendor.
```
/onboard          → Set target: TP-Link Archer C7 firmware v5.3.6
/identify-target  → Confirms: MIPS32 LE, SquashFS, BusyBox Linux
/extract-fs       → Extract root filesystem
/find-secrets     → Discovers hardcoded admin credentials
/map-attack-surface → Enumerates httpd, telnetd, upnpd services
/vuln-hunt        → Finds command injection in web interface
/write-report     → Generates CVD-ready disclosure report
```

### DFIR Investigation — Compromised Embedded Device
During an incident response, you've imaged a compromised IoT gateway. Analyze the firmware for backdoors or implants.
```
/onboard          → Set context: DFIR investigation, compromised device
/analyze-firmware → Baseline analysis of clean firmware vs. extracted image
/find-secrets     → Look for attacker-added keys or tokens
/vuln-hunt        → Identify exploitation vector
/write-report     → Generate forensic findings report
```

### Hardware Hacking / CTF
Working on an embedded CTF challenge or personal hardware project.
```
/onboard          → CTF context, relaxed constraints
/identify-target  → Figure out what you're working with
/extract-fs       → Get at the files
/find-secrets     → Find the flag or hidden credentials
```

### Automotive / ECU Firmware
Analyzing an automotive ECU firmware dump for reverse engineering.
```
/onboard          → Set target: automotive ECU, bare-metal firmware
/identify-target  → Detect architecture (typically ARM Cortex-M, Renesas, Tricore)
/analyze-firmware → Map memory regions, vectors, peripheral init
/find-secrets     → Look for hardcoded VIN bindings, unlock codes
```

---

## Recommended MCP Servers

| MCP Server | Use Case |
|---|---|
| `filesystem` | Direct file access to your firmware work directory |
| `shell` / `bash` | Run binwalk, strings, file, xxd commands directly |
| `ghidra-bridge` | If you have a Ghidra MCP bridge configured |

---

## Ethical and Legal Considerations

**Only analyze firmware you are authorized to examine.** This workspace is built for:
- Security researchers with appropriate scope agreements
- DFIR investigators analyzing evidence in authorized investigations
- Bug bounty hunters operating within defined program scope
- Hobbyists working on their own devices or legitimately obtained hardware

Unauthorized reverse engineering may violate the CFAA, DMCA Section 1201, or equivalent laws in your jurisdiction. When in doubt, consult your legal counsel and obtain written authorization.

This workspace includes constraint fields (populated during `/onboard`) specifically to document your authorization scope and maintain responsible research practices.

---

## Acknowledgments

- Pattern based on [Claude Agent Workspace Model](https://github.com/danielrosehill/Claude-Agent-Workspace-Model) by Daniel Rosehill
- Inspired by the [COSINT workspace](https://github.com/DaxxSec/COSINT) pattern
- Methodology draws on public work from the firmware RE community: binwalk, FACT, firmwalker, and the IoT security research community
