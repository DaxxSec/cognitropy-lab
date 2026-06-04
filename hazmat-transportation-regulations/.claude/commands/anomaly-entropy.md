# /anomaly-entropy

Run an entropy / anomaly scan over a batch of declarations for the statistical *tells* of fabricated, copy-pasted, or carelessly templated paperwork — the cryptanalyst's "this message has the wrong randomness" attack.

## Inputs

- A batch of dangerous goods declarations / manifests (the more, the better the baseline).
- Optional field weights (which fields matter most for this mode).

## Steps

1. Extract per-field values across the batch (emergency phone, net quantity, package count, shipper certification text, emergency-info source).
2. Measure where entropy is *too low*: identical emergency-contact strings across unrelated shippers, repeated free-text certifications, suspiciously uniform package counts.
3. Detect round-number tells: net quantities that are implausibly round (exactly 1,000 kg repeatedly), placeholder values (0, 9999, "TBD").
4. Detect structural anomalies: missing required fields, fields out of the prescribed basic-description order, encoding/format inconsistencies within one shipper.
5. Assign each declaration an anomaly score and list the contributing tells.

## Output

An anomaly report at `outputs/anomaly-entropy-<batch>-<date>.md`: the per-declaration anomaly scores, the specific tells found, and the ranked list of declarations to escalate.

## Notes

- Low entropy is suspicious *relative to expectation* — a single shipper legitimately reusing one 24-hour contact number is normal; the same number across unrelated shippers is not.
- This finds *carelessness and fabrication*, not necessarily mis-classification — pair with `/decode-manifest` to confirm the hazard error.
