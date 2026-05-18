# /redline-set

Design the runtime abort-threshold table for a hot-fire test by walking the `R-*` decision tree (`context/workflows.md` §2). Every redline is itself a scored matrix cell: likelihood × severity of missing it, plus likelihood × severity of a false trip.

## Inputs

- `test_id` — identifier for the upcoming fire.
- `daq_channels_path` — DAQ channel list (signal name, range, sample rate, noise floor, controller abort latency).
- `severity_i_ii_failure_modes` — list from the `T-*` matrix of failure modes at severity I/II requiring redline coverage.
- `controller_arch` — `software-only` | `hardware-independent-path` | `mixed`. Required.
- `nominal_traces_path` — optional; prior-test traces for the engine, used to set thresholds with engineering margin.

## Steps

1. Run `R-0` intake. Reject if DAQ list, severity I/II failure-mode list, or controller architecture is missing.
2. For each DAQ channel that monitors a parameter tied to ≥1 severity I/II failure mode, walk `R-1` to classify as candidate redline / monitor-only. SNR < 5 → reject as redline; flag for filtering or different transducer.
3. At `R-2`, set the threshold value. Prefer physics-based limits (MEOP, pump certified speed, material temperature limit). If using prior-test-data + margin, document the margin rationale (e.g. 3σ above observed nominal).
4. At `R-3`, compute redline latency = sense + decide + actuate. If parameter rate-of-rise × latency exceeds the catastrophic margin, the redline is ineffective — escalate to a hardware interlock path. Severity I redlines require an independent hardware abort path; reject if absent.
5. Walk `R-4` (per-redline miss likelihood × severity) and `R-5` (per-redline false-trip likelihood × severity). The asymmetry (a missed redline is much worse than a premature abort) must be visible in the matrix.
6. At `R-6`, define loss-of-signal policy per channel. Default = ABORT for severity I; HOLD or REVERT acceptable for non-I.
7. Validate at `R-7` that 100% of severity I failure modes are covered by at least one redline with adequate latency and independent abort path.
8. Write the redline table and per-redline matrix cells to `outputs/redlines/<test_id>-redlines-<YYYYMMDD>.md`.

## Output

Markdown file containing:
- Test ID, controller architecture, total redline count.
- Per-redline table: channel, threshold, basis (physics / prior-test+margin / judgment), latency (ms), miss-cell, false-trip-cell, loss-of-signal policy, abort path (software / independent hardware).
- Coverage cross-check table: each severity I/II failure mode in column, redline(s) covering it in another column. Empty cells → REJECT.
- Aggregate redline-quality score and recommendations (channels needing filtering, redlines needing tighter thresholds, missing hardware abort paths).
- Reproducibility footer: DAQ channel list hash, prior-test references, git SHA.

## Notes

- A redline with a 200 ms total latency on a parameter that rises 50% in 100 ms is not a redline; it's a post-incident log entry.
- False-trip rate matters operationally — a stand with too many false aborts loses fire days. Keep the asymmetry visible: tune false-trip thresholds against `R-5` cell, never below the `R-4` cell.
- Severity I parameters MUST have an independent hardware abort path. Software-only paths are unacceptable here regardless of controller pedigree.
- The redline density is a function of the engine maturity. Development engines need more redlines; flight-heritage engines can run with leaner sets backed by service history. Either way, severity I coverage is non-negotiable.
- If a redline cannot be designed for a severity I failure mode (latency too long, no observable precursor), the test card itself must change — reduce throttle range, shorten burn, add propellant inhibitors, redesign the run plan.
