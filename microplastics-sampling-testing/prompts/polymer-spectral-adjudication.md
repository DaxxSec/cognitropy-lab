# Prompt — Polymer Spectral Adjudication

## Purpose

Resolve a borderline polymer identification — the secondary-inspection adjudication. Use when the top library hit is below threshold, near-tied, or contradicts the particle's physics, and a guess would corrupt the composition data.

## Prompt Template

```
Adjudicate this microplastic polymer identification.

Spectrum: {FTIR | Raman}, acquisition {metadata: baseline, fluorescence, SNR}
Top hits (polymer : HQI):
  {hit_1}
  {hit_2}
  {hit_3}
Particle context: size {µm}, morphology {fragment/fiber/film/bead/foam},
  color {x}, weathering {pristine/oxidized}, density-cut it came through {medium}.
Diagnostic bands observed: {band_list_cm-1}

Decide:
1. Is the spectrum quality sufficient, or re-acquire / switch technique?
2. Does the top hit clear the HQI threshold AND the runner-up margin?
3. Do the observed diagnostic bands match the assigned polymer? (cite references.md)
4. Is the density consistent with the separation cut?
5. Could weathering explain a low score on a genuine plastic?
Verdict: confirmed <polymer> | confirmed natural/non-plastic | unresolved → {second technique}.
Give the one-line reason a reviewer would need.
```

## Expected Output

A verdict with explicit reasoning against threshold, margin, diagnostic bands, density consistency, and weathering — ending in `confirmed`, `natural`, or `unresolved → <next technique>`. Never a bare polymer name without the justification trail.
