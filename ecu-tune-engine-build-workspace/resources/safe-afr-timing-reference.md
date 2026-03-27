# Safe AFR & Ignition Timing Reference

Quick reference for acceptable AFR and timing windows by fuel type and application. These are general guidelines — always verify against your specific platform's known safe parameters and your tuner's recommendations.

---

## Air-Fuel Ratio (AFR) Reference

### Gasoline (91–93 Octane)

| Operating Condition | Target AFR | Danger Zone |
|---------------------|------------|-------------|
| Idle | 14.0–15.0:1 | < 11.0 (rich surge) |
| Part throttle cruise | 13.5–15.0:1 | < 11.5 or > 16.0 |
| Light load acceleration | 13.0–14.5:1 | > 15.5 |
| WOT naturally aspirated | 12.5–13.5:1 | > 14.0 (lean/detonation risk) |
| WOT boosted (street tune) | 11.0–11.8:1 | > 12.5 (lean = danger) |
| WOT boosted (race tune) | 10.8–11.5:1 | > 12.0 |

### E30 (30% Ethanol Blend)

| Operating Condition | Target AFR | Notes |
|---------------------|------------|-------|
| Idle | 13.5–14.5:1 | Lambda ~0.92–0.98 |
| WOT boosted | 10.2–11.0:1 | Ethanol needs more fuel |

### E85 (Approximately 85% Ethanol)

| Operating Condition | Target AFR | Notes |
|---------------------|------------|-------|
| Idle | 11.5–12.5:1 | Lambda ~0.92–0.98 |
| WOT boosted | 8.8–9.6:1 | High stoich — needs major fuel increase |
| WOT NA | 9.5–10.5:1 | |

### Lambda vs. AFR Conversion
| Lambda | AFR (Gasoline) | AFR (E85 approx) | Status |
|--------|----------------|-----------------|--------|
| 1.00 | 14.7:1 | 9.8:1 | Stoichiometric |
| 0.90 | 13.2:1 | 8.8:1 | Rich |
| 0.80 | 11.8:1 | 7.8:1 | Very Rich |
| 0.75 | 11.0:1 | 7.4:1 | WOT boosted target (gasoline) |
| 1.10 | 16.2:1 | 10.8:1 | Lean (dangerous at load) |

> **Use Lambda for cross-fuel comparisons** — AFR stoich changes with ethanol content. Lambda is fuel-agnostic.

---

## Ignition Timing Reference

### Safe WOT Timing Windows by Platform (General Starting Points)

> ⚠️ These are community-referenced starting points only. Your specific engine condition, fuel quality, compression ratio, and boost level will shift these numbers. Always start conservative and advance slowly.

| Platform | WOT Timing @ Peak Torque | Notes |
|----------|--------------------------|-------|
| EJ257 (Subaru STI) | 6–10° on 93 oct / 18 psi | Very knock-sensitive; conservative is wise |
| EJ205/EJ207 (WRX) | 10–14° on 93 oct / 14 psi | More tolerant than EJ257 |
| 4G63 (Evo I-IX) | 12–18° on 93 oct | Robust platform |
| 4B11 (Evo X) | 10–16° on 93 oct | Moderate knock sensitivity |
| Honda K20/K24 | 16–22° on 93 oct NA | Timing-happy NA; boosted is lower |
| Honda K-boosted | 12–16° on 93 oct / 15 psi | |
| GM LS3 NA | 22–26° at peak torque | Loves timing |
| GM LS3 boosted | 14–20° on 93 oct / 8 psi | |
| Nissan SR20DET | 12–16° on 93 oct / 14 psi | |
| Nissan RB26DETT | 10–14° on 93 oct / 18 psi | |
| Ford EcoBoost 2.0 | 14–20° on 93 oct / 20 psi | Knock-sensitive, data log carefully |

### Timing Direction Rules of Thumb
- **Advancing timing** = more power potential, more detonation risk
- **Retarding timing** = less detonation risk, less power, more exhaust heat
- **Light load / cruise cells** — more timing can be safely run here; target MBT (Maximum Brake Torque)
- **High load / high boost cells** — less timing, more conservative, monitor knock closely
- **Cold engine** — ECU should apply advance slowly during warm-up; check cold-start timing cells

---

## Boost Pressure to Injector Duty Quick Reference

Estimated injector duty cycle at various power levels (varies significantly by injector size and fuel type):

| Injector Size | ~300 WHP (93 oct) | ~400 WHP (93 oct) | ~500 WHP (93 oct) |
|--------------|-------------------|-------------------|-------------------|
| 440cc | ~95% ⚠️ maxed | N/A | N/A |
| 550cc | ~78% ✓ | ~98% ⚠️ limit | N/A |
| 660cc | ~64% ✓ | ~82% ✓ | ~98% ⚠️ limit |
| 850cc | ~50% ✓ | ~65% ✓ | ~79% ✓ |
| 1000cc | ~42% ✓ | ~55% ✓ | ~68% ✓ |
| 1200cc | ~35% ✓ | ~46% ✓ | ~56% ✓ |

> **85% duty is the practical limit** for most injectors. Above 90% and you're in dangerous territory for lean conditions at higher RPM or elevated temperatures. Consider this a hard ceiling.

> These numbers assume a single-injection-event setup on gasoline. E85 requires approximately 30–35% more fuel volume — downgrade injector capacity accordingly for ethanol applications.

---

## Knock Retard Interpretation

| Knock Retard Value | Interpretation | Action |
|--------------------|----------------|--------|
| 0° | Normal — no detonation detected | Continue |
| 0.5–1° | Minor knock event — likely transient | Monitor; note conditions |
| 1–2° | Moderate knock — investigate fuel, timing, IAT | Review conditions before next pull |
| 2–4° | Significant knock — ECU compensating actively | Do not pull again until root cause found |
| 4°+ | Severe knock | Abort session. Fuel, timing, or boost issue. |
| Frequent cycling | ECU hunting for knock threshold | Fuel quality or ignition issue |

> Note: Knock sensor sensitivity varies by platform. Some ECUs (e.g., Subaru OEM) are highly sensitive and may trigger on false positives. Learn your platform's baseline behavior before panicking over small values.
