# Optical Material Cost & Availability Hints

Rough, relative guidance. Always confirm with current vendor quotes (Schott, Ohara, Hoya, CDGM, II-VI, Corning).

## Visible (Schott / Ohara names)
| Material | Relative cost | Notes |
|---|---|---|
| N-BK7 | 1× (baseline) | Workhorse crown |
| N-SF11 | 2× | Dense flint |
| N-LAK22 | 4× | Dense crown, low dispersion |
| N-PSK53A | 6× | Ultra-low dispersion, striae-prone |
| CaF₂ | 8× | Apo, UV-transparent |
| Fused Silica | 3× | UV+, low CTE |

## IR
| Material | Relative cost | Notes |
|---|---|---|
| Germanium | 30–100× VIS | LWIR, absorbs > 100 °C |
| Silicon | 5–10× | MWIR + NIR |
| ZnSe | 20–40× | Broad IR, toxic dust |
| ZnS | 10–20× | Broad IR, tougher than ZnSe |
| Chalcogenide (GASIR, AMTIR) | 15–25× | Moldable, less brittle |

## Form Factor Cost Hints
- Aspheric glass: +3–5× over spherical
- Diffractive surface: +1–2× if replicated, +5–10× if directly cut
- Dia > 100 mm: availability drops sharply
- Ultra-tight λ/20 polishing: +5–20× over commercial λ/2

## Process Premiums
- Precision tolerance tier: +1.5–2× commercial
- High-precision tier: +4–10×
- Space-qualified testing: +2–3× plus schedule hit

## Rule of Thumb
- If you can hit spec with N-BK7 + N-SF2 (classic achromat pair), do it.
- Exotic materials should earn their place in a tradeoff documented in `work-log/`.
