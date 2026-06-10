# /track-green-lot

Register a green coffee lot with full origin-chain traceability and inventory status, and link it both ways to the roast batches it produces — the spine of the supply-chain record.

## Inputs

- Origin chain: country → region → farm / washing station / cooperative → mill/exporter → importer. ICO mark / lot ID where available.
- Quality + spec: processing method, screen size, **moisture % and water activity**, density, certifications (Organic / Fairtrade / Rainforest Alliance), crop year.
- Commercial: landed cost basis (FOB + freight + spread, or C-market + differential), arrival date, quantity received, storage type.
- For linking: a batch ID + profile version when the lot is roasted (forward link), or a SKU/batch when tracing back (reverse link).

## Steps

1. Read `context/concepts.md` ("Green coffee fundamentals", "Inventory & supply-chain model").
2. Create/locate the lot record; capture the full origin chain and ICO mark. Flag certifications for segregated handling.
3. Record quality spec; **flag aw > ~0.65** (mold/OTA risk) or moisture out of ~10–12% for QC before roasting.
4. Set inventory fields: on-hand quantity, arrival date, **crop year** (the staleness clock), storage, and landed cost basis.
5. Maintain the genealogy: append each roast batch (batch ID, profile version, charge weight) to the lot (forward); support reverse lookup SKU → batch → profile → lot for recalls.
6. Save; surface staleness (approaching past-crop) and any cert/quality flags for `/plan-green-reorder` and Workflow D.

## Output

`outputs/inventory/lots/<lot-id>.md` — the lot's origin chain, ICO mark, quality spec (moisture/aw/screen/cert/crop year), commercial basis, on-hand quantity, storage, and the bidirectional batch genealogy. The authoritative traceability record for the lot.

## Notes

- Keep certified lots **segregated** with a documented mass-balance — a re-bag or blend that breaks this voids the claim.
- Crop year is an inventory clock, not just provenance: a lot can be "in stock" and still effectively stale.
- For blends, the lot link is per-component — see `/build-blend-recipe`; never let a blend dissolve component genealogy.
