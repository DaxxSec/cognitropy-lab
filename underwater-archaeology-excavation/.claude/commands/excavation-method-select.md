# /excavation-method-select

Choose a sediment-removal method by trading cost and speed against site disturbance and recovery quality.

## Inputs

- Sediment type and overburden depth (fine mud, sand, gravel, concretion).
- Find fragility and density in the deposit.
- Water depth (determines whether airlift's compressor is practical) and visibility.
- Required recording standard (photogrammetry, context recording) the method must not compromise.

## Steps

1. Read `context/references.md` ("Excavation Method Trade-off") and `context/concepts.md` ("Excavation & Sediment-Removal Methods").
2. Classify the task: bulk overburden removal vs. fine excavation near finds — they usually need *different* methods on the same site.
3. For bulk removal, compare airlift (needs compressor; good shallow) vs. water/induction dredge (depth-agnostic; standard at depth) on cost and control.
4. For fragile/find-rich layers, default to hand-fanning with grid control; reserve airlift/dredge for sterile overburden.
5. Specify **spoil handling**: screening for missed finds and deposition clear of the site.
6. Confirm the method preserves the stratigraphy and the recording standard — recording is the only offset for excavation's irreversibility.
7. Cost the method choice and feed it into `/dive-budget-model`.

## Output

`outputs/excavation-method-<site>-YYYY-MM-DD.md`: the method (or method mix) per deposit layer, the cost/disturbance/recovery-quality rationale, the spoil-handling plan, and the recording standard it supports.

## Notes

- One method rarely fits a whole site — pair a fast bulk method for overburden with a slow, controlled method near finds.
- Airlift needs a compressor and is awkward deep; the water dredge works at any depth and orientation — depth often decides for you.
- Speed bought by disturbing context is a false economy: the destroyed stratigraphy is the unrepeatable loss.
