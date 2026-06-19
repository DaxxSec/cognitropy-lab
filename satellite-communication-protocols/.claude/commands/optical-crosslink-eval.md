# /optical-crosslink-eval

Decide whether a **free-space optical** inter-satellite or feeder link beats RF for a given hop. This is the one place where the two domains literally merge: a laser crosslink *is* an optical system doing communication. The diffraction-limited optical beam has staggering gain and a near-zero beamwidth — the benefit is enormous, but the pointing burden and weather sensitivity are the costs. Run the tradeoff honestly.

## Inputs

- The hop geometry: range, and whether it is inter-satellite (vacuum) or space-to-ground (through atmosphere)
- Optical parameters: laser wavelength (e.g. 1550 nm), aperture diameter, transmit power, pointing-acquisition-tracking (PAT) capability
- The RF alternative's budget from `/cascade-budget` for the same hop
- Constraints: SWaP (size/weight/power) budget, latency, cloud/availability needs, cost per terminal

## Steps

1. Compute the optical **antenna gain**: `G = (πD/λ)²` — with λ ~10⁵× smaller than RF, gain is ~100 dB and beamwidth (`≈ λ/D`, ~µrad) is thousands of times narrower. Tabulate against the RF gain for the same aperture.
2. Build the optical link budget in the same cascade form: Tx power → optical antenna gain → free-space loss (`(λ/4πR)²` — note the wavelength helps the antenna gains far more than it hurts spreading) → atmospheric (for ground links: clouds are opaque — extinction, not attenuation) → Rx aperture → detector sensitivity (photons/bit) → margin.
3. Price the **pointing burden**: a µrad beam needs fine-steering mirrors, beacon tracking, and platform-jitter control. This is the dominant cost and risk — the optical analog of needing diffraction-limited alignment. Quantify PAT mass/power/$ and the pointing-loss sensitivity.
4. Tradeoff: **inter-satellite (vacuum)** strongly favors optical — no weather, huge capacity, no spectrum licensing, low probability of intercept. **Space-to-ground** favors hybrid — optical for clear-sky bulk, RF fallback or ground-station diversity for clouds (cloud-free line-of-sight statistics replace rain stats).
5. Recommend RF, optical, or hybrid with the cost-benefit case: capacity gained, SWaP and $ spent, availability impact, and licensing/regulatory delta (optical needs no ITU frequency coordination).

## Output

`outputs/links/<mission-id>/optical-crosslink-eval.md` — side-by-side RF vs optical budgets, the PAT cost/risk assessment, the weather-availability comparison, and a recommendation with the dominant deciding factor named.

## Notes

- Optical wins inter-satellite because there is no atmosphere and no spectrum scarcity; it struggles space-to-ground because **clouds are a hard stop**, not a fade you can buy margin against — only site diversity (cloud-free-line-of-sight networks) recovers availability.
- The narrow beam is a security *feature* (near-impossible to intercept or jam) as well as a pointing *cost* — credit the LPI/LPD benefit when the mission values it.
