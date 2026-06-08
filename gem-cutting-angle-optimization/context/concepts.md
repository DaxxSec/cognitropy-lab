# Gem Cutting Angle Optimization — Core Concepts

Background the agent reads before acting. Two domains meet here: the **optics of faceting** (what angle to cut) and **predictive maintenance** (whether the machine can hold it). They are joined by one quantity — the **angle-error budget**.

## 1. Why angle is everything

Light entering a faceted stone through the table should bounce off the pavilion facets and return to the eye. Whether it returns is governed by **total internal reflection (TIR)**. Light inside the stone striking a pavilion facet *from the inside* reflects entirely back (rather than refracting out) only when its angle of incidence (measured from the facet normal) exceeds the **critical angle**:

```
θ_critical = arcsin(1 / n)      n = refractive index of the gem (relative to air)
```

- Higher RI → smaller critical angle → easier to achieve TIR → shallower pavilions allowed.
- Lower RI → larger critical angle → steeper pavilions required, or light leaks out.

The pavilion **main angle** (measured from the girdle plane) is what the cutter sets on the protractor. It must be steep enough that rays double-bounce off opposing pavilion facets and exit the crown, rather than passing straight through. Too shallow and you get a **window**; too steep and you get a dark center (**nailhead / extinction**). Between those failure modes is a narrow optimal band, a few degrees wide, that depends almost entirely on RI.

## 2. The three optical effects

- **Brilliance** — total white light returned to the eye. Maximized when most rays achieve TIR and exit the crown. Driven primarily by pavilion angle (TIR) and table size.
- **Dispersion / fire** — separation of white light into spectral colors. A material property (the *dispersion* coefficient) amplified by **crown angle**: steeper crowns bend exiting rays more and spread color, at some cost to raw brilliance.
- **Scintillation** — the flashing sparkle as the stone or light moves. Driven by facet count, size, and meet-point precision — many small, crisply-met facets scintillate more.

Optimization is a trade-off: a steeper crown buys fire but costs brilliance; a larger table buys brilliance but costs fire and can introduce a fish-eye. The "best" cut depends on the material's RI *and* its dispersion.

## 3. Anatomy of a faceted stone

```
        table
       ______
      /      \      ← crown facets (star, bezel/kite, upper-girdle)
     /________\     ← girdle (the widest line; the angle reference plane)
     \        /     ← pavilion facets (pavilion mains, lower-girdle)
      \______/      ← culet (point, or tiny facet)
```

- **Table %** — table width ÷ stone diameter. Round-brilliant sweet spot ≈ 53–58%.
- **Crown angle** — crown mains vs girdle plane. Classic round brilliant ≈ 34.5°.
- **Pavilion angle** — pavilion mains vs girdle plane. Classic round brilliant ≈ 40.75° (for diamond, RI 2.417).
- **Total depth %** — table-to-culet depth ÷ diameter. Round brilliant ≈ 59–62.5%.
- **Index gear** — a notched wheel (96, 80, 64, or 32 splits) that sets the rotational position of each facet; the protractor sets the angle. A design is a list of (angle, index) pairs.

## 4. Critical angle by material (why charts differ)

| Material | RI (approx) | Critical angle | Typical pavilion main |
|---|---|---|---|
| Diamond | 2.417 | 24.4° | 40.75° |
| Cubic zirconia | 2.15 | 27.7° | ~40° |
| Corundum (sapphire/ruby) | 1.762 | 34.6° | 41–43° |
| Spinel | 1.718 | 35.6° | ~42° |
| Garnet (almandine/spessartine) | 1.79 | 33.9° | ~41° |
| Topaz | 1.62 | 38.2° | ~43° |
| Tourmaline | 1.62 | 38.2° | ~43° |
| Beryl (emerald/aqua) | 1.577 | 39.3° | ~43° |
| Quartz (amethyst/citrine) | 1.544 | 40.3° | ~43° |
| Fluorite | 1.434 | 44.2° | ~45°+ |

The pattern: as RI drops, the critical angle climbs, the pavilion must steepen, and the windowing margin narrows. Below ~RI 1.45 (fluorite, opal) it is hard to cut a window-free stone at all without going very deep.

## 5. Common optical failure modes

- **Window (light leakage)** — pavilion too shallow relative to the critical angle; the center looks see-through, you can read print through it. The number-one beginner defect.
- **Fish-eye** — in round brilliants, a shallow pavilion plus a large table reflects the girdle as a white ring under the table.
- **Nailhead / dark center** — pavilion too steep; a dark unreflective spot in the middle.
- **Extinction** — broad dark zones where rays exit instead of returning; over-deep pavilion or poor crown/pavilion balance.
- **Off meet-points** — facets that should converge to a single point miss; a cutting-precision defect, almost always traceable to machine condition (runout, lap dishing, index backlash) rather than the design.

## 6. The tangent-ratio principle (porting designs across materials)

A published design's angles are correct only for the RI it was cut for. To re-use it in a different material, the standard trade method is the **tangent ratio** (Strickland / GemCad): multiply the tangent of each design angle by a constant TR and take the arctangent:

```
θ_new = arctan( TR · tan(θ_old) )
```

TR is chosen so the pavilion main lands at the recommended angle for the new RI (steeper for lower RI, shallower for higher). Scaling *all* angles by the same TR preserves meet-point geometry, so the design still closes. GemCad/GemRay automate this; `/tangent-ratio-adapt` reproduces it by hand.

## 7. The machine and what wears

A faceting machine holds the stone (on a **dop** in a **quill/spindle**) against a flat rotating **lap**, at the angle set by a protractor on a **mast**. The angle delivered to the stone is only as good as:

- **Spindle/quill runout** — wobble of the rotating dop, measured as **TIR** (total indicator runout) with a dial indicator. Runout tilts the facet by up to ±(runout/dop-length) radians, directly adding angle error and ruining meet points.
- **Master-lap flatness** — a worn lap goes **dished** (concave) or **domed**; the facet angle then varies with radial position on the lap, so "40.8°" at the rim is not 40.8° at center.
- **Index gear backlash / mast slop** — repeatability error between facets.
- **Lap grit condition** — grit dulls, sheds, or **glazes**; cut rate falls and polish quality degrades even though geometry is fine.
- **Motor/bearing health** — vibration and runout grow as bearings wear; detectable by vibration RMS or motor-current signature long before seizure.

## 8. Predictive maintenance (PdM) fundamentals

Maintenance strategies, weakest to strongest:

1. **Reactive (run-to-failure)** — fix it when it breaks (and after it has scrapped a stone).
2. **Preventive (time-based, PM)** — service on a fixed calendar/hours interval regardless of condition.
3. **Condition-based (CBM)** — service when a measured indicator crosses a threshold.
4. **Predictive (PdM)** — *trend* the indicator and act at the **potential-failure (P) point**, using the forecast to schedule before the **functional-failure (F) point**.

Key constructs:

- **P-F curve / P-F interval** — degradation is detectable (P) well before it causes functional failure (F). The P-F interval is your lead time to schedule work; PdM exists to use it.
- **RUL (remaining useful life)** — estimated time/usage until an indicator reaches its limit, from the fitted degradation trend.
- **Condition indicator** — the measured quantity (spindle TIR, lap flatness deviation, vibration RMS, cut-rate drop).
- **MTBF / Weibull** — wear-out items (bearings, laps) follow a Weibull life with shape β > 1; the hazard rises with age, justifying scheduled intervention.

## 9. The coupling: the angle-error budget

This is the workspace's central idea. An optimized cut demands the machine hold the pavilion angle within some tolerance — typically **±0.1–0.2°** for meet-point work. That budget is *consumed* by machine condition:

```
σ_total² ≈ σ_spindle² + σ_lap² + σ_index² + σ_operator²
```

Each degrading component eats budget. When the root-sum-square of error sources approaches the budget the optimization assumed, meet points start missing and faint windows appear — even though the *calculated* angle was perfect. PdM's job is to keep every contributor small enough that the sum stays under budget, scheduling the fix at the P-point. Optimization and maintenance are therefore one control loop: optimization sets the tolerance; condition monitoring tells you if the machine can still meet it.

## Common Failure Modes (combined)

- **Optimal angle, worn machine** — the math is right but spindle runout/lap dishing delivers a different angle to the stone. Caught only by `/tolerance-budget` + condition trends.
- **Wrong-RI chart** — cutting a low-RI stone on a high-RI angle chart → guaranteed window. Caught by `/critical-angle-calc`.
- **Over-steepening to "be safe"** — pushing the pavilion well past optimum to avoid windowing trades brilliance for a dark, deep, heavy stone.
- **Reactive maintenance** — discovering the lap was dished only after three meet-point failures, instead of trending it.

## Operating Constraints

- **Hardness gates grit.** Soft material (fluorite Mohs 4) needs gentle laps and light pressure; hard material (corundum Mohs 9, diamond 10) needs diamond laps and longer dwell.
- **Cleavage and heat.** Cleavage-prone or heat-sensitive stones constrain dop wax/epoxy choice and cutting pressure regardless of the optical optimum.
- **Tolerance is physical.** No optimization can deliver an angle the machine's current condition cannot hold — always validate against the live tolerance budget.
