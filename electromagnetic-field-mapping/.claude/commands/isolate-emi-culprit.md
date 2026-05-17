# /isolate-emi-culprit — Bisect an EMC/EMI Failure to the Offending Emitter

Localise the device or sub-system causing an emissions failure or radio-receiver interference. Uses a structured bisection (swap-out + proximity + spectral signature) rather than free-form swap-everything debugging.

## Inputs

- The failure description: failing frequency / range, observed amplitude vs. limit, regulatory standard if applicable (CISPR 32, FCC Part 15, EN 55032 for EMC; an SNR / RSSI degradation report for in-band interference).
- An inventory of candidate emitters: power supplies, switch-mode converters, microcontrollers + clocks, motors, radios, cables, displays.
- The result of `/map-near-field`, if already run.
- Available tools: spectrum analyser, near-field probes, current clamp, a known-good replacement subsystem for at least one suspect.

## Steps

1. **Characterise the offending emission** from the failing spectrum sweep: peak frequency, harmonic family, occupied bandwidth, modulation envelope. A clean line family with f0, 2·f0, 3·f0 is a switching converter; a comb with ~10 kHz spacing is a USB clock spread-spectrum recovery; a wideband bursty signal is often a digital interface (HDMI, MIPI, Ethernet) — see `context/concepts.md` § signatures.
2. **Hypothesise the candidate(s)** by matching the signature to suspect devices' known fundamental clock / switching rate. Build a ranked list (most-likely-first) of 3 – 5 suspects.
3. **Power-down bisection.** With the DUT in the failing mode, sequentially power off each candidate (or its sub-rail) while monitoring the failing line on the analyser. The drop attribution must be ≥ 10 dB to be conclusive; anything smaller is coupling, not source.
4. **Cross-check with proximity.** With a small H-field loop, walk over each candidate at constant height and re-confirm the candidate that drops the failing line is also a strong source at the failing frequency under near-field probing. The two checks should agree.
5. **Identify the coupling path.** A source is necessary but not sufficient — what carries the emission out? Common paths: cable common-mode, enclosure seam, ventilation aperture, ground bounce. Run a current clamp on each cable; the cable with the largest common-mode current at the failing frequency is the likely radiator.
6. **Propose mitigations** ranked by retrofit cost: snap-on ferrite (cheapest), shielded cable, board layout change (most expensive). Estimate the dB reduction from each per `context/references.md` mitigation table.
7. **Verify with one change at a time.** Apply the cheapest mitigation, re-run the failing test, record the new margin. If the failure now passes, stop; otherwise iterate. Never combine two mitigations in one test pass — the attribution will be lost.
8. **Document the root-cause chain.** Source → coupling path → emission. Save to `outputs/emi/<date>-<dut>-rootcause.md`. This trace is the artefact required for a clean post-mortem and for design feedback to engineering.

## Output

`outputs/emi/<date>-<dut>-rootcause.md` containing: emission signature, ranked suspect list, bisection log (with dB drops per power-down step), near-field confirmation, coupling-path evidence, ranked mitigations, verification results.

## Notes

- The 10 dB attribution threshold matters. A 3 dB drop when you power off the radio could be coupling-and-cancellation — confirm with near-field probing before naming a culprit.
- If two candidates each produce a partial drop, you have two correlated sources or a shared coupling path. Look at the common cable / ground network.
- Spread-spectrum clock modulation can hide a peak below the limit while still raising the average power above it — measure with both peak and quasi-peak detectors per CISPR 16.
- Cable-radiated emissions dominate above ~30 MHz for most cabled equipment. Suspect cables before suspecting the PCB unless near-field already proved otherwise.
