# /diagnose-roast-curve

Diagnose a logged roast curve for the classic defects — crash, flick, stall/bake, tipping, scorching — and assess RoR smoothness and development-time ratio.

## Inputs

- A roast log (Artisan `.alog`/CSV, Cropster/RoastLog export, or hand-logged markers): BT (and ET if available) vs time, plus charge/TP/dry-end/FC/drop.
- The intended profile or target level (so deviations can be judged against intent).
- Cupping notes for the batch, if available (baked, ashy, papery, sour, tippy).

## Steps

1. Read `context/workflows.md` (Workflow B diagnosis tree) and `context/concepts.md` ("RoR, crash & flick", "Roast defects").
2. Reconstruct the BT curve and compute **RoR** (ΔBT/Δtime). Plot/inspect the RoR shape: does it peak after TP and decline smoothly?
3. Scan for signatures: RoR diving negative near FC (**crash**); RoR rising again after a dip (**flick**); RoR → 0 before drop (**stall/bake**).
4. Compute phase splits and **DTR**; compare to the target band. Flag too-fast early RoR (tipping risk) or hot charge (scorch risk) from the curve shape and any bean evidence.
5. Correlate each signature with the cup notes; rank defects by confidence and impact.
6. Recommend the specific fix (which lever, when) and whether it's an execution issue (this batch) or a profile-design issue (re-dial in Workflow A).

## Output

`outputs/diagnostics/<batch-id>-YYYY-MM-DD.md` — the RoR assessment, a ranked list of detected defects with evidence (curve + cup), DTR vs target, and concrete corrective actions tagged execution-vs-design.

## Notes

- A crash and a controlled low-RoR finish look similar on BT but differ on RoR and cup — judge on RoR, not BT flatness alone.
- Same color, different development is common: a "fine looking" drop temp with a stalled RoR still bakes. Trust the RoR + DTR + cup over color.
- If multiple batches of one lot show the same defect, suspect green quality (see `/track-green-lot` and Workflow D), not just execution.
