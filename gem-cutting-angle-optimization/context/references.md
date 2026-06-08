# Gem Cutting Angle Optimization — Reference Tables

Compact lookup data the agent grep's mid-task. Defer to GemCad designs and the IGS encyclopedia for fuller specs.

## Refractive index, critical angle, dispersion (common faceting materials)

Critical angle = arcsin(1/RI). Pavilion main is a typical starting value, not a law.

| Material | RI | Crit. angle | Dispersion | Mohs | Typ. pavilion main |
|---|---|---|---|---|---|
| Diamond | 2.417 | 24.4° | 0.044 | 10 | 40.75° |
| Moissanite | 2.65 | 22.2° | 0.104 | 9.25 | ~40° |
| Cubic zirconia | 2.15 | 27.7° | 0.060 | 8.5 | ~40° |
| Zircon | 1.96 | 30.7° | 0.039 | 7.5 | ~40° |
| Corundum (sapphire/ruby) | 1.762 | 34.6° | 0.018 | 9 | 41–43° |
| Garnet (spessartine/almandine) | 1.79 | 33.9° | 0.027 | 7–7.5 | ~41° |
| Spinel | 1.718 | 35.6° | 0.020 | 8 | ~42° |
| Peridot | 1.67 | 36.8° | 0.020 | 6.5–7 | ~43° |
| Topaz | 1.62 | 38.2° | 0.014 | 8 | ~43° |
| Tourmaline | 1.62 | 38.2° | 0.017 | 7–7.5 | ~43° |
| Beryl (emerald/aqua) | 1.577 | 39.3° | 0.014 | 7.5–8 | ~43° |
| Quartz (amethyst/citrine) | 1.544 | 40.3° | 0.013 | 7 | ~43° |
| Fluorite | 1.434 | 44.2° | 0.007 | 4 | ~45°+ |

Rule of thumb: pavilion main ≈ critical angle + 2–4°, then optimize. Lower RI → steeper pavilion, narrower windowing margin.

## GIA-style round-brilliant proportion targets (for `/cut-grade-check`)

| Parameter | Excellent band |
|---|---|
| Table % | 53–58% |
| Crown angle | 34.0–35.0° |
| Pavilion angle | 40.6–41.0° |
| Total depth % | 59.0–62.5% |
| Girdle | thin → slightly thick |
| Culet | none / very small |

Windowing risk rises as pavilion drops below ~40.5°; fish-eye risk rises with shallow pavilion + table > 60%; nailhead rises with pavilion > 42°.

## Index gear quick reference

| Gear | Splits | Common designs |
|---|---|---|
| 96 | 96 | most published designs; divisible by 2/3/4/6/8/12 |
| 80 | 80 | older Graves designs |
| 64 | 64 | some standard rounds |
| 32 | 32 | simple cuts, ovals |

A design is a list of (angle, index) pairs; the protractor sets angle, the index wheel sets rotation.

## Lap grit progression (coarse → polish)

| Stage | Grit (mesh) | Micron | Use |
|---|---|---|---|
| Rough / preform | 80–260 | ~180–60 | shaping, fast removal |
| Coarse cut | 600 | ~25 | pavilion/crown roughing |
| Fine cut | 1200 | ~14 | pre-polish geometry |
| Pre-polish | 3000 | ~6 | meet-point refinement |
| Polish | 8000–14000 | ~3–1.5 | first polish |
| Final polish | 50000–100000 | ~0.5–0.25 | mirror finish |

Lap types: sintered/bonded diamond (cutting), ceramic, tin/lead "Batt" or BATT laps, Lucite, Corian, ZAM/cerium oxide on tin (polish). Harder stones tolerate longer dwell; soft stones glaze fine grits fast.

## Condition-indicator thresholds (for PdM commands)

Tune to your own machine baseline; these are working defaults for fine meet-point faceting.

| Indicator | How measured | Green | Watch (P-point) | Limit (F) |
|---|---|---|---|---|
| Spindle/quill TIR runout | dial indicator on dop | < 8 µm | 8–20 µm | > 20 µm (~±0.1° at typical dop length) |
| Master-lap flatness deviation | dial sweep / optical flat | < 12 µm | 12–25 µm | > 25 µm |
| Vibration RMS (motor/bearing) | accelerometer / phone app | < baseline ×1.5 | ×1.5–×3 | > ×3 |
| Cut-rate decay (lap glazing) | time-to-flat per facet | < baseline ×1.3 | ×1.3–×2 | > ×2 → dress/recharge |
| Index repeatability | re-index same facet, measure step | < 0.05° | 0.05–0.10° | > 0.10° |

## Angle-error budget (root-sum-square)

```
σ_total = sqrt(σ_spindle² + σ_lap² + σ_index² + σ_operator²)
```

Target σ_total ≤ design tolerance (typ. ±0.1–0.2°). If any single source nears its limit row above, it dominates the RSS and the budget is effectively blown.

## Upstream catalogues & tools

- **Facetdiagrams.org** — https://facetdiagrams.org/ — large free GemCad design library, searchable by material/angle.
- **United States Faceters Guild** — https://usfacetersguild.org/ — designs, tangent-ratio articles, competition rules.
- **International Gem Society (IGS)** — https://www.gemsociety.org/ — gem encyclopedia, RI and faceting reference.
- **GemCad / GemRay** — http://www.gemcad.com/ — design CAD + ray-trace light-return modeling.
- **The Rock Shop / Bob's Rock Shop tangent-ratio notes** — classic write-ups of the Strickland tangent-ratio method.
- **Reliabilityweb** — https://reliabilityweb.com/ — P-F curve, RUL, condition-based maintenance background.
