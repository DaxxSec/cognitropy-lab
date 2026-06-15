# References — Schemas, Tables, and Catalogs

Compact lookup data for the RF spectrum knowledge base. Prose lives in `concepts.md`; this file is for fast reference.

## KB entry schema

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `id` | string | yes | stable key, e.g. `868300-lora-meter` (`<center_kHz>-<slug>`) |
| `name` | string | yes | human label |
| `freq_center` | number (Hz) | yes | center frequency |
| `freq_range` | [low, high] (Hz) | yes | `low ≤ center ≤ high` |
| `bandwidth` | number (Hz) | yes | occupied (99 %) or note the threshold used |
| `modulation` | enum/string | yes | FSK/GFSK/PSK/QAM/OFDM/DSSS/FHSS/AM/FM/… |
| `access` | enum | no | FDMA/TDMA/CDMA/OFDMA |
| `service` | string | yes | broadcast / mobile / aeronautical / ISM / amateur / … |
| `region` | enum | yes | ITU-1 / ITU-2 / ITU-3 + national tag |
| `occupancy` | string | no | duty cycle / time-occupancy summary |
| `identification` | enum | yes | `unidentified` / `probable` / `confirmed` |
| `confidence` | enum | yes | must match `identification` evidence |
| `provenance` | object | yes | observer, datetime, hardware, settings (freq/span/rate/gain/antenna), location, legal basis |
| `citations` | list | yes\* | required for any identity above `unidentified` |
| `first_seen` / `last_seen` | date | yes | from provenance |
| `status` | enum | yes | `active` / `intermittent` / `historical` |
| `review_by` | date | yes | re-verification deadline |
| `related` | list of ids | no | neighbours / variants / harmonics |
| `aliases` | list | no | absorbed ids from merges |

## Frequency band reference

| Band | Range | Typical occupants |
|------|-------|-------------------|
| LF | 30–300 kHz | time signals, RFID, navigation |
| MF | 300 kHz–3 MHz | AM broadcast, maritime |
| HF | 3–30 MHz | shortwave, amateur, over-the-horizon |
| VHF | 30–300 MHz | FM broadcast, air band (108–137), marine, VHF amateur |
| UHF | 300 MHz–3 GHz | TV, cellular, ISM 433/868/915, GPS L1 1575.42, ADS-B 1090, Wi-Fi/BT 2.4G |
| SHF | 3–30 GHz | Wi-Fi 5 GHz, radar, satellite, 5G mmWave (24–40) |
| EHF | 30–300 GHz | mmWave backhaul, radar, research |

## Common ISM / license-exempt bands (region-dependent)

| Band | Region note | Common devices |
|------|-------------|----------------|
| 13.56 MHz | global | NFC, RFID |
| 433.05–434.79 MHz | Region 1 | remotes, sensors, weather stations |
| 868 MHz | Europe (R1) | LoRa, smart meters, alarms |
| 902–928 MHz | Americas (R2) | LoRa, ISM telemetry |
| 2.400–2.4835 GHz | global | Wi-Fi, Bluetooth, Zigbee |
| 5.725–5.875 GHz | global ISM | Wi-Fi, video links |

## Modulation / fingerprint cheat-sheet

| Scheme | Waterfall fingerprint | Common in |
|--------|----------------------|-----------|
| OOK/ASK | on/off bursts, single carrier | cheap remotes |
| 2-FSK / GFSK | two parallel "rails" | sensors, BLE, LoRa preamble |
| FHSS | carrier hopping across a band | Bluetooth classic, some telemetry |
| DSSS | wideband noise-like, low PSD | older Wi-Fi, GPS |
| OFDM | flat-topped wideband block | Wi-Fi, LTE/5G, DVB |
| Chirp (CSS) | sloped sweep | LoRa payload |

## Occupancy & detection formulas

- Thermal noise floor: `−174 dBm/Hz + 10·log10(RBW_Hz) + NF_dB`
- Detection threshold: `noise_floor + margin` (margin ≈ 6 dB, or 3σ of the bin distribution)
- Occupied bandwidth: smallest span containing 99 % of total power
- Duty cycle: `t_active / t_window`; time-occupancy: fraction of windows with a detection

## Authoritative allocation sources

- ITU Radio Regulations & Table of Frequency Allocations — https://www.itu.int/pub/R-REG-RR
- ITU-R study group / SM-series (spectrum monitoring) — https://www.itu.int/rec/R-REC-SM/en
- FCC (US) frequency allocation chart / NTIA — https://www.ntia.gov/page/2011/united-states-frequency-allocation-chart
- Ofcom UK Frequency Allocation Table — https://www.ofcom.org.uk/spectrum/information/uk-fat

## Signal identification & community catalogs

- Signal Identification Wiki — https://www.sigidwiki.com/wiki/Signal_Identification_Guide
- RadioReference database — https://www.radioreference.com/

## Tooling reference

| Tool | Use |
|------|-----|
| `hackrf_sweep` / `rtl_power` | wideband power-vs-frequency sweeps → ingest CSVs |
| GQRX / SDR# / SDRangel | interactive survey + waterfall fingerprinting |
| Universal Radio Hacker (URH) | decode + signature extraction for `confirmed` IDs |
| Inspectrum | burst/symbol-level inspection of IQ recordings |

## FAQ entry template

```
### Q: <question in the asker's words>
**A:** <1–3 sentence grounded answer> [kb:<entry-id>], [ref:<source>]
_Confidence: <high/med/low> · Last verified: <date>_
```

## Citation conventions

- Internal: `[kb:<entry-id>]` (resolves to a file in `outputs/kb/`)
- External: `[ref:<short-name>]` with the full URL in the entry's `citations`
- Every `probable`/`confirmed` claim carries ≥1 citation; `unidentified` may carry none.
