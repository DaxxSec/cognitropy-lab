# Scenario Builder

Use this prompt to build a comprehensive, realistic multi-pass communication scenario for testing or simulation purposes.

---

**Prompt:**

Build a complete multi-pass communication scenario for the following satellite system: [DESCRIBE SATELLITE AND MISSION]

Ground station location: [CITY OR LAT/LON]
Protocol stack: [e.g., CCSDS TC/TM, AX.25, DVB-S2]
Data rate(s): [UPLINK AND DOWNLINK RATES]
Mission phase: [LAUNCH AND EARLY ORBIT / NOMINAL OPS / CONTINGENCY]

Please generate a scenario that includes:

**1. Orbital Context**
- Pass geometry for 3 consecutive passes (AOS, TCA, LOS for each)
- Maximum elevation for each pass
- Link availability windows per pass
- Doppler shift envelope for the operating frequency

**2. Timeline of Events**
Create a detailed minute-by-minute (or second-by-second for critical phases) timeline showing:
- Ground station activation
- Signal acquisition and lock
- Protocol handshake sequence
- Data transfer events (uplink commands, downlink telemetry)
- Anomaly injection points (if stress testing)
- Loss of signal and post-pass activities

**3. Protocol Exchange Sequence**
For each communication event in the timeline, show:
- The exact frame(s) exchanged (as annotated hex or structured description)
- Expected response/acknowledgment
- Timing constraint (must complete within X seconds)
- Error condition: what happens if this step fails?

**4. Anomaly Scenarios**
Include at least 3 anomaly cases:
- Partial pass (link lost mid-pass — how does the protocol recover?)
- Out-of-sequence frame received
- Command not acknowledged (timeout handling)

**5. Success Criteria**
Define what "test passed" looks like for this scenario:
- All nominal commands acknowledged
- Telemetry received within link window
- State machine in expected state after LOS
- Error counters within bounds

**6. Test Execution Guide**
How to run this scenario in a lab environment:
- Required hardware/software
- How to inject frames (loopback, SDR, KISS over TCP)
- How to observe and log outcomes
- Automated vs. manual steps

Generate Python code snippets for any programmatically generatable parts of the scenario.
