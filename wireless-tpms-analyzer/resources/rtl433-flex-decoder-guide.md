# rtl_433 Flex Decoder Guide

A concise reference for writing custom rtl_433 flex decoders for unknown TPMS sensors.

## What is a Flex Decoder

rtl_433 has a built-in "generic" decoder framework (-X flag) that lets you define your own protocol parameters without writing C code. It's the fastest path from "I know the protocol" to "it decodes."

## Basic Syntax

```
rtl_433 -f 315M -X 'n=MyTPMS,m=OOK_PWM,s=200,l=400,r=8000,bits>=64'
```

Or via config file (`-c myTPMS.conf`):
```
decoder
  n=MyTPMS,
  m=OOK_PWM,
  s=200,
  l=400,
  r=8000,
  bits>=64,
  get=@0:{32}:id,
  get=@32:{8}:pressure_raw,
  get=@40:{8}:temp_raw,
  get=@48:{8}:flags,
  get=@56:{8}:checksum
```

## Key Parameters

| Parameter | Meaning | Example |
|---|---|---|
| `n=` | Decoder name | `n=MyTPMS_Schrader` |
| `m=` | Modulation type | `m=OOK_PWM` |
| `s=` | Short pulse width (µs) | `s=200` |
| `l=` | Long pulse width (µs) | `l=400` |
| `y=` | Sync pulse width (µs) | `y=1000` |
| `r=` | Reset/gap limit (µs) | `r=8000` |
| `bits>=` | Minimum packet bits | `bits>=64` |
| `bits=` | Exact packet bits | `bits=72` |
| `rows>=` | Minimum rows | `rows>=3` |

## Modulation Types

| Code | Description | Common for |
|---|---|---|
| `OOK_PWM` | OOK with pulse width modulation | Most NA TPMS |
| `OOK_PPM` | OOK with pulse position modulation | Some aftermarket |
| `OOK_MC_ZEROBIT` | OOK Manchester, zero-bit mode | Schrader variants |
| `FSK_PCM` | FSK with pulse code modulation | EU TPMS |
| `FSK_MC_ZEROBIT` | FSK Manchester | Continental |
| `OOK_PULSE_PREAMBLE_PULSE_RZ` | Return-to-zero OOK | Some Asian sensors |

## Field Extraction Syntax

```
get=@OFFSET:{WIDTH}:FIELDNAME
get=@OFFSET:{WIDTH}:FIELDNAME:SCALE:OFFSET_VAL
```

Examples:
```
# 32-bit sensor ID starting at bit 0
get=@0:{32}:id

# 8-bit pressure raw at bit 32, convert: raw * 0.25 = kPa
get=@32:{8}:pressure_kPa:.25:0

# 8-bit temperature raw at bit 40, convert: raw - 50 = Celsius
get=@40:{8}:temperature_C:1:-50

# 4-bit flags at bit 48
get=@48:{4}:flags

# 8-bit CRC at bit 52
get=@52:{8}:checksum
```

## Measuring Pulse Widths in inspectrum

1. Open .cu8 file, set sample rate
2. Add "Amplitude" plot
3. Zoom to a single packet
4. Use cursor measurements (shown in status bar) for pulse timing
5. Measure 5+ pulses, average them — timing jitter is normal (±10%)

## Testing Your Decoder

```bash
# Test against a capture file
rtl_433 -r capture.cu8 -X 'n=Test,m=OOK_PWM,s=200,l=400,r=8000,bits>=64'

# Verbose output to see raw bits
rtl_433 -r capture.cu8 -X 'n=Test,m=OOK_PWM,s=200,l=400,r=8000,bits>=64' -A

# Test with multiple config files
rtl_433 -f 315M -c myTPMS.conf -c myRKE.conf
```

## Checksum Brute Force (Python snippet)

```python
import crcmod, itertools

data = bytes.fromhex('AB12CD34B22A01')  # bytes 0-6, checksum is byte 7
expected_crc = 0xF3

# Try common CRC-8 polynomials
for poly in [0x07, 0x9B, 0x39, 0xD5, 0x1D]:
    crc_fn = crcmod.predefined.mkCrcFun('crc-8')  # or manual with poly
    result = crc_fn(data)
    if result == expected_crc:
        print(f"Match! poly=0x{poly:02X}")
```
