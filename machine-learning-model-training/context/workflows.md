# Machine Learning Model Training — Incident Workflows

How a training-run reliability engineer actually works a problem. These are the methodology phases and decision trees the runbooks under `.claude/commands/` instantiate for specific failure classes. The spine is the SRE incident lifecycle, re-pointed at training.

## The training-incident lifecycle

```
DETECT → TRIAGE → MITIGATE/STABILISE → RECOVER → VERIFY → POSTMORTEM
```

1. **Detect** — an alert fires (or a human notices). Capture the *first* anomalous signal and its timestamp/step. Detection signals, not symptoms, anchor the timeline.
2. **Triage** — assign a severity (see `concepts.md` taxonomy), classify the failure into a known class, and route to a runbook. Decide page-vs-defer.
3. **Mitigate / stabilise** — stop the bleeding. Either stabilise the run in place *or* kill it cleanly to preserve the last good checkpoint. Do this **before** root-causing.
4. **Recover** — bring a healthy run back, almost always *from a checkpoint*, with full state restored and the offending condition removed.
5. **Verify** — confirm the recovered run is healthy on all four axes (correctness, liveness, efficiency, integrity) for a defined window before standing down.
6. **Postmortem** — for SEV-1/SEV-2, reconstruct the timeline, find the root cause blamelessly, and produce action items that prevent recurrence.

## Phase 1 — Detection: the signals that should page you

Define these *before* launch (see `/run-healthcheck`). Watch leading indicators, not just lagging ones:

- **grad_norm** spiking above its running band → divergence is imminent (leading indicator for loss spikes).
- **loss** NaN/inf or rising for N consecutive logging intervals.
- **throughput** below X% of the established baseline for M minutes.
- **GPU memory** above Y% headroom floor (OOM risk) or **GPU util** below a floor (data-starved).
- **step heartbeat** stalled → hang/deadlock.
- **checkpoint age** exceeding the error-budget interval.

## Phase 2 — Triage decision tree

```
Is the process still stepping?
├── NO  → hang/deadlock or crash
│        ├── stack trace / OOM in logs?  → /oom-recovery-runbook
│        ├── NCCL timeout / one rank silent? → straggler/comms path of /throughput-regression-runbook
│        └── clean exit / preemption? → /checkpoint-recovery
└── YES → is the loss finite and decreasing?
         ├── NO (NaN/inf/spike/flat) → /loss-divergence-runbook
         └── YES → is throughput at baseline?
                  ├── NO  → /throughput-regression-runbook
                  └── YES → is the data trustworthy?
                           ├── NO (bad shard / drift / leakage) → /data-pipeline-incident-runbook
                           └── YES → likely SEV-3/4: log, tune alerts, continue
```

Severity is assigned in parallel: **blast radius × reversibility**. A NaN on the full fleet = SEV-1; a single auto-recovered NCCL retry = SEV-4.

## Phase 3 — Mitigation principles (stabilise first)

- **Preserve the last good checkpoint above all else.** Never `kill -9` a job mid-checkpoint-write; send a graceful stop or wait for the write to finish.
- **Prefer the smallest reversible change.** Lower LR before changing the optimizer; reduce batch before re-sharding.
- **Kill doomed runs early.** If the expected recovery cost exceeds restarting from a known-good config, stop the burn. Budget is a SEV signal.
- **One change at a time** so the verify step can attribute the fix.

## Phase 4 — Recovery patterns

- **Roll back & resume:** restore the pre-incident checkpoint, apply the mitigating config change, resume. The default for divergence and corruption.
- **Resume in place:** for preemption/OOM with an intact checkpoint, restore *full* state (weights + optimizer + scheduler + RNG + data position) and continue — the curve should be continuous.
- **Reshard & resume:** when changing parallelism degrees to fix OOM/throughput, convert the checkpoint to the new layout first.
- **Hot-fix the data, not the model:** for shard corruption, quarantine/repair the shard and resume rather than restarting from scratch.

## Phase 5 — Verification gate

Before declaring resolved, confirm for a defined window (e.g. 500–1000 steps):

- loss back on or below its pre-incident trajectory; grad_norm in-band;
- throughput within X% of baseline; no OOM/NCCL retries;
- checkpoint successfully written and *test-restored*;
- eval metric (if cheap) not regressed.

## Phase 6 — Blameless postmortem workflow

1. **Timeline** — first signal → detection → each action → resolution, with timestamps *and* training steps.
2. **Impact** — GPU-hours wasted, wall-clock lost, budget burned, any data/metric integrity effects.
3. **Root cause** — the *system* condition (config/infra/data/code), reached via "5 whys" without naming individuals.
4. **Contributing factors** — what made detection slow or recovery hard (missing alert, sparse checkpoints, no runbook).
5. **Action items** — each assignable, falsifiable, and prioritised; the best ones become a new alert threshold or a new runbook.
6. **What went well** — keep the practices that worked.

## On-call workflow for multi-day runs

- Keep a **running incident log** in `outputs/` (append-only) for the life of the run.
- At each shift boundary, run `/oncall-handoff`: current step/loss/throughput, open issues, watchpoints, next checkpoint ETA, escalation contacts.
- Re-run `/run-healthcheck` periodically as an in-run audit — alert thresholds tuned at step 0 drift as the loss landscape changes.
