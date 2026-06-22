# /joint-repair-spec — Repair Specification for a Graded Joint

Produce an actionable repair specification (method, adhesive, reinforcement, clamp schedule, acceptance check) for a joint that `/joint-integrity-grade` dispositioned as re-glue / reinforce / replace — within the conservation constraints of the piece.

## Inputs

- The joint ID, type, and its grade/disposition (C re-glue / D reinforce / F replace).
- Wood species (for adhesive and clamp-pressure choice) and current MC (must be in the glue-up window — confirm via `/moisture-spc`).
- Conservation status (antique/significant ⇒ reversible adhesives, repair-before-replace) and load context (structural seat joint vs. decorative).

## Steps

1. Restate the disposition and the **ethics constraint** (reversible-only for conservation pieces; retain original material).
2. Select the **adhesive** from `context/references.md` (hot/liquid hide for conservation; PVA for utility; epoxy only as documented last resort) and justify the choice against reversibility.
3. Specify **surface prep** (remove old crystallized hide glue, dry-fit, verify shoulder seating) and the **reinforcement** if grade D/F (new hardwood corner block + screws, fluted re-dowel, hidden spline, documented butterfly key).
4. Define the **clamp schedule**: pressure appropriate to species, clamp time, and full-cure time before load (per adhesive).
5. Define the **acceptance check** — the post-repair measurement that closes the loop (gap re-measured, racking re-tested, fed back to `/control-chart`).

## Output

A repair spec sheet: disposition, adhesive + justification, prep steps, reinforcement, clamp schedule, cure time, and the acceptance check with target tolerance. Save to `outputs/<frame-id>-<joint-id>-repair-spec.md`.

## Notes

- Confirm MC is in the glue-up window before specifying any adhesive — a perfect spec on off-window wood reopens.
- Repair-before-replace: a member is only specced for replacement (F) with explicit justification that the original is unsalvageable; the removed original is documented and retained.
- Close the loop — a repair without a post-repair acceptance measurement never reaches the control chart and the process never learns.
