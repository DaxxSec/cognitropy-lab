# /triage-source — Decision-Tree Triage of an Unknown Reading

Walk the canonical decision tree for an anomalous or unidentified field reading: classify, narrow, localize, and decide the next confirming measurement. This is the workspace's signature workflow — every branch is single-measurement falsifiable.

## Inputs

- The anomalous reading(s): position, frequency (or "broadband"), magnitude, probe used, polarization, detector mode, dwell, RBW.
- The site context (output of `/survey-plan`, if available) — exclusion zones, expected emitters, applied standard.
- Available follow-up instruments (a different probe, an antenna, a spectrum analyser, a current clamp, a TEM cell, etc.).
- Optional: visual inspection notes (was there a transmitter visible, a switching power supply, an arcing contact?).

## Steps

1. **Branch 1 — Real or artefact?** Re-take the reading with the same probe in the same position. If it disappears, log as transient and continue surveillance. If it persists, move to Branch 2. If it changed dramatically, check probe orientation, battery, and antenna factor — a wandering reading is the most common artefact mode.
2. **Branch 2 — Near-field or far-field?** Compare distance-to-emitter `r` with the reactive near-field boundary `λ / (2π)` and the radiating near-field / Fraunhofer boundary `2D² / λ` (D = antenna largest dimension, λ = wavelength). If `r < λ/(2π)` you must use a separate E and H probe — broadband isotropic E-field readings are unreliable. If `r > 2D²/λ`, treat as far-field and apply plane-wave assumptions.
3. **Branch 3 — Narrowband or broadband?** Sweep with a spectrum analyser at the recorded position. A single distinct line means an intentional emitter; multiple harmonics with monotonic decay means a switching source (DC-DC converter, BLDC motor, ignition); broadband white-ish noise spanning decades means a corona / arcing source or galvanic mains noise. Use this to choose the standard's averaging method.
4. **Branch 4 — Intentional or unintentional emitter?** Cross-reference the resolved frequency against `context/references.md` (ISM bands, broadcast plans, telecom carriers, ITU allocations). A hit in an ISM band points to intentional but uncoordinated emitters; a hit in a licensed band points to a licensed transmitter; off-band points to unintentional / EMI.
5. **Branch 5 — Localize.** With the source class known, apply the appropriate localisation method:
   - Far-field intentional → directional antenna + DF triangulation from 3 points.
   - Near-field unintentional → H-field probe walked over the suspect equipment surface, 5 cm grid (see `/map-near-field`).
   - LF magnetic → 3-axis ELF probe + power-line proximity walk; check transformer / busbar / conduit routes.
6. **Branch 6 — Compare against limit.** With class + magnitude + averaging rule in hand, compare against the applicable standard (use `/check-exposure-compliance` for the rigorous version). If under by >10 dB, document and continue. If within 10 dB, schedule a follow-up time-averaged measurement. If over, halt occupancy and escalate per the survey scope's reporting line.
7. **Log the triage decision.** Save the full branch trace — every reading taken, the branch chosen, why — to `outputs/triage/<date>-<position-slug>.md`. The trace is reviewable: another engineer should be able to redo the same triage from the file.

## Output

`outputs/triage/<date>-<position-slug>.md` containing the branch trace, follow-up measurements, the classification verdict, and the immediate action (continue / re-measure / halt). One trace per anomaly.

## Notes

- Resist branch-skipping. The decision tree exists because pattern-matching off the first reading is the failure mode this workflow prevents.
- A "no source found" verdict is legitimate — record it and move on rather than fabricating an attribution.
- For TSCM use cases the branch at step 4 also asks "covert vs. overt emitter" — a covert emitter is rarely an ISM band hit and often duty-cycle suspicious. Cross-reference `context/concepts.md` § TSCM signatures.
