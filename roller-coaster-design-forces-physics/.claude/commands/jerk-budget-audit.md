# /jerk-budget-audit

Walk the `J-*` decision tree (`context/workflows.md` §3) to audit third-derivative profile across the transition windows. Catches whiplash-class problems that envelope check passes.

## Inputs

- `trace_path` — same trace passed to `/force-envelope-check`.
- `frame` — `track` | `heartline`. Required.
- `windows` — list of transition windows `(t_start, t_end, label)`. If absent, auto-detect via zero-crossings of `d²a/dt²`.
- `noise_lpf_hz` — low-pass cutoff for noise suppression. Default 30 Hz. Don't go lower than 20 Hz or you'll erase real jerk.

## Steps

1. Run `J-0` intake — apply LPF at `noise_lpf_hz`, build window list.
2. For each window, compute `d(ax)/dt, d(ay)/dt, d(az)/dt` numerically (central differences after the LPF).
3. Walk `J-1` (lateral jerk) — peak and 0.3 s sustained. On REJECT, route to `/banking-curvature-tune`.
4. Walk `J-2` (vertical jerk) — peak and sustained.
5. Walk `J-3` (longitudinal jerk) — peak only.
6. Walk `J-4` — flag direction-flips within 0.2 s window (whiplash); flag multi-axis simultaneous jerk (vestibular).
7. Aggregate at `J-5` per window. Emit a per-window verdict table.
8. Persist to `outputs/walks/<segment_id>-jerk-<YYYYMMDD>.md`.

## Output

Markdown file with:
- LPF cutoff, window detection method, jerk numeric method.
- Per-window table: window label, peak axial jerks, sustained axial jerks, verdict, J-node.
- Cross-reference to the originating `/force-envelope-check` walk if any.

## Notes

- Numeric differentiation is **noise-amplifying**. The LPF is non-negotiable; the cutoff is the operator's policy lever.
- Direction-flip detection at J-4-a catches the rare "whip" element where a curve transitions through neutral into the opposite-sign curve in less than 0.2 s.
- Multi-axis co-occurrence at J-4-b is the marker of vestibular distress (motion sickness); rare but real on heavily-twisted modern coasters.
- If sensor data is genuinely noisy (e.g. accelerometer pack rattling), the LPF threshold is the wrong tool; replace the sensor mounting before adjusting cutoff.
