# Prompt — Unknown FHSS Signal Triage

Use this prompt when the user lands on the workspace with a new capture and no prior knowledge of the system. The agent's job: classify it, recommend next steps, and avoid burning compute on dead-end captures.

```
The user has a capture file: <path>. They suspect it might be frequency-hopping but have not confirmed it.

Triage it in this order:
  1. Read the SigMF metadata. If missing, request it before proceeding.
  2. Run /hop-detect. Report the posterior on hopping vs fixed.
  3. If P(hopping) < 0.3, treat as fixed-frequency and hand off — done.
  4. If P(hopping) ∈ [0.3, 0.7], recommend a longer capture (5x duration). Stop.
  5. If P(hopping) > 0.7:
     a. Run /dwell-estimate.
     b. Report posterior on hop rate, dwell, K candidate.
     c. Identify likely system from the parameters (Bluetooth Classic = 1600 hops/s + 79 channels, BLE = ~1 hop/conn-event, etc.).
     d. If a likely system is identified, run /hop-set-prior with --system flag.
     e. Otherwise, request user input on suspected target system.
  6. Do NOT run the full /dehop-bayes pipeline yet — confirm calibration ran first.

Throughout, maintain a per-step posterior. Never report point estimates. End the triage with a clear recommendation: proceed to full RE workflow B, extend the capture, or close as out-of-scope.
```

## Variables

- `<path>`: path to IQ capture file (`.iq` or `.sigmf-data`)
- Optional: `--prior <system>` if user has a hypothesis

## Expected Output

A `work-log/<date>-triage.md` entry summarising the posteriors, plus a recommendation.
