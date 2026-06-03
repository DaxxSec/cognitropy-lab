# /diagnose-crumb

Read a baked cross-section like a page of script — identify lamination faults from the visible crumb evidence before inferring any cause.

## Inputs

- A clear photo of the cross-section, or a careful written description (layer separation, cell shape/size, colour, feet/lift, base).
- The expected signature from the codex (what a correct bake should look like).

## Steps

1. Describe the evidence **objectively first**: layer discreteness, honeycomb regularity, any grey/leaden zones, base density, lift/feet, fat pooling. (The "diplomatic reading" — describe before judging.)
2. Match the evidence to the **defect taxonomy** in `context/references.md` (welding, grey streaks, gum line, bleed, weak feet, tunnelling).
3. Name the fault(s) and rate **severity** (cosmetic / sellable-with-note / reject).
4. State the **diagnostic confidence** and what additional evidence (e.g. the run transcription) would raise it.
5. Hand off to `/defect-stratigraphy` for root-cause if the fault is structural.

## Output

A diagnosis at `outputs/diagnosis-<product>-<date>.md`: objective reading, named fault(s) with severity, confidence, and recommended next step.

## Notes

- Resist jumping to cause from a single feature — a gum line plus welding tells a different story than either alone.
- A photo beats prose; if only prose is available, ask for the base, the feet, and one interior cell explicitly.
