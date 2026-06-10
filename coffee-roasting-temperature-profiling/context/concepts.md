# Coffee Roasting Temperature Profiling — Core Concepts

Background the agent reads before acting. Optimised for fast recall. The through-line is that a roast profile and the green-coffee inventory it consumes are **one traceable system**: a lot is bought, registered, roasted at a versioned profile, and converted to roasted inventory at a measured yield.

## The roast as three phases

A drum/air roast moves bean temperature (BT) up over 8–16 minutes, conventionally split into three phases by markers:

1. **Drying phase** — charge to "dry end" / yellowing (~150–160 °C BT, machine-relative). Free and bound moisture (green is ~10–12% water) evaporates; beans go green → yellow and smell grassy/bready. Endothermic; the bean absorbs energy without much color change.
2. **Maillard / browning phase** — dry end to first crack. Maillard reactions and Strecker degradation build melanoidins, color, and most aroma precursors; beans brown and the bready smell turns toasty. Sucrose caramelizes toward the end.
3. **Development phase** — first crack (FC) to drop. The exothermic FC pop marks rapid CO₂/steam release and structural fracture; flavors set, acidity drops, body builds. How long you stay here vs. total time is the **development-time ratio (DTR)**.

**Markers logged on every roast:** charge temp, **turning point** (TP — the low point where BT stops falling and starts rising, ~1:00–1:30 in), dry end / yellowing, **first crack** start, (optionally second crack), and **drop**. Times and the BT at each are the fingerprint of the roast.

## Temperature measurement, RoR, crash & flick

- **Bean temperature (BT)** vs **environmental temperature (ET / "air")**: BT comes from a probe in the bean mass, ET from a probe in the airflow/exhaust. Both are *machine-relative* — probe diameter, mass, and placement change the reading and the lag. Two roasters showing "200 °C at first crack" may differ by 10–20 °C in true bean temp.
- **Rate of Rise (RoR)** = ΔBT / Δtime (typically °C or °F per minute, or per 30 s). It is the *derivative* of the BT curve and the single most useful control signal. A healthy roast shows RoR peaking shortly after turning point, then **declining smoothly** to the drop.
- **Crash** — RoR drops abruptly (often diving negative) at/after first crack as the exothermic reaction and moisture release stall convective heating; correlated with baked, flat flavor.
- **Flick (or "flip")** — RoR turns back **up** after a crash, usually from an ill-timed heat increase; correlated with harsh, ashy notes.
- **Stall** — RoR approaches zero before the drop; BT flatlines and the roast "bakes." Distinct from a controlled low-RoR finish.
- **Baking** — too long, too flat through development (low/zero RoR); papery, dull, bread-like. A *time/RoR* defect, not a color defect.

## Heat-transfer levers

Drum roasters move heat by **conduction** (drum wall), **convection** (hot airflow), and **radiation**. The operator's controls:

- **Gas / burner** — sets the energy input; the primary RoR driver.
- **Airflow / fan / damper** — sets convective transfer and exhaust; more air = faster, more even heat and chaff clearance, but can scrub aromatics if excessive.
- **Drum speed** — sets bean agitation and conductive contact (machine-dependent).
- **Charge weight & charge temp** — batch size relative to roaster capacity changes thermal momentum; under/overloading distorts the curve.

## Roast degree & color (the inventory-facing "spec")

Roast level is the saleable spec and correlates (loosely) with weight loss:

- Measured by **Agtron Gourmet scale** (≈95 very light → 25 very dark; higher number = lighter) or SCA roast-color tiles, or by drop temperature + cupping.
- Common levels: Light / Cinnamon (~Agtron 90–80), Medium / City (~70–60), Medium-dark / Full City (~55–50), Dark / Vienna–French (~45–30).
- Color alone is not development — two beans at the same Agtron can be well-developed or baked. Always pair color with time-in-development / DTR.

## Roast defects (quality + traceability signals)

- **Tipping** — burnt black spots at the bean tips; too aggressive early RoR / too hot a charge.
- **Scorching / facing** — flat burnt faces from bean-on-drum contact; overloaded or too-hot drum at charge.
- **Baking / underdevelopment** — covered above; flat vs. sour-grassy respectively.
- **Quakers** — pale, under-developed beans from unripe/defective greens (a *green-quality* defect surfaced by roasting) — a signal to check the lot, not the profile.

## Green coffee fundamentals (the inventory unit)

- **Moisture content** — target ~10–12% at intake; too high = mold/instability, too low = brittle/flat.
- **Water activity (aw)** — free-water availability; stable storage ~0.50–0.60. **Above ~0.65–0.70 is a mold / ochratoxin-A risk** and a food-safety flag.
- **Density & screen size** — denser, higher-grown beans need more energy; screen size (1/64 in; SC 14–19) affects even heating. Sort/segregate by screen where possible.
- **Processing** — washed, natural, honey/pulped-natural; changes density, sugar, and ideal RoR/DTR.
- **Crop year** — *current/new crop* (this harvest), *past crop* (last year), *old crop* (older). Greens fade ("baggy," woody) with age; crop year is a **staleness clock** on inventory.
- **Storage** — jute/sisal (breathable), GrainPro/hermetic liners (moisture-stable), vacuum; conditions set how fast aw and freshness drift.

## Roast loss, yield, and the green→roasted conversion

- **Roast (weight) loss %** = (green weight − roasted weight) / green weight × 100. Sources: free-moisture loss + organic-matter pyrolysis (CO₂, volatiles).
- Typical ranges: light ~12–14%, medium ~14–16%, dark ~16–20%+ (machine- and green-dependent).
- **Yield** = roasted weight / green weight = 1 − loss. This is the **inventory conversion factor**: 100 kg green at 15% loss → 85 kg roasted.
- Roast loss is *both* a development signal (too low → likely underdeveloped; unusually high → likely too dark/over) *and* an inventory move (green decremented, roasted incremented at yield). It must reconcile against the ledger.

## Inventory & supply-chain model

- **Traceability hierarchy:** country → region → farm / washing station / cooperative → mill/exporter → importer → roaster → roasted lot/batch → SKU. **ICO marks** and lot IDs anchor the chain. Keep it unbroken — especially across blends.
- **Inventory control:** **FIFO** consumption (oldest in-spec green first); **par level** (target on-hand); **reorder point (ROP)** = lead-time demand + safety stock; **safety stock** buffers demand/lead-time variance; **EOQ** balances order vs holding cost. Green has a freshness clock, so "more stock" is not free.
- **Green market:** Arabica priced off **ICE "C" (KC) futures** + a **differential** (origin/quality/cert premium or discount); Robusta off its own contract. **Spot** vs **forward/contract** buying trades price certainty against flexibility. **Landed cost** = FOB + freight + import/finance + spread.
- **Roasted costing:** price on **roasted** weight. Roasted unit cost = (green landed cost / yield) + labor + packaging + overhead. Skipping the /yield step understates cost by the roast-loss %.

## Common Failure Modes

- **Comparing raw temps across uncalibrated machines** — "FC at 196 °C" is meaningless without the probe/calibration; profiles drift invisibly.
- **Crash-and-flick after first crack** — heat mismanaged into development; baked then ashy. The single most common curve defect.
- **Baking from a development stall** — RoR allowed to hit zero; flat, papery cup despite correct color.
- **Costing on green weight** — ignoring roast loss inflates apparent margin by ~12–20%.
- **Broken blend traceability** — a blend that dissolves component-lot genealogy can't substantiate origin/cert claims or support a targeted recall.
- **Stale green** — no crop-year clock + no FIFO → microlots quietly age past-crop and bake flat.
- **Color-as-development** — dropping by color tile alone; same Agtron, different development → different cup.

## Operating Constraints

- **Bean temperatures are machine-relative;** always record machine, probe, and calibration date. Reproducibility is defined against a calibrated reference, not absolute °C.
- **Food safety & labeling** — roast date, net weight, origin, decaf process per jurisdiction (US FDA/FALCPA, EU 1169/2011). Track moisture/aw; flag aw > ~0.65.
- **Certification chain-of-custody** — Organic/Fairtrade/Rainforest Alliance require segregated lots and mass-balance; claims must match the genealogy.
- **Roaster safety** — chaff/duct fire risk; this workspace plans curves and inventory, not fire-suppression or machine maintenance.
