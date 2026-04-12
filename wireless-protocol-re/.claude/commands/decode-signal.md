# /decode-signal — Signal Decoding Walkthrough

Walk through decoding from raw IQ capture to protocol frame structure.

## Required Inputs
- IQ capture file path or signal description
- Sample rate and center frequency
- Any known information about the signal

## Steps

### 1. Visual Inspection
Load in Inspectrum/GRC. Identify modulation from FFT shape. Measure bandwidth and symbol rate.

### 2. Modulation ID
- OOK/ASK: amplitude envelope with binary pattern
- 2-FSK: two discrete instantaneous frequency levels
- GFSK: smooth frequency transitions
- PSK: phase clusters in constellation
- LoRa: chirp pattern in spectrogram

### 3. Demodulation
Apply appropriate demodulator. Provide GNU Radio blocks or URH config.

### 4. Bit Recovery
Determine symbol rate, apply clock recovery (M&M or Gardner), extract bitstream, find byte alignment.

### 5. Frame Structure
Compare multiple transmissions for: preamble, sync word, length field, address/ID (static), payload (dynamic), CRC.

### 6. CRC Identification
Try common algorithms from domain knowledge reference. Try bit reversal and byte swapping if standard CRCs fail.

### 7. Document
Output frame specification to `outputs/` with bit-level diagram, field descriptions, CRC params, and examples.
