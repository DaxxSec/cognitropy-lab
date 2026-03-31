# Creation Report: satellite-comms-protocol-sim

## Cognitropy Assignment

| Field | Value |
|---|---|
| Date | 2026-03-30 |
| Day Number | 5 |
| Primary Category | RF/SDR/Signals |
| Primary Domain | Satellite Communication Protocols |
| Technique Modifier | Simulation and Scenario Testing |
| Crossover | No |
| Secondary Domain | N/A |

## What Was Built

**SATCOM-SIM** — a Claude agent workspace that turns Claude into a specialist satellite communications protocol engineer focused on simulation and test scenario design.

The workspace was designed with the intersection of security research and RF/SDR hobbyist use in mind. Someone with an RTL-SDR or HackRF who wants to go deeper than just receiving — they want to understand the protocols, simulate edge cases, and potentially evaluate the security posture of satellite communication systems.

## Design Decisions

**Agent Persona:** Chose a "satellite systems engineer who also does security research" persona rather than a pure academic stance. This keeps the agent practical and action-oriented — generating code, computing real numbers, producing annotated frame breakdowns rather than just explaining theory.

**Protocol Coverage:** Deliberately broad — AX.25 and APRS for the amateur radio/SDR community, CCSDS for the cubesat/professional space community, DVB-S2 for commercial broadcast, Iridium SBD and AIS for real-world tracking use cases. This makes the workspace useful across a wide range of satellite work.

**Security Focus:** Included as a core capability, not an afterthought. Satellite protocol security is an underserved research area (as demonstrated by incidents like the Viasat hack in 2022) and a natural fit for DFIR/security professionals who also have RF interests.

**SDR Integration:** Explicitly linked to HackRF One and RTL-SDR hardware throughout, acknowledging that the most likely user of this workspace has hands-on SDR experience and wants guidance at the tool level (GNURadio flowgraphs, demodulation chains) not just theory.

**Simulation Depth:** Workflows were designed to produce real, computable outputs — link budget tables with actual dB numbers, annotated hex frame breakdowns, Python simulation code — rather than vague conceptual descriptions.

## Files Created

### Core
- `CLAUDE.md` — Full agent persona with personality, capabilities, slash commands, working style
- `README.md` — Project documentation with capability table and quick start
- `CREATION_REPORT.md` — This file

### Context
- `context/project.md` — Project purpose and goals
- `context/role.md` — Agent role definition
- `context/constraints.md` — Operational constraints and boundaries

### Agent Context
- `context/for-agent/environment.md` — Runtime environment and available tools
- `context/for-agent/workflows.md` — Deep workflow documentation (250+ lines)
- `context/for-agent/tools.md` — Tool and library reference
- `context/for-agent/domain-knowledge.md` — Satellite protocol domain knowledge

### Commands (8)
- `.claude/commands/onboard.md`
- `.claude/commands/simulate-link.md`
- `.claude/commands/decode-frame.md`
- `.claude/commands/scenario-test.md`
- `.claude/commands/orbital-pass.md`
- `.claude/commands/protocol-compare.md`
- `.claude/commands/parse-telemetry.md`
- `.claude/commands/vuln-scan.md`

### Prompts (3)
- `prompts/deep-link-analysis.md`
- `prompts/protocol-security-audit.md`
- `prompts/scenario-builder.md`

### References (3)
- `resources/protocol-cheatsheet.md`
- `resources/frequency-bands.md`
- `resources/tools-reference.md`

### User Docs
- `user-docs/getting-started.md`
- `user-docs/report.md`

## Target Audience

Primary: Amateur satellite operators, cubesat engineers, SDR hobbyists with HackRF/RTL-SDR
Secondary: Security researchers studying satellite protocol vulnerabilities, DFIR analysts with RF interest
Tertiary: Students and enthusiasts learning satellite communications

## Build Quality Notes

- Workflows file is 260+ lines with step-by-step detail for all major use cases
- Domain knowledge file covers all major protocol families with technical depth
- 8 slash commands providing full workflow coverage
- Python simulation code examples woven throughout workflows
- Security perspective integrated throughout rather than siloed
