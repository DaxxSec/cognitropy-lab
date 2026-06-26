# Concepts — Microplastics Sampling & Testing

Reference knowledge for the agent. Read on demand; cite the standards in `references.md` where a method choice needs justification.

## 1. What microplastics are

- **Microplastics (MP):** synthetic polymer particles < 5 mm in the largest dimension. The upper bound (5 mm) is conventional (GESAMP/NOAA); the lower bound is method-limited.
- **Size sub-classes (common, not fully standardized):**
  - Large microplastics: 1–5 mm
  - Small microplastics: 1 µm – 1 mm
  - **Nanoplastics:** < 1 µm (some authors use < 1000 nm; definitions vary). Nanoplastics require entirely different capture/analysis and are usually out of scope for routine FTIR/Raman programs.
- **Primary vs secondary MP:** *primary* are manufactured small (microbeads, pre-production nurdles, fibers); *secondary* are fragmentation products of larger plastic via UV, mechanical, and biological weathering.
- **Morphology classes:** fragment, fiber, film, bead/sphere, foam, pellet/nurdle. Morphology is a source clue — fibers ↔ textiles/laundry, films ↔ packaging, foam ↔ EPS, spheres ↔ microbeads or industrial abrasives.

## 2. Polymers you actually see

Density drives which separation medium will float a polymer, and which fraction of the environment it occupies (floating vs sinking). Approximate densities (g/cm³):

| Polymer | Density | Float in seawater (~1.025)? | Notes |
|---|---|---|---|
| PP (polypropylene) | 0.90–0.92 | Yes | Ropes, caps, packaging |
| PE (LDPE/HDPE) | 0.91–0.97 | Yes | Bags, bottles, films — most abundant |
| EPS / PS foam | 0.01–1.05 | Yes (foam) | Expanded polystyrene |
| PS (polystyrene) | 1.04–1.07 | Marginal | Cutlery, packaging |
| PA (nylon) | 1.12–1.15 | No | Fishing nets, textiles |
| PMMA | 1.17–1.20 | No | Acrylic |
| PC (polycarbonate) | 1.20–1.22 | No | — |
| PVC | 1.16–1.45 | No | Pipe, additives raise density |
| PET (polyester) | 1.37–1.45 | No | Bottles, textile fibers — dominant in sediment |
| PTFE | 2.1–2.3 | No | Needs high-density medium |

**Tire-wear particles (TWP)** and road dust are a distinct, important class — heterogeneous, dense, and easy to miss; often a watchlist target.

## 3. Matrices and how they're sampled

- **Surface water:** neuston/manta net (standard mesh **333 µm**) for floating MP over distance; bulk-water grab + filtration cascade for smaller size classes and absolute concentration.
- **Water column / discrete depth:** Niskin or Van Dorn bottles, then filtration.
- **Sediment:** grab or core; the sink for dense polymers (PET, PVC) and aged particles.
- **Biota:** tissue/gut digestion (KOH) — exposure and trophic-transfer studies.
- **Atmospheric deposition / indoor air:** passive deposition collectors or active pumped filters — fibers dominate; contamination control is brutal here.

**Aperture sets the floor.** A 333 µm net cannot see a 50 µm fragment. The smallest reported size is a property of your gear, not the environment. Always state the size class.

## 4. From sample to particle (sample prep)

1. **Organic-matter removal (digestion):**
   - Wet peroxide oxidation (WPO, 30% H₂O₂), optionally Fenton's (H₂O₂ + Fe²⁺) — common, polymer-safe if temperature-controlled.
   - **KOH (10%)** for biota/tissue — good organic removal, gentle on most polymers.
   - **Avoid strong acid (HNO₃)** as a blanket digestant — it degrades PA, PET, and others and biases the result.
2. **Density separation:** float the plastics off the mineral matrix. Medium must be denser than the target polymers (see `references.md`): NaCl (~1.2) is cheap but misses PET/PVC; ZnCl₂ (~1.6), NaI (~1.8), or sodium polytungstate (SPT, up to ~3.1) recover dense polymers.
3. **Filtration onto a defined pore size** (e.g. 0.45–10 µm depending on target), then microscopy/spectroscopy.

## 5. Identification (the secondary screen)

- **Visual / stereomicroscopy:** fast, cheap, **unreliable alone** — visual-only ID over-calls plastic; always confirm a subset spectroscopically.
- **Nile Red staining + epifluorescence:** lipophilic dye, rapid primary screen for plastic-likely particles; **not polymer-specific** and stains some natural lipids → false positives.
- **ATR-FTIR:** definitive for particles ≳ 300–500 µm; identifies polymer by IR absorption fingerprint.
- **µ-FTIR / FPA imaging:** maps smaller particles (down to ~10–20 µm); high-throughput chemical imaging of a whole filter.
- **Raman microspectroscopy:** complements FTIR, reaches ~1 µm, but fluorescence (from dyes/biofilm) can swamp the signal.
- **Py-GC/MS & TED-GC-MS:** *mass-based*, destructive; gives polymer mass per sample but not particle counts or sizes — good for total-mass and additive work, a fusion partner for count methods.

**Hit-Quality Index (HQI):** library-match score; a working threshold is ~0.7 for FTIR correlation, but the *diagnostic bands must actually be present* and the margin over the runner-up must be real (see `/polymer-id`).

## 6. The border-screening framework (the fusion lens)

This workspace deliberately runs the program with frontier-inspection doctrine:

- **Risk-based targeting** → sample where load/decision-value is highest, not uniformly (`/risk-target-sites`).
- **Layered primary→secondary screening** → cheap high-throughput count, then definitive confirmation only on referrals (`/screen-sample` → `/polymer-id`). Randomized referral of the non-flagged fraction keeps the primary screen's false-positive rate measurable.
- **Chain of custody** → sealed, signed, logged evidence handling for legal/regulatory defensibility (`/custody-log`).
- **Watchlist + anomaly escalation** → distinctive signatures (TWP, banned microbeads, source copolymers) and baseline deviations raise alerts (`/contamination-anomaly`).
- **Sensor fusion** → combine staining + FTIR + Raman + Py-GC/MS to drive down false positives/negatives, like multi-modal scanning.
- **Throughput vs detection trade-off** → an explicit, tunable referral policy makes the false-negative rate a design choice, not an accident.

## 7. Predictive maintenance (the technique)

The "checkpoints" are physical and they degrade. Concepts that matter:

- **Service interval vs condition-based maintenance:** calendar limits (source hours, injection counts) overlaid with live condition signals (drift, blank creep).
- **Remaining useful life (RUL):** estimate from whichever bound is nearer — usage budget or drift trajectory.
- **Calibration verification & control charts:** Shewhart/Westgard rules on check-standard runs flag drift *before* it fails a batch.
- **QA-as-early-warning:** a rising blank fiber load or a falling spike recovery is frequently the first sign a filter/sieve/medium is failing — fold QA trends into the maintenance forecast (`/instrument-maintenance-forecast`).

## 8. Dominant failure modes

1. **Airborne contamination** (especially fibers) — the #1 false positive. Mitigate with glass/metal labware, cotton coats, filtered-air enclosures, covered samples, and rigorous blanks.
2. **Density-medium too light** — silently loses PET/PVC/PA; recovery spikes catch it.
3. **Acid digestion damage** — degrades susceptible polymers, biases composition.
4. **Visual/stain over-calling** — reporting unconfirmed particles as plastic.
5. **Small-particle recovery loss** — sub-100 µm particles under-recover; sets the quantitative reporting floor.
6. **No blank correction / no recovery correction** — numbers not comparable across labs or time.
7. **Over-precise reporting** — ignoring Poisson counting uncertainty at low counts.
8. **Aperture amnesia** — comparing a 333 µm-net dataset to a 10 µm-cascade dataset as if equivalent.
