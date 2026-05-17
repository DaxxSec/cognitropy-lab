# /map-near-field — Structured Near-Field Scan

Execute a structured near-field scan over a device-under-test (DUT) or board, producing a calibrated 2D or 3D field map for EMC investigation, PCB hot-spot work, or antenna near-field characterisation.

## Inputs

- The DUT under power, in a representative operating mode (CPU loaded, radio TX, motor running). Document the operating mode — fields change with it.
- A near-field probe set (H-field loops in graduated diameters, e.g. 5 mm / 10 mm / 30 mm; E-field stub probes; sometimes a coaxial E-field shielded loop).
- Spectrum analyser (or VNA in receiver mode) with calibrated probe-to-field correction factors.
- Grid spacing (default 5 mm for PCB, 10 – 25 mm for full enclosure).
- Frequency or frequency span of interest. If unknown, run a 10 MHz – 3 GHz pre-sweep first.

## Steps

1. **Pre-scan the spectrum** with the largest loop at one fixed point ~10 mm above the DUT to identify dominant emission frequencies. Lock the analyser to the strongest 1 – 4 lines for the spatial scan.
2. **Mount the DUT and reference frame.** Use a non-conductive jig. Define an origin and `x,y,z` axes; do **not** rely on freehand probing — a 2 mm position error at 5 mm height is a 14 dB amplitude error.
3. **Choose the loop diameter.** Smaller loop → better spatial resolution but lower sensitivity. Run the scan at the smallest loop that still gives ≥10 dB above the noise floor for the target frequency.
4. **Execute the spatial scan.** Move the probe over the grid at constant height `h` (typically 2 – 10 mm). For each `(x,y)` record peak amplitude over a brief dwell (≥ 10× the symbol / period of the source). Maintain probe orientation — the loop normal direction selects which H-field component you see; do at least an `Hx` and `Hy` pass for full coverage.
5. **Apply the probe correction factor** in dB to convert measured `Vrx` to A/m or V/m. Probe factors are frequency-dependent — use the calibration curve from the probe's certificate. Note the conversion in metadata.
6. **Produce a 2D heat map per frequency / per orientation** with `outputs/maps/<date>-<dut>-<freq>-<orient>.png`. Overlay the DUT outline (PCB silkscreen or enclosure top-view) for human readability.
7. **(Optional) Z-stack for 3D.** Repeat at multiple heights to build a volumetric near-field map. Useful when the dominant emitter is buried inside an enclosure.
8. **Identify hot-spots.** Rank the top-N peaks by magnitude and by gradient (a sharp peak is a localised source; a broad lobe is a distributed current path).
9. **Hand off** to `/isolate-emi-culprit` for the bisection step.

## Output

`outputs/maps/<date>-<dut>-<freq>-<orient>.png` and a CSV `outputs/maps/<date>-<dut>.csv` containing per-cell readings with metadata. A short markdown summary of top-N hot-spots in `outputs/maps/<date>-<dut>-summary.md`.

## Notes

- Probe-to-DUT proximity matters more than analyser settings. Always record `h` and probe loop diameter.
- The H-field loop is selective by orientation — running only one orientation will miss currents running along that axis.
- Above 2 GHz, cable-coupled radiation can dominate the map. Use ferrites on the probe cable and re-test to confirm what you're seeing comes from the DUT.
- For antenna near-field characterisation use a planar / spherical / cylindrical scan per IEEE Std 149-1979, not the EMC-style heat map.
