# Protocol Reverse Engineering Intake

Use this template when you have an unknown sensor and want to begin a systematic RE session.

---

## Prompt Template

```
I have an unknown TPMS sensor I want to reverse engineer. Here is what I know:

**Sensor physical info:**
- Vehicle: [YEAR MAKE MODEL] or [Unknown]
- FCC ID (if visible on sensor): [FCC ID or N/A]
- Part number: [P/N or N/A]
- Frequency found on: [315 / 433.92 / other] MHz

**Capture info:**
- Capture file: [filename.cu8] (attached/available)
- Sample rate used: [e.g., 250k]
- Duration: [X seconds]
- rtl_433 output (raw/unknown packets): [PASTE HERE]

**What rtl_433 shows:**
[PASTE rtl_433 -r capture.cu8 output here]

**What I've observed in inspectrum / URH so far:**
- Pulse widths: short=[X µs], long=[Y µs]
- Modulation appears to be: [OOK / FSK / unclear]
- Packet appears ~[N] bits long
- [Any other observations]

Please help me:
1. Confirm signal characterization from the capture
2. Extract and align a clean bit stream from multiple packets
3. Identify the packet structure (preamble, sync, fields, checksum)
4. Map the pressure and temperature fields
5. Determine the checksum algorithm
6. Draft an rtl_433 flex decoder configuration
```

---

## Tips

- Capture at least 2–3 minutes of driving to get 5–10 packets for comparison
- Note physical pressure reading from a gauge at capture time — this is your ground truth for identifying the pressure byte
- If you can vary a known value (e.g., deflate one tire slightly, recapture), field isolation becomes much easier
