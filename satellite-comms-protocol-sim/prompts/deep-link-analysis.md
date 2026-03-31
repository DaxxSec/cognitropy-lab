# Deep Link Analysis

Use this prompt for a thorough, multi-scenario link budget analysis that goes beyond the basic `/simulate-link` command.

---

**Prompt:**

Perform a deep end-to-end link analysis for the following scenario: [DESCRIBE YOUR LINK HERE]

Please cover all of the following in your analysis:

1. **Baseline link budget** — Complete link budget table under nominal conditions (clear sky, typical elevation, standard equipment)

2. **Elevation profile analysis** — How does the link margin change from 5° to 90° elevation? Produce a table showing margin at 5°, 10°, 15°, 20°, 30°, 45°, and 90°.

3. **Degradation scenarios** — Calculate link margin under:
   - Rain fade (use appropriate ITU rain zone for the location)
   - Antenna pointing error (±3°, ±5°)
   - Receiver detuned by 1 dB system noise increase
   - Worst-case Doppler at AOS/LOS (if LEO)

4. **Coding gain analysis** — Compare link performance with:
   - No FEC (uncoded)
   - AX.25 (no FEC, just CRC)
   - CCSDS legacy (RS+convolutional, ~7-8 dB gain)
   - LDPC (DVB-S2 style, ~10-11 dB gain)

5. **Protocol overhead** — Calculate effective data throughput accounting for:
   - Protocol header overhead bytes
   - Duty cycle constraints if applicable
   - ARQ overhead if using acknowledged mode

6. **Risk assessment** — Which scenarios drop below acceptable margin? What is the probability of link outage during a typical pass?

7. **Improvement recommendations** — Rank improvements by impact/effort:
   - Antenna upgrade options
   - LNA improvement
   - Coding scheme change
   - Power increase (if feasible)

Produce all calculations in tabular form, show all formulas, and flag any assumptions clearly.
