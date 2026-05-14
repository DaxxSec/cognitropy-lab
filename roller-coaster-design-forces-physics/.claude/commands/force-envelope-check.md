# /force-envelope-check

Walk a force-vs-time trace through the `F-*` decision tree (`context/workflows.md` §1) and produce a per-axis verdict tied to ASTM F2291 / EN 13814 envelopes.

## Inputs

- `segment_id` — name or id of the track segment being reviewed (e.g. `airtime-hill-3`, `inversion-2`).
- `trace_path` — CSV with `t, ax, ay, az` columns, OR inline trace.
- `frame` — `track` | `heartline`. Required. If unknown, the tree terminates at `F-0` with REJECT.
- `standard` — `F2291` | `EN13814` | `in-house:<name>`. Defaults to `F2291`.
- `sample_rate` — Hz. If absent, infer from `t` spacing.

## Steps

1. Run `F-0` intake. Verify frame, sample rate ≥ 50 Hz, standard. Abort with REJECT if any gate fails.
2. If `frame = "track"` and the segment has bank-angle data available, route through `/heartline-analysis` first; otherwise run on track-frame trace and annotate the verdict.
3. Walk `F-1` (vertical +z) — both peak and 2 s sustained windows. Cite node + measured value + time.
4. Walk `F-2` (vertical -z / airtime) — peak and sustained. Lateral-frame-of-reference matters here.
5. Walk `F-3` (lateral) — peak and >0.5g duration window. On REJECT, auto-suggest `/banking-curvature-tune`.
6. Walk `F-4` (longitudinal) — apply launch/brake limit tables if the segment is a launch or brake region.
7. Walk `F-5` (combined vector). Compute `|a| = sqrt(ax²+ay²+az²)` and peak.
8. Aggregate at `F-6` and emit a single segment verdict (PASS / PASS_WITH_NOTE / REWORK / REJECT) plus a per-axis result table.
9. Write the walk to `outputs/walks/<segment_id>-envelope-<YYYYMMDD>.md`.

## Output

Markdown file containing:
- Segment id, frame, standard, sample rate.
- Per-axis result table (axis, peak, sustained, limit, verdict, node).
- Aggregate verdict.
- Auto-suggested follow-up commands (e.g. `/jerk-budget-audit`, `/banking-curvature-tune`).
- Reproducibility footer: input file hash, git SHA of this workspace.

## Notes

- Never smooth the trace before envelope check — peaks matter. (`/jerk-budget-audit` does its own low-pass.)
- A track-frame analysis on a banked curve **understates** rider-felt vertical-g and **overstates** lateral-g. Annotate this in the verdict.
- The "5% within limit" rule for PASS_WITH_NOTE is mnemonic — the threshold is operator policy.
- If `frame = "heartline"` but the data is clearly track-frame (gravity always reads as +z magnitude even on banked curve), `F-0` should reject with a frame-mismatch error.
