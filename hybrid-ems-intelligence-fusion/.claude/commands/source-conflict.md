# /source-conflict — Detect and Arbitrate Inter-Source Disagreement

Find segments where fused sources contradict each other beyond a noise budget, classify the conflict type, and emit an arbitration decision plus a downstream impact estimate on the EMS policy.

## Inputs

- **Fused prior** — output of `/fuse-trip-prior` (with per-source breakdowns retained).
- **Per-source raw streams** — the inputs that were fused, time-aligned.
- **Conflict-gate thresholds** — defaults in `context/references.md`, vehicle-specific overrides allowed.
- **Recent `/audit-fusion-trust` report** — informs which sources have historically been unreliable here.

## Steps

### 1. Per-Sample Pairwise Disagreement
For every prediction sample `(s, t)`, compute pairwise standardised differences between source contributions:

`z_ij(s) = (μ_i(s) − μ_j(s)) / sqrt(σ_i² + σ_j²)`

A gate is open when `|z_ij(s)| > z_gate` (default 3.0).

### 2. Classify the Conflict
Map each open gate to a category:

- **Stale source** — one source's timestamp exceeds its TTL. Resolution: drop the stale source, recompute prior segment.
- **Frozen feed** — a source has not changed value for longer than its update period (V2X SPaT message frozen for >2 s, traffic feed frozen for >5 min). Treat as failed.
- **Out-of-region drift** — a source is contradicting consistently over a corridor (>500 m). Indicates calibration drift; lower its trust weight in this region.
- **Single-sample spike** — one sample disagrees but neighbours don't. Treat as noise; do not down-weight the source.
- **Coordinated disagreement** — multiple sources move together against a single contrarian. The contrarian is suspect; check for sensor fault or stale calibration.
- **Mode change** — sources agreed historically but split after an event (entry into tunnel, weather change, vehicle restart). Re-baseline.

### 3. Arbitration Decision
For each conflict, emit a `decision` and `rationale`:

- `drop_source` — exclude from fusion for the affected horizon segment.
- `down_weight` — multiply per-sample trust by 0.3–0.7 based on severity.
- `escalate` — flag for human review (e.g. unexplained coordinated disagreement, safety-critical signal mismatch).
- `noise` — log and leave fusion unchanged.

### 4. Impact Estimate on EMS Policy
Re-run `/optimize-split` with the arbitrated prior and compare against the unarbitrated baseline on:

- Fuel/energy consumption delta (g/km, kWh/100km).
- Battery throughput delta (Ah, normalised cycle equivalents).
- SOC trajectory RMS deviation.

Bound the cost of leaving the conflict unresolved.

### 5. Persist
- Write the conflict report to `outputs/conflicts/<route-hash>-<timestamp>.md` with per-segment tables.
- If the conflict resolves to `escalate`, also write `outputs/conflicts/escalate-<...>.md` with the raw data slice attached for engineer review.

## Output

A conflict report markdown file in `outputs/conflicts/` with: per-segment conflict classifications, arbitration decisions, downstream EMS-policy impact bounds, and (for escalations) the raw data slice. The fused prior is updated in-place; the original is preserved with a `.unarbitrated.json` suffix.

## Notes

- **Do not over-arbitrate.** Aggressive gating produces a fusion stack that systematically excludes new sources and devolves to "nav + elevation only." If gating fires more than 5% of samples on healthy routes, raise the `z_gate` rather than chasing each event.
- **Always preserve the unarbitrated prior.** Downstream `/audit-fusion-trust` learning needs the un-modified record to score sources fairly.
- **Coordinated-disagreement is the dangerous class.** It often means the contrarian is right and the majority is wrong (e.g. a single sensor catching a real obstacle the cloud feeds haven't seen yet). Default to escalation, not auto-drop.
