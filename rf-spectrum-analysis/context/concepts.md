# RF Spectrum Analysis — Core Concepts

Background the agent reads before acting. Optimised for fast recall, not exhaustive theory. Three interlocking frameworks: SPC, the palliative-care assessment frame, and the underlying RF measurement reality they sit on top of.

## RF Measurement Fundamentals

- **Spectrum analyser fundamentals.** Power vs frequency at a given instant. Resolution bandwidth (RBW) trades sensitivity for sweep speed: narrow RBW → more noise rejection but slower sweep. Video bandwidth (VBW) smooths the displayed trace; typically VBW = 0.3 · RBW.
- **FFT-based analysis (SDR world).** Sample rate → Nyquist bandwidth. FFT length N → bin width = sample_rate / N. Window function (Hann, Blackman-Harris, Flat-Top) shapes leakage vs sidelobe trade. PSD = |FFT|² normalised by N, window energy, and sample rate.
- **Noise floor.** A well-behaved measurement noise floor is approximately Gaussian after enough averaging. Its mean depends on receiver NF (noise figure), antenna temperature, integration time, and band. A *changing* noise floor (vs. a noisy one) is the SPC question this workspace exists to answer.
- **Occupancy.** Fraction of samples in a channel above a threshold (commonly noise floor + 6–10 dB) within a window. Inputs to capacity planning and to capability indices.
- **Reciprocal mixing & gain compression.** A strong adjacent emitter elevates the apparent noise floor on the desired channel by mixing with the local oscillator's phase noise. Often misread as "the band got noisier" — it didn't; the receiver did.
- **Antenna pattern matters.** A 6 dB gain difference between two antenna directions creates apparent emitter strength changes that are entirely measurement-side. Lock the antenna for any longitudinal record.

### Modulation quick-reference (limited; full table in `context/references.md`)

| Family | Examples | Typical fingerprint |
|--------|----------|---------------------|
| OOK / ASK | LPD remote keys, garage doors | Bursty single carrier; clear on/off envelope. |
| FSK / GFSK | 433/868/915 MHz IoT (LoRaWAN FSK mode, Sigfox D-BPSK) | Two/four tones; symmetric spectrum. |
| OFDM | Wi-Fi, LTE, 5G NR | Wide flat noise-like spectrum; well-defined channel boundary. |
| Chirp / CSS | LoRa | Up/down chirps visible in waterfall. |
| FHSS | Bluetooth Classic, some SCADA | Bursts hopping across band; ensemble shows uniform fill. |

## Statistical Process Control Primitives

### Variation: common cause vs special cause

- **Common-cause variation** — inherent to the process. Stable in distribution. Don't react to individual points; reacting *tampers* and increases variance (Deming's funnel experiment).
- **Special-cause variation** — assignable. Something changed; an investigation is justified.

SPC's job is to draw the line. The control chart provides the operational decision rule.

### Chart families

- **Variables charts** — continuous data.
  - `X-bar / R` — subgroup mean and range. Most common.
  - `X-bar / s` — subgroup mean and standard deviation. Use when subgroup size > 10.
  - `I-MR` — individuals and moving range. Use when natural subgroup size = 1.
  - `EWMA` — exponentially weighted moving average. Sensitive to small (≈0.5σ) persistent shifts.
  - `CUSUM` — cumulative sum. Similar sensitivity to EWMA; arguably easier to read for absolute shift magnitudes.
- **Attributes charts** — count or proportion.
  - `p` — proportion defective (variable subgroup size ok).
  - `np` — number defective (fixed subgroup size).
  - `c` — defect count per unit (fixed inspection unit).
  - `u` — defects per unit (variable inspection unit).

### Control limits

- **3σ default.** UCL = CL + 3σ̂; LCL = CL − 3σ̂. ARL₀ ≈ 370 under normality (false-alarm rate ≈ 0.27%).
- **σ̂ is estimated from baseline.** For X-bar/R: σ̂ = R-bar / d2(n). Constants A2, D3, D4, d2 — see `context/references.md`.
- **Western Electric & Nelson rules** — pattern detection on top of the 3σ rule. More sensitive, more false alarms. Use sparingly.

### Capability vs control

- **Control** — is the process stable? (Chart in-control? Then yes.)
- **Capability** — assuming control, does the process meet the spec? (Cp/Cpk).
- A process can be in-control and not capable (precision is fine but the mean is wrong relative to spec). Or capable and out-of-control (currently meeting spec but trending). SPC and capability indices ask different questions; report both.

## Palliative-Care Assessment Frame (Why This Cross-Domain Borrow)

Palliative care has spent decades operationalising the assessment of multidimensional, chronic, non-curable conditions. The transferable elements:

- **Multidimensional severity grading.** ESAS-r and similar instruments grade patients on multiple axes (pain, fatigue, drowsiness, depression, anxiety, appetite, wellbeing, shortness of breath, plus a free axis) at 0–10. Each axis is independently scored; total is descriptive, not used in isolation. The spectrum analogue: intensity / frequency / distress / trend, each scored independently.
- **Proportionate intervention.** The WHO analgesic ladder (3-step originally; commonly extended to 4–5 steps with interventional options) maps escalating symptom severity to escalating intervention. Don't start at the top.
- **Recurrence-aware monitoring.** Symptoms wax and wane. Single-visit assessment fails; longitudinal trajectory tracking is the practice. Maps directly to SPC's "the chart is the truth, the spot reading is a sample".
- **Multidisciplinary team review.** Complex cases get a structured MDT discussion: case summary, differential, options, recommendation, decisions required. RF interference issues often fail because the analyst, the SecOps team, and facilities aren't reading the same brief. MDT is the format that fixes that.
- **Comfort vs cure.** Many chronic symptoms can be mitigated without root-cause cure. The spectrum equivalent: sometimes you reassign a channel (palliative) rather than eradicate an interferer (curative); both are legitimate.

### Mapping table

| Palliative concept | RF spectrum analogue |
|-------------------|----------------------|
| Patient | The radio environment (site, band, channel) |
| Vitals | Noise floor, occupancy, peak power, packet-loss |
| Symptom | An emitter, interferer, drift, or user complaint |
| ESAS-r 0–10 multi-axis | `/symptom-assess` intensity/frequency/distress/trend |
| WHO analgesic ladder | `/intervention-ladder` Rungs 0–5 |
| Symptom diary / longitudinal record | `/longitudinal-track` trajectory |
| Comfort vs cure | Mitigation vs eradication (reassign channel vs locate and remove emitter) |
| MDT case discussion | `/spectrum-mdt-handoff` |
| Advance directive | Pre-agreed escalation criteria (when does this go to a regulator?) |

## Common Failure Modes

- **Limit chasing.** Re-baselining every time a chart goes out-of-control instead of investigating. This launders special causes into wider limits and silently degrades capability.
- **Subgroup-size drift.** Changing how many sweeps make a subgroup mid-record. Limits become non-comparable; the chart is no longer interpretable.
- **Measurement contamination.** Antenna moved, gain changed, USB hub rebooted, building HVAC switched on. All produce spurious special-cause signals. Lock conditions or document changes.
- **Distress inflation.** Grading every channel as `Distress = 8` so it "gets attention". The result: severity grading becomes politically rather than evidentially driven. Anchor distress to specific named affected systems and SLAs.
- **Premature intervention.** Skipping Rung 1 (reconfigure receiver) and going straight to Rung 4 (mitigate at source). 30–60% of "interference" complaints are actually receiver-side measurement artefacts.
- **Forgotten longitudinal record.** Quarterly site-survey deliverables that are not stitched together over time. Each report stands alone; trends invisible.
- **Stability-ignored capability.** Reporting Cpk on an out-of-control process. Numbers are mathematically valid, operationally meaningless.

## Operating Constraints

- **Receive-only by default.** Active probing (transmit) needs a licence or experimental authorisation under the local regulator (FCC Part 5/15 / Ofcom / BNetzA / ACMA / Innovation Canada).
- **Don't decode prohibited communications.** Several jurisdictions restrict listening to certain bands (encrypted public-safety, cellular operator backhaul, satellite uplinks) even when technically receivable.
- **Site permissions.** Long-term receiver deployment in shared facilities requires written authorisation from the facility owner.
- **Privacy.** A long-term spectrum recording may incidentally capture personal data (cordless headphones, baby monitors). Apply minimisation: don't retain demodulated audio/data beyond the analysis window; document retention in the baseline manifest.
