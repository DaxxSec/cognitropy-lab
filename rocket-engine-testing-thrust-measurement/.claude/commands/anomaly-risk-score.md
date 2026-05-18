# /anomaly-risk-score

Bin a post-test anomaly into a next-test disposition (PROCEED / PROCEED_WITH_MITIGATION / HOLD / SCRUB) by walking the `A-*` tree (`context/workflows.md` §4). Always run before the post-fire review meeting; the output is the anomaly's matrix-cell entry in the campaign log.

## Inputs

- `test_id` — identifier of the just-completed fire.
- `anomaly_id` — sequential id within the test (e.g. `RX-DEV-0042-FIRE-007-A1`).
- `anomaly_type` — `instability` | `leak` | `hard_start` | `hung_start` | `sensor_dropout` | `valve_misseq` | `hardware` | `software`.
- `time_on_test` — seconds from T+0 when observed.
- `duration` — seconds the anomaly persisted; `transient` or `persistent` for non-discrete events.
- `engine_state` — `start_transient` | `main_stage_steady` | `throttle_transient` | `shutdown`.
- `sensor_window_path` — paths to the relevant DAQ traces around the event (F, P_c, P_manifold, T_bearing, V_rms, etc.).
- `borescope_report_path` — post-fire borescope or teardown findings if available.

## Steps

1. Run `A-0` intake. Reject if anomaly type, time, engine state, or sensor window are missing.
2. At `A-1`, screen for personnel injury. Any positive → IMMEDIATE_HOLD with safety-board route, regardless of A-tree score.
3. At `A-2`, screen for asset loss. Hardware loss (chamber breach, pump rotor, stand) defaults to severity I unless a teardown demotes. Continued operability with no spec exceedance is severity III/IV candidate.
4. At `A-3`, classify the pattern. Combustion instability routes to chug / buzz / screech sub-branch with frequency + amplitude analysis. Leak → propellant / pressurant / working-fluid; quantity gate. Hard / hung start → ignition delay + chamber-P rise rate analysis. Sensor dropout → redline-relevant or monitoring-only.
5. At `A-4`, estimate recurrence likelihood. Transient (cold-soak, one-shot fluid hammer) → likelihood D–E. Design feature (injector pattern, valve geometry) → likelihood A–B for next fire absent change. Unexplained → apply anti-optimism bias (one band more frequent than gut estimate).
6. At `A-5`, plot the cell and assign disposition: HIGH → SCRUB, SERIOUS → HOLD, MEDIUM → PROCEED_WITH_MITIGATION, LOW → PROCEED. For 3+ same-type LOW events in trailing 5 tests, promote to SERIOUS.
7. Compose mitigation list at `A-5`. For PROCEED_WITH_MITIGATION, the next test card must explicitly carry these as items, traced to this anomaly id.
8. Write the entry to `outputs/anomalies/<test_id>-<anomaly_id>.md` and update the campaign anomaly index.

## Output

Markdown file containing:
- Test ID, anomaly ID, anomaly type, time on test, engine state at observation.
- Pattern classification with sub-branch (e.g. `chug @ 230 Hz, +4% chamber P amplitude`).
- Severity assignment with cited MIL-STD-882E §4.3.4 definition.
- Likelihood assignment with basis (transient / design / unexplained + rationale).
- Matrix cell + band.
- Disposition: PROCEED / PROCEED_WITH_MITIGATION / HOLD / SCRUB.
- Mitigation list (if applicable), each item tied to next test card section.
- Sign-off requirement (per band).
- Cross-link to `/redline-set` re-run if the anomaly was a redline-miss or false-trip.
- Reproducibility footer.

## Notes

- An unexplained anomaly is the most important kind. Resist the urge to demote likelihood because "we didn't fully diagnose it." Anti-optimism bias is the rule for unexplained events.
- For combustion-instability anomalies, the frequency identification is non-negotiable. Chug, buzz, and screech have very different next-test postures.
- 3+ same-type LOW events in trailing 5 tests is the campaign-pattern promotion rule. Do not let LOW events stack invisibly into a HIGH operational pattern.
- A redline-miss anomaly should trigger `/redline-set` re-run, not just a one-off threshold tweak. Missing redlines are usually a symptom of structural problems (latency, transducer choice, controller architecture).
- HOLD does not mean "indefinite pause." It means the next test does not fire until the mitigation is documented and accepted. Time-box every HOLD entry with a target re-review date.
