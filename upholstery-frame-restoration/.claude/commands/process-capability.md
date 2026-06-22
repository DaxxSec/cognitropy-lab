# /process-capability — Cp / Cpk for a Restoration Dimension

Compute process capability for a tracked characteristic against its tolerance and judge whether the bench's natural variation can hold the spec — strictly on a process the control chart shows is in control.

## Inputs

- Characteristic, its **USL** and **LSL** (or one-sided limit) for the piece type.
- σ̂ from the in-control I-MR chart (`σ̂ = M̄R / 1.128`) and the process mean X̄.
- Confirmation that `/control-chart` shows the process **in control** (no unresolved signals).

## Steps

1. **Gate:** verify the process is in control. If not, **stop** — capability of an unstable process is meaningless; return to OCAP first.
2. Compute **Cp = (USL − LSL) / (6σ̂)** — potential capability (spread only).
3. Compute **Cpk = min[(USL − X̄), (X̄ − LSL)] / (3σ̂)** — actual capability (spread + centering).
4. Compute the **centering gap** (Cp − Cpk); a large gap means the process is off-center, not too wide — a different fix (shift the mean) than tightening variation.
5. Classify against the bands in `context/references.md` (incapable / marginal / capable / high) and estimate ppm out of spec.
6. Recommend: if incapable due to spread → reduce variation (jig, method, environment); if off-center → re-target; if capable → consider whether the tolerance can be relaxed for conservation pieces.

## Output

A capability report: Cp, Cpk, centering gap, capability class, estimated ppm, and the spread-vs-centering recommendation. Save to `outputs/<characteristic>-capability.md`.

## Notes

- **Stability before capability** — this is the most-violated rule in shop SQC. A great Cpk on an out-of-control chart is fiction.
- For n = 1 craft data, prefer short-term σ̂ from M̄R over a pooled long-term s; note which you used.
- Capability is a *process* statement. It does not condemn a single antique frame that sits outside the limits but is original and sound.
