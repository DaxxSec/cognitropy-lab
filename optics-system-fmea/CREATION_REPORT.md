# Creation Report: optics-system-fmea

## Metadata

| Field | Value |
|---|---|
| Build Date | 2026-04-21 |
| Cognitropy Day | 27 |
| Primary Category | Physical Sciences |
| Primary Domain | Optics system design |
| Technique | Failure Mode and Effects Analysis (FMEA) |
| Crossover | No |
| Author | Claude Agent (Cognitropy Lab autonomous build) |

## Why This Workspace

Optics is a discipline where **small mechanical, thermal, or contamination sins produce catastrophic image-quality failures** — often months after deployment, when the system is already in the field, already in a customer's hand, or already in orbit. The conventional design flow (spec → first-order → optimize → tolerance → build) treats FMEA as a late-stage compliance artifact. This workspace inverts that: FMEA becomes the **loop-closing activity that runs alongside every design iteration**, so failure modes are identified while the cost of change is still cheap.

The technique pairing — "optics system design with FMEA" — also mirrors how aerospace and medical-device optics groups actually operate, where safety and reliability engineers sit in the design-review loop from day one.

## What Makes This Workspace Useful

1. **Claude forces a 3-candidate-minimum failure mode discussion** on every design proposal. This is a hard rule in `CLAUDE.md` — not optional.
2. **RPN scoring is standardized** per AIAG-VDA 2019 guidance, and any Severity=10 entry is auto-actioned regardless of occurrence/detection.
3. **Domain knowledge is pre-loaded** with optics equations, ISO 10110 drawing conventions, IEC 60825 laser classes, and standard aberration Zernike decompositions.
4. **Six slash commands** cover the real workflow: design → FMEA → tolerance → stray-light → thermal-vibe → (onboarding).
5. **Python-first** — recommended libraries (prysm, rayopt, poppy, opticspy) are free, scriptable, and good enough for 80% of first-pass trades without a Zemax seat.

## Technique Rationale: Why FMEA?

Cognitropy randomized "failure mode analysis" as today's technique. FMEA is the **risk-analysis method most tightly integrated with physical-system design** — more than FTA (fault tree analysis), which is top-down; more than HAZOP, which targets process plants; more than STPA, which targets software/control systems. FMEA maps 1:1 onto how an optical system physically fails: element-by-element, interface-by-interface, with an easy scoring rubric that keeps the conversation quantitative rather than vibes-based.

## Use-Case Coverage

- **Imaging**: visible cameras, UAV payloads, machine vision, endoscopes
- **Illumination**: structured light, LiDAR transmitters, microscopy köhler setups
- **Spectroscopy**: Raman, FTIR, spectrographs
- **Laser systems**: pump diodes, medical lasers, LIDAR
- **Fiber optics**: coupling, mode matching, connectorization
- **Metrology**: interferometers, wavefront sensors

## Key Deliverables

The agent is configured to produce, on demand:
- `outputs/optical-prescription.csv` — element table (R, t, nd, Vd, semi-dia)
- `outputs/fmea-worksheet.csv` — structured FMEA with RPN sort
- `outputs/tolerance-report.pdf` (via Claude-side rendering) — Monte Carlo sensitivity
- `user-docs/design-review.md` — polished CDR-ready writeup

## Diversity Check

Recent Cognitropy builds (last 5):
- Outdoor & Adventure (avalanche)
- Security & Intelligence (security clearance)
- Cyber & DFIR (supply chain)
- Engineering & Technical (dam safety, railway)

**Physical Sciences has not been built recently.** Diversity check: ✅ clean rotation.

## Build Notes

- Template copied from `.workspace-template/`, all `{{PLACEHOLDER}}` tokens replaced.
- No real credentials present (verified by grep scan).
- 6 slash commands, 4 prompts, 1 plan.md, 3 resource reference files.
- CLAUDE.md is 29 lines (under the 30-50 line budget).
- README is 128 lines (exceeds 100-line target).
