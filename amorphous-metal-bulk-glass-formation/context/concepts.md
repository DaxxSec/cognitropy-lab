# Amorphous Metal Bulk Glass Formation — Core Concepts

Background the agent reads before acting. The throughline: every metallurgical limit below is also a **capacity limit** — glass-forming ability bounds product geometry, the crystallization nose bounds dwell time, and the supercooled-liquid window bounds forming time per heat. Capacity planning here is the discipline of working inside those kinetic bounds.

## 1. What a Bulk Metallic Glass Is

A metallic glass is an alloy quenched fast enough that the atoms freeze in the disordered arrangement of the liquid instead of arranging into a crystal lattice. "Bulk" (BMG) means the critical casting thickness is ≥ ~1 mm — historically the threshold separating castable parts from the micron-thick melt-spun ribbons of the 1960s (Klement–Duwez Au-Si, 1960). BMGs have no grain boundaries, no dislocations, and no long-range order; an XRD scan shows a broad amorphous **halo** rather than sharp Bragg peaks.

Consequences that matter for production:
- **Strength/elasticity:** σ_y ≈ 1.5–2 GPa (Zr-based), elastic strain limit ≈ 2%, low E relative to strength → springy and resilient.
- **Net-shape casting:** solidifies without a crystallization shrinkage front, so it copies mold features faithfully.
- **The defect that kills the part:** room-temperature plasticity localizes into thin **shear bands**; an unconstrained BMG fails catastrophically with little tensile ductility. Partial crystallization usually makes this *worse*, not better.

## 2. Glass-Forming Ability (GFA) — the Master Constraint

GFA = how easily an alloy avoids crystallization on cooling. It is the single number that determines what you can make.

- **Critical cooling rate, Rc** — minimum cooling rate (K/s) to bypass crystallization. Lower is better. Early ribbons needed ~10⁶ K/s; good BMGs need 1–100 K/s; the best (Pd-Cu-Ni-P) need < 0.1 K/s.
- **Critical casting thickness, Dmax (or Zc)** — the thickest fully-amorphous section castable in a given route. Roughly Dmax ∝ Rc^(−1/2) for conduction-limited cooling. **This is the capacity feasibility envelope: a part whose minimum-cooling section exceeds Dmax cannot be made amorphous in that alloy, full stop.**

### Inoue's three empirical rules for high GFA
1. **Multicomponent** (≥3, usually ≥4–5 elements) — the "confusion principle": many competing crystal phases frustrate any single one from nucleating.
2. **Atomic size mismatch > ~12%** among the main constituents — promotes dense random packing the crystal can't easily reorganise.
3. **Negative heats of mixing** among the main elements — favours short-range chemical order and a deep eutectic.

### Structural picture
Dense random packing of **solute-centred clusters** (Miracle's efficient-cluster-packing model). A deep eutectic lowers the liquidus Tl, raising Trg (below), which is why the best glass-formers sit at or near deep eutectics.

## 3. GFA Parameters (what the screens actually compute)

All require thermal landmarks from DSC (§5). Higher = better unless noted.

| Parameter | Formula | Rough "good" threshold |
|-----------|---------|------------------------|
| Reduced glass transition Trg | Tg / Tl | > 0.58–0.60 |
| Supercooled-liquid width ΔTx | Tx − Tg | > 40–60 K |
| γ (Lu & Liu) | Tx / (Tg + Tl) | > 0.40 |
| γm | (2Tx − Tg) / Tl | higher better |
| ω (Long) | Tg/Tx − 2Tg/(Tg+Tl) | lower better |
| δ | Tx / (Tl − Tg) | higher better |

No single parameter is universal — they correlate with Rc/Dmax with scatter. Use **two or three together** and treat them as a screen, not a guarantee. ΔTx measures supercooled-liquid *stability* (matters for thermoplastic forming); Trg and γ correlate best with *castable thickness*.

## 4. Crystallization Kinetics — the Clock

### TTT / CCT diagrams
The **time–temperature–transformation (TTT)** curve plots the time to a detectable crystalline fraction at each temperature; it has a characteristic **nose** (shortest time, t_nose, at T_nose, usually between Tg and Tm where nucleation × growth peaks). To form glass, the cooling path must pass to the *left* of the nose. **Continuous-cooling-transformation (CCT)** is the cooling-rate version; the critical cooling line tangent to the nose gives Rc. The nose is the bottleneck resource in the capacity sense: it is the deadline every cooling and forming step races.

### Classical nucleation + growth
Steady-state homogeneous nucleation rate I ∝ exp(−ΔG*/kT)·exp(−Q/kT), with ΔG* ∝ σ³/ΔGv² (interfacial energy over driving-force squared). **Heterogeneous** nucleation on oxides/inclusions slashes the barrier — this is why oxygen control (§7) is decisive for Zr-based alloys.

### JMAK (Johnson–Mehl–Avrami–Kolmogorov) — the yield model
Isothermal crystallized fraction: **X(t) = 1 − exp[−(K·t)ⁿ]**, where n is the Avrami exponent (1–4; reflects nucleation + growth dimensionality) and K is an Arrhenius rate constant K = K₀·exp(−Ea/RT). Along a real (non-isothermal) path, integrate the additivity rule over the thermal history. **X at the slowest-cooling location → fraction of the part that is crystalline → the part either passes the amorphicity spec or it's scrap. That is yield, and yield × cycle rate = effective capacity.**

### Viscosity & fragility
Supercooled-liquid viscosity follows **VFT: η = η₀·exp[D·T₀/(T − T₀)]**. Good BMG formers are comparatively **strong** liquids (high η near Tg, ~10¹² Pa·s) — high viscosity slows atomic transport and crystallization, widening both the casting and the forming windows. Fragility (Angell plot) inversely tracks GFA in many systems.

## 5. Thermal Characterization (the data the models need)

- **DSC (differential scanning calorimetry):** on heating, a glassy alloy shows in order — a **glass transition** step at Tg, a flat **supercooled-liquid region**, a **crystallization exotherm** (onset Tx, peak Tp), then **melting endotherm(s)** (Tm solidus, Tl liquidus). ΔTx = Tx − Tg is read directly. Report onset vs peak convention and heating rate β (apparent Tg, Tx shift with β).
- **Kissinger analysis:** crystallization activation energy from heating-rate dependence — **ln(β/Tp²) vs 1/Tp** is linear with slope −Ea/R. (Ozawa/Flynn-Wall: ln β vs 1/Tp.) Feeds JMAK's K(T).
- **XRD:** broad amorphous halo = glassy; emerging sharp peaks = crystalline fraction. Primary amorphicity verdict.
- **TEM/HRTEM + SAED:** confirm absence of nanocrystals; diffuse rings = amorphous. Detects crystallinity below XRD's ~2–5 vol% limit.
- **Residual crystallization enthalpy:** a partially-crystallized sample shows a *reduced* exotherm vs the fully-glassy reference — ΔH_residual/ΔH_full estimates remaining amorphous fraction (a fast QA proxy).

## 6. Alloy Families (representative — see references.md for numbers)

- **Pd-based** (Pd₄₀Ni₄₀P₂₀, Pd-Cu-Ni-P): best GFA known, Rc < 0.1 K/s, Dmax up to ~7–8 cm — but precious-metal cost limits volume.
- **Zr-based** (Vitreloy 1 = Zr₄₁.₂Ti₁₃.₈Cu₁₂.₅Ni₁₀Be₂₂.₅): the commercial workhorse, Dmax ~1 cm, Rc ~1 K/s — **Be-bearing (toxicity, §safety)**.
- **Cu-based, Ti-based:** cheaper structural BMGs, moderate Dmax (mm-cm).
- **Fe-based** (Metglas heritage, Finemet): soft-magnetic, transformer cores; often ribbon, not bulk.
- **Mg-, La-, Ca-based:** low Tg, easy TPF, lower strength.
- **High-entropy metallic glasses (HE-MGs):** newer, multi-principal-element formers.

## 7. The Capacity-Planning Vocabulary (the technique lens)

These are the operations-management tools the workspace fuses onto BMG kinetics:
- **Theory of Constraints (TOC):** every line has one bottleneck; throughput is set by it. Here the bottleneck may be a *machine* (press, furnace) **or** the *crystallization clock* — the latter is the distinctive BMG case.
- **Little's Law:** WIP = throughput × flow-time. Sizes melt-handling and the DSC/XRD QA queue.
- **OEE = Availability × Performance × Quality.** Quality loss = crystallized/partially-amorphous scrap — directly the JMAK yield.
- **Yield-adjusted capacity:** good-parts/hr = gross-rate × first-pass yield. The whole point of `/crystallization-yield`.
- **Capacity cushion & demand forecasting:** buffer for variable yield + oxygen-driven yield risk; forecast precious-metal feedstock (Pd, Be handling).
- **Takt time vs cycle time:** the TPF window imposes a *hard* per-heat cycle ceiling no efficiency push can exceed.

## Common Failure Modes

- **Oxygen-seeded heterogeneous nucleation** — tens of ppm of O in Zr-based melts triggers quasicrystal/crystal nucleation, raising Rc and slashing Dmax and yield. The most common production yield-killer.
- **Section too thick for the alloy** — centre cools below Rc, crystallizes; surface looks glassy, core is crystalline. A geometry/Dmax mismatch, not a process error.
- **TPF over-dwell** — heating into the supercooled region too long (or too hot) crystallizes the part mid-forming; the window closes on the TTT nose.
- **Off-eutectic composition drift** — raises Tl, lowers Trg/γ, shrinks the casting window; small at% errors matter.
- **Flux/feedstock regression** — losing B₂O₃ fluxing or switching to higher-O sponge reintroduces nucleants; yield drops with no machine change.
- **Mold heat-extraction decay** — a worn/cracked/oxidised copper mold extracts heat slower; cooling rate falls below Rc for the thinnest product first.

## Operating Constraints

- **Beryllium toxicity** (Vitreloy and kin): Be fume/dust → chronic beryllium disease; OSHA PEL 0.2 µg/m³ TWA. Engineered controls mandatory for any powder/machining step; prefer Be-free GFA where feasible.
- **Reactive-melt handling:** Zr/Ti melts are O/moisture-sensitive and pyrophoric as fines → vacuum or inert-atmosphere melting.
- **HF metallography:** BMG etchants are frequently HF-bearing → delayed deep burns, systemic fluoride toxicity; institutional HF protocol + calcium gluconate on hand.
- **Physical limit:** you cannot beat Rc by wanting to. If Dmax < required section, the honest answer is "not in this alloy."
