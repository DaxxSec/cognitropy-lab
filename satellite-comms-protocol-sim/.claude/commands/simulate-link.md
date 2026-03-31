# simulate-link

Run a complete end-to-end RF link budget simulation.

When this command is invoked:

1. **Gather parameters** — Ask the user for:
   - Satellite orbital regime and approximate altitude (or specific satellite name)
   - Frequency band and specific frequency
   - Transmit power (watts or dBm/dBW)
   - Transmit antenna type or gain (e.g., "monopole on satellite", "9-element Yagi")
   - Receive antenna type or gain
   - Protocol and target data rate
   - Required BER or just "does it close?"
   - Ground station location (optional, for elevation-specific calculations)

2. **Compute the budget** using the link budget workflow from workflows.md:
   - Calculate free-space path loss (show the formula and intermediate values)
   - Add atmospheric and other system losses
   - Compute received power
   - Calculate system noise temperature and noise floor
   - Derive C/N0, Eb/N0, and BER
   - Compare against required Eb/N0 for the modulation scheme

3. **Produce the formatted link budget table** — Full tabular output with dB values clearly labeled, PASS/FAIL indicator, and margin in dB.

4. **Provide interpretation** — What does the margin mean practically? Is it robust to rain, low elevation, pointing errors? What would improve it?

5. **Protocol overhead note** — If the user specifies a protocol (AX.25, CCSDS), note the protocol overhead and its effect on effective throughput.

If the user says something like "simulate a 437 MHz cubesat link" without full parameters, make reasonable assumptions for a typical 1U/3U cubesat scenario and label all assumptions clearly.
