# /form-sim — End-to-End Form Simulation

Simulate a planned form before any glass is fired. The output is a feasibility verdict (`green` / `yellow` / `red`), a per-step working time budget, a gravity-sag risk profile, a recommended cool curve, and a written form spec saved to `planning/form-<slug>-v<n>.md`.

## Required Inputs
- A description or sketch of the target form (height, max width, wall thickness profile, foot/stem/neck if present)
- Glass family (must be one of the COE families captured in `/onboard`)
- Color plan (rod lots, frit, applied vs. cased) — must pass COE compatibility check
- Studio ambient temperature (today's reading) — defaults to the envelope average if omitted
- Glory hole soak temperature (today's measured value, or default from environment.md)

## Procedure

### 1. Geometry Capture
Record the form parameters explicitly:
- Total mass estimate (g) — from a similar past piece or a quick volume × density estimate (ρ ≈ 2.5 g/cm³)
- Max wall thickness (mm) — drives the cool curve
- Max horizontal reach (mm) — drives the gravity sag check
- Number of distinct features (lip, foot, neck, applied handles, cane pickup) — drives the operation count

### 2. Gather Plan
Estimate gather count from total mass and the studio's typical per-gather mass (default: 250–400 g per gather for a standard blowpipe). Output a gather schedule with target masses per gather and the marvering/blocking step between them.

### 3. Working Time Budget
For each operation in the plan:
- Estimate the surface temperature drop (`ΔT_op`) — see `context/for-agent/domain-knowledge.md` for the typical per-operation values
- Sum drops since last reheat
- Flag the step where cumulative drop puts surface below the working point (10⁴ poise)
- Recommend reheat insertions before any flagged step

Output: a per-step table `step | operation | ΔT_op | cumulative_T_drop | working_point_remaining_s | reheat?`

### 4. Gravity Sag Check
For any horizontal reach > 100 mm or any feature pulled out cantilever:
- Compute the indicative sag rate using the analytic formula in domain-knowledge (`sag_rate ∝ ρ·g·L²/η`)
- Flag if expected sag during the planned operation duration exceeds the form-type threshold (vessels: 1 mm; flat plates: 0.5 mm at the rim; sculptural: artist-defined)

### 5. COE Compatibility Gate
Hard check. Cross-reference the color rod lots against the base glass COE family in `resources/glass-viscosity-reference.md`. Any mismatch ≥ 0.5 (× 10⁻⁷ K⁻¹) is a hard stop. Print the failing pair and refuse to proceed.

### 6. Cool Curve Recommendation
Hand off the (mass, max wall thickness, glass family) tuple to the rules in `/cool-curve`. Inline the recommended program in the form spec.

### 7. Verdict and Spec
Combine into a verdict:
- **Green** — all gates pass with margin
- **Yellow** — one or more gates pass tightly; advise dry-run or a smaller-scale test piece first
- **Red** — at least one gate fails; advise rework of the plan

Save the full form spec to `planning/form-<slug>-v<n>.md` (auto-increment `<n>`). Append a one-line summary to the day's batch record under "planned forms".

### 8. Optional: Generate Sim Module
If the user wants reproducible numbers, write a small Python module to `outputs/sim/<slug>.py` that re-runs the calculations against the same inputs. The sim module imports nothing external — pure stdlib — so it survives studio computers with no internet.
