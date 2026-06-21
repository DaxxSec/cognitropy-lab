# /sample-rate-plan

Plan the sample-rate / bandwidth / Nyquist budget for a capture or transmit application, sized to hardware and link constraints.

## Inputs

- **Signal(s) of interest** — center frequency(ies), individual bandwidths, total span if multiple.
- **Application** — narrowband single-signal, wideband survey, multi-channel.
- **Hardware** — SDR max sample rate, ADC bits, USB/PCIe link.
- **Host** — storage write speed (for capture), available RAM.
- **Constraints** — capture duration (drives storage), real-time vs. record-and-process.

## Steps

1. Read `context/concepts.md` "Nyquist + sample-rate fundamentals" + `context/references.md` "Sample-rate cheat-sheet".
2. Compute the minimum sample rate: for a signal of bandwidth B, need rate ≥ B (complex/IQ sampling captures B Hz of spectrum at rate B); apply an oversampling factor (typ. 1.25-2×) for filter roll-off room.
3. For multi-signal: if signals span total width W, need rate ≥ W to capture them in one pass (then channelize), OR retune per signal if they're far apart.
4. Check against hardware max sample rate + ADC bit depth (8-bit HackRF vs 12-bit USRP affects dynamic range, not rate).
5. Check link capacity: rate × bytes-per-sample × 2 (I+Q) must fit USB/PCIe throughput. (e.g. 20 Msps × 1 byte × 2 = 40 MB/s → at USB 2.0 limit.)
6. For capture-to-disk: rate × bytes/sample × 2 × duration = file size; check storage write speed sustains the rate.
7. Compute the Nyquist/aliasing budget — confirm the anti-alias filter + decimation will reject out-of-band energy.
8. Recommend the rate + bytes-per-sample format (int8 / int16 / float32) trading dynamic range vs. throughput.
9. Write the plan to `outputs/rate-plans/<app>-<YYYY-MM-DD>.md`.

## Output

A markdown rate plan at `outputs/rate-plans/<app>-<YYYY-MM-DD>.md` containing: signal(s) bandwidth analysis, minimum rate + chosen rate with oversampling rationale, sample format choice, link-capacity check (rate vs USB/PCIe), storage budget if capturing (file size + write-speed check), Nyquist/anti-alias budget, and any constraint that forced a compromise.

## Decision points

- **If required rate exceeds hardware max** → can't capture full span in one pass; channelize via retuning, or use wider-band hardware.
- **If required rate exceeds USB/PCIe link** → reduce sample format (int16→int8), reduce rate, or move to faster-link hardware.
- **If capture storage can't sustain the write rate** → faster storage (NVMe), compression (lossless on IQ ~2×), or shorter captures.

## Notes

- IQ (complex) sampling at rate R captures R Hz of bandwidth — not R/2. This is the key difference from real sampling; people who halve it waste half their rate.
- 8-bit vs 12-bit ADC is a dynamic-range decision (~48 dB vs ~72 dB), not a rate decision; weak-signal-near-strong-signal work needs the bits.
- Always leave Nyquist guard band — don't place a signal at the very edge of the captured bandwidth where the anti-alias filter rolls off.
- Record-and-process decouples capture rate from compute rate; real-time couples them and is the harder constraint.
