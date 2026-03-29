# Decode

Decode a TPMS packet from rtl_433 JSON output, raw hex bytes, or a bit string.

## Usage

Paste any of the following:
- rtl_433 JSON output
- Raw hex bytes (e.g., `A0 B2 2A 01 C4 F3 ...`)
- Bit string (e.g., `10101010 11001010 ...`)
- Base64-encoded payload

Tell me what protocol or sensor model it is, if known. If unknown, I'll attempt identification.

## What I'll produce

For a successfully decoded packet:

```
Protocol:    Schrader EG53MA4
Sensor ID:   0x8C32A1F4  (32-bit)
Pressure:    raw=0xB2 (178) → 178 × 0.25 = 44.5 kPa → 6.45 PSI  ← SANITY: low, check scale
Temperature: raw=0x2A (42) → 42 - 50 = -8°C  ← cold storage / winter
Battery:     OK (flag=0)
Motion:      Active (flag=1)
Counter:     0x3 (rolling, 2-bit)
Checksum:    CRC-8/SMBUS over bytes 0-6 = 0xF3 ✓ VALID
```

I'll flag:
- Pressure values outside 15–45 PSI range (likely wrong scale factor)
- Temperature values outside -40°C to +125°C (sensor operating range)
- Invalid checksums with the correct value shown
- Sensor IDs that don't match expected bit width for the protocol

## Provide context if you have it

- Vehicle year/make/model
- Region (NA or EU)
- Which wheel the sensor was in (FL/FR/RL/RR)
- Any OBD TPMS data for cross-reference
