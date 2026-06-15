# /kb-ingest-sweep — Ingest a Spectrum Sweep into Entry Drafts

Convert a raw spectrum sweep or capture log into structured, schema-compliant knowledge-base entry drafts, one per detected emitter.

## Inputs

- Sweep data: a `hackrf_sweep` / `rtl_power` CSV, an IQ recording with metadata, or a survey notes file
- Capture metadata: center frequency / span, sample rate, gain, antenna, location, timestamp (required for provenance)
- Optional: an existing KB path (`outputs/kb/`) so detections can be matched against known entries rather than re-created

## Steps

1. **Parse the sweep.** Read the power-vs-frequency data. Estimate the noise floor per sub-band (median or 10th-percentile of bins), then threshold detections at `noise_floor + N·σ` (default N = 6 dB above floor, or 3σ if a distribution is available).
2. **Cluster detections.** Group adjacent above-threshold bins into candidate signals. For each, measure center frequency, occupied bandwidth (e.g. 99 %-power or −20 dB), peak and mean power, and duty cycle if time-resolved data exists.
3. **Match against the KB.** For each candidate, search `outputs/kb/` for an entry whose frequency range and bandwidth overlap. If matched → mark as **update** (note any drift in power/occupancy vs. the stored entry). If unmatched → mark as **new draft**.
4. **Draft entries.** Populate the entry schema (see `context/references.md`) for each candidate. Leave `identification` as `unidentified` where the signal can't be named yet, and record measured parameters + full provenance.
5. **Write drafts and summarize.** Save drafts to `outputs/kb/_drafts/` and emit an ingest summary: counts of new vs. updated vs. unidentified, plus the highest-priority unknowns to triage next.

## Output

Draft entry files in `outputs/kb/_drafts/<freq>-<slug>.md` and an ingest report at `outputs/ingest-<date>.md` (detection table, new/update/unknown counts, recommended next captures).

## Notes

- Never auto-promote a draft to a canonical entry — `/emitter-entry-author` reviews and promotes. Ingest only proposes.
- Antenna and gain materially change measured power; carry them in provenance so a later "the level changed" claim isn't actually a config change.
- For `rtl_power`/`hackrf_sweep`, bin width is set at capture time; under-resolved bins blur narrowband signals together — flag clusters near the bin-width limit as "may be multiple emitters."
