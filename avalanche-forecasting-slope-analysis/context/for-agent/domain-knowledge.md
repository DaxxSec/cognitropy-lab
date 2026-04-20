# Domain Knowledge: Avalanche Science Fundamentals

## Snowpack Anatomy

A snowpack is a stratified sequence of layers deposited by storm events and modified by weather, metamorphism, and loading. Forecasting centers on three ingredients:

1. **Slab** - cohesive layer(s) on top
2. **Weak layer** - cohesionless or poorly-bonded layer underneath
3. **Bed surface** - the sliding plane

An avalanche requires all three plus a trigger. "No weak layer, no slab avalanche."

## Metamorphism Regimes

| Regime | Driver | Typical Grain | Hazard Signal |
|---|---|---|---|
| Equilibrium (rounding) | Gentle gradient (< 10 C/m) | Rounded | Bonding improves over time |
| Kinetic growth (faceting) | Strong gradient (> 10 C/m), cold near-ground | Facets, depth hoar | Cohesionless weak layer, persistent |
| Melt-freeze | Diurnal melt | Rounded polycrystals | Ice crust bed surfaces; wet slab potential |
| Surface hoar growth | Clear calm cold nights + moist surface | Feathery crystals | Buried -> classic PWL |

## The Nine Avalanche Problem Types

1. **Dry Loose** - point-release sluffing of unconsolidated dry snow
2. **Wet Loose** - point-release of wet snow, often during warming
3. **Storm Slab** - soft slab of new snow, typically lasts 24-48 h after storm
4. **Wind Slab** - slab formed downwind of ridges; localized, aspect-sensitive
5. **Persistent Slab** - slab on a PWL (buried surface hoar, near-surface facets, depth hoar); the professional killer
6. **Deep Persistent Slab** - PWL near the ground, often basal depth hoar or faceted November snow
7. **Wet Slab** - slab weakened by meltwater or rain; fast-evolving
8. **Cornice Fall** - cornice failure that may trigger slab below
9. **Glide** - full-depth release on smooth ground (grass, rock slabs); timing notoriously unpredictable

Each type has characteristic distribution (aspect/elevation/terrain), sensitivity (trigger threshold), and likelihood/size matrices defined by the Conceptual Model of Avalanche Hazard (CMAH).

## Stability Tests

| Test | What it tells you | Key score notation |
|---|---|---|
| **Compression Test (CT)** | Initiation sensitivity | CT # (number of taps), + failure character (SP/SC/PC/BRK/RP) |
| **Extended Column Test (ECT)** | Initiation + short-distance propagation | ECTP # (propagates) / ECTN # (no prop) / ECTX (no fail) |
| **Propagation Saw Test (PST)** | Propagation propensity | PST ## /100 END / ARR / SF |
| **Rutschblock (RB)** | Large-area loading | RB 1-7 with failure character |
| **Hand / Shear** | Quick qualitative | hardness F / 4F / 1F / P / K / I |

**ECTP on a PWL < 20 taps = major red flag.**
**PST < 50/100 END = propagation is likely.**

## Conceptual Model of Avalanche Hazard (CMAH)

Hazard = f(likelihood, size) for each problem type, summed across aspects and elevations to produce the danger rating.

- **Likelihood** combines sensitivity and spatial distribution.
- **Size** uses the D-scale (D1 relatively harmless -> D5 catastrophic, destroys village).

## North American Public Avalanche Danger Scale

| Level | Travel Advice | Trigger | Size / Distribution |
|---|---|---|---|
| 1 Low | Generally safe conditions. Watch for unstable snow on isolated terrain features. | Unlikely | Small in isolated areas |
| 2 Moderate | Heightened avalanche conditions on specific terrain features. | Possible on specific features | Small in specific areas / Large in isolated |
| 3 Considerable | Dangerous conditions. Careful snowpack evaluation, cautious route-finding, conservative decision-making essential. | Likely natural / very likely human | Large in specific / Very large in isolated |
| 4 High | Very dangerous conditions. Travel in avalanche terrain not recommended. | Very likely | Large in many / Very large in specific |
| 5 Extreme | Avoid all avalanche terrain. | Certain | Very large in many |

## FACETS - Human Factor Heuristic Traps

- **F**amiliarity
- **A**cceptance
- **C**ommitment
- **E**xpert halo
- **T**racks / scarcity
- **S**ocial facilitation

Every `/incident-review` run must surface which FACETS trap(s) may have been in play.
