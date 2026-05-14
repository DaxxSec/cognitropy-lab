# /restraint-class-decide

Walk the `R-*` decision tree (`context/workflows.md` §2) to select the **minimum** restraint class for a train configuration.

## Inputs

- `ride_name` — for the audit trail.
- `inversions` — list of inversion elements (cobra-roll, vertical-loop, zero-g-roll counts as `false` here — it's not an inversion in the restraint sense because rider doesn't hang from the harness; track manuals are authoritative).
- `neg_z_floor` — minimum (most negative) -z value across the ride, in g, with the source segment id.
- `lateral_peak` — peak |ay| across the ride, in g, with source segment.
- `launch_peak` — peak +x (forward) if a launch exists, else null.

## Steps

1. Confirm inputs at `R-0`. If any required input is missing, abort and request it.
2. Branch at `R-1` — inversions present?
3. If yes, walk `R-3`: soft-vest vs OTSR fixed-yoke vs individual-hydraulic, based on lateral sustained and launch peak.
4. If no inversions, walk `R-2` to select a candidate based on `-z` floor.
5. Apply `R-4` to upgrade the candidate one tier if lateral peak ≥ 1.0g.
6. Emit `R-5` — the highest minimum class from the tree plus a one-line rationale per node visited.
7. Note operator override field — operator may specify a class above minimum (commercially common), but never below.
8. Persist the walk at `outputs/restraint-decisions/<ride_name>-<YYYYMMDD>.md`.

## Output

Markdown summary with:
- Selected minimum restraint class.
- Path through R-tree (R-1 → R-2 → R-4 or R-1 → R-3, with sub-node ids).
- Drivers: which input forced the class.
- Operator override (placeholder).

## Notes

- Restraint class is **global to the ride**, not per element. Run once per train config.
- A downgrade decision (e.g. OTSR → lap-bar) requires a documented walk attached to the change order — this command's output is that walk.
- ASTM F2291 §6 and the manufacturer's restraint manual are authoritative; the R-tree is a structured first pass.
- If `inversions` is empty but rider can be **uplifted** (-z < -1.0g) on a wing rider or floorless seat, treat as if inversion-present (riders rely on shoulder containment even without a full inversion).
