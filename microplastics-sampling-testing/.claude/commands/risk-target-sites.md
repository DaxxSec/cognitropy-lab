# /risk-target-sites

Intelligence-led targeting for a sampling network. Finite field and lab capacity should go where contamination load and decision-value are highest — the microplastics analogue of risk-based border targeting, not uniform coverage.

## Inputs

- A list of candidate sites with available metadata: coordinates, matrix (surface water / sediment / biota / air), and any of: distance to nearest WWTP/CSO outfall, upstream urban catchment area, river-mouth or tidal-mixing zone, aquaculture/fishing intensity, known industrial discharges, prevailing-current convergence (gyre/eddy), historical counts if any.
- Program objective (trend detection, hotspot mapping, source attribution, compliance).
- Capacity constraint: number of sites and replicates affordable this campaign.

## Steps

1. Normalize each driver to 0–1. Treat missing drivers explicitly (impute to the site-set median and flag, never silently zero).
2. Score each site with a transparent weighted model. Default weights (tune per program):
   - Proximity to outfall/CSO: 0.25
   - Urban runoff / impervious catchment: 0.20
   - Hydrodynamic accumulation (gyre, eddy, depositional zone): 0.20
   - Known industrial/sectoral source: 0.15
   - Decision-value (regulatory boundary, drinking-water intake, protected habitat): 0.20
3. Apply **coverage constraints** so targeting doesn't collapse onto one cluster: enforce at least one reference/low-risk control site and spatial spread (no two selected sites within the same mixing cell unless replication is the goal).
4. Rank, then select down to capacity. Mark each selection *primary target* (high score) or *baseline/control* (deliberately low score, needed to interpret the rest).
5. Write the rationale: top three drivers per selected site, and why each rejected high-score site was dropped (usually access, redundancy, or coverage).

## Output

A targeting list under `outputs/targeting/<campaign>.md`: ranked table (site, score, top drivers, primary/control tag, replicates), the weight set used, imputation flags, and a one-paragraph rationale. This list feeds `/sampler-deployment-plan`.
