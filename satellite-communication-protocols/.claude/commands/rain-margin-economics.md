# /rain-margin-economics

Turn the rain-fade distribution into a cost-benefit on margin. Availability is bought in dB, and the last "nine" is the most expensive — the satcom analog of buying depth of field by stopping down: each extra stop costs light (here, costs dB/throughput) for diminishing sharpness (availability). This command finds whether to buy static margin, switch to ACM, or add site diversity.

## Inputs

- ITU-R rain region or measured rain-rate statistics for the ground site(s); frequency, elevation angle, polarization tilt
- The clear-sky margin from `/cascade-budget`
- Target availability (e.g. 99.5%, 99.9%, 99.99%) and the cost of an outage minute
- Candidate mitigations and their costs: extra static margin (dB → power/aperture $), ACM (scheduler + return-path $), site diversity (second gateway $ + switching), uplink power control

## Steps

1. Build the **fade-exceedance curve**: rain attenuation `A(p)` exceeded for p% of an average year via ITU-R P.618 (`A_0.01` from rain rate and specific attenuation `γ_R = k·R^α`, then scaled to other exceedances). This is the cumulative distribution the margin must cover.
2. Read off the dB needed for each target availability. Note the **convexity**: going 99.9% → 99.99% can cost several times the dB of 99% → 99.9%.
3. Price each dB three ways and compare: (a) **static margin** (always-on aperture/power cost, even in clear sky — wasteful), (b) **ACM** (pays only the throughput dropped during fades), (c) **site diversity** (two sites rarely rain hard at once; decorrelation buys availability cheaply at high frequencies).
4. Compute expected annual outage cost at each availability and the **marginal $ per nine**. Find where the cost of the next nine exceeds the outage cost it prevents — that is the economic availability target, which may be *below* the requested one.
5. Recommend the cheapest mitigation mix that meets the *economically justified* availability, and flag any requested availability whose marginal cost exceeds its benefit as gold-plating.

## Output

`outputs/links/<mission-id>/rain-margin-economics.md` — the fade-exceedance curve, dB-per-availability, the static-vs-ACM-vs-diversity cost comparison, the marginal $ per nine, and a recommended margin/mitigation plan.

## Notes

- Rain attenuation also *raises sky-noise temperature*, degrading G/T on top of the path loss — count both, or the deep-fade budget is optimistic.
- Site diversity gain comes from spatial **decorrelation** of intense rain cells (typically >10 km separation); it is the high-band analog of aperture synthesis — two cheap apertures beating one expensive one.
