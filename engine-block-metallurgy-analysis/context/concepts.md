# Engine Block Metallurgy Analysis — Core Concepts

Background the agent reads before acting. Optimised for fast recall during a case, not exhaustive theory.

## 1. Engine block materials and where they're used

| Material family | Typical grades | Microstructure | Where used | Notes |
|---|---|---|---|---|
| Gray cast iron | ASTM A48 Class 25–40; SAE J431 G3000/G3500 | Type A flake graphite in pearlite (±ferrite) | Mainstream petrol blocks, liners | Cheap, great damping & machinability, brittle; UTS 175–290 MPa |
| Compacted graphite iron (CGI / vermicular) | ISO 16112 GJV-400/450/500; ASTM A842 | Vermicular (worm-like) graphite + nodules, pearlitic | Modern HD diesel blocks/heads (6.7L Power Stroke, Audi V8 TDI) | ~75% stronger & ~2× fatigue vs gray iron; nodularity tightly controlled |
| Ductile (nodular/SG) iron | ASTM A536 60-40-18…100-70-03 | Spheroidal graphite (Mg-treated) | Crankshafts, caps, some blocks | High strength + ductility; Mg fade ruins nodularity |
| Hypoeutectic Al-Si | A319, A356, A380 | α-Al dendrites + eutectic Si | Aluminium blocks with iron/steel liners | Heat-treatable (T5/T6/T7); needs liners or coatings |
| Hypereutectic Al-Si | A390, Alusil (AlSi17) | Primary Si particles + eutectic | Linerless blocks (bore is honed Si) | Primary-Si size & distribution control bore wear |

**Carbon equivalent (CE)** governs how close an iron is to the eutectic (≈4.3% C):
`CE = %C + (%Si + %P)/3`. CE < 4.3 → hypoeutectic (more chill tendency, primary austenite dendrites); CE > 4.3 → hypereutectic (kish/flotation graphite risk). Engine gray irons run CE ≈ 3.8–4.2.

## 2. Graphite morphology — the single most diagnostic feature in cast iron

Per **ASTM A247 / ISO 945-1**, graphite is classified on three axes:

- **Form / type (Roman numerals I–VII):** I = nodular (spheroidal), II = irregular nodular, III = vermicular/compacted, IV = aggregate, V = crab-form, VI = irregular flake, VII = flake (lamellar).
- **Distribution (gray-iron flake, A–E):** A = uniform random (best), B = rosette, C = kish/superimposed (hypereutectic), D = interdendritic random (fast cooling), E = interdendritic preferred (worst, weak).
- **Size (1–8):** 1 = coarse (>100 mm at 100×) … 8 = fine.

**Nodularity %** (ISO 945-4 / ASTM A247 image analysis) is the fraction of graphite that is spheroidal — the key acceptance metric for ductile and CGI. Ductile typically requires ≥80–90% nodularity; CGI is a *controlled* window (often 0–20% nodules with the balance vermicular). Drift outside the window is a classic process escape.

**Matrix phases** under the graphite matter as much: ferrite (soft, ductile), pearlite (strong, wear-resistant), and unwanted phases — free cementite/carbides (chill, embrittling), steadite (Fe-Fe₃C-Fe₃P ternary eutectic, brittle network at high P), and martensite/bainite from rapid cooling or localized overheating.

## 3. Graphite degeneration (Mg-treated irons)

Diagnostic of process problems in ductile/CGI:

- **Mg fade** → reversion to flake graphite at the casting skin or thick sections (low residual Mg, long pour-to-solidification time).
- **Chunky graphite** → heavy sections, excess Ce/rare earths, slow cooling — collapses ductility.
- **Exploded / spiky graphite** → too much Mg or rare earth.
- **Graphite flotation (kish)** → hypereutectic CE, graphite rises to cope surface.

## 4. Casting defect catalogue

- **Gas porosity** — smooth, round, often subsurface; from dissolved H₂ (aluminium) or N₂/CO. Tends to be distributed.
- **Shrinkage porosity** — jagged, dendritic, interconnected; in last-to-freeze regions (hot spots, junctions). Distinct from gas under SEM.
- **Inclusions** — sand, slag, dross (oxide films in aluminium), refractory. EDS gives composition (Si/O sand, Al-Mg-O dross).
- **Cold shut / misrun** — incomplete fusion of two metal fronts; smooth rounded boundary.
- **Hot tear** — irregular, oxidized crack from solidification shrinkage under restraint; intergranular.
- **Chill / inverse chill** — white iron (carbides) at surface (chill) or core (inverse, P/S-related).
- **Core shift** — wall-thickness asymmetry; not a microstructural defect but drives local cooling rate and stress.

## 5. Engine-block failure modes

- **Thermal fatigue** — cyclic ΔT (warm-up/cooldown, knock) cracks valve bridges, bore bridges, deck. Network of short cracks; oxidized faces.
- **High-cycle mechanical fatigue** — main-bearing bulkheads, bolt bosses. Striations, beach marks, single origin.
- **Coolant-side cavitation erosion** — pitting of wet-liner outer wall from vibration-induced bubble collapse.
- **Bore scuffing/scoring** — adhesive wear; lubrication failure or soft/under-refined bore surface (Al-Si).
- **Detonation/pre-ignition damage** — eroded piston/ring-land + localized head/deck attack; thermal signature.
- **Creep & oxidation** — sustained high-temp exhaust-side service.
- **Overload/brittle fracture** — single overstress event; cleavage in gray iron.

## 6. Bayesian probability assessment (today's technique)

Failure analysis is hypothesis competition under partial evidence — exactly what Bayes formalizes.

**Bayes' theorem (odds form), the working tool:**
`posterior odds = prior odds × likelihood ratio (LR)`
where `LR = P(evidence | H₁) / P(evidence | H₀)`.

Chaining independent findings: multiply LRs. `O(H | E₁,E₂,…) = O(H) · LR₁ · LR₂ · …`. Work in **log-odds** (add `log LR`) to avoid underflow and to see each finding's contribution additively.

- **Prior odds** — base rates for this material + service condition (e.g. CGI process escapes are rarer than overheat events in high-mileage field returns). State them; don't hide them.
- **Likelihood ratio** — how much more probable the evidence is under one hypothesis than another. LR ≫ 1 strongly favors H₁; LR ≈ 1 is non-diagnostic; LR ≪ 1 favors H₀. A finding "consistent with" a cause but equally consistent with the alternative has LR ≈ 1 and must not move the verdict.
- **Posterior** — the updated probability over causes. Convert odds back: `P = O/(1+O)`.
- **Bayesian network** — when causes share evidence (a hot zone explains both thermal fatigue *and* Mg fade), model conditional dependencies rather than naively multiplying.
- **Value of information** — the next test to run is the one whose expected posterior swing (information gain) is largest, not the cheapest or most familiar.
- **Reliability priors** — Weibull life models with informative priors on shape/scale (β, η) let a few failures update an a-priori life estimate instead of demanding a full fleet.

## Common Failure Modes (of the *analysis*)

- **Confirmation bias** — anchoring on the first plausible cause; cured by keeping all hypotheses with explicit priors and demanding LRs.
- **Treating "consistent with" as proof** — non-diagnostic evidence (LR ≈ 1) presented as confirmation.
- **Double-counting correlated evidence** — multiplying LRs of findings that are not conditionally independent (e.g. two measures of the same thermal event).
- **Base-rate neglect** — ignoring how rare a casting escape is versus a service abuse event before weighing evidence.
- **Prep artefacts read as features** — polishing pull-out mistaken for porosity; over-etch mistaken for a phase. Cured by as-polished + etched comparison.

## Operating Constraints

- Destructive testing is one-way: document as-received condition (photos, dimensions, hardness) and retain an archive specimen before sectioning.
- Cite the standard *and revision* for every classification (graphite type, hardness, point count) — methods change between editions.
- Metallurgy establishes material state and failure mechanism, not legal fault. Keep that boundary in every report.
