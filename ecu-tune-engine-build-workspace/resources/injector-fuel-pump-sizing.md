# Injector & Fuel Pump Sizing Reference

Use this guide to check if your current fuel system is adequate for your power goals, or to size new injectors and a fuel pump for a build.

---

## Injector Sizing Formula

The fundamental formula for required injector flow rate:

```
Required Injector Size (cc/min) = (HP × BSFC) / (Number of Cylinders × Duty Cycle)
```

**Where:**
- **HP** = target wheel horsepower (add ~15–20% for drivetrain loss to get crank HP)
- **BSFC** = Brake Specific Fuel Consumption
  - Naturally aspirated gasoline: ~0.45–0.50
  - Turbocharged gasoline: ~0.50–0.55
  - Turbocharged E30: ~0.60–0.65
  - Turbocharged E85: ~0.65–0.75
- **Duty Cycle** = recommended maximum 0.80 (80%) — leave headroom

### Example Calculation
Target: 400 WHP turbocharged on 93 octane | 4 cylinders | 80% duty

```
Crank HP estimate = 400 × 1.18 = 472 HP
Required total flow = 472 × 0.52 = 245 lb/hr
Per injector = 245 / 4 = 61.3 lb/hr
Convert to cc/min = 61.3 × 10.5 = ~644 cc/min
```

Result: 660cc injectors would be the minimum; 750cc–850cc gives comfortable headroom.

---

## Injector Quick-Sizing Table (Turbocharged Gasoline, 80% Duty)

| Power Goal (WHP) | 4-Cyl Required (cc/min) | 4-Cyl Recommended | 6-Cyl Required | Notes |
|------------------|------------------------|-------------------|----------------|-------|
| 250 WHP | ~430 cc | 440–550 cc | ~290 cc ea | Stock-ish range |
| 300 WHP | ~510 cc | 550–660 cc | ~340 cc ea | |
| 350 WHP | ~600 cc | 660–750 cc | ~400 cc ea | |
| 400 WHP | ~685 cc | 750–850 cc | ~455 cc ea | |
| 450 WHP | ~770 cc | 850–1000 cc | ~515 cc ea | |
| 500 WHP | ~855 cc | 1000 cc | ~570 cc ea | |
| 600 WHP | ~1025 cc | 1200–1650 cc | ~685 cc ea | Port injection limit territory |
| 700 WHP+ | 1200+ cc | 2000cc or dual inject | 800+ cc ea | Consider dual injection |

> Add ~30–35% to required cc/min for E30 blends; add ~65–70% for E85.

---

## Common Injector Sizes Reference

| cc/min | lb/hr | Common Applications |
|--------|-------|---------------------|
| 370 cc | 35 lb/hr | OEM small displacement NA |
| 440 cc | 42 lb/hr | OEM subaru WRX / common upgrade starting point |
| 550 cc | 52 lb/hr | Common street tune injector |
| 660 cc | 63 lb/hr | Popular upgrade for 300–400 WHP |
| 750 cc | 71 lb/hr | Mid-range performance injector |
| 850 cc | 80 lb/hr | Popular for 400–500 WHP |
| 1000 cc | 95 lb/hr | High-flow single-stage; common EVO/STI upgrade |
| 1200 cc | 114 lb/hr | High-power stage |
| 1600 cc | 152 lb/hr | Big single setups |
| 2150 cc | 205 lb/hr | Full race / top-end builds |

---

## Injector Impedance: High vs. Low

| Type | Resistance | Notes |
|------|------------|-------|
| High impedance (saturated) | 12–16 Ω | Works directly with OEM ECU; most OEM and upgrade injectors |
| Low impedance (peak & hold) | 2–3 Ω | Requires peak & hold driver; common in OEM high-flow applications |

> ⚠️ Running low-impedance injectors without a peak & hold driver on a saturated-drive ECU will destroy the injectors and may damage the ECU. Verify before installing.

---

## Fuel Pump Sizing

### Required Flow Rate Formula
```
Required fuel pump flow (lb/hr) = (HP × BSFC) / 0.6 (efficiency factor)
```

### Pump Sizing Table (In-Tank, Gasoline, at operating fuel pressure)

| Power Goal (WHP) | Min Pump Flow | Recommended Pump | Notes |
|------------------|---------------|------------------|-------|
| Up to 300 WHP | ~190 lb/hr | OEM pump or Walbro 255 | Many OEM pumps fine here |
| 300–400 WHP | ~250 lb/hr | Walbro 255 / AEM 340 | Walbro 255 is a common upgrade |
| 400–500 WHP | ~320 lb/hr | AEM 340 / Bosch 044 ext | |
| 500–600 WHP | ~400 lb/hr | Walbro 450 / Deatschwerks 300C | |
| 600–700 WHP | ~490 lb/hr | DW400 / Aeromotive Stealth 340 | |
| 700–800 WHP | ~570 lb/hr | Dual-pump setup recommended | |
| 800 WHP+ | 650+ lb/hr | Dual pump or external Bosch 044 | |

> Note: Pump flow ratings are typically at 43 psi. At elevated fuel pressures (many boosted setups run 58+ psi rising rate), actual pump output is significantly lower. Derate by ~15–25% for boosted applications with rising rate FPR.

> For E85: Multiply required flow by ~1.35 to account for increased volume needed.

---

## Signs Your Fuel System is the Limiting Factor

1. **Lean AFR at high RPM / high boost** — injectors running out of capacity
2. **Injector duty cycle above 85%** in datalogs
3. **Fuel pressure drop at WOT** — pump can't keep up
4. **Power falls off at top of RPM range** despite boost being maintained
5. **Tune requires excessive enrichment** at high RPM to prevent lean out — may indicate pump or injector limit

---

## Fuel System Upgrade Order (Common Path)

1. **Upgrade injectors first** (if undersized for target power)
2. **Upgrade fuel pump** (if duty cycle is high or pressure drops under load)
3. **Upgrade fuel pressure regulator** (if running rising-rate FPR or standalone)
4. **Upgrade fuel lines** (only needed above ~600 WHP on most setups)
5. **Consider dual-pump / surge tank** (above ~700–800 WHP or E85 at lower power levels)

Always retune after any fuel system change.
