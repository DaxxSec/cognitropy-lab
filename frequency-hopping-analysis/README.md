# Frequency Hopping Analysis Workspace

> A Claude Agent Workspace for detecting, dehopping, and reverse-engineering frequency-hopping spread-spectrum (FHSS) radios from SDR captures, using Bayesian probability assessment to recover hop sets, dwell times, and sequences under low SNR and partial-observation conditions.

## What This Workspace Does

Frequency hopping is hard to analyse with the visual-waterfall workflow that suffices for fixed-frequency signals. A 1600-hops/s Bluetooth radio sweeps 79 channels in 50 ms — by the time you see the burst, it's gone. A SINCGARS net hops over the entire 30–88 MHz VHF band with cryptographic sequences. A LoRa channel-hopping deployment looks like noise unless you pre-channelise and integrate.

This workspace turns your SDR capture (HackRF, USRP B2xx/X310, BladeRF, RTL-SDR for narrowband studies) into a structured Bayesian analyser. Instead of guessing hop rate from a spectrogram, the agent maintains a posterior `p(hop_set, hop_rate, dwell, sequence | observations)` and updates it as you feed in more bursts. You see calibrated uncertainty — not "I think it's hopping at 100/s," but "P(hop_rate ∈ [98, 103] hops/s | data) = 0.94, with a secondary mode near 50 hops/s if every-other-burst was missed."

The pipeline covers detection (is this even hopping?), characterisation (rate, dwell, set size), dehopping (channelize + select best channel per dwell window), sequence identification (pseudo-random vs. table vs. AFH), and adversarial-signal flagging (narrowband jammers, sweep jammers, follower jammers operating inside the hop set).

## Why This Workspace Exists

Two reasons.

**The first** is that frequency hopping defeats the standard "tune, demodulate, decode" SDR loop. Operators new to FHSS typically run `rtl_433` or `URH` on a hopping signal, see garbage, and conclude the signal is encrypted. It's usually not — they're decoding 1/N of the bursts. Dehopping has to come first.

**The second** is that hop-set / dwell / sequence estimation is fundamentally a problem of inference under uncertainty. Channel detectors fire and misfire. Bursts get lost in noise or stomped by collisions. The "right" answer depends on a prior — what kind of radio is this, what regulator filings say, what other captures look like. Bayesian inference is the only honest way to handle that. Maximum-likelihood point estimates and rule-of-thumb thresholds give wrong answers ~30% of the time on real captures and don't tell you when they're wrong. Posteriors do.

## Getting Started

### Prerequisites

- **SDR hardware capable of capturing the full hop range simultaneously.** For 2.4 GHz Bluetooth-class systems: ≥ 80 MHz instantaneous bandwidth (USRP B210, X310, BladeRF 2.0, LimeSDR). For VHF/UHF tactical: 30–88 MHz coverage in one or two captures. For narrowband (< 1 MHz hop set): even an RTL-SDR works.
- **Storage.** A 100 MS/s 16-bit IQ capture eats 400 MB/s. Plan for ≥ 1 TB if you're recording full sessions.
- **Python 3.10+** with `numpy`, `scipy`, `matplotlib`, `pymc` (Bayesian inference), `numba` (JIT for the channel-energy loop), `sigmf` (capture metadata).
- **GNU Radio 3.10** for IQ I/O and channelisation flowgraphs.
- **Legal authorisation** to receive the target system. See `context/constraints.md` and the Legal & Ethical section below.

### Quick Start

1. Clone this workspace.
2. Run `/onboard` — the agent will gather SDR hardware details, target system info, hop-set hypotheses, and legal authorisation, then write `context/project.md`, `context/role.md`, `context/constraints.md`, `context/for-agent/environment.md`.
3. Take a wideband capture covering the suspected hop range (e.g. `hackrf_transfer -f 2441500000 -s 80000000 -a 0 -l 32 -g 40 -r capture.iq -n 80000000` for an 80 MS/s, 1 s 2.4 GHz dump).
4. Run `/hop-detect capture.iq` — the agent decides hopping vs. fixed and gives a posterior on hop rate.
5. If hopping is confirmed, run `/hop-set-prior` to build a prior on candidate channels.
6. Run `/dehop-bayes` to recover the per-dwell channel sequence and dehopped baseband.
7. Hand the dehopped stream to your demodulator (URH, GNU Radio, custom Python).

### Calibration Day

Before trusting the analyser on an unknown signal, run the full pipeline on a known one. Bluetooth Classic from a phone in inquiry mode is the canonical calibration target — 79 channels, 1 MHz spacing, 1600 hops/s, 625 µs dwell, hop sequence determined by LAP. If the posterior on hop rate doesn't peak inside [1590, 1610] hops/s with > 0.9 mass, fix the prior or likelihood before going further.

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/onboard` | Gather SDR setup, target system, hop hypotheses, authorisation | First-time setup |
| `/hop-detect` | Detect hopping vs. fixed signal, posterior on hop rate and dwell | First analysis pass on any new capture |
| `/hop-set-prior` | Build prior `p(channel_active)` from filings, leaks, observed energy | Before running the dehopper, especially on novel systems |
| `/dehop-bayes` | Run Bayesian dehopper: per-dwell channel posterior + Viterbi MAP path | After hop detection confirms hopping |
| `/dwell-estimate` | Posterior on dwell time, guard intervals, jitter | When demodulation fails despite a confident hop-set |
| `/sequence-id` | Identify sequence type (PN / table / AFH); recover seed if possible | After dehop produces a clean per-dwell channel index list |
| `/jammer-flag` | Detect narrowband, sweep, and follower-jammer interference | When dehop posterior has anomalous rejected dwells |
| `/report-findings` | Generate structured Bayesian-FHSS report with credibility intervals | At end of an engagement / analysis cycle |

## Directory Structure

```
frequency-hopping-analysis/
├── CLAUDE.md                              # Agent role + foundational instructions
├── README.md                              # This file
├── CREATION_REPORT.md                     # Workspace genesis details
├── context/
│   ├── project.md                         # Target system, scope, success criteria (filled by /onboard)
│   ├── role.md                            # Your background, RF + Bayes experience
│   ├── constraints.md                     # Legal, jurisdictional, scope boundaries
│   └── for-agent/
│       ├── domain-knowledge.md            # FHSS theory, hop-set design, Bayesian model
│       ├── workflows.md                   # End-to-end analysis workflows w/ decision trees
│       ├── environment.md                 # SDR hardware, software stack, capture rig
│       └── tools.md                       # Tool configurations, capture commands, GR flowgraphs
├── .claude/commands/
│   ├── onboard.md
│   ├── hop-detect.md
│   ├── hop-set-prior.md
│   ├── dehop-bayes.md
│   ├── dwell-estimate.md
│   ├── sequence-id.md
│   ├── jammer-flag.md
│   └── report-findings.md
├── prompts/
│   ├── unknown-fhss-triage.md             # Quick triage for an unfamiliar hopping signal
│   ├── bluetooth-classic-calibration.md   # End-to-end calibration on Bluetooth Classic
│   └── prior-elicitation.md               # Structured interview to elicit a hop-set prior
├── resources/
│   ├── known-fhss-systems.md              # Reference table of common hopping radios
│   ├── bayesian-likelihood-models.md      # Likelihood model derivations for the analyser
│   └── channelizer-design-notes.md        # Polyphase channelizer choices and pitfalls
├── planning/                              # Active analysis plan, pivot history
├── outputs/                               # Posteriors, dehopped streams, reports, plots
├── user-docs/
│   ├── getting-started.md                 # Quick-start narrative
│   └── why-bayes-for-fhss.md              # Tutorial: why MLE fails on hopping signals
└── work-log/
    └── session-log.md                     # Session log template
```

## The Bayesian Model in One Page

Define the latent state at dwell `t` as `c_t ∈ {1..K}` (which of K candidate channels is in use), with parameters:

- `θ = (hop_rate, dwell, guard, K)` — system-level hyperparameters with their own priors
- `s` — sequence type: `s ∈ {pn, table, afh, unknown}`
- `seed` — sequence seed (if `s = pn` or `s = table`)

Likelihood per dwell window: a multi-channel energy detector emits `e_{t,k}` for each candidate channel `k`; we model it as `e_{t,k} ~ Exponential(λ_signal)` if `c_t = k` else `e_{t,k} ~ Exponential(λ_noise)`, with `λ_signal / λ_noise` learned from a quiet portion of the capture.

Prior on `c_t`: depends on `s`. For PN sequences, `c_t = f(seed, t)` deterministically given seed; we sum out the seed with a uniform prior over the seed space (small enough to enumerate for short PN, otherwise importance-sampled). For AFH, `p(c_t | c_{t-1})` is a learned Markov kernel.

Posterior is computed via Viterbi for MAP `(c_1, .., c_T)` and forward-backward for marginals. PyMC handles the hyperparameter posterior on `θ`. See `context/for-agent/domain-knowledge.md` for derivations and `resources/bayesian-likelihood-models.md` for code.

## Example Use Cases

### Bluetooth Classic Inquiry-Mode Recovery
You captured 1 s of 2.4 GHz spectrum during a phone discovery scan. The agent confirms 1600 hops/s, recovers the LAP from the hop sequence (Bluetooth's LAP-derived hop is reversible from sequence observation), and identifies the master device.

### Proprietary IoT Sensor Network
A smart-meter network in 902–928 MHz hops over a 50-channel set. The agent detects hopping, builds a prior from FCC ID filings, runs the dehopper, identifies the sequence as table-driven with a 16-period repeat, and recovers the table for downstream demodulation by URH.

### Adaptive Frequency Hopping (AFH) Bluetooth
Bluetooth Low Energy in a noisy 2.4 GHz environment uses AFH to avoid Wi-Fi channels. The agent characterises the AFH adaptation rate, identifies which channels are blacklisted by the master, and infers the Wi-Fi co-tenant's primary channel.

### Tactical-Style Hopping Net (Authorised Range)
On an authorised range, an agency-approved tactical radio hops over 30–88 MHz at 100 hops/s with a cryptographic sequence. The agent characterises hop rate, dwell, and channel set without recovering the cryptographic sequence (which is out of scope), produces a public-band interference report, and flags suspected follower-jammer activity.

### Spectrum Forensics — Was This Capture Jammed?
A capture of an FHSS link with intermittent failures. The agent's `/jammer-flag` runs a Bayesian classifier on each dwell, flags 12% of dwells as having a co-channel narrowband interferer, and produces a time-frequency map of the jamming.

## Recommended MCP Servers

- **filesystem** — IQ capture I/O, posterior pickling, output reports
- **shell** — Run `hackrf_transfer`, `uhd_rx_cfile`, GNU Radio flowgraphs, `gr-bluetooth`
- **python** — Custom analyzer code, PyMC inference, numba-accelerated channelization

## Legal & Ethical Considerations

- **Authorisation.** Receive only signals you own, are publicly broadcast (e.g. ISM-band consumer radios), or have explicit written authorisation to test. Many jurisdictions criminalise reception of certain bands (cellular, public-safety, certain federal allocations) regardless of intent.
- **18 USC 2511 / Wiretap Act (US).** Receiving and decoding the *content* of certain communications (cellular, public-safety encrypted traffic) is illegal even passively. This workspace's recovery of hop sequences is for system characterisation; do not chain it to content recovery on protected systems.
- **Encryption.** If a hopping radio also encrypts payload, this workspace recovers the hop sequence only — never the encryption key. Cryptographic recovery is out of scope and requires separate authorisation.
- **Transmission.** Never transmit on a hopping system without proper licensing. Replay attacks, follower jamming, and spoofing of hopping radios are serious crimes.
- **Disclosure.** If you discover a vulnerability (predictable hop sequence, weak PRNG seed) in a commercial product, follow responsible disclosure with the vendor and CISA / national CERT before public release.

## Technical References

- [Bluetooth Core Specification 5.4 — Vol 2 Part B (Baseband)](https://www.bluetooth.com/specifications/specs/) — authoritative Bluetooth Classic / AFH hop sequence definition
- [GNU Radio gr-bluetooth](https://github.com/greatscottgadgets/gr-bluetooth) — open Bluetooth Classic dehopper, useful as a likelihood-model reference
- [UBertooth project](https://github.com/greatscottgadgets/ubertooth) — Michael Ossmann's Bluetooth analyser; the `bluetooth_rxtx.c` BR/EDR FHSS code is the canonical reference implementation
- [Adafruit / Sparkfun FHSS application notes](https://learn.adafruit.com/) — accessible FHSS theory for IoT modules
- [PyMC Documentation](https://www.pymc.io/) — the Bayesian inference framework this workspace relies on
- [SigMF Specification](https://sigmf.github.io/SigMF/) — capture metadata format used throughout
- [FCC ID Lookup](https://fccid.io) — to pull regulator filings on commercial FHSS products for prior elicitation
- [Skolnik, *Introduction to Radar Systems*, 3rd ed.](https://www.mheducation.com/) — Chapter on frequency-agile radar covers FH theory rigorously (radar, but the math is the same)
- [Sigidwiki Frequency Hopping page](https://www.sigidwiki.com/wiki/Frequency-hopping_spread_spectrum) — public catalogue of identified hopping signals with examples
