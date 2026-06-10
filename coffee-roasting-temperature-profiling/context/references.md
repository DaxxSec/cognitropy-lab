# Coffee Roasting Temperature Profiling — Reference Tables

Compact lookup data. All temperatures are **machine-relative ballparks** for orientation, not absolute set-points — calibrate per `/calibrate-roaster` and record your own machine's markers.

## Roast levels → Agtron / weight-loss (orientation)

| Level | Agtron Gourmet (≈) | Drop region | Typical weight loss | Common use |
|-------|--------------------|-------------|---------------------|------------|
| Light / Cinnamon | 90–80 | just into FC | 12–14% | filter, clarity-forward single origin |
| Medium / City | 75–65 | end of FC | 14–15% | filter / versatile |
| Medium-dark / Full City | 60–50 | into/near 2C | 15–17% | espresso, balance |
| Dark / Vienna | 50–40 | early 2C | 17–19% | dark espresso |
| Very dark / French | 40–30 | well into 2C | 19–22%+ | dark, heavy body |

Higher Agtron number = lighter roast. Color ≠ development — always pair with DTR.

## Roast phase markers (ballpark, machine-relative)

| Marker | BT region (°C) | BT region (°F) | Notes |
|--------|----------------|----------------|-------|
| Charge | 180–220 | 356–428 | depends on batch size / machine |
| Turning point (TP) | 80–100 | 176–212 | low point, ~1:00–1:30 |
| Dry end / yellowing | 150–160 | ~300–320 | end of drying phase |
| First crack (FC) | 196–205 | 385–401 | start of development |
| Second crack (2C) | 224–230 | 435–446 | dark roasts only |
| Drop | per level | per level | by BT + time-in-development |

## RoR / DTR targets (guidance)

| Quantity | Typical target | Notes |
|----------|----------------|-------|
| Total roast time | 8–14 min (drum) | shorter for some air roasters |
| RoR shape | peak after TP, **smooth decline** to drop | no crash, no flick |
| Development time | ~1:00–2:30 | absolute time in development |
| **DTR** (dev time / total time) | ~15–25% | Rao-style guidance; cup-confirm per coffee |

## Green coffee quality ranges

| Property | In-spec range | Flag |
|----------|---------------|------|
| Moisture content | ~10–12% | <9% brittle/flat; >12.5% instability |
| Water activity (aw) | ~0.50–0.60 | **> ~0.65–0.70 → mold / ochratoxin-A risk** |
| Screen size | SC 14–19 (1/64 in) | segregate mixed sizes for even roast |
| Crop year | current / new crop | past crop = fading; old crop = woody/baggy |

## Inventory & supply-chain formulas

| Formula | Definition |
|---------|------------|
| Roast loss % | (green − roasted) / green × 100 |
| Yield | roasted / green = 1 − loss |
| Green needed | roasted demand ÷ yield |
| Roasted unit cost | (green landed cost ÷ yield) + labor + packaging + overhead |
| Reorder point (ROP) | (avg demand × lead time) + safety stock |
| Safety stock | z × σ(demand over lead time) (service-level z) |
| Par level | target on-hand to cover cycle + buffer |
| EOQ | √(2 · D · S / H) (D=annual demand, S=order cost, H=holding cost) |
| Landed cost | FOB + freight + import/finance + spread |
| Arabica green price | ICE "C" (KC) futures + differential |

## Crop-year / market terminology

- **New / current crop** — most recent harvest; freshest, brightest.
- **Past crop** — prior year; fading acidity, drifting toward woody.
- **Old / mature crop** — older; baggy, flat; usually blend-only.
- **Differential** — premium/discount to the "C" for origin, quality, cert, prep.
- **FOB / FOT** — free on board / free on truck; common offer price points.
- **Spot vs forward** — buy-now vs contracted future delivery (price certainty vs flexibility).

## Standards, organizations & catalogues

- **Specialty Coffee Association (SCA)** — https://sca.coffee/research — cupping protocol, roast-color/Agtron standards, green grading & defect handbook, water-activity guidance.
- **International Coffee Organization (ICO)** — https://www.ico.org/ — indicator prices, ICO marks, trade stats.
- **ICE Coffee "C" Futures (KC)** — https://www.ice.com/products/15/Coffee-C-Futures — Arabica benchmark.
- **Agtron** — roast-color measurement (Gourmet scale, color tiles/discs).
- **CQI (Coffee Quality Institute)** — https://www.coffeeinstitute.org/ — Q grading, green standards.

## Roast-logging software

- **Artisan Roasterscope** — https://artisan-scope.org/ — free/open-source; RoR, markers, overlay/compare, `.alog` + CSV export.
- **Cropster** — https://www.cropster.com/ — commercial roast + inventory/QC platform.
- **RoastLog** — https://roastlog.com/ — commercial roast logging + profiles.

## Operating cheat-sheet

- Calibrate BT probe (ice point 0 °C / boiling ~100 °C at sea level, altitude-adjusted) before trusting cross-machine numbers.
- Always state whether a weight is **green** or **roasted**.
- FIFO + crop-year clock together prevent stale-green bakes.
- One golden profile per (SKU, lot, machine); version on any change.
