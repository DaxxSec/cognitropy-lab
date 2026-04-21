# Getting Started — optics-system-fmea

## 1. Run `/onboard`
Claude will interview you about your optical system, required standards, environmental conditions, and available tooling. Expect ~10 minutes.

## 2. Run `/design-optical-system`
Claude proposes 3 architectures and writes `outputs/prescription-v1.csv` for the one you pick. Each candidate comes with ≥3 seed failure modes.

## 3. Run `/run-fmea`
Structured FMEA pass. Claude walks you through functions → modes → effects → causes → RPN scoring and proposes mitigations.

## 4. Run robustness commands in any order:
- `/tolerance-analysis` — Monte Carlo + sensitivity
- `/stray-light-audit` — ghost/scatter/baffle
- `/thermal-vibration-review` — athermalization + modal

## 5. Wrap up
When you say "review ready", Claude assembles `user-docs/design-review.md` with all artifacts.

## Tips
- Edit `context/constraints.md` directly if you want to change tolerance tier, risk appetite, or regulatory scope mid-project.
- Every session, Claude appends to `work-log/YYYY-MM-DD.md` — this is your audit trail.
- FMEA worksheet is CSV so you can import it into your PLM/QMS.
