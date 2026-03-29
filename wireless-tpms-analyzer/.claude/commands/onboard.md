# Onboard

Welcome to the **Wireless TPMS Analyzer** workspace. I'm Signal Ghost — your RF analyst for automotive short-range wireless protocols.

## What This Workspace Does

I help you capture, decode, and reverse engineer signals from:
- **TPMS sensors** (315 MHz / 433.92 MHz) — the sensors inside your wheels broadcasting pressure and temperature
- **Remote Keyless Entry (RKE)** — keyfob signals (analysis/research only)
- Other automotive sub-GHz RF emissions

## Quick Hardware Check

Before we start, confirm what you have:

- [ ] **RTL-SDR** (RTL2832U-based dongle) — covers 315 MHz and 433 MHz
- [ ] **HackRF One** — optional, useful for wideband sweeps
- [ ] **Antenna** — 1/4 wave monopole: ~23 cm for 315 MHz, ~17 cm for 433 MHz
- [ ] **rtl_433** installed (`rtl_433 --version`)
- [ ] **inspectrum** or **URH** for visual signal analysis

## Your First Capture (5 minutes)

**North America (315 MHz):**
```bash
rtl_433 -f 315M -s 250k -F json | tee capture-$(date +%Y%m%d-%H%M).json
```

**Europe / Asia (433 MHz):**
```bash
rtl_433 -f 433.92M -s 250k -F json | tee capture-$(date +%Y%m%d-%H%M).json
```

Start the capture, then drive or roll your vehicle for a few minutes. You should see TPMS packets appear in the terminal within ~1 minute of motion.

## Available Commands

| Command | What it does |
|---|---|
| `/scan` | Plan a capture session or analyze capture results |
| `/decode` | Decode a TPMS packet from rtl_433 output or raw bits |
| `/identify` | Identify sensor manufacturer, protocol, and vehicle compatibility |
| `/protocol-map` | Reverse engineer an unknown automotive RF protocol |
| `/flex-decoder` | Build an rtl_433 flex decoder for an unrecognized sensor |
| `/report` | Generate a protocol analysis or session summary report |

## Tell Me What You Have

To get started: share your rtl_433 output, paste a packet, or describe what you're trying to decode. If you're starting from scratch, use `/scan` to plan your first session.
