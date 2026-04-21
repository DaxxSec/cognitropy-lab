# Domain Knowledge: Optics + FMEA

This file is a condensed reference for the agent. Read this when the user asks for a calculation, a design trade, or an FMEA scoring decision.

## 1. Paraxial Optics Quick Reference

| Quantity | Formula | Notes |
|---|---|---|
| Thin-lens power | φ = 1/f = (n−1)(1/R₁ − 1/R₂) | Lensmaker's, air |
| Two-element combo | φ = φ₁ + φ₂ − φ₁φ₂·d | d = axial separation |
| f/# | N = f / D_EP | D_EP = entrance pupil |
| Numerical aperture | NA = n·sin(θ) | ≈ 1/(2·N) in air, small angles |
| Diffraction-limit spot (Airy) | d_A = 2.44·λ·N | First dark ring |
| Rayleigh resolution | 1.22·λ/D | Angular |
| Depth of focus (±) | ±λ·N² | Rayleigh criterion |
| Depth of field | 2·N·c·(1 + m)/m² | c = circle of confusion, m = magnification |

## 2. Wave / Fourier Optics

- **Fourier-transform property of a lens**: amplitude at back focal plane is the 2D FT of amplitude at front focal plane.
- **Strehl ratio (Maréchal)**: S ≈ exp(−(2πσ/λ)²) where σ is RMS WFE. Diffraction-limited ⇔ S ≥ 0.8 ⇔ σ ≤ λ/14.
- **MTF cutoff (incoherent)**: ξ_c = 1/(λ·N) cyc/mm
- **Gaussian beam waist**: w(z) = w₀·√(1 + (z/z_R)²), z_R = π·w₀²/λ

## 3. Aberrations (Seidel)

| Aberration | Dependence | Knob |
|---|---|---|
| Spherical | h⁴ | Bending, stop shift, asphere |
| Coma | h³·y | Stop shift, lens splitting |
| Astigmatism | h²·y² | Field-flattener, stop |
| Field curvature | h²·y² | Petzval sum balancing |
| Distortion | y³ | Symmetric about stop cancels |
| Axial color | h² | Achromat (crown+flint) |
| Lateral color | h·y | Apochromat, stop at symmetry |

**Petzval sum**: Σ(φᵢ/nᵢ) → want near zero for flat field.

## 4. Radiometry

| Quantity | Units |
|---|---|
| Radiant flux Φ | W |
| Irradiance E | W/m² |
| Radiance L | W/m²/sr |
| Throughput (etendue) A·Ω | m²·sr |

**Invariant**: L/n² is conserved through a lossless system.

## 5. Detector / Photon Statistics

- **Shot-noise limit**: SNR = √N_photon
- **Well capacity / ADC match**: ensure bit depth > log2(FW/read noise)
- **Nyquist**: sample at ≥ 2× highest spatial frequency

## 6. Tolerance Basics

Typical glass tolerances (commercial / precision / high-precision):
| Parameter | Commercial | Precision | High-Precision |
|---|---|---|---|
| Radius (%) | ±0.2 | ±0.1 | ±0.02 |
| Thickness (mm) | ±0.15 | ±0.05 | ±0.025 |
| Decenter (mm) | ±0.1 | ±0.025 | ±0.010 |
| Tilt (arcmin) | ±3 | ±1 | ±0.3 |
| Surface irreg (fringes) | 5 | 1 | 0.25 |
| Scratch-dig (MIL-O-13830) | 80-50 | 60-40 | 20-10 |

## 7. FMEA Fundamentals

### Scoring
- **Severity (S)**: impact if failure occurs (1–10)
- **Occurrence (O)**: likelihood of cause (1–10)
- **Detection (D)**: ability to detect before customer (1–10)
- **RPN = S × O × D**, max 1000

### Action priority
- RPN ≥ 200 → mandatory redesign
- RPN 100–199 → action required
- RPN < 100 → document, monitor
- **Any S = 10 → action regardless of RPN** (safety-related)

### AIAG-VDA 7-step process
1. Planning & preparation
2. Structure analysis
3. Function analysis
4. Failure analysis (modes/effects/causes)
5. Risk analysis (S, O, D scoring)
6. Optimization (actions, reassess)
7. Results documentation

### Common Optical Failure Modes (starter catalog)
| Mode | Typical cause | Detection |
|---|---|---|
| Contamination | Mishandling, outgassing | Visual + particle count |
| Bond-line fracture | CTE mismatch, shock | DIC, thermal cycling |
| Element decenter | Assembly drift, shock | Autocollimator |
| Coating delamination | Thermal cycling, humidity | Visual, MIL-C-675 tape |
| Ghost / scatter | Uncoated surfaces, flares | Stray-light test |
| Athermal drift | Barrel CTE, glass dn/dT | Thermal chamber test |
| Stress birefringence | Over-tight mount, molding | Polariscope |
| Laser-induced damage | Fluence > LIDT | LIDT scan |
| Fogging | Internal humidity | Dew-point |
| Mount resonance | Modal coincidence | Shake table |

## 8. Standards Crib

- **ISO 10110-5** — surface form tolerances (sag, slope, irregularity)
- **ISO 10110-7** — surface imperfection (scratch-dig equivalent)
- **ISO 14644** — cleanroom classification
- **IEC 60825-1** — laser AEL by class (1, 1M, 2, 2M, 3R, 3B, 4)
- **MIL-STD-810** — environmental test methods
- **ANSI Z136** — US laser-safety equivalent

## 9. Units & Constants

- c = 2.998×10⁸ m/s
- h = 6.626×10⁻³⁴ J·s
- k_B = 1.381×10⁻²³ J/K
- Photon energy: E = hc/λ → 1 µm ≈ 1.24 eV
- Planck blackbody peak (Wien): λ_max·T ≈ 2898 µm·K
