# Coffee Roasting Temperature Profiling — Workflows and Methodology

Step-by-step procedures and decision trees. The technique woven through all of them is **inventory and supply-chain tracking**: profiles are versioned artifacts, batches are instances that consume a tracked green lot, and roasting is a green→roasted inventory move at a measured yield. `concepts.md` defines the terms; this file is what the agent *does*.

## Workflow A: New lot → dialed-in golden profile

**Goal:** Take a freshly received green lot to an approved, versioned production profile — with the lot tracked in inventory from intake.

### Steps
1. `/track-green-lot` at intake: record origin chain, ICO mark, certs, processing, screen size, **moisture % and water activity**, crop year, arrival date, and on-hand quantity. This opens the inventory record the profile will draw against.
2. `/calibrate-roaster` if the machine/probe hasn't been verified recently — without it, the curve isn't reproducible or cross-comparable.
3. Cup / assess the green; pick a target roast level and intent (filter vs espresso, single-origin clarity vs blend component).
4. `/design-roast-profile`: set charge weight & temp, target turning point, drying/Maillard/development phase splits, RoR shape, FC timing, and **DTR target** for the chosen level.
5. Sample-roast; `/diagnose-roast-curve` on the log; `/tune-rate-of-rise` to fix crash/flick/stall; iterate 2–4 batches.
6. `/calc-roast-loss` each iteration; confirm loss is consistent with the target level and reconciles to the green drawn.
7. Cup the candidates, approve one, **version it** (e.g. v1.0) as the golden profile for this SKU/lot, and save to `outputs/profiles/`.

### Decision Points
- If RoR **crashes** after FC → reduce/anticipate the heat cut earlier; do **not** add heat into the crash (causes flick). See Workflow B diagnosis tree.
- If cup is **flat/baked** but color is right → development stalled; raise development-phase RoR floor or shorten DTR.
- If beans **tip/scorch** early → charge temp too high or batch over capacity; lower charge temp / reduce batch size.
- If green **aw > ~0.65 or moisture unusually high/low** → flag for storage/QC before committing a production profile.

## Workflow B: Production run → reproducibility → inventory move

**Goal:** Run a golden profile in production, confirm the batch matches, and post the green→roasted inventory move.

### Steps
1. Confirm the lot to roast (FIFO: oldest in-spec, in-crop green first) and that on-hand covers the planned batches.
2. Roast to the golden profile; log charge weight, ambient, gas/airflow events, and all markers.
3. `/match-profile-batch`: score the batch's markers (TP, dry end, FC, drop, DTR) against the golden within tolerance.
4. `/calc-roast-loss`: weight-loss %, yield; compare to the profile's expected loss band.
5. Post inventory: decrement green by charge weight, increment roasted by drop weight (at yield), tag the batch with lot ID + profile version.
6. Out-of-tolerance? Quarantine, `/diagnose-roast-curve`, decide rework/blend-down/discard, and record the disposition against the lot.

### Diagnosis decision tree (from a logged curve)
- **RoR dives negative near FC, cup baked** → *crash*. Cut heat earlier and gentler; verify airflow not over-scrubbing.
- **RoR rises again after a dip, cup ashy/harsh** → *flick*. Remove the late heat bump; smooth the gas step.
- **RoR ≈ 0 before drop, cup papery/flat** → *stall/bake*. Raise development RoR floor or drop sooner.
- **Black tips / burnt faces** → *tipping/scorching*. Lower charge temp, reduce batch, check drum speed.
- **Markers fine but loss off-band** → check scale calibration and that the *right lot* (moisture!) was charged; high-moisture green loses more.

## Workflow C: Demand forecast → roast schedule → procurement

**Goal:** Turn roasted-SKU demand into a green-consumption plan and keep green on the shelf and in-crop.

### Steps
1. `/forecast-roast-schedule`: convert SKU demand (and blend recipes) into green demand per lot — remember to **gross up by 1/yield** (roasted demand ÷ yield = green needed).
2. Lay out the roast week/month as batches against roaster capacity; sequence by FIFO and by profile (group same-profile batches).
3. `/plan-green-reorder`: for each lot/origin compute lead-time demand, reorder point, par, and safety stock; flag lots projected to stock out **or** to cross into past-crop before consumption.
4. For flagged lots, decide procurement: spot vs forward, and how the **C-market + differential** moves landed cost.
5. Save the schedule + reorder plan to `outputs/`; re-run as sales actuals arrive.

### Decision Points
- Lot will **stock out before lead time** → reorder now (or expedite / substitute a comparable lot and re-dial via Workflow A).
- Lot will **go past-crop before consumed** → reduce future buys, push it into a blend, or accelerate its roast schedule.
- **C-market spiking / differential widening** → consider a forward contract to lock cost; note the price basis in the lot record.
- **Comparable green substituted** → never assume the old golden profile transfers; re-validate via `/match-profile-batch` and likely Workflow A.

## Workflow D: Quality complaint → recall traceback

**Goal:** From a roasted-SKU complaint, reconstruct the genealogy and scope the affected inventory tightly.

### Steps
1. Capture the SKU, roast date, and batch/lot ID from packaging.
2. `/track-green-lot` (reverse view): SKU/batch → profile version → green lot(s) → importer/exporter → farm/station.
3. `/match-profile-batch` + `/diagnose-roast-curve` on the implicated batch: was it in-tolerance? what defect (e.g. development stall)?
4. Scope: was it one batch (profile execution) or the whole lot (green quality, e.g. quakers/aw)? Pull the lot's other batches' match scores to bound it.
5. Decide recall scope, corrective action (re-dial profile, reject remaining green, re-train), and record the disposition in the lot/profile history.

### Decision Points
- Defect is **execution** (one batch out of tolerance) → scope to that batch/day; keep roasting the lot.
- Defect is **green** (multiple batches, quakers, off aw/moisture) → scope to the lot; quarantine remaining green and notify supplier.
- **Certification claim** affected → verify chain-of-custody mass-balance held; if broken, suspend the claim on affected SKUs.

## Methodology: the roast-profile lifecycle (versioned artifact)

1. **Design** — target curve from green + level (Workflow A.4).
2. **Sample & tune** — iterate to a smooth declining RoR and target DTR (A.5–6).
3. **Approve & version** — cup-approved → golden vN.n, tied to the lot/SKU (A.7).
4. **Produce** — run in production, every batch matched and reconciled (Workflow B).
5. **Monitor** — track batch match scores and loss over the lot's life (drift detection).
6. **Retire / re-dial** — on lot change, crop-year roll, or machine change, supersede with a new version; keep old versions for traceback.
