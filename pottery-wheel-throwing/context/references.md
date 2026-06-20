# Pottery Wheel Throwing — Reference Tables

Compact lookup data for studio-flow, kiln, and footprint tasks. Defer to upstream sources for fuller specs.

## Orton cone chart (self-supporting, 108 °F/hr final ramp)

| Cone | °C | °F | Typical use |
|------|------|------|-------------|
| 022 | 590 | 1094 | Low overglaze / lustre |
| 06 | 999 | 1830 | Common **bisque** / low-fire glaze |
| 04 | 1060 | 1940 | Bisque / earthenware glaze |
| 1 | 1154 | 2109 | Mid-low stoneware |
| 6 | 1222 | 2232 | **Mid-fire** stoneware glaze (most studios) |
| 8 | 1263 | 2305 | High-mid stoneware |
| 10 | 1285 | 2345 | **High-fire** stoneware / porcelain / reduction |

Heat-work (time × temperature) sets the cone, not peak temperature alone. Verify with witness cones.

## Typical stage durations (mug-scale, experienced thrower)

| Stage | Active time | Wait time | Notes |
|------|------------|-----------|-------|
| Wedge (per batch) | 2–5 min | — | Lost time / changeover |
| Center + throw | 6–14 min | — | Serial skilled |
| Leather-hard dry | — | 6–24 h | Humidity-dependent |
| Trim | 2–6 min | — | Serial skilled |
| Bone-dry | — | 1–7 days | Faster with airflow/heat |
| Bisque fire | — | 8–12 h + cool | Batch server |
| Glaze | 1–4 min | — | Serial skilled |
| Glaze fire | — | 8–14 h + cool | Batch server |

## Kiln firing energy (rough planning figures — measure your own)

| Kiln (electric) | Interior | Cone 6 firing | Notes |
|------|----------|--------------|-------|
| Small test/hobby | ~1–2 cu ft | ~8–15 kWh | High surface-to-volume → poor efficiency |
| Medium studio | ~7 cu ft | ~30–50 kWh | The common workhorse |
| Large production | ~10–11 cu ft | ~55–90 kWh | Best kWh/piece when fully loaded |

Gas kilns: account in therms (1 therm ≈ 29.3 kWh). Bisque (cone 06) uses less than a cone-6 glaze firing. **kWh/piece = firing energy ÷ pieces loaded** — load density is the dominant variable.

## Glaze hazardous-material screen

| Material | Hazard | Limit / guidance |
|---|---|---|
| Lead compounds | Neurotoxin; leaches from food surfaces | Avoid on foodware; FDA leachable-lead action levels; ASTM C738 test |
| Barium carbonate | Acutely toxic; soluble | Use frit form; not on unlined food surfaces |
| Cadmium (inclusion stains) | Toxic; leaches | Food-contact leach test required; liner glaze advised |
| Lithium carbonate | Toxic dust; flux | Dust control; substitute spodumene where possible |
| Manganese dioxide | Fume hazard at temperature | Ventilate firing; respirator when handling dry |
| Free silica (quartz, flint) | Respirable carcinogen | OSHA PEL 50 µg/m³; wet methods, HEPA |
| Soluble colorants (Cu, Co, Cr) | Aquatic toxicity in waste water | No drain disposal; settle/reclaim |

## Traffic-engineering formula cheat-sheet (studio-applied)

| Quantity | Formula | Studio reading |
|---|---|---|
| Webster optimal cycle | `C₀ = (1.5L + 5)/(1 − Y)` | Batch cadence; high kiln load/unload L → longer cycles |
| Critical flow ratio | `yᵢ = qᵢ / sᵢ` | Demand ÷ saturation flow for product line i |
| Sum critical ratios | `Y = Σ yᵢ` (need Y < 1) | Y ≥ 1 ⇒ oversaturated ⇒ add capacity |
| Capacity | `c = s · g/C` | Stage throughput at its green share |
| Degree of saturation | `X = v/c` | X > 1 ⇒ backlog grows each cycle |
| Green ratio | `λ = g/C` | Fraction of the cycle a stage is "on" |
| Webster delay (approx) | `d = C(1−λ)²/[2(1−λX)] + X²/[2q(1−X)]` | Wait per piece; explodes as X→1 |

## Grid CO₂e intensity (order-of-magnitude; fetch live for real claims)

| Grid context | gCO₂e/kWh (approx) | Use |
|---|---|---|
| Low-carbon (hydro/nuclear heavy) | ~30–100 | Best case for electric firing |
| Mixed grid | ~250–450 | Typical |
| Coal-heavy / peaker | ~600–900 | Electric firing footprint high; off-peak/gas may win |

Always state the factor and source used; fetch a current value via a grid-carbon API for any published number.

## Upstream catalogues & sources

- **Orton Ceramic** — https://www.ortonceramic.com/ — cones, firing references.
- **Digitalfire** — https://digitalfire.com/ — glaze/material database, food-safety, firing chemistry.
- **Highway Capacity Manual (TRB)** — https://www.trb.org/ — saturation flow, delay, LOS.
- **ISO 14040/14044** — https://www.iso.org/standard/37456.html — LCA framework.
- **OSHA silica** — https://www.osha.gov/silica-crystalline — PEL and controls.
- **ASTM C738 / C895** — leachable-metals test methods for glazed ceramic surfaces.
