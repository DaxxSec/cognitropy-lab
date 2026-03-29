# Wireless TPMS Analyzer

A Claude Agent workspace for passive analysis and reverse engineering of automotive short-range wireless protocols — primarily Tire Pressure Monitoring Systems (TPMS) and Remote Keyless Entry (RKE) signals using RTL-SDR, HackRF, and open-source tooling.

## What This Workspace Does

This workspace configures Claude as **Signal Ghost**, a domain expert agent that helps you:

- Capture and characterize 315 MHz / 433.92 MHz automotive RF signals
- Decode TPMS sensor transmissions from known manufacturer protocols (Schrader, Continental, Huf, Pacific Industries, and others)
- Reverse engineer unknown or undocumented TPMS/RKE protocols
- Identify sensors by their RF fingerprint and correlate to vehicle makes/models
- Build custom `rtl_433` flex decoders for new sensor protocols
- Analyze signal modulation, encoding, and protocol structure from raw IQ captures
- Document findings in structured protocol analysis reports

## Domain Coverage

**RF/SDR + Automotive (cross-domain)**

This workspace sits at the intersection of software-defined radio and vehicle electronics — perfect for hobbyists, security researchers, and RF experimenters who want to go deeper than "it just works" with their TPMS scanner.

## Hardware Supported

- RTL-SDR (RTL2832U) — recommended starting point
- HackRF One — for wideband sweeps and signal characterization
- YARD Stick One — for deeper protocol testing (research use)
- Any SDR with 300–500 MHz coverage and adequate sensitivity

## Key Slash Commands

| Command | Description |
|---|---|
| `/onboard` | Get oriented in this workspace |
| `/scan` | Plan or review a passive TPMS capture session |
| `/decode` | Decode a captured TPMS packet from rtl_433 output or raw bits |
| `/identify` | Identify sensor brand, protocol, and vehicle compatibility |
| `/protocol-map` | Map out an unknown automotive RF protocol from first principles |
| `/flex-decoder` | Build an rtl_433 flex decoder for an unrecognized sensor |
| `/report` | Generate a structured protocol analysis report |

## Getting Started

See `user-docs/getting-started.md` for hardware setup, software installation, and your first capture session.
