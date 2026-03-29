# Project Context

## Purpose

The Wireless TPMS Analyzer workspace is a research and learning environment for passive analysis of automotive short-range wireless protocols. The primary focus is Tire Pressure Monitoring System (TPMS) transmissions, with secondary coverage of Remote Keyless Entry (RKE) and other 300–500 MHz vehicular RF emissions.

## Problem Being Solved

Every modern vehicle continuously broadcasts radio signals from its TPMS sensors — yet most people have no idea what data is being transmitted, how it's encoded, or what protocols are in use. The tooling to capture and decode these signals (RTL-SDR + rtl_433) is cheap and accessible, but understanding what you're seeing requires knowledge scattered across forum posts, academic papers, and FCC filings.

This workspace consolidates that knowledge and wraps it in an expert agent that can:
- Help you go from raw IQ capture to decoded, human-readable sensor data
- Identify which manufacturer protocol a sensor is using
- Reverse engineer protocols not yet supported by rtl_433
- Explain the RF fundamentals behind what you're observing

## Scope

**In scope:**
- Passive RF capture and analysis (receive-only)
- Protocol documentation and reverse engineering
- Sensor identification and vehicle correlation
- Educational content on TPMS security/privacy research
- Building custom rtl_433 flex decoders

**Out of scope:**
- Active transmission or signal replay guidance
- Defeating immobilizers or keyless entry systems for unauthorized access
- Any activity that would violate FCC Part 15 rules or the CFAA

## Use Context

Sessions typically begin with a capture file or a copy-paste of rtl_433 JSON output and progress toward a structured protocol analysis. The workspace also supports longer-term projects like documenting all TPMS sensors in a vehicle fleet or building a custom decoder for a rare sensor type.
