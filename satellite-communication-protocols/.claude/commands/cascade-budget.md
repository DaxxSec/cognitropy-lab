# /cascade-budget

Compute the full link budget as a cascaded gain/loss train and report the margin at every stage. This is ray-tracing the optical system: light (signal power) enters, each surface adds gain or subtracts loss, and you read the throughput at the detector (the demodulator).

## Inputs

- The `cascade-ledger.md` scaffold from `/open-link-budget`
- Hardware values: Tx power (dBW), antenna diameters & efficiencies, system noise temperature or G/T
- Atmospheric assumptions: elevation angle, ITU-R rain region or a specified rain rate, water-vapor density
- Allocated bandwidth (Hz) and the candidate MODCOD's required Es/N₀

## Steps

1. **EIRP:** `EIRP = P_tx − L_feed + G_tx`, with `G_tx = 10·log₁₀(η·(πD/λ)²)`. Record the antenna's −3 dB beamwidth `≈ 70λ/D` for the pointing-loss line.
2. **Free-space spreading:** `FSPL(dB) = 20·log₁₀(4πd/λ) = 92.45 + 20log₁₀(d_km) + 20log₁₀(f_GHz)`. This is the inverse-square spreading — the dominant loss, exactly like geometric falloff of irradiance.
3. **Atmosphere:** subtract gaseous absorption (ITU-R P.676), rain attenuation at the target exceedance (P.618), cloud (P.840), and a scintillation allowance (P.618 §8). Add the rain-induced increase in sky noise temperature to the receive system.
4. **Receive side:** `G/T = G_rx − 10·log₁₀(T_sys)`; `T_sys = T_antenna + T_LNA + downstream/​gain`. Compute `C/N₀ = EIRP − FSPL − L_atm + G/T − k` where `k = −228.6 dBW/Hz/K` (Boltzmann).
5. **Down to Eb/N₀:** `C/N = C/N₀ − 10log₁₀(B)`; `Es/N₀ = C/N₀ − 10log₁₀(R_s)`; `Eb/N₀ = Es/N₀ − 10log₁₀(bits/symbol · code_rate)`. Subtract implementation loss from `/aberration-audit`.
6. **Margin:** `margin = Eb/N₀_achieved − Eb/N₀_required(MODCOD, target BER)`. Tabulate the running total after every stage so the reader sees where the budget is spent.

## Output

`outputs/links/<mission-id>/budget-<direction>.md` — the filled cascade with a per-stage running total, the final link margin, and a one-line verdict (closes / negative / marginal). Flag any stage whose value is still a placeholder.

## Notes

- Boltzmann's constant in dB is `k = −228.6 dBW/Hz/K`; forgetting it (or sign-flipping it) is the most common budget error.
- Keep clear-sky and rain-faded columns side by side — the clear-sky margin is what `/rain-margin-economics` spends down to hit the availability target.
- Pointing loss is not optional on narrow Ka/optical beams: a 0.5° error on a 0.4° beam can cost >3 dB.
