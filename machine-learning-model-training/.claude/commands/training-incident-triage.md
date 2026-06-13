# /training-incident-triage

First responder for any live training failure: capture the first signal, assign a severity, classify the failure, and route to the correct runbook.

## Inputs

- The first anomalous signal and when it appeared (metric name, value, timestamp, training step)
- Run metadata: model size, parallelism degrees, precision, LR/schedule, batch size, hardware/fleet
- Access to recent logs (loss, grad_norm, throughput, GPU mem/util, scheduler/NCCL messages)
- (Optional) the previous known-good run/config for comparison

## Steps

1. **Snapshot state.** Record current step, loss, grad_norm, throughput, GPU memory headroom, and whether the process is still stepping. Note the *first* anomalous signal, not just the loudest symptom.
2. **Check liveness.** Is the run still producing steps/heartbeat? If not, decide crash vs hang vs preemption.
3. **Assign severity** using the `concepts.md` taxonomy: blast radius × reversibility → SEV-1…SEV-4. Decide page-now vs defer.
4. **Classify the failure** with the Phase-2 decision tree in `workflows.md` (finite loss? throughput at baseline? data trustworthy?).
5. **Route** to the matching runbook from the symptom→runbook table in `references.md`, and state the *one* immediate stabilising action to take first.
6. **Open the incident record** (timeline scaffold) in `outputs/`.

## Output

An incident header written to `outputs/incident-<date>-<short-id>.md`: severity, failure class, the routed runbook, the first stabilising action, and an empty timeline ready for the responder to fill.

## Notes

- Triage is fast and reversible — over-classify severity rather than under; you can downgrade later.
- If two classes seem to apply (e.g. OOM *and* throughput drop), pick the one that is *causal* (OOM crashing → recovery first).
- Do not start root-causing here; this command only routes.
