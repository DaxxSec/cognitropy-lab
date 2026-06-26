# /screen-sample

Run the two-tier screening protocol on a processed sample. Mirrors primary→secondary border inspection: a fast, cheap primary count flags candidate particles; only referrals go to slow, definitive secondary confirmation. Tune the referral rules to trade throughput against false negatives.

## Inputs

- Processed-sample run ID (post density-separation + digestion) and its `/custody-log` and `/blank-audit` status.
- Primary-screen method: visual sort under stereomicroscope and/or Nile Red staining + epifluorescence.
- Secondary-screen capacity available this batch (µ-FTIR / Raman particle-hours).
- Referral policy (default below).

## Steps

1. **Gate on prerequisites.** Refuse to screen if `/blank-audit` hasn't passed for the batch or the custody chain is broken. Inconclusive blanks → stop, do not count.
2. **Primary screen.** Count and size candidate particles; classify morphology (fragment / fiber / film / bead / foam) and color. Record the field-of-view fraction examined if subsampling the filter.
3. **Apply referral rules** (which particles earn secondary confirmation):
   - All particles on a watchlist morphology (e.g. fibers for textile programs, beads for microbead compliance).
   - A representative, size-stratified random subset of the rest (e.g. 10–30% per size bin) so the confirmed-polymer fraction is estimable — the analogue of randomized secondary referral that keeps the primary screen honest.
   - Any particle whose staining/visual signal is ambiguous.
4. **Secondary screen.** Hand referrals to `/polymer-id`. Record confirm/deny and polymer per particle.
5. **Estimate the false-positive rate** of the primary screen from the confirmed fraction (Nile Red stains some natural particles; visual ID over-calls). Carry this correction into `/concentration-report`.
6. Log the screening yield: particles counted, referred, confirmed-plastic, confirmed-natural, unidentifiable.

## Output

A screening record under `outputs/screens/<run-id>.md`: primary counts by morphology/size/color, the referral set and rationale, secondary confirmations, the primary false-positive correction factor, and the prerequisite-gate verdict. Feeds `/concentration-report`.
