# /sequence-id — Identify Hop Sequence Type and Recover Seed

Given a per-dwell channel path from `/dehop-bayes`, identify whether the sequence is pseudo-random (PN), table-driven, adaptive (AFH), or unknown. Where possible, recover the seed / table.

## Inputs

- `channel_path.npy` from `/dehop-bayes`
- `quality_mask.npy` from `/dehop-bayes` (skip low-confidence dwells)
- Optional: `--system <bluetooth|wmbus|ble|...>` to enable system-specific recovery

## Steps

### 1. Filter low-confidence dwells
- Drop dwells with quality < 0.7. Track how many were dropped.
- If > 30% are dropped, warn the user that `/dehop-bayes` may need to re-run with a tighter dwell estimate first.

### 2. Period detection
- Run an autocorrelation on the channel index sequence.
- Look for non-trivial peaks indicating a periodic table.
- If no period < `T/2` shows up, table is unlikely (but doesn't rule out long PN).

### 3. Hypothesis tests
Compute log-likelihood under each model:

#### H_pn
- Try to fit an LFSR / Gold code generator. Bluetooth-style table is excluded here (uses §6 below).
- Use Berlekamp-Massey to find minimum LFSR length consistent with the observed sequence.
- If a short LFSR (< 16 bits) reproduces the path, log-likelihood is high.

#### H_table
- Look for periodic repetition. If period `P` is found and matches the fundamental period of an integer-arithmetic generator (e.g. modular hop counter), classify as table.

#### H_afh
- Estimate empirical transition matrix `\hat{A}_AFH`.
- Compare to memoryless (uniform-on-allowed-channels) transition matrix.
- If transition matrix is close to memoryless on a *subset* of channels (the rest being blacklisted), classify as AFH.

#### H_unknown
- Catch-all if none of the above achieves a posterior > 0.5.

### 4. System-specific recovery

#### Bluetooth Classic
- The hop sequence is derived from the LAP (24 bits) and CLK (28 bits) per the Bluetooth Core Spec § 2.6.
- Run UAP-LAP discovery (gr-bluetooth-style): for each LAP candidate, predict the next 32 hops; the LAP that maximises the hit rate is the recovered LAP.
- Confirm by computing the posterior `p(LAP | observed_hops)`.

#### BLE
- The hop sequence is `(c_{t+1} = (c_t + hopIncrement) mod 37)` for non-AFH, modulo channel-map blacklist.
- `hopIncrement ∈ {5..16}`. Try all 12, pick the one that fits.

#### WMBus mode N
- 8-channel table; recover the table directly from the observed sequence.

### 5. Posterior over sequence type
Normalise the four log-likelihoods:
```
P(s | data) ∝ exp(loglik(s)) * prior(s)
```
Default prior: `[0.4, 0.3, 0.2, 0.1]` for `[pn, table, afh, unknown]`. Override per `context/project.md`.

### 6. Output

Write `outputs/<engagement>/sequence-id.json`:

```
{
  "sequence_type_posterior": {
    "pn": 0.05,
    "table": 0.92,
    "afh": 0.02,
    "unknown": 0.01
  },
  "recovered_parameters": {
    "system": "bluetooth-classic",
    "LAP": "0x9E8B33",
    "hop_period": null,
    "lfsr_taps": null,
    "afh_blacklist_count": null
  },
  "n_dwells_used": 1598,
  "n_dwells_dropped_low_confidence": 4,
  "predictability_horizon_dwells": "infinite (deterministic given LAP)",
  "notes": "..."
}
```

Save the recovered hop sequence (full table or generator description) to `outputs/<engagement>/recovered-sequence.txt` in a system-appropriate format.

### 7. Predictability assessment

For the report: how many future hops can we predict given recovered parameters?
- PN: predictable for the lifetime of the seed (all future, until reseed event).
- Table: predictable for one period after which it repeats.
- AFH: predictable for ~seconds (until next AFH update).
- Unknown: not predictable.

Predictability has direct security implications for the system being analysed. **If the recovery is for a security assessment, document the predictability horizon prominently in `/report-findings`.**

## Output

Posterior over sequence type, recovered parameters where possible, and a predictability horizon. Hand to `/report-findings`.
