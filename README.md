# DaxxSpaces

A curated index of Claude Agent Workspaces — purpose-built agent environments for cybersecurity, reverse engineering, automotive tuning, and beyond. Each workspace follows the [Agent Workspace Model](https://github.com/danielrosehill/Claude-Agent-Workspace-Model) pattern: a self-contained repository with `CLAUDE.md` instructions, slash commands, subagents, context directories, and MCP configurations.

New workspaces are generated daily by an automated Claude agent and pushed here after secrets scanning and validation.

---

## How These Work

Each workspace is a standalone directory that can be cloned and pointed at with Claude Code (or any compatible agentic CLI). The structure includes:

| Component | Purpose |
|---|---|
| `CLAUDE.md` | Agent instructions, role definition, memory protocol |
| `context/` | Project details, user role, constraints, agent-specific workflows |
| `.claude/commands/` | Slash commands (with `onboard.md` required) |
| `work-log/` | Session history and findings |
| `planning/` | Active goals and investigation plans |
| `resources/` | Reference materials, cheat sheets, toolchain docs |
| `outputs/` | Generated reports, analysis results, exports |

---

## Workspace Index

### Cybersecurity & DFIR

| Workspace | Description |
|---|---|
| [Firmware RE Workspace](./firmware-re-workspace) | Firmware reverse engineering assistant — extract, disassemble, analyze, and document embedded firmware images to uncover architecture, attack surface, vulnerabilities, and hardcoded secrets. |
| [Phishing Kit Analyzer](./phishing-kit-analyzer) | Phishing kit analysis specialist — dissect, reverse-engineer, and extract intelligence from phishing kits deployed on compromised infrastructure. |

### Automotive & Engine Tuning

| Workspace | Description |
|---|---|
| [ECU Tune & Engine Build](./ecu-tune-engine-build-workspace) | Performance tuning and engine build assistant — ECU calibration, datalog analysis, engine modification planning, and build documentation. |

### Development & Debugging

| Workspace | Description |
|---|---|
| [Expo Debugger](./expo-debugger-workspace) | Senior React Native / Expo debugging specialist — systematic triage, diagnosis, and fix for Expo-managed apps with Railway backends. |

---

## Stats

- **Total Workspaces:** 4
- **Categories:** 3
- **Last Updated:** 2026-03-26

---

## About

Built and maintained by [DaxxSec](https://github.com/DaxxSec). Inspired by [Daniel Rosehill's Claude Code Projects Index](https://github.com/danielrosehill/Claude-Code-Projects-Index) and the [Agent Workspace Model](https://github.com/danielrosehill/Claude-Agent-Workspace-Model).

Workspaces are auto-generated daily by a scheduled Claude agent, scanned for secrets leakage, indexed, and pushed to this repository. Local copies are removed after successful push.
