# Workflows — End-to-End FHSS Analysis

Four canonical workflows. Each step references the slash command that automates it. The agent picks a workflow at the start of each engagement based on what's in `context/project.md`.

## Workflow A — "Is this even hopping?" (Triage)

**When:** New unknown signal. Hopping not yet confirmed.

```
   /hop-detect <capture>
       │
       │   posterior on hop rate
       │   P(hopping) > 0.9?  ──── NO ──→  Treat as fixed-frequency. Hand to a
       │                                    standard SDR analysis workflow.
       │
       ▼  YES (or P(hopping) ∈ [0.3, 0.9])
   /dwell-estimate <capture>
       │
       │   posterior on T_d
       │
       ▼
   Decision:
     - Confident hop rate + dwell ─→ proceed to Workflow B
     - Posterior multimodal ─────→ capture more data, re-run /hop-detect
     - Posterior peaked at 0 hops/s ─→ fixed signal; close
```

The triage workflow is intentionally cheap. `/hop-detect` runs in seconds on a 1 s capture; `/dwell-estimate` adds another few seconds. Don't burn time on full dehopping until both are confident.

## Workflow B — Full Reverse Engineering (Public-Band Target)

**When:** Hopping is confirmed, target is in a band the user is authorised to receive (ISM consumer, range-authorised tactical with WMBus / similar).

```
   /hop-set-prior  ──→  Builds prior on candidate hop frequencies from:
       │                 - Regulator filings (FCC ID lookup)
       │                 - User's stated target system
       │                 - Observed spectrum activity
       │
       ▼
   /dehop-bayes  ─────→  Per-dwell channel posterior + Viterbi MAP path.
       │                 Outputs: channel_path.npy, posterior_marginals.npz,
       │                          dehopped IQ stream (per-channel concatenated)
       │
       ▼
   /sequence-id  ─────→  Identifies sequence type. If PN or table, attempts
       │                 seed/table recovery. If AFH, characterises kernel.
       │                 Outputs: sequence_type.json with posterior over types.
       │
       ▼
   Hand off dehopped IQ to:
       - URH for protocol decoding
       - GNU Radio flowgraph for demod
       - rtl_433 if a known-protocol candidate emerged
       │
       ▼
   /report-findings  ──→  Structured Bayesian report.
```

### B-Decision: When to give up on sequence recovery

If `/sequence-id` returns `posterior(s = unknown) > 0.5`, the sequence is not recoverable from this capture. Either:
- The sequence is cryptographic (and recovery is out of scope without authorisation).
- The capture is too short (extend, re-run from `/hop-detect`).
- The PN register is too long for the available SNR (compute information-theoretic limit per `domain-knowledge.md` §7).

Document the limit in the report rather than chasing it.

## Workflow C — Calibration

**When:** Before trusting the analyser on an unknown signal. **Mandatory** at the start of every new physical environment / SDR setup.

```
   1. Put a phone (any modern Android or iPhone) into Bluetooth pairing mode
      within ~3 m of the SDR antenna.
   2. Capture: 80 MS/s, 2.441 GHz center, 1 s, gain ~40 dB.
      hackrf_transfer -f 2441500000 -s 80000000 -a 0 -l 32 -g 40 \
                      -r calibration.iq -n 80000000
   3. Run the full Workflow A → Workflow B pipeline.
   4. Validate:
        - Posterior on hop rate peaked in [1590, 1610] hops/s with > 0.9 mass?
        - Posterior on K peaked at 79?
        - /sequence-id returns s = "table" with > 0.7 mass (Bluetooth Classic
          is not PN — it's a deterministic table given LAP)?
        - At least one LAP recovered?
   5. If any check fails:
        - Re-check antenna, gain, distance.
        - Re-run with `--fixed-prior bluetooth-classic` to constrain the model.
        - If still failing, either the capture or the model is broken.
   6. Save calibration evidence in `outputs/calibration-<date>/`.
```

**Rule:** No production analysis runs unless calibration ran in the same session and passed.

## Workflow D — Adversarial / Jammer Triage

**When:** Existing FHSS link reports failures and operator suspects jamming.

```
   /jammer-flag <capture>
       │
       │   posterior over {none, narrowband, sweep, follower}
       │
       ▼
   Branch:
     • narrowband > 0.5 ──→ Identify jamming frequency, characterise duty
                           cycle, produce coexistence recommendation.
     • sweep      > 0.5 ──→ Estimate sweep rate and bandwidth. Compare against
                           catalogued sweep-jammer profiles.
     • follower   > 0.5 ──→ Estimate response delay and frequency lock.
                           Critical: follower jammers indicate adversary
                           with sophisticated SDR + low latency. Escalate.
     • none       > 0.5 ──→ Failure is not jamming — investigate co-channel
                           collisions, hardware faults, or AFH-triggered
                           channel exclusion.
       │
       ▼
   /report-findings (with jammer focus)
```

### D-Important
Follower-jammer detection has a high false-positive rate against legitimate AFH systems whose adaptation looks superficially similar. The agent must report the posterior, not the MAP — let the user decide what threshold warrants escalation.

## Cross-Workflow Decision Trees

### Should I extend the capture?

```
   ┌──────────────────────────────────────────┐
   │ Is posterior on R_h multimodal?          │── YES ──→  Extend by 5×
   └────────┬─────────────────────────────────┘
            │ NO
            ▼
   ┌──────────────────────────────────────────┐
   │ Is posterior CI on R_h > 10% of mean?    │── YES ──→  Extend by 2×
   └────────┬─────────────────────────────────┘
            │ NO
            ▼
   ┌──────────────────────────────────────────┐
   │ Is sequence-id confidence < 0.7?         │── YES ──→  Extend by 5×
   └────────┬─────────────────────────────────┘
            │ NO
            ▼
        Capture is sufficient.
```

### Should I narrow the prior?

If the posterior is sharply concentrated where the prior is flat, narrowing the prior won't change much — leave it and document. If the posterior runs into a prior boundary, the prior is too tight — widen it.

## Outputs Convention

Every workflow writes to `outputs/<YYYY-MM-DD>-<engagement-name>/`:

- `capture.sigmf-meta` + `capture.sigmf-data` — original IQ with full metadata
- `posterior.npz` — saved posterior samples
- `channel_path.npy` — MAP per-dwell channel index
- `spectrogram_with_path.png` — visual overlay
- `report.md` — `/report-findings` output
- `calibration.json` — link to the calibration run that authorised this analysis

Never edit a previous engagement's outputs directory. If the engagement is re-run, write a new dated directory and link.
