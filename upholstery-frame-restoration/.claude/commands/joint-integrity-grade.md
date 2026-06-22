# /joint-integrity-grade — Grade Joints & Assign Repair Disposition

Grade each structural joint of a frame for gap, racking, and glue-line condition, then assign a disposition (sound / re-glue / reinforce / replace) consistent with conservation ethics.

## Inputs

- Joint inventory for the frame (each mortise-tenon, dowel joint, corner block, lap/bridle, rail).
- Per-joint observations: visible glue-line gap (mm), movement under hand load (none/slight/rocking), splits/checks, fastener state (tight/stripped/missing), corner-block attachment.
- Racking deflection of the seat box under a defined reference side-load, if measured.
- Conservation status of the piece (antique/significant vs. utility) and known wood species.

## Steps

1. Score each joint on three axes — **gap**, **movement/racking**, **member condition** — each green/amber/red against the bands in `context/references.md`.
2. Roll the three axes into a joint grade: **A (sound)**, **B (serviceable, monitor)**, **C (re-glue)**, **D (reinforce)**, **F (replace member)**.
3. Map grade → disposition under the **repair-before-replace** rule: prefer clean-and-re-glue (C) and reinforcement (D) over member replacement (F); F requires explicit justification that the original is unsalvageable.
4. For each C/D/F joint, hand off to `/joint-repair-spec` for the method, adhesive, and clamp schedule.
5. Tally the defect causes (loose corner block, hide-glue release, dowel rock, rail split…) and feed `/defect-pareto` if grading a batch.

## Output

A joint grade matrix: joint ID, three-axis scores, overall grade, disposition, and conservation note. A seat-box racking summary. Save to `outputs/<frame-id>-joint-grades.md`.

## Notes

- Corner blocks are the dominant anti-racking element — a detached block usually outranks a small joint gap as the real cause of "wobble."
- Reversibility gates adhesive choice at disposition time, not after; never spec an irreversible epoxy on a conservation piece to hit a grade.
- "Rocking" under hand load is a moment-stiffness failure even when the glue line looks closed — grade on behavior, not appearance alone.
