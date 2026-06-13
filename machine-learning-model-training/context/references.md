# Machine Learning Model Training — Reference Tables

Compact lookup data for live incident work. Prose lives in `concepts.md` / `workflows.md`.

## Severity matrix

| SEV | Trigger | Example | Response |
|-----|---------|---------|----------|
| **SEV-1** | Run destroying value | NaN/inf loss, garbage grads, silent non-learning on full fleet | Page now; stabilise or kill immediately |
| **SEV-2** | Degraded, value at risk | Throughput halved, recurring OOM, straggler node, eval regressing | Respond within the hour |
| **SEV-3** | Healthy, latent risk | Sparse checkpoints vs failure rate, disk filling, mis-tuned alert | Next business hours / handoff |
| **SEV-4** | Informational | One-off NCCL retry, single slow shard, self-healed transient | Log only |

## Symptom → runbook router

| Symptom | Failure class | Runbook |
|---------|---------------|---------|
| Loss → NaN/inf, spike, or flat from step 0 | Numerical / optimisation | `/loss-divergence-runbook` |
| `CUDA out of memory`, OOM-killed, fragmentation | Memory | `/oom-recovery-runbook` |
| tokens/s or samples/s dropped, low GPU util, straggler | Efficiency | `/throughput-regression-runbook` |
| Crash, preemption, node failure, need to resume | Recovery | `/checkpoint-recovery` |
| Corrupt/missing shard, tokenizer drift, leakage | Data integrity | `/data-pipeline-incident-runbook` |
| NCCL timeout / hang / one rank silent | Comms / straggler | start `/throughput-regression-runbook` (straggler path) |
| Unsure / first responder | Any | `/training-incident-triage` |

## Suggested alert thresholds (tune per run in `/run-healthcheck`)

| Metric | Warning | Page | Notes |
|--------|---------|------|-------|
| `loss` | rising 3 intervals | NaN/inf or +X% over EMA | use EMA band, not raw |
| `grad_norm` | > 2× running median | > clip_value sustained | leading indicator of spikes |
| throughput | < 90% baseline 5 min | < 70% baseline 10 min | normalise to MFU if model changes |
| GPU mem headroom | < 15% | < 5% | OOM precursor |
| GPU util | < 80% 10 min | < 50% sustained | data-starvation signal |
| step heartbeat | none for 2× step-time | none for 5× step-time | hang/deadlock |
| checkpoint age | > 1.5× interval | > 2× interval | error-budget breach |

## Checkpoint completeness checklist

A resume is only continuous if the checkpoint restores **all** of:

- [ ] model weights
- [ ] optimizer state (Adam `m`/`v` moments, etc.)
- [ ] LR-scheduler state / step counter
- [ ] RNG state (Python, NumPy, framework, per-device CUDA)
- [ ] dataloader / sampler position (epoch + index, or stream offset)
- [ ] global step + token/sample count
- [ ] config + framework/CUDA/driver versions + data-snapshot hash

## OOM mitigation ladder (smallest change first)

1. reduce per-device batch size (raise grad-accumulation to hold global batch)
2. enable activation / gradient checkpointing
3. enable / increase ZeRO stage (1→2→3) or FSDP sharding
4. shorten max sequence length / pack sequences
5. switch fp16/fp32 → bf16; offload optimizer states (ZeRO-Offload) as last resort
6. add tensor/pipeline parallelism (re-shard checkpoint to new layout)

## Loss-divergence mitigation ladder

1. roll back to checkpoint *before* the spike
2. lower learning rate (and/or lengthen warmup)
3. confirm gradient clipping is on and tuned
4. fp16 → bf16 (removes loss-scaling collapse) or fix loss-scale window
5. skip / inspect the offending data batches
6. check for a recent code/config change (diff vs last good run)

## Key references

- Google SRE Book — Postmortem Culture & Effective Troubleshooting: https://sre.google/sre-book/table-of-contents/
- Google SRE Workbook — Incident Response: https://sre.google/workbook/incident-response/
- PyTorch general checkpoint recipe: https://pytorch.org/tutorials/recipes/recipes/saving_and_loading_a_general_checkpoint.html
- PyTorch reproducibility: https://pytorch.org/docs/stable/notes/randomness.html
- PyTorch FSDP: https://pytorch.org/docs/stable/fsdp.html
- DeepSpeed ZeRO: https://www.deepspeed.ai/tutorials/zero/
- NVIDIA Megatron-LM: https://github.com/NVIDIA/Megatron-LM
- OPT-175B logbook (real incident logs): https://github.com/facebookresearch/metaseq/tree/main/projects/OPT/chronicles
- Weights & Biases (metrics/alerts): https://docs.wandb.ai/ · MLflow tracking: https://mlflow.org/docs/latest/tracking.html
- `torch.nn.utils.clip_grad_norm_`: https://pytorch.org/docs/stable/generated/torch.nn.utils.clip_grad_norm_.html
