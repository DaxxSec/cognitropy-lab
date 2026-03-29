# Creation Report: wireless-tpms-analyzer

**Created:** 2026-03-29
**Domain:** RF/SDR × Automotive (cross-domain mashup)
**Agent Persona:** Signal Ghost

## Why This Workspace

The Cognitropy Lab scanned 9 existing workspaces before today's build. Domain distribution was heavily weighted toward Science/Research (4 workspaces), with single representatives in Cyber/DFIR, Automotive, Hardware/Embedded, and Dev Productivity. **RF/SDR/Signals had zero representation** — the clear gap.

Given Daxx's dual hobby of RF/SDR (HackRF, RTL-SDR) and automotive (ECU tuning, engine builds), a cross-domain workspace targeting automotive RF protocols was the natural choice. TPMS specifically was selected because:

1. It's a beginner-accessible entry point into automotive RF — sensors transmit continuously at walking pace and above
2. Protocols are well-documented enough to be educational, yet varied enough that custom reverse engineering is often needed
3. It bridges both hobbies authentically (you're decoding signals FROM your car)
4. There's active security research interest in TPMS tracking/privacy implications

## What Was Built

### Slash Commands (7)
- `/onboard` — Workspace orientation, hardware checklist, first-capture workflow
- `/scan` — Plan or analyze a passive capture session (frequency, duration, antenna tips)
- `/decode` — Decode TPMS packets from rtl_433 JSON, raw hex, or bit strings
- `/identify` — Identify manufacturer, protocol, and vehicle compatibility from sensor data
- `/protocol-map` — Guided workflow for reverse engineering an unknown automotive RF protocol
- `/flex-decoder` — Generate rtl_433 flex decoder configuration for unrecognized sensors
- `/report` — Generate a structured protocol analysis or session summary report

### Prompts (3)
- `capture-session-review.md` — Template for reviewing a completed capture session
- `protocol-re-template.md` — Step-by-step protocol reverse engineering intake
- `sensor-id-correlation.md` — Correlate multiple sensor IDs to vehicles/wheels

### Resources (3)
- `tpms-frequency-protocol-reference.md` — Frequency bands, manufacturer protocols, regional regulations
- `rtl433-flex-decoder-guide.md` — Flex decoder syntax reference and worked examples
- `modulation-cheatsheet.md` — Quick reference for OOK/ASK/FSK identification from waveforms

### Context Documents
Full agent context covering role definition, constraints (research-only, no active transmission guidance), environment setup, toolchain, workflows, and deep domain knowledge.

## Intended Users

- RF/SDR hobbyists curious about what their car is broadcasting
- Automotive enthusiasts who want to go deeper than their TPMS scan tool
- Security researchers studying vehicular wireless protocols
- Students learning protocol reverse engineering with a practical, accessible target

## Diversity Impact

This workspace fills the RF/SDR domain gap and represents the first cross-domain RF × Automotive workspace in the lab. Domain count after today: RF/SDR: 1, Automotive: 1 (now with RF depth), all others unchanged.
