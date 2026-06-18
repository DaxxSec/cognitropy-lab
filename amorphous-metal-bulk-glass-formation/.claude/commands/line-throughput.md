# /line-throughput

Build a capacity / bottleneck model of the casting line (melt → flux → cast → quench → demold → TPF → QA) and name the binding constraint — which may be a machine *or* the crystallization clock.

## Inputs

- Per-station cycle times and station counts for the line.
- First-pass yield per stage (from `/crystallization-yield`) and any rework path.
- Demand target (parts/period) and available run time.
- Whether any stage is kinetically bounded (TPF window from `/tpf-window`, quench from `/cooling-budget`).

## Steps

1. Read `context/workflows.md` Workflow 4 (TOC five focusing steps) and `references.md` for the capacity formulas.
2. Compute each station's **effective rate** = stations × yield / cycle-time. The minimum over stations is the **bottleneck throughput**.
3. Flag whether the bottleneck is a **machine** (press, furnace, demold) or the **crystallization clock** (TPF window / quench margin) — the distinctive BMG case, where no machine speed-up helps.
4. Apply **Little's Law** (WIP = throughput × flow-time) to size buffers so the constraint never starves or blocks.
5. Compute **OEE** (Availability × Performance × Quality), with Quality = first-pass amorphous yield, and a **capacity cushion** vs demand.
6. Recommend the next move per TOC: exploit → subordinate → elevate the constraint; predict where the bottleneck migrates after elevation (often QA).

## Output

`outputs/line-throughput-YYYY-MM-DD.md`: per-station effective rates, the bottleneck station and its type (machine vs kinetic), Little's-Law WIP/buffer sizing, OEE, capacity cushion vs demand, and the prioritised TOC action. Cross-link to `/product-mix-plan`.

## Notes

- If the constraint is the crystallization clock, the levers are metallurgical (lower Tl, widen ΔTx, raise cooling rate, flux for oxygen) — escalate to `/gfa-assess` / `/melt-flux-spec`, not to buying a faster press.
- Don't let QA quietly become the bottleneck — if every part needs DSC/XRD, the inspection queue can dominate; size it with `/amorphicity-qa`.
- Yield enters twice: as the Quality term in OEE and as the multiplier in effective rate. Keep the definition consistent and stated.
