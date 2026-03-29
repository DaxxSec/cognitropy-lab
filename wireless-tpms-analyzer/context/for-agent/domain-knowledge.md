# Domain Knowledge

## TPMS Background

**Regulatory mandate:** TREAD Act (2000) required all US passenger vehicles manufactured after Sept 2007 to include TPMS. EU followed with 661/2009/EC (mandatory from 2014). This means virtually every vehicle on the road today is broadcasting.

**Two system types:**
- **Direct TPMS (dTPMS):** Battery-powered sensor in each wheel transmits pressure, temperature, and ID via RF. This is what we analyze.
- **Indirect TPMS (iTPMS):** Uses ABS wheel speed sensors to infer pressure changes. No RF emissions — not relevant here.

## Frequency and Modulation

| Region | Frequency | Modulation |
|---|---|---|
| North America | 315 MHz | OOK (On-Off Keying), some FSK |
| Europe / Asia | 433.92 MHz | FSK predominant, some OOK |
| Some EU / aftermarket | 434.15 MHz | FSK |
| Premium / newer | 868 MHz | FSK / BPSK (less common) |

**OOK:** Simple on/off amplitude modulation. Easy to decode with a threshold. Preamble is usually alternating 1/0 pulses for clock sync.

**FSK:** Two frequencies represent 0 and 1. Deviation is typically ±25–75 kHz at 433.92 MHz. Requires FM demodulation before bit slicing.

## Major Manufacturer Protocols

### Schrader Electronics
- Most common OEM supplier globally
- Protocol EG53MA4: 64 bits, OOK, Manchester encoded, 315 MHz
- Packet: 8-bit preamble + 4-bit sync + 32-bit ID + 8-bit pressure (kPa/4) + 8-bit temperature (°C + 50) + 4-bit flags + 8-bit CRC
- CRC8 polynomial: 0x07 (CRC-8/SMBUS)

### Continental / VDO
- Dominant in European vehicles (VW, Audi, BMW, Mercedes)
- FSK at 433.92 MHz, ±50 kHz deviation
- 128-bit packets in some implementations
- Temperature in 0.5°C increments

### Huf Electronics / Beru RDKS
- VAG Group (VW/Audi) primary supplier
- 433.92 MHz FSK, proprietary framing
- Sensor IDs are programmed to ECU via OBD diagnostic

### Pacific Industries (DENSO)
- Toyota, Lexus, Honda OEM supplier (Japanese market)
- 315 MHz, 4-byte IDs, OOK
- Known to use XOR checksums rather than CRC

### Sensata Technologies
- Aftermarket and some Ford/GM OEM
- Multiple protocol variants (legacy and current)
- Some Sensata sensors support both 315 and 433 MHz

## Pressure Conversion Formulas

Most sensors encode pressure as a raw byte. Common conversions:

```
Schrader:  pressure_kPa = raw_byte * 0.25        (range: 0–63.75 kPa per LSB)
           pressure_PSI = pressure_kPa / 6.895

Continental: pressure_kPa = raw_byte * 1.364 - 7.0  (typical)

Generic:   If raw = 0xB2 (178):
           If scale is 1/4 kPa:  178 * 0.25 = 44.5 kPa = 6.45 PSI  (too low — wrong scale)
           If scale is kPa:      178 kPa = 25.8 PSI  (reasonable for car tire)
```

**Tip:** Cross-reference decoded pressure against a known-good TPMS gauge to confirm the scale factor.

## Temperature Conversion

Common offsets:
- `temp_C = raw_byte - 50`  (Schrader standard)
- `temp_C = raw_byte * 0.5 - 40`  (Continental variant)
- `temp_C = raw_byte - 40`  (some aftermarket sensors)

## Sensor ID Structure

- Typically 24–32 bits, hardcoded during manufacturing
- Printed as 6–8 hex digits on the sensor body (check with a glass)
- The ECU stores all 4 sensor IDs and matches incoming transmissions
- After a tire rotation or sensor replacement, ECU relearn procedure is required
- Some sensors include a rolling counter (3–4 bits) that increments each transmission — useful for identifying duplicates/replays

## Transmission Triggers

TPMS sensors have two transmission modes:
1. **Motion-triggered (rolling mode):** Sensor wakes when accelerometer detects rotation (typically >~5–10 km/h). Transmits every 60–90 seconds during normal driving.
2. **Static LF-triggered mode:** Many sensors respond to a 125 kHz LF trigger signal from diagnostic tools. Not useful for passive capture.

**Practical implication:** For parking-lot capture, push or drive the vehicle. Walking-pace is usually enough to trigger rolling mode.

## Privacy / Security Research Context

The landmark paper is "Security and Privacy Vulnerabilities of In-Car Wireless Networks: A Tire Pressure Monitoring System Case Study" (Rouf et al., IEEE S&P 2010). Key findings:
- TPMS transmissions can be received from 40m+ with a directional antenna
- Static sensor IDs enable vehicle tracking
- No authentication or encryption in any OEM protocol surveyed at time of publication
- Pressure spoofing (active, not covered here) can trigger dashboard warnings

This research drove subsequent interest in TPMS privacy. Some modern sensors now use rolling IDs, though this is still not universal.
