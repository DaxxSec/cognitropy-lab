# /layout-contour-lines

Lay out contour or key lines across a slope from a DEM or field survey, and decide on-contour vs graded alignment with a safe channel grade.

## Inputs

- DEM/survey data or a slope profile (station → elevation), and field boundaries.
- Target practice (contour cultivation, contour bunds, key lines, or terrace/waterway alignments).
- Desired channel grade for graded alignments (default range 0.1–0.6%), or "level" for storage-type.
- Available stable outlet location(s).

## Steps

1. Read `context/concepts.md` "Contour-based support practices".
2. Derive the slope and aspect from the DEM; identify the drainage divides and concentrated-flow paths (these constrain where alignments can safely terminate).
3. Choose **on-contour (level)** vs **graded**: level for storage/infiltration on permeable soils in humid–subhumid settings; graded to carry water at a non-erosive grade to a stable outlet.
4. Generate contour/key lines at the target interval (use `/design-terrace-interval` output if terracing). For graded lines, set a constant safe grade and verify grade continuity (no reverse or flat spots).
5. Check the critical contour row length for contour cultivation — flag where flow would overtop the ridge before reaching the outlet.
6. Confirm every graded alignment terminates at a designed stable outlet, never on bare slope.

## Output

`outputs/layout/contour-lines-<field>-YYYY-MM-DD.md` (+ optional GeoJSON/CSV of alignment vertices) — alignment list with grades, on-contour vs graded decision and rationale, outlet assignments, and flagged critical-length or grade-continuity issues.

## Notes

- Reverse grades and flat spots cause ponding and breaching — survey-verify grade continuity before construction.
- Key-line patterning spreads water across ridges; pair with `/budget-infiltration` to confirm ridges can absorb the spread flow.
- Hand layout to `/design-terrace-interval` and `/size-grassed-waterway` for the structures these lines define.
