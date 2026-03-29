# Modulation Identification Cheatsheet

Quick reference for identifying signal modulation type from waterfall display or IQ file inspection.

## Visual Identification in GQRX / SDR#

| What you see in the waterfall | Likely modulation |
|---|---|
| Narrow signal, signal appears/disappears (on/off) | OOK / ASK |
| Two distinct frequency bands alternating | FSK |
| Signal stays on but varies in brightness | ASK (amplitude) |
| Consistent frequency, regular phase reversals | BPSK (less common in TPMS) |
| Wide deviation, changes frequency rapidly | WBFM (not TPMS) |

**TPMS signals typically look like:** A narrow burst (~10–50 ms) that appears, transmits cleanly, and disappears. Repeats 3–6 times. At 315 MHz these bursts often appear spaced ~1 second apart.

---

## OOK (On-Off Keying)

**How it works:** Carrier is ON for a 1-bit, OFF for a 0-bit (or vice versa). The simplest amplitude modulation.

**In inspectrum:** Amplitude plot shows clean HIGH/LOW transitions. Measure pulse widths directly.

**Variants:**
- **OOK-NRZ:** Direct: 1=long pulse, 0=short pulse (or vice versa). Measure by pulse duration.
- **OOK-PWM:** Pulse Width Modulation: 0 and 1 encoded as different pulse widths.
- **OOK-PPM:** Pulse Position Modulation: encoded as gap width between pulses.
- **OOK-Manchester:** Each bit is 2 symbols. Rising edge = 1, falling edge = 0 (or reverse). Recognizable by constant transition rate — every symbol period has one edge.

**rtl_433 modulation codes:** `OOK_PWM`, `OOK_PPM`, `OOK_MC_ZEROBIT`

**Common TPMS uses:** Schrader (NA), Pacific Industries, most older NA sensors.

---

## FSK (Frequency Shift Keying)

**How it works:** Two frequencies represent 0 and 1. The carrier is always on — signal is identified by frequency deviation.

**In inspectrum:** Frequency plot shows alternating between two frequency levels. The spread is the FSK deviation (typically ±25–75 kHz at 433 MHz).

**In GQRX:** Signal appears as a wider, always-present band that "shifts" subtly when data is being sent.

**rtl_433 modulation codes:** `FSK_PCM`, `FSK_MC_ZEROBIT`, `FSK_PULSE_PCM`

**Common TPMS uses:** Continental (EU), Huf/RDKS, most European OEM sensors.

**Key parameter:** Deviation — how far above/below center frequency the two states are. Typical: ±38 kHz for 433.92 MHz TPMS.

---

## Encoding Within Modulation

Once you identify OOK or FSK, you still need to determine the bit encoding:

| Encoding | Description | How to identify |
|---|---|---|
| NRZ | 0=short/low, 1=long/high | Two distinct pulse widths |
| Manchester | Each bit = 2 symbols with a transition | All pulse widths are equal (half-bit period) |
| Differential Manchester | Transition at start of every bit, extra transition = 1 | Complex but consistent |
| Return-to-Zero (RZ) | Pulse always returns to zero mid-bit | Pulses are shorter than bit period |

**Manchester tip:** If you see only one pulse width in an OOK signal, it's likely Manchester encoded. The bit = the edge direction, not the level.

---

## Symbol Rate Estimation

```
Symbol rate (baud) = 1 / pulse_width_seconds

Example: pulse width = 200 µs = 0.0002 s
Symbol rate = 1 / 0.0002 = 5000 baud = 5 kbaud

For Manchester: actual bit rate = symbol_rate / 2 = 2.5 kbps
```

Typical TPMS symbol rates: 2.5–10 kbaud

---

## Common Problems

| Symptom | Likely Cause |
|---|---|
| No signal visible | Wrong frequency, too far from vehicle, or vehicle not moving |
| Signal present but rtl_433 can't decode | Unknown protocol — use `/protocol-map` |
| Lots of garbage output | Gain too high — reduce with `-g 30` or lower |
| Packets decoded but pressure looks wrong | Conversion formula mismatch — check scale factor |
| Only 3 sensors found (expecting 4) | One sensor faulty or not activated — roll the vehicle more |
