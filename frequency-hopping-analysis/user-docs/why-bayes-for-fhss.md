# Why Bayesian Inference for FHSS Analysis

A short tutorial on why MLE-and-thresholds fails on hopping signals, why Bayesian inference is the right framing, and what concretely changes when you switch.

## The MLE workflow most analysts start with

It looks something like this:

1. Channelize the IQ stream into K candidate channels.
2. For each dwell window, find the channel with maximum energy.
3. Threshold: if max > 6 dB above noise floor, accept that as the hop.
4. String the per-dwell maxima together to get the hop sequence.

This is maximum-likelihood per dwell with a hard threshold. It works on clean captures and falls apart on real ones.

## Where it falls apart

### Spectral leakage between adjacent channels

A burst on channel 14 leaks 13 dB into channel 13 and 15 if you used a rectangular FFT window. At low SNR (say 8 dB above noise on channel 14), the leakage on 13 and 15 is *also* above noise. The argmax bounces between 13, 14, 15 dwell-by-dwell. The MLE per-dwell decision is correct on average — but you see a "hop sequence" that triple-pings every channel, which doesn't match any sequence model and breaks downstream demodulation.

A Bayesian model with a likelihood that explicitly accounts for leakage assigns most posterior mass to channel 14 and small but nonzero mass to 13 and 15. The forward-backward smoother — using the sequence prior — pulls confidently to channel 14 because that's the only channel consistent with the surrounding hops.

### Partial coverage

Your SDR captures 20 MHz but the system hops over 80 MHz. MLE on the energies you see produces a confident posterior on K = 20 channels — wrong by a factor of 4. A Bayesian prior with mass on "channels exist outside band" can return the correct K (or, more honestly, return a posterior that says "K is at least 20 but I can't tell the upper bound from this capture").

### Collisions

Two FHSS radios in the same band, neither of which you knew about. Your dehopper sees energy on two channels in many dwells. Per-dwell MLE picks one of them (whichever leaks slightly more on average) and produces a clean-looking sequence that's wrong half the time. The correct framing is two latent emitters; only an explicit two-emitter Bayesian model recovers them.

### Calibration

MLE never tells you it's wrong. The argmax is always *some* channel. Without a posterior, you can't distinguish "the analyser is confident in channel 14" from "the analyser bounced between 13 and 14 randomly". Both produce the same point estimate.

## Bayesian inference fixes these by construction

### 1. Likelihoods are explicit

You write the noise model and the leakage model. The forward-backward solver gives you the right answer modulo your model — and if your posterior predictive check fails, you know your model is wrong, and you can fix it.

### 2. Priors handle missing data

"Channel exists but I didn't see it" is not a contradiction with a Bayesian prior. It's just a posterior with mass on unobserved channels.

### 3. Calibration is built in

Run the analyser on Bluetooth Classic, where you have ground truth via gr-bluetooth. The posterior either covers the truth or it doesn't. If it doesn't, the model is wrong — and you fix it before trusting it on unknown captures.

### 4. Reporting is honest

Every claim ships with a credibility interval. "Hop rate is 1601 ± 8 hops/s" is qualitatively different from "Hop rate is 1601 hops/s." The interval tells the next analyst (or future-you) how much weight to put on the claim.

## What changes in your workflow

### You write priors explicitly

Old workflow: "I'll set the threshold to 6 dB and see what happens."
New workflow: "I'll set λ_signal / λ_noise = 4 (≈ 6 dB) and see what posterior I get."

These look superficially similar — but the new framing makes the threshold a parameter you can later marginalise over.

### You always calibrate

The Bayesian framing forces calibration: you can't sanity-check a posterior without ground truth. So you always calibrate first. This is good practice you should have been doing anyway, but the threshold-and-MLE workflow makes it tempting to skip.

### You report intervals, not points

Every number in the final report is a 95% CI. Internally, you carry the full posterior so downstream calculations propagate uncertainty.

### Posterior multimodality is information, not noise

If your posterior on hop rate is bimodal at 1600 hops/s and 800 hops/s, that's *informative* — usually it means the capture was too short to see the second hop, and the analyser correctly hedged. With MLE you'd just see the argmax.

## The cost

- Inference is slower (tens of seconds to minutes per capture vs. seconds for MLE).
- You have to write priors, which is a skill.
- Posterior predictive checks add a step and require you to look at outputs, not just trust them.

The cost is real but small. The benefit — knowing when the analyser is wrong — is what makes the workflow trustworthy.

## When MLE is fine

Cleanup captures with high SNR (> 20 dB), well-known target system, full bandwidth coverage, no jamming. In those cases, MLE and Bayesian inference agree to within rounding. Use MLE if you want — but you don't know your capture is in the easy regime until you've done the Bayesian analysis once and confirmed.

In other words: even when MLE is fine, you didn't know it was fine without the Bayesian check.
