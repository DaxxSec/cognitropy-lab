# HAZMAT Transportation Regulations — Reference Tables

Compact lookup data the agent grep's during a decode. Defer to the live regulation for authority and current values.

## Hazard classes & divisions

| Class | Hazard | Divisions | Uses PG? |
|-------|--------|-----------|----------|
| 1 | Explosives | 1.1 1.2 1.3 1.4 1.5 1.6 | No (compatibility group letter instead) |
| 2 | Gases | 2.1 flammable · 2.2 non-flam/non-tox · 2.3 toxic | No |
| 3 | Flammable liquids | — | I / II / III |
| 4 | Flammable solids | 4.1 solid · 4.2 spont. combustible · 4.3 dangerous when wet | I / II / III |
| 5 | Oxidizing | 5.1 oxidizer · 5.2 organic peroxide | 5.1: I/II/III · 5.2: no |
| 6 | Toxic / infectious | 6.1 toxic · 6.2 infectious | 6.1: I/II/III · 6.2: no |
| 7 | Radioactive | categories I / II / III-YELLOW | No (transport index) |
| 8 | Corrosive | — | I / II / III |
| 9 | Miscellaneous | incl. lithium batteries, env. hazardous | III or none |

## Packing groups

| PG | Degree of danger |
|----|------------------|
| I | Great danger |
| II | Medium danger |
| III | Minor danger |

## Common UN numbers (cribs for decode + transposition checks)

| UN | Proper Shipping Name | Class | PG | Note / look-alike |
|----|----------------------|-------|----|-------------------|
| UN 1203 | Gasoline / Petrol | 3 | II | ⚠ 1230 = Methanol |
| UN 1230 | Methanol | 3 (+6.1) | II | look-alike of 1203 |
| UN 1090 | Acetone | 3 | II | |
| UN 1993 | Flammable liquid, n.o.s. | 3 | I/II/III | generic — demands technical name |
| UN 1075 | Petroleum gases, liquefied (LPG) | 2.1 | — | |
| UN 1017 | Chlorine | 2.3 (+8) | — | TIH — green-page isolation |
| UN 1830 | Sulfuric acid (>51%) | 8 | II | ⚠ 1380 = pentaborane (very different) |
| UN 1789 | Hydrochloric acid | 8 | II/III | |
| UN 1845 | Carbon dioxide, solid (dry ice) | 9 | — | common undeclared (air) |
| UN 1950 | Aerosols | 2 | — | flammable/toxic per contents |
| UN 1266 | Perfumery products | 3 | II/III | nail polish, fragrances |
| UN 3077 | Env. hazardous substance, solid, n.o.s. | 9 | III | |
| UN 3082 | Env. hazardous substance, liquid, n.o.s. | 9 | III | |
| UN 3480 | Lithium ion batteries | 9 | — | undeclared #1 (power banks) |
| UN 3481 | Lithium ion batteries in / with equipment | 9 | — | |
| UN 3090 | Lithium metal batteries | 9 | — | |
| UN 0004 | Ammonium picrate, dry | 1.1D | — | explosive |

## Kemler / Hazard Identification Number (HIN) prefixes — ADR orange plate (upper number)

| Code pattern | Meaning |
|--------------|---------|
| First digit | Primary hazard (2 gas · 3 flammable liq · 4 flammable solid · 5 oxidizing · 6 toxic · 8 corrosive) |
| Doubled digit (e.g. 33, 88) | Intensified primary hazard |
| Second/third digit | Additional hazard (e.g. ...1 explosive · ...5 oxidizing · ...6 toxic · ...8 corrosive · ...9 risk of reaction) |
| Leading **X** | Reacts dangerously with water — no water |
| Examples | 33 = highly flammable liq (fp < 23 °C) · 30 = flammable liq · 668 = highly toxic + corrosive · X423 = flammable solid, water-reactive |

## Common-goods → undeclared-DG crib list

| Plain-language description | Likely UN / class | Watch for |
|----------------------------|-------------------|-----------|
| Power bank / portable charger | UN 3480 / Class 9 | Air DG handling required |
| Laptop / phone (with battery) | UN 3481 / Class 9 | "packed with equipment" |
| Aerosol / spray can | UN 1950 / Class 2 | flammable propellant |
| Perfume / nail polish | UN 1266 / Class 3 | flammable solvent |
| Pool shock / chlorine tabs | Class 5.1 oxidizer | segregation from organics |
| Dry ice / "keep frozen" | UN 1845 / Class 9 | asphyxiant; air limits |
| Paint / thinner / adhesive | UN 1263 / Class 3 | flammable |
| Lighter / fuel cell | Class 2.1 | aircraft prohibited cases |
| Magnetized cargo | (air special) | magnetic field limits |

## Segregation (concept summary — verify against the modal table)

- **IMDG** uses segregation codes **1–4**: *away from* → *separated from* → *separated by a complete compartment/hold* → *separated longitudinally by an intervening compartment/hold*.
- **HMR (road)** uses the **§177.848 segregation table** ("X" = may not be loaded/stored together; numbered notes for conditions).
- Classic conflicts: oxidizers (5.1) vs flammables (3/4) · acids (8) vs cyanides/sulfides (6.1, evolve toxic gas) · water-reactives (4.3) vs anything wet.

## ERG structure (Emergency Response Guidebook)

- **Yellow pages** — indexed by UN number → guide number.
- **Blue pages** — indexed by material name → guide number.
- **Orange pages** — the numbered response guides (e.g. Guide 128 flammable liquids non-polar).
- **Green pages** — initial isolation & protective-action distances for TIH and water-reactive materials.

## Upstream catalogues

- **eCFR Title 49 (HMR)** — https://www.ecfr.gov/current/title-49 — §172.101 Hazardous Materials Table.
- **PHMSA Hazmat** — https://www.phmsa.dot.gov/hazmat — US guidance, special permits, incident data.
- **ERG** — https://www.phmsa.dot.gov/hazmat/erg/emergency-response-guidebook-erg — current edition + app.
- **UN Model Regulations (Orange Book)** — https://unece.org/transport/dangerous-goods/about-recommendations-transport-dangerous-goods-model-regulations
- **ADR** — https://unece.org/about-adr — road, Kemler codes.
- **IMDG Code (IMO)** — https://www.imo.org/en/OurWork/Safety/Pages/DangerousGoods-default.aspx — sea, segregation table.
- **IATA DGR** — https://www.iata.org/en/programs/cargo/dgr/ — air, lithium battery rules.
- **CVSA inspection program** — https://www.cvsa.org/inspections/inspections/ — standardized inspection levels.
- **ISO 6346 container check digit** — https://en.wikipedia.org/wiki/ISO_6346 — arithmetic validation for container numbers.

## ISO 6346 container number check-digit (for `/transposition-check`)

Format: 4 letters (3 owner + category U/J/Z) + 6 digits + 1 check digit. Letters map A=10…Z=38 (skipping multiples of 11); each of the 10 positions is weighted by 2^position (1,2,4,…,512); sum mod 11 (a result of 10 → 0) gives the check digit. A mismatch = a transcription/transposition error in the container number.
