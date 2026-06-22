# /beat-sync-check

Verify that "hero" cues break within tolerance of their musical beats, with time-of-flight compensation applied — the artistic SYNC obligation.

## Inputs

- The canonical cue sheet (hero cues, `device`/bore, `t_fire`, `tof`).
- The music map: beat/downbeat times `{b_i}` (DAW markers, `librosa`/`madmom`), and which beat each hero cue targets.
- Sync tolerance τ per cue role (defaults in `context/references.md`).

## Steps

1. Identify hero cues and their target beats; pull bore-specific ToF from `context/references.md` (or the product sheet).
2. Set / confirm pre-fire compensation: `t_fire = b_i − tof(device)`. Flag any hero cue whose `t_fire` would be negative or collide on a shared channel.
3. Compute `t_effect = t_fire + tof` and sync error `e_i = t_effect − b_i`.
4. **SYNC:** discharge `|e_i| ≤ τ` for each hero cue; report the robustness margin `τ − |e_i|`.
5. For cues failing SYNC, classify: micro-adjustable (nudge `t_fire`), ToF-uncertainty-bound (widen τ or downgrade hero→ambient), or structurally impossible (two different-bore heroes on one beat & channel → re-rack). Route to the constraint-violation triage tree.

## Output

`outputs/beat-sync-YYYY-MM-DD.md`: per-hero-cue table (target beat, `tof`, `t_fire`, `t_effect`, `e_i`, margin, verdict) and the list of SYNC failures with their repair class.

## Notes

- Always compensate by the cue's **own** ToF; a mixed-bore accent chain breaks raggedly otherwise.
- SYNC is artistic — never resolve a SYNC miss with an edit that opens a SEP/REUSE obligation. Safety dominates.
- If ToF uncertainty (wind, lift variance) exceeds τ, the beat is not reliably hittable for that bore — say so rather than reporting false precision.
