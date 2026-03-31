# orbital-pass

Simulate an orbital pass with Doppler shift, timing, and protocol scheduling.

When this command is invoked:

1. **Get pass parameters** — Ask for:
   - Target satellite (name, NORAD ID, or "ISS" for example)
   - Observer location (city name or lat/lon/alt)
   - Frequency of interest (for Doppler calculation)
   - Protocol context (what they plan to do during the pass)
   - TLE if user has a recent one, otherwise note that agent will use example/typical values

2. **Compute pass geometry** using the orbital pass workflow from workflows.md:
   - AOS (Acquisition of Signal) time and azimuth
   - TCA (Time of Closest Approach) elevation and azimuth
   - LOS (Loss of Signal) time and azimuth
   - Pass duration
   - Maximum elevation angle

3. **Generate Doppler profile** — Show how the frequency shifts during the pass:
   - Doppler at AOS
   - Doppler at TCA (approximately 0 Hz)
   - Doppler at LOS
   - Rate of change (Hz/second) — important for software Doppler correction
   - Provide Python code to compute and plot the full profile

4. **Protocol timing window** — Based on the pass geometry:
   - When does the link margin exceed the threshold for the user's protocol/data rate?
   - How many bytes/packets can be exchanged at the target rate?
   - What's the recommended uplink/downlink timing sequence?

5. **Produce the pass report** — Full formatted pass table including:
   - AOS/TCA/LOS times and azimuths
   - Max elevation and pass quality rating (< 15° = poor, 15-45° = good, > 45° = excellent)
   - Doppler profile summary
   - SDR tuning instructions (set initial freq, compensate manually or via Doppler tracking)
   - Protocol window recommendations

6. **Optional**: Generate GPredict or Orbitron-compatible pass data, or a Python script to run the calculation live.

Note: Always label whether TLE data is from the user (live) or an example, and remind user to get fresh TLEs from Celestrak for actual operations.
