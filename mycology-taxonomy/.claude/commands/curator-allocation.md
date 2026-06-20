# /curator-allocation

Allocate scarce expert-curator hours across taxonomic groups by difficulty-weighted demand and backlog, balancing utilization and holding a safety buffer.

## Inputs

- Roster of curators with hours available and their taxonomic-group expertise.
- Per-group demand (specimens queued) and **difficulty tier** (service-time weight) from the register.
- Current per-group backlog and target turnaround per tier.
- Arrival/service variability (for the safety-capacity buffer).

## Steps

1. Read `context/concepts.md` "Variability matters" and `context/workflows.md` "Loop B, Step 4".
2. Convert each group's demand to **difficulty-adjusted service time** (specimen count × tier weight from `context/references.md`) — not raw counts.
3. Compute per-group utilization `ρ` under the current allocation; find groups near saturation and groups idling.
4. Re-allocate curator hours to balance `ρ` across groups, respecting expertise constraints (a *Cortinarius* specialist can't be retasked to it by fiat).
5. Reserve a **safety-capacity buffer** sized by Kingman variability — never plan a key reviewer to 100%.
6. Output the assignment and the resulting per-group `ρ` and projected turnaround.

## Output

- `outputs/capacity/curator-allocation-<date>.md` — per-curator assignment, per-group ρ before/after, buffer reserved, and expected turnaround per group.

## Notes

- Allocating by specimen count instead of difficulty-weighted time systematically under-resources hard groups (*Cortinarius*, *Inocybe*, *Fusarium*).
- Expertise is a hard constraint, not a preference — don't balance utilization by assigning specimens to curators who can't determine them.
- Pair with `/backlog-forecast`: fix the bottleneck group first; subordinate the rest.
