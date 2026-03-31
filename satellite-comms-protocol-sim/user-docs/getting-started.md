# Getting Started with SATCOM-SIM

## What Is This?

SATCOM-SIM is a Claude agent workspace that makes Claude into a specialist satellite communication protocol engineer. Instead of getting general answers, you get a domain expert who understands protocol bit fields, can compute link budgets from scratch, simulates orbital Doppler effects, and thinks about security the way a DFIR person would.

## Prerequisites

You don't need much to get started:
- A Claude account (claude.ai or API access)
- This workspace folder open in your Claude session
- Optionally: RTL-SDR or HackRF hardware for hands-on satellite work

## Step 1: Open the Workspace

Point Claude at this workspace directory. If you're using Claude with file access, the agent will automatically read the context files and adopt the SATCOM-SIM persona.

## Step 2: Run the Onboard Command

Type `/onboard` to get a brief orientation and let the agent understand what you're trying to accomplish.

## Step 3: Pick Your Use Case

### "I want to receive a satellite"
Tell the agent which satellite (or "any visible with RTL-SDR"), your location, and your equipment. Start with `/orbital-pass` to find the next pass window, then the agent will guide you through GNURadio setup.

### "I'm building a cubesat / ground station"
Use `/simulate-link` to check whether your communication link will close. Then use `/scenario-test` to build a test plan for your protocol implementation.

### "I want to understand CCSDS"
Just ask: "Explain how CCSDS TC transfer frames work." The agent will walk you through the frame structure with annotated examples. Then try `/decode-frame` with a sample frame.

### "I'm researching satellite security"
Start with `/vuln-scan` and describe the protocol or system you're looking at. The agent will apply structured security analysis methods and give you findings with severity ratings.

### "I received something weird and I don't know what it is"
Paste the hex bytes and use `/decode-frame`. The agent will try to identify and parse the protocol.

## Common Commands Reference

```
/onboard           → Get oriented
/simulate-link     → Link budget calculation
/decode-frame      → Parse satellite protocol frames
/scenario-test     → Build a test plan with test vectors
/orbital-pass      → Next pass + Doppler profile
/protocol-compare  → Compare two protocols side-by-side
/parse-telemetry   → Decode telemetry data
/vuln-scan         → Security audit
```

## Tips for Best Results

- **Be specific about your frequency.** "437 MHz" tells the agent a lot about what protocol you're likely using.
- **Mention your hardware.** "RTL-SDR" vs "HackRF" vs "USRP" changes what advice makes sense.
- **Paste actual data.** If you have a hex dump of a frame, paste it. The agent works better with real data than hypotheticals.
- **Say what you're trying to accomplish**, not just what you want to do. "I want to decode this frame" and "I want to test my AX.25 parser handles this edge case correctly" get different answers.

## Example First Session

```
You: /onboard
Agent: [Introduces itself, asks about your use case]

You: I have an RTL-SDR and I want to receive the ISS APRS beacon.
     I'm in San Jose, CA.
Agent: [Runs /orbital-pass equivalent, gives next pass window,
        tuning instructions, GNURadio/Gqrx settings, explains
        what APRS frames to expect]

You: Got a frame! Here's the hex: 7E 82 A0 A4 A6 A8 40...
Agent: [Runs /decode-frame, annotates every field, decodes
        the APRS position report]
```

## Getting Help

If the agent gets confused or goes off-topic, just redirect:
- "Stay focused on satellite protocols"
- "I need you to compute this numerically, not conceptually"
- "Give me the actual byte values, not just a description"
