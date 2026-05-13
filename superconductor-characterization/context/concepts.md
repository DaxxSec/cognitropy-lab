# Superconductor Characterization — Core Concepts

Background the agent reads on demand. Optimised for fast recall during planning and reporting; defer to Tinkham, the IEC 61788 series, and the SuST handbooks for theoretical depth.

## Superconductivity Primitives

A superconductor is a material with zero DC resistance and the Meissner effect (perfect diamagnetism) below a critical temperature T_c, a critical field H_c (Type-I) or a pair of fields H_c1 / H_c2 (Type-II), and a critical current density J_c. The Ginzburg-Landau coherence length ξ sets the spatial scale over which the order parameter can vary; the magnetic penetration depth λ sets the field-screening scale. The GL parameter κ = λ / ξ distinguishes Type-I (κ < 1/√2) from Type-II (κ > 1/√2). Almost every practically useful superconductor is Type-II.

### Critical surfaces

The (T, B, J) operating space of any superconductor is bounded by the **critical surface** J_c(T, B). Moving toward the surface increases dissipation; crossing it transitions the material to the normal state and (in a magnet) generates a quench. Characterization measures the position and shape of this surface for a specific sample.

### Type-II flux dynamics

Above H_c1, magnetic flux penetrates as quantised vortices (Φ_0 = h/2e ≈ 2.07 × 10⁻¹⁵ Wb). Each vortex feels a Lorentz force F = J × Φ_0 when current flows; pinning sites (oxygen vacancies, BaZrO3 nano-rods in REBCO, α-Ti precipitates in NbTi, Cu-Sn grain boundaries in Nb3Sn) hold vortices in place. Pinning strength sets J_c; thermal activation over the pinning barrier sets the n-value (E ∝ J^n near J_c) and the creep regime.

## Material Classes

### Low-temperature superconductors (LTS)

- **NbTi.** Workhorse for MRI, NMR, accelerator dipoles. Tc ~ 9.2 K, Hc2(0) ~ 14.5 T. Ductile, drawable, cheap on a per-amp basis. IEC 61788-1 Jc measurement standard applies.
- **Nb3Sn.** A15 intermetallic. Tc ~ 18 K, Hc2(0) ~ 27 T. Strain-sensitive, brittle (wind-and-react). High-field accelerators (LHC inner-triplet, HL-LHC, FCC), fusion (ITER central solenoid). IEC 61788-2.
- **Nb3Al, V3Ga.** Niche, mostly research.
- **MgB2.** Discovered 2001. Tc ~ 39 K, isotropic, simple chemistry. Useful at 20 K with a cryocooler.

### High-temperature superconductors (HTS)

- **YBCO / REBa2Cu3O7−δ (REBCO).** Tc ~ 92 K, Hc2 ~ 100+ T at 4 K, highly anisotropic (Γ ~ 5–7). Coated-conductor architecture (Ni-W substrate / buffer stack / RE-Ba-Cu-O film / Cu stabiliser). Engineering Jc dominated by pinning landscape — BaZrO3 / BaHfO3 nano-columns enhance high-field, in-field Jc.
- **Bi-2212 / Bi2Sr2CaCu2O8+δ.** Round wire (Powder-In-Tube, Ag-sheathed). Tc ~ 85 K. Anisotropic but isotropic-in-cross-section; key candidate for very-high-field NMR and fusion inserts. IEC 61788-3.
- **Bi-2223 / Bi2Sr2Ca2Cu3O10+δ.** Tape. Tc ~ 110 K. Useful at 77 K (LN2) for power-cable and fault-current-limiter applications. IEC 61788-3.

### Iron-based superconductors

- **FeSe, BaFe2(As1-xPx)2, NdFeAs(O,F).** Tc up to ~55 K. Multi-band, moderately anisotropic, of interest for fault-current limiters and as a model system.

### Unconventional / research

- UTe2 (Tc ~ 2 K, candidate spin-triplet), twisted bilayer graphene (Tc ~ 1.7 K, gate-tunable), heavy-fermion (CeCoIn5), nickelate films (Nd0.8Sr0.2NiO2). These rarely show up on engineering capacity plans but do appear in research-lab queues.

## Measurement Modalities

### Transport

- **Four-probe R(T)** — gold standard for Tc; eliminates contact resistance from the V signal. AC lock-in at 17–73 Hz preferred over DC.
- **V-I characteristic** — Ic at a defined E-field (1 µV/cm or 0.1 µV/cm), n-value (slope of ln V vs ln I near Ic).
- **In-field Ic(B, T, θ)** — drives the `/jc-anisotropy-map` command.

### Magnetic

- **DC magnetisation M(T) ZFC/FC** — onset of diamagnetism gives Tc; ZFC/FC split reveals pinning and granularity.
- **M(H) hysteresis loop** — magnetic Jc via Bean critical-state model: Jc ∝ ΔM / sample width.
- **AC susceptibility χ′(T) and χ″(T)** — penetration-depth onset (real part) and energy dissipation peak (imaginary part); sensitive to pinning and Jc(B_AC).

### Microwave

- **Cavity Q vs T** — surface resistance Rs(T) = G/Q via the cavity geometry factor G. Drives `/microwave-q-screen`.
- **Two-coil mutual inductance** — penetration depth λ(T) of thin films.

### Calorimetric

- **Specific heat C(T) at H = 0 and in field** — thermodynamic Tc, gap Δ, density of states; jump ΔC/γTc tests the strong-coupling correction.

### Spectroscopic (advanced)

- **STM/STS** — direct gap mapping, Bogoliubov quasi-particle interference.
- **ARPES** — band structure and gap symmetry.
- **Inelastic neutron scattering** — spin-fluctuation resonance.

## IEC 61788 Series — Standards That Apply

IEC 61788 codifies superconductor measurement so different labs report comparable numbers. The agent should cite the right part in every test report:

- IEC 61788-1: DC critical current of Nb-Ti composite superconductors
- IEC 61788-2: DC critical current of Nb3Sn composite superconductors
- IEC 61788-3: DC critical current of Ag- and/or Ag-alloy sheathed Bi-2212 / Bi-2223
- IEC 61788-4: Residual resistance ratio (RRR) of Nb-Ti / Nb3Sn / Bi-based composites
- IEC 61788-6 / -7: Mechanical (room-T tensile, strain) tests
- IEC 61788-10: Critical temperature by resistivity method
- IEC 61788-11: AC loss in transverse field
- IEC 61788-13: AC loss in alternating field
- IEC 61788-14: General testing principles
- IEC 61788-15: Intrinsic property of Re-Ba-Cu-O bulk
- IEC 61788-19: Surface resistance of superconductors at microwave frequencies
- IEC 61788-22 (et seq.): HTS coated-conductor properties

(Cross-check the IEC website at run-time — the series is actively extended.)

## Capacity Planning Glossary

The lab is modelled as a queueing service system. The glossary below maps standard symbols to lab quantities; full formulas live in `references.md → Queueing models`.

- **λ (lambda)** — arrival rate of samples (samples/week). From intake history, ideally with trend.
- **E[S]** — mean service time per sample (hours). Includes cooldown + measurement + warmup.
- **Var[S], C_s² = Var[S]/E[S]²** — service-time variance and squared coefficient of variation. Pre-cooldown variance dominates.
- **c** — number of parallel servers (cryostats), or magnet-bound bottleneck count.
- **ρ = λ × E[S] / c** — utilisation. Sustainable: ρ ≤ 0.80. Crisis: ρ → 1, queue length diverges.
- **L = λ × W (Little's Law)** — mean number of samples in the system; W is mean lead time.
- **Wq** — mean waiting time before service starts. M/G/1: Wq = ρ × E[S] × (1 + C_s²) / (2(1 − ρ)).
- **MTBF / MTTR** — mean time between (cryostat / magnet / cryogen-plant) failures, mean time to repair. Drives the headroom buffer.
- **Cp / Cpk** — process capability. Useful for stating "our Tc measurement uncertainty fits inside the customer spec, with what margin."
- **Holt-Winters / ETS** — exponential smoothing for arrival-rate forecasting on a seasonal intake (e.g. fiscal-year-end batching).
- **Erlang-C** — wait-probability for M/M/c. Useful when several samples queue for a pooled cryostat farm.

## Common Failure Modes

- **Magnet quench.** Loss of superconductivity in the magnet, energy dumps as resistive heat. Days of recovery; major LHe loss; in-progress sample lost.
- **Thermal runaway / Jc collapse during V-I.** Sample heats above Tc mid-measurement; sometimes recoverable, often irreversible.
- **Flux jump.** Avalanche of vortex motion in NbTi or REBCO at low T, high B, fast ramp; classic precursor to a quench.
- **Training pulses.** A wound magnet does not reach design field on the first ramp; successive ramps train it. Plan training time at any new-build or recovery.
- **Contact heating.** Poor contact (I-V pad) dissipates at the contact and shifts apparent Tc.
- **Hydride precipitation in Nb cavities** — boosts R_res below ~150 K dwell; mitigated by 100 °C vacuum bake.
- **Trapped magnetic flux on cooldown.** Ambient field frozen into the sample below Tc; degrades Q in cavities and Jc in films. Use μ-metal shielding.
- **Cryogen exhaustion mid-run.** Worst case is a magnet at field with LHe below the bottom heat exchanger. Run the `/lhe-budget` check the morning of the run.
- **Thermometer drift / mis-calibration.** Cernox curves shift after large field cycling; recalibrate against a fixed-point (e.g. Pb superconducting transition) every 6 months.

## Operating Constraints

- **Personnel safety.** Fringe-field 5-gauss line marked; pacemaker-screening checked; O2 monitoring at every cryostat.
- **Quench-protection circuits.** Persistent-mode magnets store MJ-class energy; dump resistor and voltage tap monitoring are mandatory.
- **Cryogen handling.** Transfer lines vented, relief valves verified, asphyxiation monitors connected. LN2 splash PPE required.
- **Magnetic media exclusion zone.** Hard drives and credit cards above 0.5 mT zone are destroyed.
- **Reporting standards.** Every IEC-compliant result cites the relevant part *and* the instrument-level metadata. A bare "Tc = 89 K" is unreportable.
- **Capacity discipline.** Sustainable utilisation ρ ≤ 0.80. Crossing 0.85 triggers a planning intervention before the queue collapses.
