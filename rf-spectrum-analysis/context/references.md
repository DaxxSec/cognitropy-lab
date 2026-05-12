# RF Spectrum Analysis — Reference Tables

Compact lookup data. The agent reaches for this mid-task instead of re-deriving.

## SPC Constants for X-bar / R Charts

| n | A2 | D3 | D4 | d2 |
|---|----|----|----|----|
| 2 | 1.880 | 0    | 3.267 | 1.128 |
| 3 | 1.023 | 0    | 2.575 | 1.693 |
| 4 | 0.729 | 0    | 2.282 | 2.059 |
| 5 | 0.577 | 0    | 2.115 | 2.326 |
| 6 | 0.483 | 0    | 2.004 | 2.534 |
| 7 | 0.419 | 0.076 | 1.924 | 2.704 |
| 8 | 0.373 | 0.136 | 1.864 | 2.847 |
| 9 | 0.337 | 0.184 | 1.816 | 2.970 |
| 10 | 0.308 | 0.223 | 1.777 | 3.078 |

Source: AIAG SPC Reference Manual, 4th ed., Appendix B.

## Western Electric Rules

1. One point > 3σ from CL.
2. 2 of 3 consecutive points > 2σ on the same side.
3. 4 of 5 consecutive points > 1σ on the same side.
4. 8 consecutive points on the same side of CL.
5. 6 consecutive points trending up or down.
6. 14 consecutive points alternating up and down.
7. 15 consecutive points within 1σ (over-control / re-baseline candidate).
8. 8 consecutive points outside 1σ either side.

## Capability Index Verdict and DPMO

| Cpk / Ppk | Verdict | Expected DPMO (one-sided, normal) |
|-----------|---------|-----------------------------------|
| ≥ 1.67 | Excellent (Six Sigma) | ≤ 0.6 |
| 1.33–1.67 | Capable | 0.6 – 32 |
| 1.00–1.33 | Marginal | 32 – 1 350 |
| 0.67–1.00 | Not capable | 1 350 – 22 750 |
| < 0.67 | Inadequate | > 22 750 |

## Severity-Tier Rubric (workspace-specific, ESAS-inspired)

| Axis | 0 | 1–3 | 4–6 | 7–9 | 10 |
|------|---|-----|-----|-----|----|
| Intensity (above baseline) | 0 dB | +1 to +3 dB | +4 to +10 dB | +11 to +25 dB | > +25 dB |
| Frequency (duty cycle) | None | < 1% | 1–25% | 26–75% | > 75% |
| Distress | No system affected | Annoyance only | Documented degradation | Service-impacting | Safety / compliance critical |
| Trend | −5 improving fast | −2 improving | 0 stable | +2 worsening | +5 worsening fast |

**Tier mapping:** Sum of `intensity + frequency + distress + |trend|`. `0–8 = Tier 1`, `9–16 = Tier 2`, `17–24 = Tier 3`, `25+ = Tier 4`.

## ISM and SRD bands (selected; verify locally)

| Band | Region | Typical use | Max EIRP (typ.) |
|------|--------|-------------|-----------------|
| 433.05–434.79 MHz | EU SRD (R1) | Car keys, sensors, LPD | 10 mW ERP |
| 868–868.6 MHz | EU SRD (R1) | LoRa, Sigfox, Wireless M-Bus | 25 mW ERP |
| 902–928 MHz | US ISM (R2) | LoRa, Sigfox, 900 ISM mesh | 1 W (FHSS) |
| 2400–2500 MHz | Global ISM | Wi-Fi, Bluetooth, ZigBee, microwave ovens | 100 mW EIRP (1 W in US FHSS) |
| 5725–5875 MHz | Global ISM | Wi-Fi 5/6/6E, point-to-point | 1 W EIRP (typ.) |
| 5945–7125 MHz | Wi-Fi 6E / 7 | UNII-5/6/7/8 | LPI / SP per region |
| 24.000–24.250 GHz | Global ISM | Doppler radar, FMCW | per region |

## Modulation-Family Cheat-Sheet

| Family | Spectrum look | Typical bandwidth | Where you find it |
|--------|---------------|-------------------|-------------------|
| OOK / ASK | Bursty single carrier | < 100 kHz | LPD remotes, ASK temperature sensors |
| FSK / GFSK | Two/four tones, symmetric | 10 kHz – 1 MHz | 433/868/915 IoT |
| MSK / GMSK | Constant envelope, smooth | 200 kHz | GSM legacy, AIS marine |
| LoRa (CSS) | Up/down chirps in waterfall | 125 / 250 / 500 kHz | Long-range IoT |
| BPSK / QPSK | Flat, two-/four-state constellation | as designed | Satellite, DVB |
| OFDM | Wide flat noise-like | channel-wide | Wi-Fi, LTE, 5G NR, DVB-T2 |
| FHSS | Bursts hopping; ensemble uniform | per hop | Bluetooth Classic, SCADA |
| DSSS | Spread, processing-gain visible | wider than data | Wi-Fi 802.11b, GPS |

## SDR Quick-Reference

| Device | Tuning | Inst. BW | Typical sample rate | Notes |
|--------|--------|----------|---------------------|-------|
| RTL-SDR Blog v4 | 24 MHz – 1.766 GHz (HF via direct sampling) | ~2.4 MHz | up to 3.2 MS/s | Cheapest; 8-bit ADC. |
| HackRF One | 1 MHz – 6 GHz | ~20 MHz | up to 20 MS/s | Half-duplex; 8-bit; well supported by `hackrf_sweep`. |
| Airspy R2 / Mini | 24 MHz – 1.8 GHz | ~10 MHz | up to 10 MS/s | 12-bit ADC, better DR. |
| USRP B205mini | 70 MHz – 6 GHz | ~56 MHz | up to 61.44 MS/s | UHD; full-duplex; lab-grade. |
| KrakenSDR | 24 MHz – 1.766 GHz × 5 ch | ~2.4 MHz | up to 2.56 MS/s | Coherent 5-channel; DoA. |
| Tek RSA600 / R&S FSV | per model | wide | n/a | Vendor-class real-time spectrum analysers; deep analysis modes. |

## Upstream Catalogues

- **Sigidwiki — Signal Identification Guide** — https://www.sigidwiki.com/ — community catalogue of known emission types with audio/waterfall samples.
- **ITU Radio Regulations** — https://www.itu.int/pub/R-REG-RR — global allocation, footnotes, region tables.
- **FCC Online Table of Frequency Allocations** — https://www.fcc.gov/oet/spectrum/table — US allocations and notes.
- **ETSI EN 300 220** — https://www.etsi.org/standards-search?search=EN+300+220 — EU SRD spec for the 25–1000 MHz range.
- **AIAG SPC Reference Manual (4th ed.)** — canonical industrial SPC reference, constants tables, attribute charts.
- **ISO 22514-2** — capability statistics in time-dependent processes.
- **NIST/SEMATECH e-Handbook of Statistical Methods** — https://www.itl.nist.gov/div898/handbook/ — free reference covering SPC, capability, normality testing.
- **ESAS-r Administration Manual (Alberta Health Services)** — https://www.albertahealthservices.ca/assets/info/peolc/if-peolc-ed-esas-r-administration-manual.pdf — the multidimensional symptom rubric the workspace's severity axes are modelled on.
- **WHO Pain Ladder / Cancer Pain Relief guidance** — https://www.who.int/publications/i/item/9789241550390 — the proportionate-intervention pattern adapted in `/intervention-ladder`.

## Operating Cheat-Sheets

- **A2·R-bar gives the X-bar half-width.** For n=5, A2=0.577. So UCL_X-bar = X-bar-bar + 0.577·R-bar.
- **σ̂ from R-bar:** σ̂ = R-bar / d2(n). For n=5, d2=2.326.
- **EWMA σ:** σ_EWMA = σ·√(λ/(2−λ)·(1−(1−λ)^(2t)))  → asymptotically σ·√(λ/(2−λ)).
- **CUSUM tabular defaults:** k = 0.5σ (reference value), h = 4σ (decision interval). For 1σ shifts, ARL ≈ 8.4 vs ARL₀ ≈ 168.
- **Cpk and Ppk differ when within-subgroup σ differs from overall σ.** If the chart is in-control they are close; if Ppk << Cpk, there is between-subgroup variation the chart didn't catch — re-examine subgrouping.
- **6 dB above noise floor** is the conventional threshold for "this is a signal not noise" in occupancy calculations. Some workflows use 3 dB (more sensitive, more false positives) or 10 dB (less sensitive).
