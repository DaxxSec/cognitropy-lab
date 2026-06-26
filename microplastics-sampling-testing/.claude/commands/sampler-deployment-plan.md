# /sampler-deployment-plan

Turn a targeting list into an executable campaign — the checkpoint-network design step. Decides where stations sit, how many replicates, what mesh/pore size each "checkpoint" screens at, and where the field blanks go.

## Inputs

- Targeting list from `/risk-target-sites` (sites + primary/control tags).
- Matrix and gear available (manta/neuston net, bulk-water filtration cascade, Niskin/Van Dorn, sediment grab/core, active air pump).
- Target lower size cutoff (drives mesh/pore selection — e.g. 333 µm net vs 20 µm cascade vs 1 µm for µ-Raman work).
- Logistics: vessel time, tide/flow windows, personnel.

## Steps

1. For each site, fix **station geometry**: surface vs depth strata, transect vs point, and replicate count (minimum triplicate at primary targets; pooled or single at controls is acceptable if justified).
2. Select the **screening aperture** per station: net mesh or filter pore size sets the smallest particle the station can catch. State the size class explicitly — counts are meaningless without it. Note the inherent false-negative: anything below the aperture is invisible.
3. Place **field blanks** like control lanes: at least one field blank per site or per day (whichever is more frequent), handled identically to a real sample but exposed only to ambient air and reagents. This is what later lets `/blank-audit` separate signal from your own contamination.
4. Estimate **throughput**: volume filtered or net-tow distance × stations × replicates vs available time. If throughput exceeds capacity, push the lowest-value stations back to controls or next campaign — do not silently reduce replicates at primary targets.
5. Set the **sample-volume floor** so the expected count clears the counting-uncertainty target (see `context/references.md` — Poisson n for a target relative error).
6. Emit a field checklist: gear, mesh sizes, blank schedule, volumes/tow lengths, custody seals to pre-stage, and the contamination-control kit.

## Output

A deployment plan under `outputs/campaigns/<campaign>.md`: per-station table (geometry, replicates, aperture/size class, volume), the field-blank schedule, throughput estimate vs budget, and the field checklist. Each planned sample gets a pre-assigned ID for `/custody-log`.
