# /aperture-tradeoff

Run the cost-benefit on the hardware levers that buy dB: antenna diameter, transmit power, LNA noise temperature, and ground-station count. Each is a curve with a knee — the optics designer's "stop down for sharpness until diffraction takes over." Find each knee and recommend how far to push before the marginal dB stops paying.

## Inputs

- The current `budget-<direction>.md` and its shortfall/surplus vs target margin
- A cost model per lever: $/m² (or the gain-vs-diameter law `G ∝ D²` and cost-vs-diameter, often `cost ∝ D^2.5–3`), $/W of RF power (and its DC/thermal tail), $/K of LNA cooling, $ per added ground station
- Mass/power/regulatory constraints (spacecraft mass budget, EIRP/PFD limits, real-estate)

## Steps

1. For each lever, express **marginal benefit in dB** per unit: dish `+6 dB per doubling of D` (∝ D²); Tx power `+1 dB per +1 dBW` until the HPA saturates (then AM/AM distortion eats it — the diffraction-limit analog); G/T `+x dB per −ΔK` of T_sys; ground stations buy *availability and gateway capacity*, not raw link dB.
2. Compute **marginal cost** per unit for each lever in $ (and kg, W where binding).
3. Form the **marginal dB-per-dollar** for each lever and rank them. The cheapest dB wins the next increment.
4. Walk each lever to its **knee**: the point where the next increment's dB/$ falls below the next-best lever, or where a hard constraint (mass, saturation, EIRP limit, beamwidth too narrow to point) binds. A bigger dish narrows the beam (`70λ/D`) — past a point, pointing loss and tracking cost claw back the gain.
5. Compare against the *software* correctors from `/aberration-audit`: sometimes recovering 1 dB of implementation loss is an order of magnitude cheaper than 1 dB of aperture.

## Output

`outputs/links/<mission-id>/aperture-tradeoff.md` — a ranked dB-per-dollar table, each lever's knee, the binding constraints, and a recommended increment set that closes the margin gap at minimum cost.

## Notes

- Gain rises as `D²` but cost rises faster (`~D^2.5–3`) and beamwidth shrinks as `1/D` — this is exactly why "just use a bigger dish" has a knee instead of being free.
- G/T improvements are double-counted bargains: a colder LNA helps *every* pass and both rain and clear sky, where a power increase only helps the forward direction.
