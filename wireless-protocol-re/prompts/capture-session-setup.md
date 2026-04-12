# Capture Session Setup Prompt

## Purpose
Use this prompt to quickly configure an optimized capture session for a specific target device or frequency.

## Prompt Template

I need to set up a capture session for:

- **Target:** [e.g., wireless doorbell, car keyfob, LoRa sensor]
- **Expected frequency:** [e.g., 433.92 MHz, or "unknown, probably 315 or 433"]
- **My SDR:** [e.g., RTL-SDR v3]
- **Available storage:** [e.g., 50 GB]
- **Time available:** [e.g., 2 hours]
- **Goal:** [e.g., capture enough data to decode the protocol]

Please:
1. Calculate optimal sample rate, gain, and bandwidth settings
2. Estimate how many transmissions I need to capture for reliable analysis
3. Provide the exact capture command(s) to run
4. Set up squelch/triggered capture if appropriate to save storage
5. Recommend a file naming convention and session logging approach
6. Estimate total storage consumption and processing time

If the frequency is uncertain, provide a quick scan command first to locate the signal.

## Expected Output
- SDR configuration parameters with rationale
- Ready-to-run capture commands
- Storage and time estimates
- Session logging template
