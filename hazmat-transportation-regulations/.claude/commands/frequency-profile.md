# /frequency-profile

Frequency-analyse the distribution of dangerous-goods codes across a shipper, lane, or fleet, and surface the statistical outliers worth a targeted inspection — frequency analysis applied to inspection triage.

## Inputs

- A corpus of manifests / declarations for a shipper, lane, or fleet (or a prior baseline to refresh).
- The grouping dimension(s): shipper, origin–destination lane, mode, time window.
- Codebook edition for decoding the codes.

## Steps

1. Decode each manifest's UN numbers, classes, and packing groups into a normalised set of codes.
2. Build frequency distributions per grouping dimension (UN-number histogram, class histogram, PG histogram).
3. Establish the baseline "normal" profile for the group (what this shipper/lane usually carries).
4. Score each shipment for deviation from the baseline (rare-class appearance, class never seen on this lane, sudden volume shift).
5. Rank shipments by outlier score; output the head of the list as inspection targets.

## Output

A frequency-profile report at `outputs/freq-profile-<group>-<date>.md`: the baseline distributions, the outlier ranking, and a short rationale per flagged shipment. Optionally persist the baseline to `outputs/baselines/` for reuse.

## Notes

- A frequency outlier is a *lead*, not a violation — a clean codebook decode on an outlier usually means a legitimate one-off.
- Combine with `/anomaly-entropy`: outlier + fabrication tell = top priority.
- Beware small samples; a thin baseline produces false outliers. Note the sample size in the report.
