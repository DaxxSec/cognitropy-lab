# /cool-curve — Annealing Schedule Design and Critique

Compute or critique a lehr (annealing oven) program for a piece, given mass, max wall thickness, and glass family. The output is a four-segment program with hold times and ramp rates, plus a verdict on a user-supplied program if one is given.

## Background

Annealing removes residual stress from a hot-formed piece by holding it just above the strain point (where viscosity drops far enough that residual stress relaxes within minutes), then ramping down slowly enough that the temperature gradient between surface and core never produces tensile stress greater than the glass's tensile strength.

The dominant constraint is **wall thickness**, not mass — heat conduction through glass is slow (~0.9 W/m·K), so thick walls take much longer to equalize than thin ones. The rule of thumb:

```
max ramp rate (°C/h) ≤ K / (max_wall_thickness_mm)²
```

Where `K` is a glass-family constant (`K ≈ 1500` for soda-lime COE 90/96/104, `K ≈ 800` for borosilicate 33 — borosilicate's lower COE means smaller stress per °C of gradient, but its lower thermal expansion is offset by higher annealing temp, so the safe ramp constant is empirically lower).

## Required Inputs
- **Glass family** (Bullseye 90 / System 96 / Effetre 104 / Borosilicate 33 / other — must be in `resources/glass-viscosity-reference.md`)
- **Piece mass (g)** — drives the hold time at anneal point
- **Max wall thickness (mm)** — drives the ramp rate
- **Geometry hint** — vessel / sculpture / flat plate / bead / cane (different geometries have different worst-case thermal gradients)
- **Critique target (optional)** — a user-proposed program, given as a list of segments

## Procedure

### 1. Look Up Anchor Temperatures
From `resources/glass-viscosity-reference.md`:
- **Anneal point** (η = 10¹³ poise): ~482 °C for soda-lime, ~565 °C for borosilicate, ~516 °C for COE 90 (manufacturer-specific)
- **Strain point** (η = 10¹⁴·⁵ poise): typically ~30 °C below anneal point
- Confirm against manufacturer data; never use the rough numbers in this file when the manufacturer publishes specifics

### 2. Compute Hold Time
Hold at the anneal point until the core reaches anneal-point temperature. Empirical baseline:
- Up to 6 mm wall: 30 minutes
- 7–12 mm: 60 minutes
- 13–25 mm: 2 hours
- 26–50 mm: 4 hours
- > 50 mm: scale roughly with thickness² (this is castings territory — defer to Bullseye TipSheets)

Add 30 minutes of base hold for any piece > 1 kg regardless of thickness, to allow inner mass to equilibrate.

### 3. Compute Ramp Rate (Anneal → Strain)
This is the most stress-sensitive segment.
- `rate_anneal_to_strain = K / (max_wall_thickness_mm)²`, capped at 200 °C/h (lehr controllers cap there anyway)
- Round down to a controller-friendly number (50, 100, 150 °C/h)

### 4. Compute Ramp Rate (Strain → 100 °C)
Below strain, the glass is rigid; differential cooling is less dangerous but still produces strain that won't relax.
- Allow approximately **2× the anneal-to-strain rate**
- Cap at 300 °C/h

### 5. Compute Ramp Rate (100 °C → Room)
Below 100 °C, residual stress generation is minimal. Most lehrs simply turn off and cool naturally; force-cooling under 100 °C is generally fine.

### 6. Assemble the Program
Output a four-segment program:
| Segment | From → To | Rate | Hold |
|---------|-----------|------|------|
| 1 | Loading temp → anneal point | controller-default | hold computed in step 2 |
| 2 | Anneal point → strain point | rate from step 3 | none |
| 3 | Strain point → 100 °C | rate from step 4 | none |
| 4 | 100 °C → room | natural cool / off | done |

### 7. Critique Mode (if user supplied a program)
For each segment in the user's program:
- Compare against the computed rates
- Flag any segment that exceeds the safe rate by > 20% (red), 0–20% (yellow), at-or-below (green)
- Specifically check that the hold-at-anneal is long enough for the piece's mass and thickness

### 8. Output
- Write the program (or critique) to `outputs/cool-curves/<piece-id>-or-<form-slug>.md`
- Append a one-line summary to the day's batch record
- If the program is part of a `/form-sim` flow, inline it back into the form spec
- If critiquing and the user's program is unsafe, refuse to mark the form spec "ready" until corrected

## Notes and Edge Cases

- **Thick castings:** Anything above ~25 mm wall thickness exits the empirical comfort zone of this rule. Defer to Bullseye TipSheets, Schott documentation, or a dedicated FEA simulation.
- **Mixed wall thicknesses in one piece:** Use the worst case (thickest wall), not the average.
- **Sealed forms:** Hollow forms with a sealed cavity behave thermally as if they were solid at the wall thickness — be conservative.
- **Coldworked or polished pieces:** Existing surface stress from grinding may amplify. If the piece will be coldworked after anneal, no special change to the curve, but flag for the post-coldwork stress check (`/post-mortem` covers the diagnosis if it cracks).
