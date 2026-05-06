# /hop-set-prior — Build a Prior over Candidate Hop Channels

Construct a prior distribution `p(channel_active)` over candidate hop channels. This prior feeds `/dehop-bayes` and dramatically tightens posteriors when good external information exists.

## Inputs

- Target system identifier (from `context/project.md`)
- Optional FCC ID (for regulator-filing lookup)
- Optional capture path (if pre-existing wideband data is available)
- Band of interest (start_freq, stop_freq)

## Steps

### 1. Identify the band's regulatory regime
- Look up the FCC / ETSI / national-regulator allocation for the band.
- Pull legal channel grids (e.g. 2.4 GHz Bluetooth Classic = 79 channels at 1 MHz spacing starting at 2402 MHz).
- Initial prior: uniform over the legal channel grid.

### 2. Pull regulator filings if FCC ID is given
- Use `https://fccid.io` to fetch the test report.
- Extract: declared hop count, hop rate, hop band, modulation, dwell.
- Tighten the prior with these declared parameters. Filings are not always accurate, so down-weight them rather than locking — `p(declared) = 0.7`, `p(other_grids) = 0.3 / |other_grids|`.

### 3. Pull observed energy from capture
- If a capture is provided, run a long-window FFT (1 s integration if available).
- Channels with persistent energy → prior weight increased.
- Channels with no energy → prior weight decreased but not zero (system might not have used them in this capture).
- This is an empirical-Bayes step; flag it in the report as such.

### 4. Mix with system-specific knowledge
For known systems, use the system-specific prior:

| System | Prior |
|--------|-------|
| Bluetooth Classic | Uniform over 79 channels, channel 0 at 2402 MHz, 1 MHz spacing |
| BLE | Uniform over 37 data channels (channels 0–36 in BLE numbering, mapped to 2404, 2406, ..., 2480 MHz) plus 3 advertisement channels (37, 38, 39 → 2402, 2426, 2480) |
| WMBus mode N | 8 channels at 169.40625, 169.41875, ..., 169.4750 MHz |
| LoRa US 902–928 | 64 uplink channels at 902.3, 902.5, ..., 914.9 MHz, 8 downlink at 923.3, ... |
| Unknown | Uniform over the user-specified band, channel BW estimated from autocorrelation |

### 5. Combine
Bayes-rule combine:
```
prior(channel_k) ∝ regulator_prior(k) * empirical_prior(k) * system_prior(k)
```
Normalise to sum to 1.

### 6. Output

Write to `outputs/<engagement>/hop-set-prior.json`:

```
{
  "band": [2402000000, 2480000000],
  "K_candidate": 79,
  "channel_grid_hz": [2402000000, 2403000000, ..., 2480000000],
  "channel_bw_hz": 1000000,
  "prior": [0.0127, 0.0127, ..., 0.0127],
  "evidence_weights": {
    "regulator": 0.4,
    "empirical": 0.4,
    "system": 0.2
  },
  "notes": "Pulled from FCC ID 2APXJ-WL400 + 1 s capture observation"
}
```

## Output

A normalised prior over candidate channels, ready for `/dehop-bayes`. The prior is informative — using it improves dehop accuracy by 10–30 percentage points on low-SNR captures vs. a flat prior.
