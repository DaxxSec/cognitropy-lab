# /sample-queue-plan

Build a sample-throughput plan for the characterization queue using Little's Law and M/G/1 utilisation. Returns expected queue length, lead time, utilisation ρ, and a flag list of samples that push the system over its sustainable limit.

## Inputs

- Sample list: per sample, the required measurement set (R(T), V(I), M(T), M(H), AC χ, cavity Q, Cp, etc.) and priority tier (P0 / P1 / P2)
- Service-time estimate per measurement type (mean and standard deviation, hours) — pull from `context/references.md → Service-time distributions`
- Server inventory: number of cryostats × usable hours/week (account for transfers, warmups, maintenance)
- Arrival rate λ (samples/week) for the horizon, ideally with last 8-week historical mean and trend
- Target utilisation ceiling (default ρ_target = 0.80; hard ceiling 0.85)

## Steps

1. For each sample, sum its required service time S_i across measurements; treat the cryostat as the contended resource.
2. Compute mean service time E[S] = (Σ S_i) / N and variance Var[S]; derive squared coefficient of variation C_s² = Var[S] / E[S]².
3. Compute arrival rate λ from intake history; set offered load a = λ × E[S]. Server count c = active cryostats. Utilisation ρ = a / c.
4. Apply M/G/1 (single server per cryostat) Pollaczek-Khinchine wait-time formula: E[Wq] = ρ × E[S] × (1 + C_s²) / (2 × (1 − ρ)). For c > 1 cryostats running independent queues, model each as M/G/1 with λ_i = λ / c; for a pooled queue, use M/G/c approximation (Allen-Cunneen).
5. Apply Little's Law: L = λ × W where W = Wq + E[S]. Report mean queue length L and lead time W per priority tier.
6. Stress-test: simulate +20 % arrival rate and −1 cryostat (single-point failure); flag any scenario where ρ > ρ_target.
7. Recommend actions: defer P2 work, add a parallel cryostat, batch low-variance measurements together to reduce C_s², or split a high-variance measurement off the main queue.

## Output

Markdown report at `outputs/sample-queue-plan-<YYYY-MM-DD>.md`:
- Queue parameters table (λ, E[S], Var[S], C_s², ρ, L, W)
- Per-sample lead-time table sorted by priority then arrival
- Flag list: samples or scenarios that push ρ > 0.80
- Mitigation recommendations
- Cross-reference to the matching `/lhe-budget` run (capacity is helium-bound on most days)

## Notes

- M/G/1 assumes Poisson arrivals; if intake is calendar-driven (batched at month boundaries), a discrete-event simulation (`simpy`) is more honest. Note this caveat in the report.
- ρ → 1 makes Wq diverge superlinearly; the 0.80 ceiling is not arbitrary — it preserves head-room for the inevitable quench / cryostat fault.
- Pre-cooldown time is the largest single contributor to service-time variance. If a cryostat needs 24 h to cool from 300 K to 4 K, schedule cooldowns overnight to recover daytime hours.
- Don't model the magnet as an independent server unless it physically is (e.g. shared between two cryostats); in single-magnet cryostats the magnet hours are already inside S_i.
