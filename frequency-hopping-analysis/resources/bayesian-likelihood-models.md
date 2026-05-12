# Reference — Bayesian Likelihood Models

Reference implementations for the per-dwell channel likelihood, the forward-backward HMM, and Viterbi MAP. These are the math + code the dehopper relies on.

## Notation

- `T` = number of dwell windows
- `K` = number of candidate channels
- `e[t, k]` = energy detector output for channel k at dwell t (T × K matrix, real, positive)
- `c[t]` ∈ {1, ..., K} = latent channel index at dwell t
- `λ_signal`, `λ_noise` = Exponential rate parameters for signal/noise hypotheses
- `π[k]` = per-step prior on channel k from `/hop-set-prior`
- `A[k, k']` = transition probability from channel k to k' (sequence model)

## 1. Per-dwell channel likelihood

```python
def per_dwell_loglik(e_t, lam_signal, lam_noise):
    """
    e_t: (K,) array of energies at this dwell
    Returns (K,) array of log p(e_t | c_t = k) for each k.
    """
    import numpy as np
    K = e_t.shape[0]
    loglik = np.zeros(K)
    for k in range(K):
        # If c_t = k, channel k is signal; all others are noise.
        ll_signal_k = np.log(lam_signal) - lam_signal * e_t[k]
        ll_noise_others = sum(
            np.log(lam_noise) - lam_noise * e_t[j]
            for j in range(K) if j != k
        )
        loglik[k] = ll_signal_k + ll_noise_others
    return loglik
```

Numba-compile this; it's the inner loop of the dehopper.

## 2. Forward-backward HMM

```python
def forward_backward(loglik, log_pi, log_A):
    """
    loglik: (T, K) per-dwell log-likelihoods
    log_pi: (K,) log of initial / per-step prior
    log_A:  (K, K) log transition matrix (use uniform if sequence type unknown)
    Returns: log_alpha (T,K), log_beta (T,K), log_gamma (T,K) marginals.
    """
    import numpy as np
    from scipy.special import logsumexp

    T, K = loglik.shape
    log_alpha = np.full((T, K), -np.inf)
    log_beta  = np.full((T, K), -np.inf)

    log_alpha[0] = log_pi + loglik[0]
    for t in range(1, T):
        for k in range(K):
            log_alpha[t, k] = loglik[t, k] + logsumexp(log_alpha[t-1] + log_A[:, k])

    log_beta[T-1] = 0.0
    for t in range(T-2, -1, -1):
        for k in range(K):
            log_beta[t, k] = logsumexp(log_A[k, :] + loglik[t+1] + log_beta[t+1])

    log_gamma = log_alpha + log_beta
    log_gamma -= logsumexp(log_gamma, axis=1, keepdims=True)
    return log_alpha, log_beta, log_gamma
```

`log_gamma` is the per-dwell channel posterior. Used directly by `/dehop-bayes`.

## 3. Viterbi MAP path

```python
def viterbi(loglik, log_pi, log_A):
    """
    Returns the MAP path (T,) over channel indices.
    """
    import numpy as np
    T, K = loglik.shape
    delta = np.full((T, K), -np.inf)
    psi = np.zeros((T, K), dtype=np.int64)

    delta[0] = log_pi + loglik[0]
    for t in range(1, T):
        for k in range(K):
            scores = delta[t-1] + log_A[:, k]
            psi[t, k] = np.argmax(scores)
            delta[t, k] = loglik[t, k] + scores[psi[t, k]]

    path = np.zeros(T, dtype=np.int64)
    path[T-1] = np.argmax(delta[T-1])
    for t in range(T-2, -1, -1):
        path[t] = psi[t+1, path[t+1]]
    return path
```

## 4. Sequence-type-conditional transition matrices

### Uniform (`s = unknown`)
```python
log_A = np.full((K, K), -np.log(K))
```

### Bluetooth-style table (`s = table`, system = bluetooth-classic)
```python
# Build deterministic A given LAP, CLK, t.
# log_A becomes very sparse: log_A[k, hop_table(k, LAP, CLK, t)] = 0, else -inf.
# In practice, marginalise over LAP by enumeration.
```

### AFH (`s = afh`, BLE-style)
```python
# Empirical: estimate A from observed channel sequence (assumed mostly correct from initial Viterbi pass).
# Apply sparsity prior: most entries of A should be near uniform on a subset (active channels).
```

### PN sequence (`s = pn`)
```python
# Deterministic given seed: same sparse A as table, but with a much larger seed space.
# For LFSR with register length L, enumerate seeds (2^L); for Bluetooth-style 28-bit hop input,
# enumerate is infeasible — instead, compute hop sequence for each candidate LAP (24 bits) and
# pick the one that maximises forward likelihood.
```

## 5. Hyperparameter inference with PyMC

```python
import pymc as pm
import numpy as np

def fit_hyperparameters(energies, prior):
    """
    energies: (T, K) energy matrix
    prior: dict from /hop-set-prior
    """
    with pm.Model() as model:
        log_R_h = pm.Uniform("log_R_h", lower=0, upper=5)  # log10 hops/s
        R_h = pm.Deterministic("R_h", 10**log_R_h)
        duty = pm.Beta("duty", alpha=8, beta=2)

        log_lam_signal = pm.Normal("log_lam_signal",
                                   mu=np.log(estimate_lam_signal(energies)),
                                   sigma=0.5)
        log_lam_noise = pm.Normal("log_lam_noise",
                                  mu=np.log(estimate_lam_noise(energies)),
                                  sigma=0.5)

        loglik = compute_marginalised_loglik(
            energies, R_h, duty, np.exp(log_lam_signal), np.exp(log_lam_noise), prior
        )
        pm.Potential("loglik_potential", loglik)

        trace = pm.sample(2000, tune=1000, chains=4, target_accept=0.9)

    return trace
```

`compute_marginalised_loglik` runs the forward pass and returns the log-marginal-likelihood (sum of `log_alpha[T-1]`). The forward pass should be JIT-compiled with numba and accept symbolic PyMC tensors via PyTensor's `Op` interface. See PyMC's HMM examples for the pattern.

## 6. Posterior predictive check

```python
def ppc_check(trace, observed_energies):
    """Sample synthetic captures from the posterior; compare to observed."""
    import arviz as az
    posterior_samples = az.extract(trace, num_samples=200)
    synthetic_summaries = []
    for sample in posterior_samples:
        synthetic = simulate_capture(sample.R_h, sample.duty, ...)
        synthetic_summaries.append(summarise(synthetic))
    observed_summary = summarise(observed_energies)
    kl = compute_kl(observed_summary, synthetic_summaries)
    return kl
```

KL > 0.5 indicates likely model misspecification; the dehopper command warns and recommends remediation.

## 7. Numerical notes

- Always work in log space. `K = 79` channels, `T = 1600` dwells/sec → `T*K ≈ 10^5` per second; floating-point underflow is real.
- `scipy.special.logsumexp` over the whole row is the right primitive.
- Numba-compile the forward-backward inner loop with `@njit(parallel=True)` — gives ~50× speedup on a 4-core CPU.
- For full-band Bluetooth captures, prefer X310 + 100 MS/s. PFB at 80 channels at 100 MS/s decimates to 1.25 MS/s per channel; comfortable for 1 MHz Bluetooth modulation.

## 8. Testing

Unit tests in `tests/` (referenced from `outputs/`, not committed by the daily build):

- `test_forward_backward_consistency()` — α·β should equal the marginal evidence at every t
- `test_viterbi_vs_argmax_marginal()` — for a deterministic sequence, Viterbi MAP should equal per-dwell argmax
- `test_calibration_bluetooth_classic()` — full pipeline on a recorded BT calibration capture should recover LAP

Run before any model change.
