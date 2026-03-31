# Environment

## Runtime Context

This agent runs in a Claude conversation session. The user may or may not have code execution available depending on their Claude setup. Assume the user might be running Claude with tool access (code execution, web search) but design outputs to be useful even without those tools.

## Expected User Hardware

Based on the target audience, assume users may have one or more of the following:

**SDR Hardware:**
- RTL-SDR (RTL2832U-based dongles) — cheap, ~$25, receive-only, ~24 MHz to ~1.7 GHz
- HackRF One — ~$350, receive and transmit (with appropriate licensing), 1 MHz to 6 GHz
- USRP (B200/B205mini) — professional SDR, wider coverage, higher dynamic range
- Airspy — high dynamic range SDR, 24–1800 MHz

**Computing:**
- Linux workstation (Ubuntu/Debian most common in the SDR community)
- macOS with SDR software installed
- Raspberry Pi for portable ground station setups

**Software Ecosystem (assume available):**
- GNURadio — the primary SDR signal processing framework
- SatDump — satellite imagery and signal decoder
- SDR# (Windows) or Gqrx (Linux/macOS) — SDR receivers
- gr-satellites — GNURadio blocks for amateur satellite protocols
- Predict or GPredict — orbital pass prediction
- Hamlib/rigctl — radio control library
- Python 3 with: numpy, scipy, matplotlib, skyfield, pyorbital, construct (for binary parsing)

## Available Python Libraries for Simulation

When generating simulation code, prefer these libraries:

```python
# Orbital mechanics and pass prediction
from skyfield.api import load, EarthSatellite, Topos
from skyfield.positionlib import Geocentric

# Signal processing
import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

# Binary protocol parsing
import construct  # for declarative struct parsing
import bitstring  # for bit-level manipulation

# RF calculations
# (usually done with numpy directly — no dedicated library needed)
```

## File Formats the Agent Should Know

- **TLE files** — Two-Line Element sets for orbital parameters
- **IQ files** — Raw complex samples (float32, int16, uint8), used by SDR software
- **WAV files** — Sometimes used to store IQ data or audio from satellite passes
- **AX.25 frames** — Binary frames, often in KISS format over serial or TCP
- **CCSDS binary** — Raw binary conforming to CCSDS Blue Book specifications
- **SatDump output** — JSON/binary telemetry outputs from decoded satellites

## Typical Session Flow

1. User describes a satellite system or protocol they're interested in
2. Agent clarifies the specific protocol version and context
3. Agent produces either: a simulation, a test scenario, a frame decoding, a link budget, or a security analysis
4. User iterates, asking for modifications or exploring edge cases
5. Agent produces Python code, tables, or annotated examples as artifacts
