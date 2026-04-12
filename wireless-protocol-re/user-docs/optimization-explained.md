# How the Optimization Algorithms Work

This workspace uses five resource optimization algorithms to make wireless protocol RE more efficient. Here is what each does in plain language.

## 1. Weighted Spectrum Scheduling

**Problem:** Your SDR can only look at a small slice of spectrum at a time (e.g., 20 MHz with HackRF), but you want to survey a wide range (maybe 300 MHz to 1 GHz).

**Solution:** Instead of scanning sequentially from low to high frequency, we assign priority scores to each frequency band. ISM bands (433, 868, 915 MHz) get higher priority because they have more interesting signals. Your specified target frequencies get the highest priority. We scan high-priority bands first, so you find interesting signals faster.

## 2. Adaptive Dwell Time

**Problem:** How long should you listen to each frequency band before moving on? Too short and you miss intermittent signals. Too long and you waste time on empty spectrum.

**Solution:** We use a "multi-armed bandit" approach (like deciding which slot machine to play). We start by spending equal time on each band, then gradually shift more time to bands where we're finding signals. A small percentage of time is always reserved for exploring new bands in case something was missed.

## 3. Signal Priority Queuing

**Problem:** Your spectrum sweep found 20 signals. Which do you analyze first?

**Solution:** Each signal gets a score based on four factors: novelty (does it match a known protocol?), signal strength (stronger = easier to analyze), duty cycle (more active = more data to work with), and complexity (more complex modulation = potentially more interesting). Signals are ranked by this composite score.

## 4. Capture Storage Optimization

**Problem:** Raw IQ data is enormous. At 20 Msps, you fill 144 GB per hour. Most of that is silence.

**Solution:** Squelch-triggered capture only records when a signal is actually present. Decimation reduces sample rate when you don't need the full bandwidth. Compression (zstd) typically achieves 2-4x reduction on RF data. Combined, these can reduce storage by 10-100x for intermittent signals.

## 5. Parallel Analysis Pipeline

**Problem:** Decoding signals takes time. If you have multiple signals to analyze, doing them one at a time is slow.

**Solution:** We model the analysis pipeline as a graph of tasks. Some tasks can run in parallel (demodulating two different signals at the same time), while others must be sequential (you can't do frame analysis before demodulation). The scheduler figures out the optimal execution order and allocates CPU resources accordingly.
