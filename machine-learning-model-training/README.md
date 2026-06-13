# Machine Learning Model Training Workspace

> Operate ML model training the way an SRE team operates production — with severity levels, runbooks, on-call handoffs, and blameless postmortems.

## What This Workspace Does

Training a modern model is no longer a script you launch and forget. A single pretraining or fine-tuning run can hold thousands of GPU-hours hostage, fail silently at 2 a.m. on day three, and burn a five-figure compute budget before anyone notices the loss went to `NaN`. This workspace reframes model training as a **reliability discipline**: every run is a service with an error budget, every failure mode is a documented *incident class*, and every recovery follows a *runbook* instead of improvised heroics.

The organising technique here is **incident-response runbooks**. Instead of one giant "debug my training" command, the workspace ships a triage entry point and a set of failure-class-specific runbooks — loss divergence, OOM, throughput regression, data-pipeline corruption, checkpoint recovery. Each runbook encodes the detection signals, the severity rubric, the *stabilise-first* mitigation order, the recovery procedure, and the verification gate. On-call handoffs and blameless postmortems close the loop so each incident makes the next run more reliable.

It is deliberately framework-agnostic in spirit (PyTorch / DeepSpeed / Megatron-LM / JAX), because reliability practices outlive any one stack. Where a fix is framework-specific, the runbook says so.

## Why This Workspace Exists

The public training logbooks of large runs — Meta's OPT-175B chronicles, the BLOOM logbook, the PaLM and GLM-130B reports — read like incident postmortems: hardware failures, loss spikes, restarts from checkpoints, manual learning-rate surgery. Those teams *invented* incident response for training because the cost of not having it was catastrophic. Most smaller teams rediscover the same failures from scratch, expensively. This workspace codifies that hard-won operational knowledge into reusable runbooks so a single engineer (or an agent) can respond to a 3 a.m. divergence with a procedure instead of panic.

## Getting Started

### Prerequisites

- A training stack with structured logs / metrics (loss, grad-norm, throughput, GPU memory, GPU util) — e.g. Weights & Biases, MLflow, TensorBoard, or plain JSONL logs.
- Checkpointing enabled with **full** state (model + optimizer + scheduler + RNG + dataloader position).
- Access to the training launcher config (LR, batch size, precision, parallelism degrees) and the job scheduler logs (Slurm/Kubernetes) if multi-node.
- Optional: an alerting channel (Slack/PagerDuty) wired to your metric thresholds.

### Quick Start

1. Clone this workspace next to (or inside) your training project.
2. Run `/run-healthcheck` *before* you launch a long run — it produces a pre-flight checklist and a set of alert thresholds / run SLOs tuned to your config.
3. When something fires, start at `/training-incident-triage` — it assigns a severity and routes you to the right runbook.
4. Work the matching runbook (`/loss-divergence-runbook`, `/oom-recovery-runbook`, etc.); save the incident report it produces to `outputs/`.
5. After recovery, run `/training-postmortem` to capture the timeline, root cause, and action items — then fold any new failure class back into a runbook.

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/training-incident-triage` | Severity assignment + symptom classification + runbook routing | First responder for any live training failure |
| `/loss-divergence-runbook` | Stabilise and recover a diverging / spiking / NaN loss | Loss → inf/NaN, sudden spike, plateau-then-explode |
| `/oom-recovery-runbook` | Diagnose CUDA/host OOM and resume safely | `CUDA out of memory`, OOM-killed processes, allocator fragmentation |
| `/throughput-regression-runbook` | Find why a run got slower (samples/s, tokens/s, MFU) | Throughput drop, GPU util sag, stragglers, IO/comms stalls |
| `/checkpoint-recovery` | Restore a run with full, deterministic state | After any crash, preemption, or node failure |
| `/data-pipeline-incident-runbook` | Respond to bad shards, tokenizer drift, leakage | Corrupt/missing data, label drift, eval contamination found mid-run |
| `/run-healthcheck` | Pre-flight + in-flight checks; define thresholds & SLOs | Before launch, and as a periodic in-run audit |
| `/oncall-handoff` | Generate a shift-handoff doc for a multi-day run | End of an on-call shift on a long run |
| `/training-postmortem` | Blameless postmortem with assignable action items | After any SEV-1/SEV-2 incident is resolved |

## Directory Structure

```
machine-learning-model-training/
├── CLAUDE.md                 # Agent role, context refs, command list
├── README.md                 # This file
├── .claude/commands/         # Bespoke training-reliability runbooks
├── context/
│   ├── concepts.md           # Training internals + incident taxonomy + failure modes
│   ├── workflows.md          # The incident lifecycle applied to training
│   └── references.md         # Severity matrix, symptom→runbook router, thresholds, checklists
├── prompts/                  # Reusable prompt templates (reports, postmortems, alert design)
└── outputs/                  # Incident reports, postmortems, handoffs
```

## Example Use Cases

### 3 a.m. NaN loss on day three of a pretraining run
Triage assigns SEV-1 (run is producing garbage gradients), routes to `/loss-divergence-runbook`, which has you confirm the last clean step, roll back to the previous checkpoint, lower the LR / re-enable grad clipping / check bf16 vs fp16 loss-scaling, and resume — then schedules a postmortem.

### A fine-tune that was 1.4 it/s yesterday is 0.6 it/s today
`/throughput-regression-runbook` walks the differential: did the dataloader become IO-bound, is one GPU a straggler dragging the all-reduce, did a noisy neighbour land on the node, did someone change `num_workers` or precision?

### Resuming after a Slurm preemption
`/checkpoint-recovery` verifies the checkpoint restores *optimizer momentum, LR-scheduler step, RNG state, and dataloader position* — not just weights — so the resumed curve is continuous rather than a visible discontinuity.

### Discovering a leaked eval set mid-run
`/data-pipeline-incident-runbook` treats contamination as a SEV — quarantine the shard, quantify exposure, decide whether to continue/restart, and document for the model card.

## Recommended MCP Servers

- **Filesystem MCP** — read training logs, configs, and checkpoint metadata directly from the run directory.
- **GitHub MCP** — correlate an incident with the commit/PR that changed the training config or model code.
- **A metrics/observability MCP (or W&B/MLflow API)** — pull loss, grad-norm, throughput, and GPU telemetry into triage.
- **Slack / PagerDuty MCP** — post incident summaries and on-call handoffs to the channel that owns the run.

## Legal & Ethical Considerations

- **Data provenance & leakage:** a contamination incident isn't only a metrics problem — it has model-card and disclosure implications. Document training-data incidents honestly.
- **Cost stewardship:** GPU-hours are real money and real energy. "Kill the run early and cleanly" is often the responsible call; treat budget burn as a first-class incident signal.
- **Blamelessness:** postmortems name systems, not people. Never use this workspace's artifacts to assign individual fault.

## Technical References

- [Google SRE Book — Effective Troubleshooting & Postmortems](https://sre.google/sre-book/table-of-contents/) — the incident-response and blameless-postmortem source material this workspace adapts.
- [PyTorch — Saving & Loading a General Checkpoint](https://pytorch.org/tutorials/recipes/recipes/saving_and_loading_a_general_checkpoint.html) — what "full state" actually means.
- [PyTorch — Reproducibility](https://pytorch.org/docs/stable/notes/randomness.html) — seeds, deterministic algorithms, the recovery foundation.
- [DeepSpeed ZeRO](https://www.deepspeed.ai/tutorials/zero/) & [PyTorch FSDP](https://pytorch.org/docs/stable/fsdp.html) — sharding levers for OOM runbooks.
- [The BLOOM training chronicles / OPT-175B logbook](https://github.com/facebookresearch/metaseq/blob/main/projects/OPT/chronicles/OPT175B_Logbook.pdf) — real incident logs from a 175B run.
- [Megatron-LM](https://github.com/NVIDIA/Megatron-LM) — parallelism strategies referenced in throughput/OOM runbooks.

## Optional plugin

If you have the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, additional global commands (`/workspace-foundational:context-sweep`, `/workspace-foundational:find-template`) are available; the workspace works without it.
