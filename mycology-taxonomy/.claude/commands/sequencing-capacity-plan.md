# /sequencing-capacity-plan

Plan a sequencing run's batch and plate sizing so it meets the turnaround SLA at an acceptable per-unit cost, accounting for wait-to-fill effects.

## Inputs

- Plate format (96 / 384 well) and per-run setup cost (reagents, hands-on time, instrument time).
- Sequencing mode: Sanger (one marker per reaction) or amplicon/Illumina (multiplexed with indices).
- Arrival rate `λ` of sequence-ready specimens and the current sequencing backlog.
- Markers per specimen (e.g. ITS only vs ITS + secondary) and the turnaround SLA target.

## Steps

1. Read `context/concepts.md` "Batching" and `context/workflows.md` "Loop B, Step 3".
2. Compute per-unit cost vs batch size (setup cost amortised across the plate) and the reagent floor.
3. Model the **wait-to-fill** delay: at rate `λ`, mean wait for a batch of size B ≈ `(B−1)/(2λ)`. Larger batches lower cost but raise turnaround.
4. Find the batch size where wait-to-fill + run time stays within the SLA; identify the cost/turnaround crossover where running a partial plate is justified.
5. For amplicon runs, plan indexing/multiplexing capacity (how many specimens × markers fit per run) and library-prep throughput.
6. Recommend a run cadence (e.g. weekly plate vs fill-triggered) and the trigger rule.

## Output

- `outputs/capacity/sequencing-plan-<date>.md` — recommended batch size, run cadence, per-unit cost, expected wait-to-fill, SLA compliance, and the partial-plate decision rule.

## Notes

- Underfilled plates waste reagent budget; overfilled cadence blows turnaround — the plan is the balance point, not a maximum.
- If sequencing is the bottleneck stage from `/backlog-forecast`, batch sizing alone may not be enough; flag the need for added run frequency or capacity.
- Keep markers-per-specimen consistent with the tier plan from `/morphology-key` (hard taxa need secondary markers → fewer specimens per plate).
