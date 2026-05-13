# Superconductor Characterization — Reference Tables

Lookup data the agent reaches for during planning and reporting. Compact by design — defer to IEC 61788 parts, vendor datasheets, and the cited textbooks for fuller specs.

## Material Parameter Table (representative values, 4.2 K unless noted)

| Material | Tc (K) | Hc2(0) (T) | Engineering Jc (A/mm², 4.2 K, 12 T) | Anisotropy Γ | IEC part |
|----------|-------:|----------:|------------------------------------:|-------------:|---------:|
| Nb-Ti | 9.2 | 14.5 | ~600 (NbTi @ 5 T; degrades >9 T) | 1 (isotropic) | 61788-1 |
| Nb3Sn (RRP) | 18 | 27 | ~1500 | 1 (isotropic) | 61788-2 |
| Nb3Al (rapid heat) | 18.8 | 32 | research | 1 | — |
| MgB2 | 39 | 18–20 | ~200 (in-field) | 1.5–4 | — |
| Bi-2212 (round wire) | 85 | >100 | ~500–1000 | 50–150 (mat'l) | 61788-3 |
| Bi-2223 (tape) | 110 | >100 | ~200 (77 K, sf) | 50+ | 61788-3 |
| REBCO (coated) | 92 | 100+ (extrap.) | ~3000 (H‖ab) / ~600 (H‖c) | 5–7 | 61788-22 series |
| FeSe / Fe-pnictide | 8–55 | 30–70 | research-grade | 1.5–4 | — |

Numbers are representative. Always cite the lot, lot-test date, and vendor for vendor-acceptance work.

## Cryogen Thermodynamic Data

| Cryogen | BP (K) | Latent heat (kJ/L) | Liquid density (g/L) | Gas-liquid expansion |
|---------|-------:|-------------------:|---------------------:|--------------------:|
| Helium-4 | 4.222 | 2.6 | 125 | 757× |
| Helium-3 | 3.191 | 0.49 | 59 | — |
| Nitrogen | 77.36 | 161 | 808 | 696× |
| Neon | 27.07 | 86 | 1210 | 1430× |
| Hydrogen | 20.27 | 31 | 71 | 850× (DO NOT USE except in specialised facilities) |

Rule of thumb: 1 W of parasitic heat boils ~1.4 L LHe per day. A clean closed-cycle 4 K cryostat avoids this entirely at the cost of 1.5–7 kW of wall-plug power.

## Cryogen Consumption Coefficients (per-cryostat, indicative)

| Cryostat / mode | Static boil-off (L/day) | Per-ramp burn (L) | Notes |
|----------------|-----------------------:|-----------------:|-------|
| VTI 4 K, idle | 3–6 | n/a | Adds ~3 L/day per active sample-stick |
| VTI 1.8 K, superfluid | 6–12 | 1–2 (pump-down) | Includes pumping latent + lambda transition |
| Closed-cycle PPMS, 4 K → 1.8 K | ≈0 | n/a | Cooling-water and electrical only |
| 14 T magnet ramp, 0 → 14 T at 0.2 T/min | n/a | 4–8 | Eddy-current heating on persistent switch |
| 16 T magnet ramp, full sweep | n/a | 10–15 | Higher coil heat capacity |
| Sample exchange at 4.2 K | n/a | 2–4 | Per insertion if not load-lock |

## IEC 61788 Reporting Quick Reference

Use the part matching the test:

- DC Jc on LTS round wire / strand → 61788-1 (NbTi), 61788-2 (Nb3Sn).
- DC Jc on Ag-sheathed Bi-2212 / Bi-2223 → 61788-3.
- Residual Resistance Ratio (RRR) → 61788-4.
- Mechanical (room-T tensile, strain) → 61788-6, 61788-7.
- Tc by resistivity method → 61788-10.
- AC loss in transverse field → 61788-11; alternating field → 61788-13.
- General testing principles → 61788-14.
- RE-Ba-Cu-O bulk intrinsic property → 61788-15.
- Microwave surface resistance → 61788-19.
- HTS coated-conductor properties → 61788-22 (and subsequent extensions).

## Four-Probe Contact Geometry — Quick Rules

- Place V-contacts at least 3 × sample-width away from I-contacts to avoid current-spreading artefacts.
- For 4 mm wide tape, I → V separation ≥ 12 mm; V-tap separation L_tap selected per IEC 61788 part (typically 10 mm for HTS tape Ic).
- Contact resistance target for transport Jc: ≤ 1 µΩ·cm² (lower for low-resistance LTS).
- Solder for HTS: indium (BP ≈ 156 °C); for LTS Cu stabiliser: Sn-Pb or Sn-Ag.

## Queueing Models — Working Formulas

For a single-server cryostat queue (M/G/1):

```
ρ = λ × E[S]          # utilisation (must be < 1)
C_s² = Var[S] / E[S]² # squared coefficient of variation
E[Wq] = ρ × E[S] × (1 + C_s²) / (2 × (1 − ρ))   # Pollaczek-Khinchine
E[W] = E[Wq] + E[S]   # total time in system
L = λ × E[W]          # Little's Law (mean samples in system)
```

For c parallel cryostats (M/M/c approximation when service ≈ exponential):

```
a = λ × E[S]                            # offered load
ρ = a / c
C(c, a) = Erlang-C wait probability
E[Wq] = C(c, a) × E[S] / (c × (1 − ρ))
```

For a more honest M/G/c (Allen-Cunneen) approximation:

```
E[Wq] ≈ (C(c, a) × E[S] / (c × (1 − ρ))) × ((1 + C_s²) / 2)
```

Headroom rule of thumb: ρ ≤ 0.80 sustainable; 0.80–0.85 stress; > 0.85 plan a mitigation; > 0.90 expect customer escalations within two weeks.

## Holt-Winters Forecasting — Configuration

For weekly intake λ_t:

- **Level α** = 0.3 (responsive to trend shifts but not noise)
- **Trend β** = 0.1 (slow trend update)
- **Seasonality γ** = 0.0 unless an annual cycle is documented (fiscal-year intake spikes — typical γ = 0.2 with period = 52 weeks)
- Re-fit quarterly; archive fits to `outputs/_capacity/forecasts/`.

## Quench-Protection Quick Specs

- Voltage tap trip threshold: 100–300 mV across coil sections for protected magnets.
- Trip latency target: < 5 ms from threshold to switch open.
- Dump resistor sized for V_terminal < voltage-to-ground rating of coil insulation under full current.
- Persistent switch open-time after quench: per vendor, typically 30+ s to dissipate before re-energising.

## Upstream Catalogues

- **IEC Webstore** — https://webstore.iec.ch/ — IEC 61788 parts and updates.
- **NIST Cryogenic Technologies Group** — https://www.nist.gov/pml/applied-physics-division — cryogen properties, thermometry standards.
- **NHMFL (National High Magnetic Field Laboratory)** — https://nationalmaglab.org/ — high-field user-facility reference, Hc2 measurements, training data.
- **Superconductor Wires & Tapes Benchmarks (IEEE-CSC SNF)** — https://snf.ieeecsc.org/ — public benchmark Ic(B, T) data for LTS and HTS.
- **CERN EDMS / SM18 reports** — https://edms.cern.ch/ — Nb3Sn, NbTi acceptance procedures for accelerator-grade conductors.
- **arXiv cond-mat.supr-con** — https://arxiv.org/list/cond-mat.supr-con/recent — pre-prints; useful for emerging materials.

## Major Facilities Directory

| Facility | Capability | Notes |
|----------|-----------|-------|
| NHMFL (Tallahassee, USA) | DC ≤ 45 T, pulsed >100 T, hybrid | User facility; proposal-based access |
| HFML (Nijmegen, NL) | DC ≤ 38 T, pulsed | European Magnetic Field Laboratory consortium |
| LNCMI (Toulouse / Grenoble, FR) | Pulsed 80+ T (Toulouse), DC 36 T (Grenoble) | EMFL |
| HZDR (Dresden, DE) | Pulsed 70+ T | EMFL |
| KEK / IMR Tohoku (JP) | DC 30–45 T | National user facilities |
| WHMFC (Wuhan, CN) | DC ≤ 45 T (planned hybrid) | Newer facility |
| Brookhaven SMD / SBIR | RHIC and EIC magnet test stands | Accelerator-magnet acceptance |
| CERN SM18 | Cryostat hall for LHC / HL-LHC / FCC magnet acceptance | Nb-Ti + Nb3Sn campaigns |
| FRIB / FNAL SCRF Vertical Test Stands | SRF cavity Rs / Q-slope | Accelerator-cavity material screening |

## Operating Cheat-Sheets

- **Tc midpoint vs onset.** Onset = first deviation from normal-state R(T) line. Midpoint = 50 % of normal-state R. Zero-R = E < 1 nV/cm definition. Report all three when transition is broad.
- **n-value rule.** Higher n = sharper transition = better pinning. Engineering Nb-Ti: n ~ 50–80. REBCO: n ~ 25–45. Bi-2212: n ~ 15–25. A drop in n between batches usually precedes a Jc drop.
- **Two-fluid limit.** R_BCS ~ exp(−Δ / kT). Below T ~ Tc/3, BCS contribution becomes vanishing; residual resistance R_res dominates microwave loss.
- **Bean critical-state.** For a slab of width 2a, full-penetration field H* = Jc × a / c_geom. Below H*, M = − H/2 (Meissner-like); above, hysteresis loop opens proportionally to Jc.
- **WHH formula.** Hc2(0) ≈ 0.693 × Tc × |dHc2/dT|_Tc; valid for clean, single-band, weakly-coupled superconductors. For multi-band (MgB2, Fe-pnictides) WHH underestimates.
