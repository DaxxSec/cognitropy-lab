# Build Report: satellite-comms-protocol-sim

## Cognitropy Lab — Day 5

**Date:** 2026-03-30
**Assignment:** RF/SDR/Signals → Satellite Communication Protocols → Simulation and Scenario Testing

---

## What Was Built

**SATCOM-SIM** is a Claude agent workspace that provides specialist-level assistance for satellite communication protocol work, with a focus on simulation and scenario testing. The agent persona is a satellite systems engineer who also thinks like a security researcher — practical, opinionated, and capable of producing real artifacts (link budget tables, annotated frame breakdowns, Python simulation code, test plans) rather than just explanations.

## Why This Domain

Satellite communications is an area where the gap between "learning from documentation" and "understanding how it actually works" is enormous. Protocol specs (especially CCSDS Blue Books) are dense and assume significant background knowledge. Link budget calculations are full of unit traps and system-interaction complexity. And satellite security is an underserved research area that's increasingly important as LEO mega-constellations become critical infrastructure.

The workspace was designed for people who have an RTL-SDR or HackRF and want to go deeper — from "I'm receiving ISS APRS" to "I understand what every bit of that frame means and how the link margin was calculated." It's also deeply relevant for cubesat teams who are designing protocol stacks and need help with test scenario generation.

## Key Design Choices

**Domain depth over breadth.** Rather than trying to cover "everything RF", the workspace is specifically scoped to Earth-space communication protocols. This lets the agent context be genuinely deep rather than superficially broad.

**Security perspective throughout.** Rather than having security as an add-on, it's integrated into every workflow. When discussing AX.25, you also discuss authentication (or lack thereof). When building a scenario test, you also generate security test cases.

**Practical orientation.** Every workflow produces something concrete: a table, annotated hex, Python code, a numbered test plan. The agent is instructed to show work (formulas, intermediate values) rather than just give answers.

**SDR hardware realism.** The workspace explicitly references RTL-SDR, HackRF, and GNURadio throughout, because that's the toolchain most users in this space actually have. It's honest about what cheap hardware can and can't do.

## Slash Commands Summary

| Command | Purpose |
|---|---|
| `/onboard` | Orientation and capability overview |
| `/simulate-link` | Full end-to-end link budget |
| `/decode-frame` | Annotated frame parsing |
| `/scenario-test` | Test plan + test vectors |
| `/orbital-pass` | Pass geometry + Doppler profile |
| `/protocol-compare` | Side-by-side protocol analysis |
| `/parse-telemetry` | Telemetry field decoding |
| `/vuln-scan` | Security vulnerability audit |

## Who Benefits

- Amateur satellite operators (RTL-SDR, HackRF users)
- Cubesat/small satellite engineering teams
- Security researchers studying satellite protocol vulnerabilities
- DFIR professionals with RF/SDR background (like Daxx)
- Students studying satellite communications
- Ground station software developers needing test vectors

## Build Statistics

- Files created: 22
- Slash commands: 8
- Prompts: 3
- References: 3
- Workflows depth: 260+ lines, 7 detailed workflows
- Domain knowledge: Full protocol coverage (AX.25, CCSDS, DVB-S2, APRS, Iridium, AIS)
- Python code examples: 15+ snippets across all files
