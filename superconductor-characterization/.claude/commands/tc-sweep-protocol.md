# /tc-sweep-protocol

Generate a four-probe R(T) Tc-sweep procedure for a specific sample. Returns a measurement procedure with explicit excitation, sweep rate, uncertainty budget, and the per-sample capacity cost that feeds back into `/sample-queue-plan`.

## Inputs

- Sample ID, material class (LTS bulk, HTS coated conductor, MgB2, Bi-2212/2223 tape, unconventional), nominal expected Tc (K) with uncertainty window
- Sample geometry: length × width × thickness, contact pads positions and material (Ag, In, Au-wire-bond, sputtered Au, pressed-In)
- Cryostat: bath / VTI / closed-cycle, temperature range, thermometer (Cernox + CCS), expected ramp rate (K/min)
- Measurement criterion for Tc: 50 % drop, onset, zero-resistance, or 1 µV/cm definition
- Available bias current set (10 µA, 100 µA, 1 mA, 10 mA, custom) and pulse vs DC

## Steps

1. Compute expected sample resistance at room temperature and just-above-Tc using sheet resistance × geometry; verify it lies inside the nanovoltmeter range at the planned bias.
2. Choose a bias current that gives a measurable V (target ≥10 µV at 4-probe ≥ 1 mΩ samples) while keeping current density well below Jc. For HTS samples, additionally check 1 µV/cm corresponds to bias × sample-length / (chosen current) — common practice for Ic definition.
3. Plan contact configuration: I+ / V+ / V− / I− on outer/inner pads with V-contacts at least 1 mm inside the I-contacts to avoid current-spreading artefacts.
4. Specify sweep policy: ramp from T_high (≥1.5 × Tc) to T_low (≤0.5 × Tc) at 0.2 K/min through the transition, 1 K/min outside it. Repeat on warming to confirm reversibility (no thermal hysteresis from poor anchoring).
5. Specify data cadence: lock-in time-constant 100–300 ms with 5×TC settle between points; record T_sample, T_block, B (residual ≤ 1 mT verified), V, I, timestamp.
6. Estimate measurement uncertainty: dominated by thermometer accuracy (~10 mK for Cernox calibrated, ~50 mK uncalibrated) and self-heating at the contacts. Quote Tc as a value ± expanded uncertainty (k=2).
7. Estimate capacity cost: cooldown (4–24 h depending on cryostat), measurement (1–4 h), warmup (2–6 h), sample exchange (0.5–1 h). Feed this back into `/sample-queue-plan`.
8. Reference the applicable IEC 61788 part (e.g. IEC 61788-10 for Tc by resistivity method) for reporting conventions.

## Output

Markdown procedure at `outputs/tc-sweep-<sample-id>-<YYYY-MM-DD>.md`:
- Instrument settings (bias, time-constant, ramp rates, sample-rate)
- Per-step protocol checklist (mount → anchor → cool → sweep → warm → unload)
- Uncertainty budget table
- Capacity cost (hours, helium L) feeding the queue planner

## Notes

- Self-heating at the contacts can shift apparent Tc by tens of mK; verify contact resistance ≤ 1 µΩ·cm² for high-current samples before trusting a sweep.
- For HTS samples near 90 K, ambient field of the cryostat can shift Tc and broaden the transition; trap-cool or use μ-metal shielding for narrow transitions.
- AC R(T) via lock-in at 17–73 Hz is generally cleaner than DC, but at very low resistance use a transformer pre-amp and watch for ground loops.
- Don't conflate "midpoint Tc" and "onset Tc" in a report — the Tc Tinkham defines and the Tc a magnet designer uses are not the same number.
