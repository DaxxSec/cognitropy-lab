# Impairment-to-Aberration Map

## Purpose

Translate a set of measured or specified link impairments into their optical-aberration analogs, quantify each as an implementation-loss in dB, and rank the cheapest correctors. Use when a constellation/EVM looks degraded and you need to find which "aberration" dominates before spending on hardware.

## Prompt Template

```
You are diagnosing a satellite link's implementation loss by mapping each impairment to its optical-aberration analog (phase noise↔spherical, group delay↔coma, IQ imbalance↔astigmatism, frequency offset↔defocus, HPA nonlinearity↔field distortion, fade↔extinction, scintillation↔seeing).

Operating point:
- **MODCOD / modulation order:** [e.g. 16APSK 3/4]
- **Symbol rate / bandwidth:** [Msym/s, MHz]
- **Measured impairments:** [phase-noise mask dBc/Hz, group-delay ripple, IQ gain/phase imbalance, frequency/Doppler error, HPA backoff, interference, scintillation index]
- **Measured EVM (if any):** [%]

Please:
1. Map each impairment to its aberration analog and quantify its dB of implementation loss at this MODCOD.
2. Combine them as noise powers (not by adding dB) into a total implementation loss and an effective Strehl.
3. Rank the aberrations by dB contribution.
4. For each, name the corrector and a rough $/dB, and flag the single cheapest dB to recover first.
```

## Expected Output

- A table: impairment → aberration → dB loss → corrector → ~$/dB
- Total implementation loss and effective Strehl
- A ranked "fix this first" recommendation (software before hardware where possible)
