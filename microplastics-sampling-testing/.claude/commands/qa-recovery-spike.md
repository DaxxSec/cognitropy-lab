# /qa-recovery-spike

Evaluate extraction recovery from a reference-particle spike. Counts mean nothing if the method silently loses particles during digestion, density separation, and filtration — recovery is the correction that makes concentrations comparable across labs and over time.

## Inputs

- Spike definition: reference microplastics added to a blank matrix — type (e.g. fluorescent PE/PS microspheres, fragmented PET, polyester fibers), nominal count, size distribution, polymer mix.
- Recovered count after the full method, by size and polymer.
- The method version the spike validates (must match the samples it will correct).

## Steps

1. **Compute percent recovery overall and stratified** by size bin and polymer: recovery% = recovered / spiked × 100. Stratify — small particles (<100 µm) and low-density films often recover worse, and recovery is polymer-dependent.
2. **Flag size-dependent loss.** If recovery falls off below a size threshold, that threshold becomes the method's effective reporting floor — report it, don't pretend the small-size data is quantitative.
3. **Check the density cut.** Poor recovery of dense polymers (PET, PVC) usually means the density medium was too light (NaCl can't float PET) — recommend ZnCl₂/NaI/SPT. Poor recovery of fibers can mean filtration loss or static.
4. **Apply or reject correction.** If recovery is acceptable and stable, set a per-stratum recovery-correction factor for `/concentration-report`. If recovery is erratic, the method is not yet fit for quantitative reporting — return qualitative only.
5. **Trend recovery** across spikes; a declining recovery is a predictive-maintenance signal (worn sieve, clogged filtration, aging density medium) → `/instrument-maintenance-forecast`.

## Output

A recovery record under `outputs/qa/recovery/<method-version>.md`: overall and stratified recovery %, the size reporting floor, density-cut diagnosis, the recovery-correction factors (or a "qualitative-only" verdict), and the recovery-trend update.
