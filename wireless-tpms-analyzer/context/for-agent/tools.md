# Tools

## Primary Toolchain

### rtl_433
**Purpose:** Decode known TPMS, RKE, and other ISM-band transmissions in real time or from IQ files.

Key commands:
```bash
# Real-time decode, 315 MHz, JSON output
rtl_433 -f 315M -s 250k -F json

# Decode from saved IQ file
rtl_433 -r capture.cu8 -F json

# List all supported devices
rtl_433 -R help

# Force a specific decoder
rtl_433 -f 433.92M -R 59  # Schrader protocol 59

# Flex decoder from config file
rtl_433 -f 315M -c my_sensor.conf

# Output to file and stdout simultaneously
rtl_433 -f 315M -F json:output.json -F kv
```

Flex decoder syntax for custom protocols — key parameters: `name`, `modulation`, `short`, `long`, `reset`, `bits`, `rows`, `get`.

### inspectrum
**Purpose:** Visualize IQ captures, measure symbol timing, extract bit sequences manually.

Key workflows:
- Open `.cu8` file, set sample rate
- Add amplitude/frequency plot overlay to identify modulation
- Use cursor to measure pulse widths (read from status bar)
- Export derived symbols to text for further analysis

### Universal Radio Hacker (URH)
**Purpose:** Full protocol RE workflow — import IQ, demodulate, interpret bit stream, define protocol fields.

Key features:
- Auto-detect modulation and parameters
- Label protocol fields with names and bit widths
- Group repeated packets and diff them
- Built-in checksum/hash analyzer
- Fuzzing generator for protocol testing (research use)

### GNU Radio Companion
**Purpose:** Custom signal processing flowgraphs for non-standard protocols.

Typical TPMS flowgraph blocks:
```
RTL-SDR Source → Low Pass Filter → AM Demod (OOK) or NBFM Demod (FSK)
→ Threshold → Binary Slicer → Clock Recovery MM → File Sink / Message Passing
```

### SigDigger
**Purpose:** Fast IQ file characterization — identify signal parameters quickly before committing to a full RE session.

### Python DSP Scripts
Common patterns:
```python
import numpy as np
# Load RTL-SDR cu8 file
samples = np.fromfile('capture.cu8', dtype=np.uint8)
iq = (samples[::2] - 127.5) + 1j * (samples[1::2] - 127.5)

# OOK demodulation
envelope = np.abs(iq)
bits = (envelope > threshold).astype(int)
```

## Supporting Tools

| Tool | Use |
|---|---|
| `rtl_power` | Wideband power spectral survey to find active frequencies |
| `GQRX` / `SDR#` | Visual waterfall for initial characterization |
| `sox` | Audio-format signal processing (some TPMS tools output audio) |
| `jq` | Parse and filter rtl_433 JSON output |
| `fccid.io` | Look up FCC filings for sensor model documentation |
| Wireshark (with LTE/GSM dissectors) | Not directly applicable but useful mindset transfer |

## Hardware Reference

| Device | Freq Range | Best For |
|---|---|---|
| RTL-SDR v3 | 500 kHz – 1.75 GHz | 315/433 MHz TPMS capture |
| HackRF One | 1 MHz – 6 GHz | Wideband survey, 868 MHz coverage |
| YARD Stick One | 300–928 MHz | Protocol testing (own devices only) |
