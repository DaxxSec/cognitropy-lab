# Environment

> Populated by `/onboard`. Until then this is a checklist for the user.

## SDR Hardware

| Field | Value |
|-------|-------|
| Primary SDR | (HackRF One / RTL-SDR v3 / USRP B210 / X310 / BladeRF 2.0 / LimeSDR / Pluto) |
| Instantaneous bandwidth | (e.g. 80 MHz on USRP B210) |
| Frequency range | (e.g. 70 MHz – 6 GHz) |
| Sample-rate ceiling | (e.g. 56 MS/s on B210) |
| Reference clock | (internal / external 10 MHz / GPSDO) |
| Antenna(s) | (wideband disc, log-periodic, frequency-specific dipole) |
| RF front end | (LNA, attenuator, filter — model + insertion loss) |
| RF-isolated environment | (Faraday cage, anechoic chamber, none) |

GPSDO is strongly recommended for FHSS work — un-disciplined LO drift directly degrades the channelizer.

## Compute

| Field | Value |
|-------|-------|
| OS | (Linux preferred; macOS works for analysis) |
| CPU | (cores + arch) |
| RAM | (≥ 16 GB for typical 1 s @ 80 MS/s captures) |
| GPU | (optional; helps PyMC NUTS for large hyperparameter spaces) |
| Storage | (capture path + free space) |

## Software Stack

The agent expects:

- `python3.10+` with: `numpy`, `scipy`, `matplotlib`, `pymc>=5`, `numba`, `sigmf`, `arviz`
- `gnuradio>=3.10`
- `gr-bluetooth` (compiled against the same GR version)
- `inspectrum` for visual capture inspection
- `urh` for downstream protocol decoding
- `rtl_433` for known-protocol comparison
- `hackrf` / `uhd` / `bladerf` host tools (whichever match the SDR)
- `git`, `make`, a C/C++ toolchain (for compiling GR out-of-tree modules)

## Capture Conventions

All captures land in `outputs/captures/<YYYY-MM-DD>/` and must be SigMF-tagged:

```
{
  "global": {
    "core:datatype": "ci16_le",
    "core:sample_rate": 80000000,
    "core:hw": "HackRF One",
    "core:author": "<your-name>",
    "core:description": "Bluetooth Classic calibration capture"
  },
  "captures": [{
    "core:sample_start": 0,
    "core:frequency": 2441500000,
    "core:datetime": "2026-05-06T10:00:00Z"
  }],
  "annotations": []
}
```

The agent enforces SigMF metadata on every capture before running analysis. A capture without metadata is rejected with a request to populate the JSON.
