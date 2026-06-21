# hardware-selection

## Purpose

Use when choosing (or repurposing) SDR hardware for a specific RF problem. Structures the selection against frequency, bandwidth, duplex, dynamic range, link, and budget so the device matches the actual problem rather than being over- or under-bought.

## Prompt Template

```
Acting as the SDR development engineer recommending hardware for an RF problem.

Requirements:

- **Frequency range needed:** [Hz min – max]
- **Instantaneous bandwidth needed:** [VALUE]
- **Duplex:** [receive-only / half-duplex / full-duplex]
- **Dynamic range sensitivity:** [8-bit OK / need 12-bit+ for weak-near-strong]
- **Host link available:** [USB 2.0 / USB 3.0 / PCIe / Ethernet]
- **Budget:** [VALUE]
- **Form factor:** [desktop / embedded / portable]
- **Application:** [what it's for — informs the tradeoffs]

Please:
1. Filter the hardware matrix by frequency range (eliminate devices that can't reach the band).
2. Filter by instantaneous bandwidth.
3. Filter by duplex requirement (half-duplex devices eliminated if full-duplex needed).
4. Filter by ADC bits / dynamic range.
5. Check link compatibility (high sample rates need USB 3.0 / PCIe / 10GbE).
6. Rank survivors by budget + form-factor fit.
7. Recommend primary + fallback with the specific spec tradeoffs called out.
8. Flag any requirement no single device satisfies (forcing a converter or multi-device setup).
```

## Expected Output

- Candidate filter table (pass/fail per criterion)
- Primary + fallback recommendation with tradeoffs
- Link/host compatibility note
- Approximate cost
- Any unmet requirement forcing a compromise

## Notes

- Don't over-buy: a spectrum monitor doesn't need a full-duplex 16-bit USRP. Match hardware to the actual RF problem.
- Full-duplex requirement eliminates HackRF (half-duplex) — steers to USRP / Lime / BladeRF / Pluto.
- Weak-signal-near-strong needs 12-bit+ dynamic range; 8-bit devices (RTL, HackRF) will be limited.
- If no single device covers the frequency range, consider an up/downconverter or a multi-device setup.
