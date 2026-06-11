# Concepts — Shape Memory Alloy Phase Transformation, with Environmental Impact Assessment

Domain knowledge the agent reads before acting. Two bodies of knowledge are fused here: the **martensitic phase transformation** that gives SMAs their behavior, and the **life-cycle assessment** lens through which every transformation-engineering choice is also weighed for environmental cost.

---

## 1. The martensitic transformation

SMA behavior comes from a reversible, diffusionless, first-order solid-state transformation between a high-temperature parent phase (**austenite**, ordered B2 in NiTi) and a low-temperature product phase (**martensite**, monoclinic B19′ in NiTi). It is **thermoelastic**: the interface advances and retreats reversibly with temperature or stress, with a small, well-defined hysteresis — unlike the irreversible martensite of steels.

- **Diffusionless / displacive**: atoms move cooperatively by less than an interatomic spacing; composition is unchanged. This is why it is fast and reversible.
- **Twinning and variants**: martensite forms in self-accommodating twin variants. Under stress, favorable variants grow (**detwinning**) — this is the macroscopic shape change, recoverable on heating back to austenite.
- **R-phase**: an intermediate rhombohedral phase common in aged or thermally-cycled Ni-rich NiTi. It has very small hysteresis (~1–5 °C) and small strain — useful for precise, low-hysteresis actuation, but it complicates the DSC signature (multistage B2 → R → B19′).

### Transformation temperatures

Four characteristic temperatures define the hysteresis loop (per ASTM F2004, by tangent construction):

| Symbol | Meaning | Segment |
|--------|---------|---------|
| **Ms** | Martensite start (austenite → martensite begins) | cooling |
| **Mf** | Martensite finish | cooling |
| **As** | Austenite start (reverse begins) | heating |
| **Af** | Austenite finish (fully austenitic) | heating |

Ordering is typically Mf < Ms < As < Af. **Thermal hysteresis** = Af − Ms (or peak-to-peak), ~20–40 °C for binary NiTi, ~1–5 °C for the R-phase, and larger for some Cu/Fe alloys.

### Two functional behaviors

- **Shape Memory Effect (SME)**: deform martensite (detwin) at low T, then heat above Af — the part recovers its austenite shape. One-way SME recovers ~6–8% strain. **Two-way SME (TWSME)**, imprinted by training, gives spontaneous (no-load) shape change on cooling, but only ~2–5% strain and it fades with use.
- **Superelasticity / pseudoelasticity**: above Af, applied stress induces martensite (SIM), which reverts on unloading — large recoverable strain (up to ~8%) with a characteristic stress plateau and mechanical hysteresis. Operative only in the window **Af < T < Md** (Md = the temperature above which slip precedes transformation).

### Governing relations

- **Clausius–Clapeyron analogue**: `dσ/dT = −ΔH / (T · ε_tr · ρ)` — the transformation stress rises ~linearly with temperature. Binary NiTi: ~5–8 MPa/°C. This links the thermal and mechanical transformations and sets the SIM stress at any temperature.
- **Ni-composition sensitivity (NiTi)**: above 50 at% Ni, transformation temperatures fall ~10 °C per +0.1 at% Ni — extreme sensitivity that dominates manufacturing tolerance. Below 50 at% Ni (Ti-rich), temperatures plateau (~60–70 °C) because excess Ti forms Ti₂Ni and the matrix composition is buffered.
- **Aging (Ni-rich)**: 400–500 °C aging precipitates **Ni₄Ti₃**, depleting matrix Ni, raising Af, and often introducing the R-phase / multistage transformation — a post-melt lever to tune temperature without re-melting.

---

## 2. Alloy families

| Family | Examples | Notes |
|--------|----------|-------|
| **NiTi (Nitinol)** | ~49.5–51 at% Ni | Workhorse: best combination of strain, fatigue life, corrosion resistance, biocompatibility. Af tunable roughly −50 to +110 °C. |
| **High-temperature SMA** | NiTiHf, NiTiZr, NiTiPd, NiTiPt | Af up to ~300–500 °C for actuators in hot environments. Pd/Pt are costly and carry heavy embodied-carbon / supply-risk penalties. |
| **Cu-based** | CuZnAl, CuAlNi | Cheaper, easier to melt, good for higher-temp damping; more brittle, prone to grain-boundary fracture and aging instability. No Ni-allergen issue but Cu/Al toxicity questions. |
| **Fe-based** | FeMnSi, FeNiCoTi | Low cost, weldable, large parts (civil/seismic); smaller recoverable strain, often one-way only. |

---

## 3. Characterization methods

- **DSC** — heat flow vs. temperature; the primary transformation-temperature and enthalpy measurement (ASTM F2004). Exotherm on cooling (A→M), endotherm on heating (M→A).
- **Tensile / isothermal stress–strain** — plateau stress, recoverable vs. residual strain, superelastic loops (ASTM F2516 for superelastic NiTi).
- **Bend-and-free-recovery (BFR)** — Af on small / finished parts (ASTM F2082).
- **Electrical resistivity vs. T** — transformation tracking on wires; resistivity changes sharply through the R-phase.
- **XRD / EBSD** — phase identification and variant / texture analysis.

---

## 4. Failure and degradation modes

- **Functional fatigue** — gradual degradation of *functional* properties (Af drift, plateau-stress drop, growing residual strain, lost stroke) from dislocation accumulation. Fast in the first ~10²–10³ cycles, then saturates. Mitigated by lower strain amplitude, stabilization / training, stronger matrix (Ni-rich + aging).
- **Structural fatigue** — crack initiation and fracture; does *not* saturate. Surface finish (electropolishing) and lower stress amplitude help.
- **Overheating** — service above the shape-set / training temperature erases the memory.
- **Oxidation / interstitial pickup** — O and C pickup forms Ti₄Ni₂O / TiC, shifts transformation temperatures (consumes Ti → mimics Ni-rich), and embrittles. Also the central recycling barrier.
- **Off-stoichiometry** — small Ni:Ti deviations move Af by tens of degrees.

---

## 5. Life-cycle assessment (the environmental lens)

LCA (ISO 14040 / 14044) quantifies environmental burden across a product's life. Every transformation-engineering decision in this workspace is paired with its life-cycle consequence.

- **Phases of LCA**: goal & scope → inventory analysis (LCI) → impact assessment (LCIA) → interpretation.
- **System boundaries**: *cradle-to-gate* (extraction → finished part), *cradle-to-grave* (adds use + end of life), *gate-to-gate* (one process). Always declare the boundary and the **functional unit** (the service the product delivers, e.g. "one actuator giving 3 mm stroke for 10⁵ cycles") — comparisons are only valid per functional unit.
- **Impact categories**: GWP (kg CO₂e), cumulative energy demand (MJ), acidification, eutrophication, resource depletion / supply risk, human toxicity. Characterization methods: ReCiPe, TRACI, CML.

### Why SMAs are environmentally demanding

- **High embodied energy of the constituents.** Both nickel and titanium are energy-intensive to win; titanium especially (the Kroll process). Figures are database- and ore-dependent — present them as ranges, not point values (see `references.md`).
- **High scrap / buy-to-fly ratio.** NiTi machining and the tight composition control generate large scrap fractions; the scrap ratio is often the single biggest footprint lever — frequently larger than the choice of alloy.
- **Vacuum melting (VIM / VAR)** and multi-pass hot / cold working with interpass anneals add substantial process energy.
- **Low actuation efficiency in use.** SMA actuators are latent-heat-driven; electrical-to-mechanical efficiency is only a few percent. The honest environmental case for SMA is usually *system-level* (fewer parts, lower mass, no gearbox, silent), not raw energy efficiency.
- **Hard to recycle to functional grade.** Interstitial sensitivity means remelted scrap rarely returns to medical / actuator grade — it is usually downcycled. "Recyclable in principle" ≠ "recycled in practice."
- **Nickel-release / toxicity.** Ni is a sensitizer and a regulated metal. For implants / skin contact, the TiO₂ passive layer and surface finish (electropolishing) govern leaching; REACH limits nickel release and ISO 10993 governs biocompatibility.

### The integrating principle

Treat performance and environmental cost as **two axes of one decision**, not sequential gates. The greenest *material* choice and the greenest *system* choice can differ — only a use-phase break-even tells you which dominates for a given application. Keep value judgments (impact weightings) explicit and challengeable; a Pareto frontier with a hidden weighting is just an opinion wearing a chart.
