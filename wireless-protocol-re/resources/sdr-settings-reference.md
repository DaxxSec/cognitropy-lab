# SDR Settings Quick Reference

## HackRF One Specifications
| Parameter | Value |
|-----------|-------|
| Frequency range | 1 MHz – 6 GHz |
| Instantaneous bandwidth | Up to 20 MHz |
| Sample rate | 2–20 Msps |
| Resolution | 8-bit (I/Q) |
| Gain stages | LNA (0–40 dB), VGA (0–62 dB), AMP (0/14 dB) |
| Half-duplex | Yes (TX or RX, not both) |

### Recommended Settings by Frequency Band
| Band | Sample Rate | LNA | VGA | AMP | Notes |
|------|------------|-----|-----|-----|-------|
| 315 MHz | 2 Msps | 24 | 30 | On | Narrow signals, low sample rate OK |
| 433 MHz | 2 Msps | 24 | 30 | On | Most ISM devices are narrowband |
| 868/915 MHz | 2–4 Msps | 32 | 30 | On | LoRa needs wider BW |
| 2.4 GHz | 10–20 Msps | 32 | 40 | On | Wi-Fi/BLE need higher rates |

## RTL-SDR v3 Specifications
| Parameter | Value |
|-----------|-------|
| Frequency range | 24 MHz – 1.766 GHz |
| Instantaneous bandwidth | Up to 2.4 MHz (stable), 3.2 MHz (max) |
| Sample rate | Up to 3.2 Msps (2.4 recommended) |
| Resolution | 8-bit (I/Q) |
| Gain | 0–49.6 dB (auto or manual) |
| Direct sampling | HF mode for < 24 MHz |

### Recommended Settings
| Band | Sample Rate | Gain | Notes |
|------|------------|------|-------|
| 315 MHz | 1.024 Msps | 40 | Adequate for most 315 MHz devices |
| 433 MHz | 1.024 Msps | 40 | Standard for weather stations etc. |
| 868/915 MHz | 2.048 Msps | 42 | Wider BW for LoRa |

## Storage Calculations

| Sample Rate | Bits | Storage per Second | Storage per Minute | Storage per Hour |
|-------------|------|-------------------|-------------------|-----------------|
| 1 Msps | 8-bit I/Q | 2 MB/s | 120 MB/min | 7.2 GB/hr |
| 2 Msps | 8-bit I/Q | 4 MB/s | 240 MB/min | 14.4 GB/hr |
| 10 Msps | 8-bit I/Q | 20 MB/s | 1.2 GB/min | 72 GB/hr |
| 20 Msps | 8-bit I/Q | 40 MB/s | 2.4 GB/min | 144 GB/hr |

## File Formats
| Format | Extension | Description |
|--------|-----------|-------------|
| Complex unsigned 8-bit | .cu8 | RTL-SDR default (unsigned int8 I/Q pairs) |
| Complex signed 8-bit | .cs8 | HackRF default (signed int8 I/Q pairs) |
| Complex float 32-bit | .cf32 / .cfile | GNU Radio default (float32 I/Q pairs) |
| Complex signed 16-bit | .cs16 | Some SDRs, 16-bit signed I/Q |
| WAV | .wav | Some tools use WAV container for IQ data |

## Antenna Selection Guide
| Frequency | Recommended Antenna | Gain | Notes |
|-----------|-------------------|------|-------|
| < 500 MHz | Telescopic whip | 0 dBi | Extend to quarter-wave (17 cm for 433 MHz) |
| 433 MHz | DIY quarter-wave ground plane | 2 dBi | 17.3 cm element, 4 ground radials |
| 868/915 MHz | Quarter-wave monopole | 2 dBi | 8.2 cm element |
| 2.4 GHz | PCB or rubber duck | 2–5 dBi | Included with most SDRs |
| Wideband | Discone | -2 to 2 dBi | 25 MHz–1.3 GHz, good for surveys |
| Directional | Log-periodic / Yagi | 5–12 dBi | Frequency-specific, good for weak signals |
