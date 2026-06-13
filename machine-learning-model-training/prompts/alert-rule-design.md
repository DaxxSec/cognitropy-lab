# Alert Rule & SLO Designer

## Purpose

Propose alerting rules and run SLOs from a run's metric history so the right failures page you early — without alert fatigue. Use during `/run-healthcheck` or after a postmortem reveals a detection gap.

## Prompt Template

```
You are designing alerting for a training run, balancing early detection against alert fatigue.

I have a run to instrument:

- **Run profile:** [MODEL SIZE, PRECISION, BATCH, PARALLELISM, EXPECTED RUN LENGTH]
- **Baseline metrics:** [NOMINAL throughput, MFU, GPU mem headroom, GPU util, grad_norm band, step time]
- **Metrics backend:** [W&B / MLflow / TensorBoard / JSONL + alert channel]
- **Failure history:** [PAST INCIDENTS ON SIMILAR RUNS, IF ANY]
- **Cost facts:** [GPU-HOUR COST, FLEET MTBF IF KNOWN]

Please:
1. Propose warning + page thresholds for loss, grad_norm, throughput, GPU memory, GPU util, heartbeat, and checkpoint age — tuned to these baselines (use EMA/relative bands, not absolutes).
2. Recommend a checkpoint interval sized against MTBF and cost-per-step.
3. Define 3–5 run SLOs / error-budget statements.
4. Flag which alerts are leading indicators vs lagging.
5. Call out likely false-positive sources and how to dampen them.
```

## Expected Output

- A threshold table (warning/page per metric) ready to wire
- A justified checkpoint interval
- 3–5 run SLOs / error-budget statements
- Leading-vs-lagging classification and false-positive dampening notes
