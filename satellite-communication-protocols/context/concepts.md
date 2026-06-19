# Satellite Communication Protocols — Core Concepts

Background the agent reads before acting. The organising idea: **a satellite communication link is an optical system.** Both are cascades of budgeted gains and losses, both are bounded by a conservation law you approach but never beat, both are degraded by aberrations, and both are designed by trading benefit against cost at the margin. This file builds that mapping, then loads the satcom substance on each side of it.

## The Unifying Idea: A Link Is an Optical Train

An optical designer traces flux from source to detector through every surface, accounting for each gain (concentration) and loss (reflection, absorption, aberration). A link engineer traces signal power from transmitter to demodulator through the same kind of train:

| Optical system | Satellite link |
|---|---|
| Source radiance | Transmit power `P_tx` (dBW) |
| Light-gathering aperture (∝ D²) | Antenna gain `G = η(πD/λ)²` |
| Throughput / radiance budget | Link budget (the dB cascade) |
| Inverse-square irradiance falloff | Free-space path loss `(4πd/λ)²` |
| Absorption / extinction in glass & air | Gaseous + rain + cloud attenuation |
| Detector sensitivity (NEP) | Receiver figure of merit `G/T` |
| Étendue / optical invariant (AΩ conserved) | **Shannon–Hartley capacity** (the bound) |
| Diffraction limit `θ ≈ 1.22 λ/D` | Antenna beamwidth `θ ≈ 70 λ/D` |
| Strehl ratio (achieved / ideal peak) | Achieved spectral efficiency / Shannon |
| Aberrations (Seidel, chromatic) | Impairments (phase noise, ripple, IQ, fade) |
| Aperture stop / f-number | Allocated bandwidth & power |
| Field stop / field of view | Beam coverage footprint |
| Stop down for sharpness vs light | Climb MODCOD for bits vs required SNR |

Keep this table live: when a satcom decision feels unfamiliar, translate it to the optical analog and the cost-benefit usually becomes obvious.

## The Link Budget Cascade

Worked in **decibels** so gains add and losses subtract. Core terms:

- **EIRP** (Effective Isotropic Radiated Power) `= P_tx − L_feed + G_tx` (dBW). The "source brightness after the first lens."
- **Free-Space Path Loss (Friis):** `FSPL(dB) = 92.45 + 20·log₁₀(d_km) + 20·log₁₀(f_GHz)`. The dominant loss; pure inverse-square spreading.
- **G/T** (receiver figure of merit) `= G_rx − 10·log₁₀(T_sys)` (dB/K). System noise temp `T_sys = T_antenna + T_receiver`, referred to a common point.
- **Carrier-to-noise-density:** `C/N₀ = EIRP − FSPL − L_atm + G/T − k`, with **Boltzmann** `k = −228.6 dBW/Hz/K`.
- **Down to the modem:** `C/N = C/N₀ − 10log₁₀(B)`; `Es/N₀ = C/N₀ − 10log₁₀(R_s)`; `Eb/N₀ = Es/N₀ − 10log₁₀(η_bits·R_code)`.
- **Link margin** `= Eb/N₀_achieved − Eb/N₀_required` at the target BER/PER. Margin is the design's slack against fades and unknowns.

## The Bound: Shannon Capacity as Étendue

**Shannon–Hartley:** `C = B·log₂(1 + S/N)` (bits/s). Per hertz, `η_max = log₂(1 + SNR)`. This is a *conservation law*, the information analog of **étendue** (`G = n²·A·Ω`, the optical invariant): in optics you cannot increase brightness by concentrating in area without losing in angle; in comms you cannot raise bits/Hz without raising SNR or bits/s without bandwidth. The minimum energy per bit is the **Shannon limit** `Eb/N₀ ≥ (2^η − 1)/η`, → `ln 2 = −1.59 dB` as `η → 0`. Real systems (DVB-S2X LDPC+BCH) sit ~0.7–1 dB above this — a Strehl near 1.

## Aperture, Gain, Beamwidth — Same Physics

Antenna gain `G = η·(πD/λ)²` is the same `D²/λ²` light-gathering law as a telescope. The **−3 dB beamwidth** `θ ≈ 70·λ/D` (degrees) is the **diffraction limit** `1.22·λ/D` (radians) wearing engineering units — an antenna beam *is* a diffraction pattern. Consequence: bigger aperture → more gain **and** narrower beam → harder pointing. This coupling is why "use a bigger dish" has a knee, not a free lunch.

## Strehl Ratio and the Aberration↔Impairment Dictionary

The **Strehl ratio** (optics: achieved peak intensity ÷ diffraction-limited ideal; Maréchal: Strehl > 0.8 ⇔ RMS wavefront error < λ/14) maps to **achieved spectral efficiency ÷ Shannon**, or equivalently the link's total implementation loss. Each impairment is an aberration:

- **Phase noise ↔ spherical aberration** — symmetric blur of every constellation point; integrates the oscillator dBc/Hz mask to an rms phase error.
- **Group-delay / amplitude ripple ↔ coma** — frequency-dependent ISI tails; corrected by equalization.
- **IQ gain/phase imbalance ↔ astigmatism** — axis-dependent stretch; sets an image-rejection floor.
- **Carrier/Doppler offset ↔ defocus** — whole constellation rotates/slips; tracked by carrier loops.
- **HPA AM/AM & AM/PM nonlinearity ↔ field-dependent distortion** — worsens with backoff reduction; corrected by predistortion.
- **Rain/gas absorption ↔ extinction**, **scintillation ↔ atmospheric seeing** (the Fried-parameter `r₀` analog; mitigated by diversity, the comms "adaptive optics").

Combine impairments as **noise powers**, never by adding dB.

## MODCOD, ACM, and "Stopping Down"

A MODCOD pairs a modulation (QPSK, 8PSK, 16/32/64APSK) with an FEC code rate. Higher order + higher rate = more bits/Hz but more required Es/N₀ — the comms version of opening the aperture for light at the cost of depth of field. **DVB-S2X** offers a dense ladder (~0.7–1 dB from Shannon per point). **Adaptive Coding and Modulation (ACM)** changes the operating MODCOD per-frame as SNR varies — *dynamic stop-down* — trading throughput instead of paying static margin during fades.

## Atmospheric Propagation (the "air path")

- **Rain attenuation (ITU-R P.618):** `γ_R = k·R^α` dB/km from rain rate `R`; the dominant loss above ~10 GHz. Climbs steeply with frequency (Ku < Ka < Q/V). Also **raises sky-noise temperature**, degrading G/T.
- **Gaseous absorption (P.676):** oxygen line at 60 GHz, water-vapor line at 22 GHz.
- **Ionospheric scintillation (P.531) & tropospheric scintillation (P.618 §8):** rapid amplitude/phase fluctuation, the atmospheric-seeing analog; worst at low elevation and low latitude/equatorial and high-latitude.
- **Cloud (P.840):** minor for RF, **opaque for optical** — a hard stop, not a fade.

## Cost-Benefit Framework (today's technique)

Every lever is a curve of benefit vs cost; the discipline is to operate at the **knee** and never spend a dB that buys less than it costs:

- **Marginal analysis:** `Δbenefit/Δcost` per increment; stop when it falls below the next-best lever or a hard limit.
- **$ / dB, $ / bit, $ / nine:** common currencies for comparing apertures, power, coding, and availability.
- **Pareto frontier:** the non-dominated set of (efficiency, required-SNR) or (availability, cost) points; never operate inside it.
- **Knee of the curve / diminishing returns:** the last "nine" of availability and the last dB of aperture are the most expensive.
- **Opportunity cost & TCO:** a dB of static margin is paid every clear-sky second forever; ACM/diversity may be cheaper lifetime.

## Common Failure Modes

- **Dropping Boltzmann or sign-flipping `k`** — the single most common budget error.
- **Adding impairment dBs directly** instead of combining noise powers — overstates or understates implementation loss.
- **Claiming spectral efficiency above the Shannon ceiling** — a re-derivation always exposes it.
- **Static margin as a dumping ground** — undocumented dB hidden in "margin" makes the budget undefendable.
- **Ignoring rain's noise-temperature hit** — counting only path loss makes deep-fade budgets optimistic.
- **Forgetting the gain↔beamwidth coupling** — a bigger dish whose beam the platform can't point loses what it gained.

## Operating Constraints

- **ITU Radio Regulations:** frequency coordination, EIRP and power-flux-density (PFD) limits, orbital-slot/spectrum filings. EIRP is legally capped — a budget that needs more is non-compliant, not just expensive.
- **Physics:** Shannon and étendue are not negotiable; thermal noise floor `kTB`; the speed of light sets GEO's ~250 ms one-way latency (a real cost-benefit factor vs LEO).
- **Spacecraft SWaP:** mass, prime power, and thermal limits bound every "just add power/aperture" lever onboard.
