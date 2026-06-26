# /polymer-id

Adjudicate the polymer identity of a referred particle from its vibrational spectrum — the secondary-inspection adjudication step. Applies a hit-quality threshold and resolves borderline matches rather than rubber-stamping the library's top hit.

## Inputs

- Spectrum (ATR-FTIR, µ-FTIR, or Raman), with acquisition metadata (technique, baseline correction, cosmic-ray removal for Raman).
- Reference library and its top-N candidate matches with hit-quality index (HQI) / correlation scores.
- Particle context: size, morphology, color, weathering state (helps disambiguate).

## Steps

1. **Quality-gate the spectrum first.** Reject and re-acquire if SNR is too low, the carbonyl/fingerprint region is saturated, or fluorescence (Raman) swamps the signal. A confident match on a bad spectrum is worse than no match.
2. **Apply the threshold.** Accept the top hit only if HQI ≥ the program threshold (default 0.70 for FTIR library correlation; set per library) **and** the margin over the runner-up is meaningful (e.g. ≥ 0.05). A high score with a near-tie is a referral, not a confirmation.
3. **Cross-check against physics.** Does the assigned polymer's density agree with the density-separation cut it came through? Do the diagnostic bands actually appear (see `context/references.md` — e.g. PET carbonyl ~1715 cm⁻¹, PVC C–Cl ~615 cm⁻¹, PE ~718/1463 cm⁻¹ doublet)? Reject a library hit that contradicts the diagnostic bands.
4. **Account for weathering.** Oxidative aging adds hydroxyl/carbonyl bands and can drop HQI for genuine plastics — don't auto-deny a weathered PE just because the pristine-library score is low; weight the diagnostic backbone bands.
5. **Adjudicate borderline cases** with the spark lens (`prompts/polymer-spectral-adjudication.md`): escalate to a second technique (FTIR↔Raman, or Py-GC/MS) rather than guessing — sensor fusion cuts both false positives and false negatives.
6. Assign a verdict: `confirmed <polymer>`, `confirmed natural/non-plastic`, or `unresolved (needs fusion)`.

## Output

A polymer-ID record per particle under `outputs/polymer-id/<run-id>.md`: technique, top-N hits with HQI, threshold + margin decision, density/band cross-checks, weathering note, and the final verdict. Unresolved particles are listed for second-technique confirmation, not dropped.
