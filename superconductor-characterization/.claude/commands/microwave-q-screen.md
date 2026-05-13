# /microwave-q-screen

Screen surface resistance Rs(T) of a sample via the loaded Q of a superconducting cavity at cryogenic temperature. Validates mode purity, coupling, and field-dependence; returns a per-temperature Rs estimate and a disposition for the sample.

## Inputs

- Cavity geometry and design mode (e.g. cylindrical TE011 at 1.3 GHz, TE013 at 9.6 GHz, dielectric-loaded sapphire at 9.4 GHz)
- Cavity geometry factor G (Ω, computed from EM simulation, e.g. G ≈ 270 Ω for a 1.3 GHz elliptical Nb cavity in TM010)
- Sample geometry and mounting (end-plate replacement, hot-finger insert, mushroom-resonator pellet)
- Target T-sweep: e.g. 1.8 K, 2.0 K, 2.5 K, 3.0 K, 4.2 K (drag along 4.2 K → 9 K for Nb research)
- VNA frequency range, IF bandwidth, calibration plane, and reference cables
- Drive field amplitude target (B_peak on cavity wall, mT) — relevant for high-field Q-slope studies

## Steps

1. Pre-cool the cavity loaded with the sample; verify no thermal leak by holding 4.2 K for ≥30 min before sweeping.
2. Sweep T at 2-min dwell per step; at each step, measure S11 (and S21 if a transmission probe is present) around the mode; fit a Lorentzian to extract f₀ and loaded Q_L.
3. Compute external coupling β = Q_L × |Γ| / (1 − |Γ|) (under-coupled) or β = Q_L × |Γ| / (|Γ| − 1) (over-coupled); deduce unloaded Q_0 = Q_L × (1 + β).
4. Check mode purity: confirm the mode of interest is at the expected frequency and is not split or hybridised with a parasitic; reject the point and reposition the coupler if Q_L disagrees with the cavity-only baseline by >2× at room-T cross-check.
5. Compute surface resistance Rs(T) = G / Q_0. Decompose into Rs(T) = R_BCS(T, f, Δ, ξ, λ) + R_res where R_BCS follows the BCS prediction (e.g. Halbritter, Mattis-Bardeen) and R_res is the residual (typically 5–50 nΩ for clean bulk Nb).
6. If a Q-slope (Q drops at higher drive amplitude) is observed, repeat the sweep at three drive levels and report the slope class (low-field, medium-field, high-field Q-slope per accelerator-cavity convention).
7. Sample disposition: accept → continue to bulk cavity processing; reject → return to chemistry for additional buffered chemical polish / electropolish / EP-Nb retreat.

## Output

Markdown report at `outputs/microwave-q-screen-<sample-id>-<YYYY-MM-DD>.md`:
- Rs(T) curve and BCS / residual decomposition
- Q-slope class if applicable
- Disposition (accept / reject / re-test)
- Reference to IEC 61788-19 (surface resistance) reporting practice
- Capacity cost (cavity hours, helium, vacuum-cycle hours)

## Notes

- Sapphire-loaded resonators give 10⁻⁴ field-distribution sensitivity vs. bulk cavities but require sapphire-quality control (Q_sapphire) traceability.
- Residual resistance R_res is dominated by trapped flux, hydride precipitation, and surface contaminants; flag any sample that came through a magnetic mounting fixture.
- Q-slope is irreversible across thermal cycles for some defect classes; if a sample improves after a 100 °C bake, it was the hydride class.
- The 1.8 K superfluid run dominates helium burn — group three samples into a single cooldown if cavity exchange under cold conditions is feasible.
