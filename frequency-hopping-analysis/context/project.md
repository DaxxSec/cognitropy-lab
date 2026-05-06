# Project Context

> Populated by `/onboard`. Until then, this is a stub describing what the agent expects.

## Target System

Describe the FHSS system you want to analyse:

- **Common name** (e.g. "Bluetooth Classic from a Pixel 8", "Honeywell wireless fire panel", "unknown 915 MHz device labeled FCC ID 2APXJ-WL400")
- **Suspected hop band** (e.g. 2.4 GHz ISM, 902–928 MHz, 30–88 MHz)
- **Suspected hop rate** (orders of magnitude — 10/s? 100/s? 1000/s? unknown?)
- **Suspected dwell** (matches hop rate? guard intervals?)
- **Suspected channel count** (e.g. Bluetooth = 79, WMBus = 8, BLE AFH = 37)
- **Public information available** — FCC ID filings, vendor datasheet, leaked firmware, prior reverse-engineering work

## Goals

What does success look like? Pick one or more:

- [ ] Confirm whether the signal is hopping at all (vs. fixed-frequency, vs. burst-pattern noise)
- [ ] Recover the full channel set
- [ ] Recover the hop sequence (per-dwell channel index over time)
- [ ] Identify sequence type (PN, table-driven, AFH, unknown)
- [ ] Recover the PN seed / table for predictability assessment
- [ ] Dehop the IQ stream so a downstream demodulator (URH, GR) can decode payload
- [ ] Characterise interference / jammers active in the hop band
- [ ] Produce a public-friendly findings report
- [ ] Calibration only — verify the analyser works on a known reference

## Out of Scope

Default out-of-scope (override with explicit authorisation in `constraints.md`):

- Decoding encrypted payloads
- Transmitting on the target system
- Active probing / jamming
- Reception of communications protected by the Wiretap Act / equivalent

## Captures

Track the IQ captures collected for this project:

| Capture | Date | Hardware | Center | BW | Duration | Notes |
|---------|------|----------|--------|----|----|-------|
|         |      |          |        |    |    |       |

## Open Questions

Track open empirical questions that drive the analysis plan:

- Q1: ?
- Q2: ?
