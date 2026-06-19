# /open-link-budget

Open a new link-design case and lay out its "optical train": the ordered cascade of stages the signal passes through, each a budget line waiting to be filled. This is the satcom analog of sketching the lens layout before tracing a single ray.

## Inputs

- Mission geometry: orbit (GEO / MEO / LEO + altitude), or explicit slant range; min/max elevation angle for ground links
- Frequency band and polarization (e.g. Ka-band 20 GHz downlink, RHCP)
- Direction(s) to design: forward downlink, return uplink, feeder, and/or inter-satellite link
- Targets: required data rate (Mbps), required link availability (e.g. 99.5%), and the BER/PER or Eb/N₀ quality floor
- Known hardware if any (antenna diameters, Tx power, system noise temperature)

## Steps

1. Create `outputs/links/<mission-id>/` and write `mission.md` capturing every input above with its source and a confidence tag (firm / estimate / placeholder).
2. Lay out the **cascade ledger** as an ordered list of stages — the optical train: `Tx power → feed/line loss → Tx antenna gain (EIRP) → pointing loss → free-space spreading (FSPL) → atmospheric (gas/rain/scintillation) → Rx antenna gain → Rx system (G/T) → received C/N₀ → bandwidth → Es/N₀ → coding gain → Eb/N₀ → margin`.
3. Mark each stage `gain (+)` or `loss (−)` and note which design lever controls it (aperture, power, MODCOD, site, etc.) so later cost-benefit commands know what is tunable.
4. Record the **two ceilings** for this mission up front: the Shannon capacity for the allocated bandwidth (the étendue the design will be measured against) and the ITU/regulatory EIRP and PFD limits (the legal stops).
5. Seed empty values for every stage; leave a `provenance` column so nothing enters the budget without a source.

## Output

`outputs/links/<mission-id>/cascade-ledger.md` — the empty-but-structured budget train plus `mission.md`. This is the scaffold `/cascade-budget` fills in and every other command reads.

## Notes

- Open one ledger **per link direction** — uplink and downlink have different EIRP, G/T, and rain geometry and must not share a row.
- Naming a lever's controlling parameter now ("this loss is set by dish diameter") is what makes `/aperture-tradeoff` and `/modcod-pareto` mechanical later. Skipping it forces a re-trace.
