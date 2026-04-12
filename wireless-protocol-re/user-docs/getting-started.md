# Getting Started with Wireless Protocol RE

## Step 1: Run /onboard

This configures the workspace for your specific hardware, targets, and goals. Have ready:
- Your SDR model and antenna information
- The device or frequency range you want to analyze
- Your experience level with SDR tools

## Step 2: Discover Signals

Use `/spectrum-sweep` to scan your target frequency range. The optimizer will:
- Prioritize ISM bands and your specified frequencies
- Allocate scan time proportional to expected signal density
- Score discovered signals by novelty, strength, and complexity

## Step 3: Capture Target Signal

Use `/capture-plan` to generate optimized capture parameters:
- Correct sample rate for your signal bandwidth
- Appropriate gain settings for your SDR
- Storage-efficient squelch triggering
- Ready-to-run terminal commands

## Step 4: Decode

Use `/decode-signal` for a guided walkthrough:
- Visual modulation identification
- Demodulation with the right technique
- Bit and frame extraction
- CRC identification

## Step 5: Map the Protocol

Once you have multiple decoded frame types, use `/protocol-map` to build a state machine showing how the protocol works end-to-end.

## Step 6: Document

Use `/report-findings` to generate a formal report suitable for sharing, archiving, or responsible disclosure.

## Tips for Beginners
- Start with a known device (cheap 433 MHz weather station or remote) to learn the workflow
- Use `rtl_433 -R 0 -S all` to save all detected signals for offline analysis
- Inspectrum is your best friend for visual signal identification
- The CRC bruteforce guide in resources/ will save you hours of trial and error
