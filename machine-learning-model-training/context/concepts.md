# Machine Learning Model Training — Core Concepts

Background the agent should read before working a training incident. Optimised for fast recall during a live failure, not exhaustive theory. The framing throughout: **a training run is a production service, and its failures are incidents.**

## The training run as a system

A run is a loop over `(load batch → forward → loss → backward → optimizer.step → maybe checkpoint/eval)`, parameterised by a config (model arch, optimizer, LR schedule, precision, batch size, parallelism degrees) and fed by a data pipeline, executing on a fleet of accelerators under a job scheduler. An incident is any state where the run is **wasting GPU-hours** (slower than budgeted, producing garbage, or dead). The four health axes:

- **Correctness** — is the loss going down and are gradients finite? (loss, grad-norm, eval metrics)
- **Liveness** — is the process making steps at all? (step rate, heartbeat, scheduler state)
- **Efficiency** — are the accelerators doing useful work? (throughput, MFU, GPU util, memory headroom)
- **Integrity** — is the state recoverable and the data trustworthy? (checkpoint validity, data provenance)

## Incident severity taxonomy (training-adapted)

Borrowed from SRE SEV levels and re-anchored to GPU-hours and recoverability:

- **SEV-1 — Run is destroying value.** Loss is NaN/inf, gradients are garbage, or the model is silently learning nothing while burning the full fleet. Every minute is wasted budget. *Page immediately; stabilise or kill now.*
- **SEV-2 — Run degraded, value at risk.** Throughput halved, intermittent OOM with auto-restarts, one straggler node, eval metrics regressing run-over-run. Recoverable but bleeding. *Respond within the hour.*
- **SEV-3 — Run healthy, latent risk.** Checkpoint cadence too sparse for the failure rate, disk filling, an alert threshold mis-tuned, a deprecation warning. *Handle in business hours / next handoff.*
- **SEV-4 — Informational.** A one-off transient that self-healed (single NCCL retry, one slow data shard). *Note in the log; no action.*

Severity is set by *blast radius × reversibility*, not by how loud the stack trace is.

## Optimisation & numerical stability (where loss incidents come from)

- **Learning rate** is the single most common cause of divergence. Too-high LR (or a warmup that's too short) produces loss spikes; the standard mitigations are LR reduction, longer warmup, and gradient clipping.
- **Gradient clipping** (`clip_grad_norm_`) caps the update magnitude; an exploding `grad_norm` is the leading indicator of an imminent loss spike — watch it, not just the loss.
- **Mixed precision** trades memory/speed for numerical headroom. `fp16` has a narrow dynamic range and needs **loss scaling** to avoid gradient underflow → `NaN`; `bf16` has fp32's exponent range and usually removes the loss-scaling failure class entirely. A sudden NaN after thousands of clean steps in fp16 is frequently a loss-scale collapse.
- **Loss spikes** in large-model pretraining are a documented phenomenon (PaLM, OPT, GLM-130B). Standard playbook from those teams: roll back to a checkpoint *before* the spike, skip the offending data batches, and/or lower LR — then continue.
- **Optimizer state** (Adam's `m`/`v` moments) is part of the run's state. Resuming without it restarts momentum and creates a visible discontinuity.

## Distributed training (where OOM and throughput incidents come from)

- **Data parallel (DDP / ZeRO-1/2/3, FSDP):** each rank holds a model replica (or a shard of it) and syncs gradients via **all-reduce**. ZeRO-3/FSDP shard parameters, gradients, *and* optimizer states across ranks — the primary OOM lever.
- **Tensor / pipeline / sequence parallel (Megatron-style):** split a single layer or the layer stack across devices. Mis-set parallelism degrees are a classic OOM and throughput cause.
- **Collectives & NCCL:** all-reduce/all-gather over NVLink/InfiniBand. A single slow ("straggler") rank stalls the whole collective — one bad GPU drags global throughput. `NCCL timeout` / hangs are a distinct incident class.
- **GPU memory budget** ≈ parameters + gradients + optimizer states + **activations** + fragmentation. Activations scale with batch size × sequence length and are the usual lever via **activation/gradient checkpointing** (recompute instead of store).

## Throughput & efficiency metrics

- **Samples/s or tokens/s** — the headline rate. **MFU (Model FLOPs Utilization)** normalises it against the hardware's peak FLOPs so you can tell a slow run from a small model.
- **GPU utilization vs. SM efficiency** — high "util" can still hide a data-starved GPU spinning on a tiny kernel; watch the **input pipeline** (dataloader workers, prefetch, IO).
- **Stragglers** — heterogeneous per-rank step times; the slowest rank sets the pace in synchronous training.

## The data pipeline (where integrity incidents come from)

- **Sharded datasets** (WebDataset, tfrecords, parquet) can have **corrupt or truncated shards** that crash or silently skip data.
- **Tokenizer / preprocessing drift** — a tokenizer or normalisation change between data-prep and training silently shifts the input distribution.
- **Label drift / leakage** — eval-set contamination in the training corpus inflates metrics and is a model-card disclosure issue, not just a bug.
- **Class/shard imbalance after a resume** — a non-deterministic dataloader that doesn't restore its position re-reads or skips data on resume.

## Checkpointing & recovery (the integrity backbone)

A *complete* checkpoint is **model weights + optimizer state + LR-scheduler state + RNG/seed state + dataloader position + step counter + config/version metadata**. Missing any one produces a discontinuous resume. Checkpoint cadence is an error-budget decision: `expected_loss_on_failure ≈ MTBF⁻¹ × checkpoint_interval × cost_per_step`. Sharded checkpoints (FSDP/ZeRO) must be reloaded with the *same* parallelism layout or via a resharding step.

## Common Failure Modes

- **NaN/inf loss** — fp16 loss-scale collapse, too-high LR, bad batch, or numerical overflow in a custom op.
- **Silent non-learning** — loss flat from step 0: frozen params, zero/garbled LR, detached graph, or all-padding batches.
- **OOM mid-run** — activation growth from a long sequence, memory fragmentation, a leak in a custom loop, or an eval pass that doesn't free memory.
- **Throughput cliff** — IO-bound dataloader, a straggler GPU, thermal throttling, a noisy neighbour, or a precision/`num_workers` regression.
- **Hang / deadlock** — NCCL timeout, mismatched collective calls across ranks, or one dead rank.
- **Discontinuous resume** — checkpoint restored weights but not optimizer/scheduler/RNG/data position.
- **Metric regression run-over-run** — a config/data change made the new run worse than the last good one (needs a diff, not a guess).

## Operating Constraints

- **GPU-hours are budget and energy.** Killing a doomed run early is responsible, not failure.
- **Determinism is best-effort on GPU** — full bitwise reproducibility may cost throughput; log enough to *re-derive* an incident even when you can't bit-match it.
- **Data incidents have disclosure obligations** — leakage/contamination must reach the model card and stakeholders, not just the fix.
