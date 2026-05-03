# Domain Knowledge — Glassblowing Form Shaping (Sim + Microbiome-Style Tracking)

## Glass as a Material

Glass is an amorphous solid with no melting point — instead it has a continuous viscosity-vs-temperature curve. Form-shaping happens in the narrow band where viscosity is low enough for the glass to deform under hand tools but high enough that it holds shape between operations. Outside this band the work is impossible (too cold) or destructive (too hot).

### Anchor Viscosity Points
| Anchor | Viscosity (poise) | Behavior | Soda-lime ~T | Borosilicate ~T |
|--------|-------------------|----------|--------------|-----------------|
| Working point | 10⁴ | Easily deformed by hand tools | ~1050 °C | ~1250 °C |
| Softening point | 10⁷·⁶ | Deforms under its own weight | ~720 °C | ~820 °C |
| Annealing point | 10¹³ | Stress relaxes within minutes | ~482 °C | ~565 °C |
| Strain point | 10¹⁴·⁵ | Stress takes hours to relax; below this no useful relaxation | ~452 °C | ~525 °C |

The four-point reference (working / softening / annealing / strain) is enough for nearly all studio decisions. Manufacturer datasheets give exact values per product.

### COE Families (commonly seen in studios)
- **Bullseye COE 90** — Fusing/casting glass; sheet, frit, billet
- **System 96** — Spectrum / Uroboros / Oceanside; sheet, frit, rod
- **Effetre / Moretti COE 104** — Italian soft glass; rods, the dominant lampworking soft glass
- **Reichenbach RW104** — German soft glass nominally compatible with Effetre 104, but lot-to-lot variation requires pretest
- **Kugler COE 104** — Premium soft glass from Augsburg
- **Schott Borosilicate 33 (Pyrex/Duran family)** — Lampworking borosilicate; tubes, rods
- **Northstar / Glass Alchemy borosilicate** — Color rod borosilicate, US-sourced, COE 33

**Hard rule:** never combine glasses across families in a single piece. The COE delta produces strain on cooling that exceeds tensile strength within hours to weeks. "Compatible" stamps from a single manufacturer are still subject to lot variation — when in doubt, run a small fused test piece and inspect under crossed polarizers for stress fringes before committing the full plan.

## Form-Shaping Operations

### Hot-Shop (Furnace + Glory Hole) Vocabulary
- **Gather** — Collecting molten glass on a blowpipe or punty by dipping into the furnace. Per-gather mass is roughly 200–400 g for a standard pipe; double-gather ~600 g; triple ~900 g+
- **Marvering** — Rolling the gather on a steel marver (table) to shape and cool the surface uniformly
- **Blocking** — Shaping with a water-soaked wood block (cherry traditionally) — produces a smooth rounded form
- **Jacks** — Steel tongs used to constrict the glass at a defined point (typically for necking before transfer or for forming a foot)
- **Paddles** — Wood or graphite, used to flatten or compress
- **Blow** — Air introduced through the pipe to inflate; controlled by puffs and wraps
- **Optic mold** — Cast iron mold with vertical ribs; pressed into to give a textured surface that survives subsequent inflation as twisted ribbing
- **Punty transfer** — Attaching a second iron (the punty) to the bottom of the piece so the blowpipe can be cracked off and the rim opened
- **Glory hole** — A small reheating furnace (typically 1100–1200 °C) used to reheat the working piece between operations

### Lampworking (Torch) Vocabulary
- **Torch** — Hand-held or bench-mounted, oxy-propane or oxy-natural-gas, surface-mix or pre-mix
- **Cane** — Stretched colored glass rod
- **Stringer** — Very fine cane, used for surface decoration
- **Frit** — Crushed glass, applied to surface for color or texture
- **Bead release** — Coating on the mandrel to allow the bead to be removed after annealing
- **Mandrel** — Steel rod onto which a bead is wound
- **Garaging** — Holding the in-progress work in a heated chamber when not actively torching, to prevent thermal shock

## Working-Time Budget Math

When a gather leaves the glory hole, it cools by radiation, convection, and tool contact. Empirical surface temperature drops per operation (soda-lime; borosilicate roughly 60% of these values due to lower thermal expansion):

| Operation | Approx. surface ΔT | Notes |
|-----------|---------------------|-------|
| Air cool, 10 s | ~30 °C | Free in studio ambient |
| Marvering, 5 s | ~80 °C | Steel marver is a heat sink |
| Blocking, 3 s | ~50 °C | Wet wood block, water on contact |
| Jacks, 5 s | ~40 °C | Brief contact, less mass than block |
| Blow puff (rapid) | ~10 °C | Internal cooling from cold air |
| Optic press, 3 s | ~70 °C | Iron mold, brief but full contact |
| Bench paddle, 3 s | ~30 °C | Light contact |

**Working time per heat (heuristic):** for a 300 g gather coming out at glory-hole soak temp (~1150 °C), the surface is below working point (10⁴ poise, ~1050 °C) after roughly 60 s of bench work. Reheat between operations to reset the budget. Larger gathers retain heat longer; thinner extensions (canes, lips) cool faster.

## Gravity Sag

A horizontal extension or the wall of an upright vessel deforms under its own weight at a rate proportional to:

```
sag_rate ∝ (ρ · g · L²) / η
```

Where ρ ≈ 2.5 g/cm³, g = 9.8 m/s², L = unsupported length, η = viscosity (function of temperature).

Practical thresholds (these are heuristic, not first-principles, but they match studio experience):

| Form type | Tolerable sag in 30 s at working temp | Notes |
|-----------|---------------------------------------|-------|
| Vessel wall (upright) | ~1 mm | Compensate by rotation in glory hole |
| Goblet stem (vertical) | ~0.5 mm | Stem geometry is intentional, sag is failure |
| Plate rim (horizontal) | ~0.5 mm at the rim | Most demanding |
| Sculptural extension | Artist-defined | Often the sag IS the form |

If the simulator predicts > threshold, recommend either: shorter unsupported length (reposition support point), faster operation (reheat sooner), or higher viscosity working temp (cool slightly before the operation).

## Annealing Physics

When a hot piece is placed in the lehr, the surface cools faster than the core. Above the strain point, the glass relaxes any developing stress within minutes. Below the strain point, stress is locked in. The annealing program manages this:

1. **Hold at anneal point** — long enough that surface and core both reach thermal equilibrium (~anneal temp). Hold time scales with mass and wall thickness (see `cool-curve.md` for the table).
2. **Anneal-to-strain ramp** — the most stress-sensitive segment. Ramp rate must keep the temperature gradient through the glass low enough that the core-to-surface ΔT × COE × Young's modulus stays below tensile strength (~50 MPa for soda-lime, ~60 MPa for borosilicate). Empirical: rate ≤ K / thickness² with K ≈ 1500 (soda-lime), 800 (borosilicate).
3. **Strain-to-100 °C ramp** — glass is rigid; differential cooling continues to generate strain but no relaxation occurs. Ramp can be 2× the anneal-to-strain rate.
4. **Below 100 °C** — natural cool to room.

A piece that survives the bench but cracks in the lehr almost always failed at segment 2.

## Failure-Mode Taxonomy (Summary)

Fully detailed in `resources/failure-mode-taxonomy.md`. Five primary modes:

1. **Cold check** — bench-time crack from working too cold or cold tool on hot glass
2. **Thermal shock** — sudden ΔT crack, usually at lehr load
3. **Anneal crack** — ramp-stage crack from too-fast cooling for the wall thickness
4. **Residual strain** — post-anneal crack from insufficient hold or too-fast strain-to-room ramp
5. **COE mismatch (slow cracker)** — days-to-months crack from incompatible glass families joined

Plus secondary contributors: devit (surface crystallization), cord (compositional inhomogeneity), bubble inclusions, coldwork-induced surface stress.

## Microbiome-Style Documentation Patterns

Soil-microbiome research treats every plot as a tracked entity with an explicit lineage (seed lots, inoculants, amendments), an environmental envelope (temperature, moisture, pH at observation), an intervention sequence (tilling, watering, amending dates and quantities), an outcome (yield, biomass, taxonomic assay), and successional follow-ups (7d, 30d, 90d revisits). The same schema applied to glass:

| Microbiome field | Glass equivalent | Why it matters |
|------------------|-------------------|----------------|
| Plot ID | Batch ID (date + sequence) | Universal handle for queries |
| Seed lot / inoculant | Cullet melt ID, color rod lot + supplier | Upstream cause for any failure mode 5 (COE) |
| Amendment | Frit, applied color, cane | Same — surface inclusions trace here |
| Air temp / moisture | Studio ambient °C / RH | Working time budget shifts with ambient |
| Soil temp / pH | Glory hole soak T / lehr program ID | The "in vivo" environment of the work |
| Tilling / watering / amending | Gathers, marvering, jacks, blocks | The intervention sequence — order matters |
| Yield / biomass | Pieces produced, with mass, finished/abandoned | Direct outcome |
| 7d / 30d / 90d revisit | Post-anneal inspection, 24h shelf, 30d crack survey | Modes 4 & 5 only show up on follow-up |

**Why the analogy holds:** in both fields, the immediate result of the day's work is necessary but not sufficient — the actual outcome includes successional changes that take weeks. In both, upstream lot-level variation drives a meaningful fraction of failures. In both, ad-hoc journaling is the historical norm and structured records are the productivity intervention.

**Why this isn't theater:** a six-month batch index is queryable. A six-month studio notebook is not. The agent's job is to keep the records strict enough that grep and `/lineage-trace` work.

## Reference Numbers Summary

| Quantity | Soda-lime | Borosilicate |
|----------|-----------|--------------|
| Working point | 1050 °C | 1250 °C |
| Annealing point | 482 °C | 565 °C |
| Strain point | 452 °C | 525 °C |
| Density | 2.5 g/cm³ | 2.23 g/cm³ |
| COE | 90–104 × 10⁻⁷/K | 33 × 10⁻⁷/K |
| Tensile strength | ~50 MPa | ~60 MPa |
| Young's modulus | ~70 GPa | ~64 GPa |
| Thermal conductivity | ~0.9 W/m·K | ~1.2 W/m·K |
| Per-gather mass (typical) | 250–400 g | 100–250 g (usually rod stock, smaller) |
| Working window (per heat, 300 g gather) | ~60 s | ~90 s |
| Anneal hold (12 mm wall) | 60 min | 60 min |
| Cool-curve K constant | 1500 °C·mm²/h | 800 °C·mm²/h |

These are studio-grade approximations. Always defer to manufacturer datasheets and to the studio's own observed values once the batch records have accumulated.
