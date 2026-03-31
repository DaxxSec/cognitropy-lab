# satellite-comms-protocol-sim

**A Claude Agent Workspace for Satellite Communication Protocol Simulation & Scenario Testing**

Part of the [Cognitropy Lab](https://github.com/DaxxSec/cognitropy-lab) — daily AI agent workspace builds exploring the full spectrum of human knowledge.

---

## What This Workspace Does

SATCOM-SIM is a specialist Claude agent workspace that turns your Claude session into an expert satellite communications protocol engineer. It helps you simulate protocol stacks, design test scenarios, analyze link budgets, decode captured frames, and audit satellite communication systems for security vulnerabilities.

Whether you're tracking amateur satellites with an RTL-SDR, building a cubesat ground station, studying CCSDS protocol compliance, or researching satellite communication security — this workspace gives you an opinionated, deeply knowledgeable AI collaborator who actually understands what a TC Transfer Frame looks like at the bit level.

## Who This Is For

- **Amateur satellite operators** using SDRs to receive and decode satellite signals (APRS, AX.25, NOAA, etc.)
- **Cubesat teams** designing protocol stacks and ground station software
- **Security researchers** analyzing satellite protocol implementations for vulnerabilities
- **RF engineers** running link budget analyses and propagation simulations
- **Students and enthusiasts** learning satellite communications and orbital mechanics
- **DFIR professionals** investigating satellite-related incidents or signal anomalies

## Key Capabilities

- **Protocol simulation** — AX.25, CCSDS, DVB-S2, APRS, Iridium SBD, AIS, and more
- **Link budget analysis** — Full end-to-end link calculations with noise and margin modeling
- **Scenario testing** — Multi-step protocol test scenarios with orbital timing
- **Frame decoding** — Parse and annotate satellite protocol frames from hex or binary
- **SDR integration guidance** — GNURadio flowgraphs, HackRF/RTL-SDR workflows
- **Security auditing** — Protocol vulnerability analysis and adversarial scenario simulation
- **Orbital mechanics** — TLE-based pass prediction and Doppler simulation

## Slash Commands

| Command | Description |
|---|---|
| `/onboard` | Get oriented and understand workspace capabilities |
| `/simulate-link` | Run an end-to-end link budget simulation |
| `/decode-frame` | Decode a satellite protocol frame from hex/binary |
| `/scenario-test` | Design a multi-step protocol test scenario |
| `/orbital-pass` | Simulate orbital pass with Doppler and timing |
| `/protocol-compare` | Side-by-side protocol implementation comparison |
| `/parse-telemetry` | Parse and analyze satellite telemetry |
| `/vuln-scan` | Security audit of a protocol or implementation |

## Quick Start

1. Open this workspace in Claude
2. Run `/onboard` to get oriented
3. Tell the agent what you're working on — a satellite you want to track, a protocol you're implementing, a link budget you need to close, or a security question about a satellite system
4. The agent will guide you through the relevant simulation or analysis workflow

## Cognitropy Assignment

- **Date:** 2026-03-30
- **Category:** RF/SDR/Signals
- **Domain:** Satellite Communication Protocols
- **Technique:** Simulation and Scenario Testing
- **Day:** 5 of the Cognitropy Lab build streak

## License

MIT — use freely, adapt for your own satellite experiments.
