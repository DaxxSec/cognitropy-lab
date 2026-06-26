# Prompt — Monitoring Program Review

## Purpose

Quarterly (or campaign-cycle) review that pairs **detection performance** against **network uptime** — the fusion of screening quality and predictive-maintenance discipline. Answers: were this period's numbers comparable, and is the network healthy enough to keep producing them?

## Prompt Template

```
Review the {period} microplastics monitoring program.

Detection inputs:
- Confirmed-plastic yield & primary false-positive rate per batch: {data}
- Blank LODs and any quarantined batches: {data}
- Recovery (overall + by size/polymer) from spikes: {data}
- Anomaly/watchlist escalations and their dispositions: {data}

Network inputs:
- Instrument calibration-verification history (drift, Westgard flags): {data}
- Maintenance forecast adherence; deferred services; quarantines: {data}
- Sampler condition (mesh/pump/sieve) events: {data}

Produce:
1. Comparability verdict: was the dataset internally consistent (stable LOD,
   recovery, calibration), or are there caveat windows? Name them.
2. Detection-performance summary with the size reporting floor.
3. Network-health summary: which assets are nearing RUL or overdue.
4. Top 3 risks to next quarter's data and the action for each.
5. One targeting/throughput adjustment recommendation for next cycle.
```

## Expected Output

A review memo: a clear comparability verdict (with any caveat windows named), detection and network-health summaries, the top-3 forward risks with owners/actions, and one concrete targeting or throughput change for the next cycle.
