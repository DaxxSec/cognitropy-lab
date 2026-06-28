# /read-batch

Sweep a batch with the fixed inspection search pattern, logging a finding at every station — the discipline that defeats satisfaction of search.

## Inputs

- A diagnostic-quality batch (passed `/study-quality`).
- Sample size to inspect (e.g. 10 spheres) and the recipe header.

## Steps

1. For each sampled sphere, walk the pattern **in order** and record a finding at every station, even "normal":
   - **Shape** — round / tailed / dimpled / collapsed.
   - **Membrane** — uniform thin / thin spots / thick / rubbery full-gel.
   - **Surface** — smooth / wrinkled / cloudy / grainy / weeping.
   - **Buoyancy** — sinks / floats.
   - **Burst** — clean liquid release / weak / none / premature leak.
   - **Flavor** — true / bitter-metallic / dilute.
2. Tally finding frequencies across the sample (e.g. "6/10 float").
3. Flag **co-occurring** findings explicitly (e.g. float + thin top) — do not stop at the first.
4. Pass each non-normal finding to `/differential`; pass the batch to `/sphere-rads`.

## Output

A findings table (station × frequency) saved to `outputs/`, with co-occurrence flags, feeding the differential and category steps.

## Notes

- The point of a fixed order is to keep the obvious defect from blinding you to the second one (satisfaction of search).
- Record frequencies, not just "present/absent" — Occurrence scores in the FMEA depend on them.
