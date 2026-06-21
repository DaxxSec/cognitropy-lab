# Affinity Maturation Strategy

## Purpose

Reason from a lead's current kinetics to a concrete maturation campaign — diversification choice, library design, and selection scheme — with a developability guardrail. Use when affinity misses target and you need a defensible plan rather than a brute-force library.

## Prompt Template

```
You are designing an affinity-maturation campaign as a senior antibody engineer.

I have a lead to mature:

- **Lead ID & sequences:** [VH / VL]
- **Current kinetics:** [KD], [kon], [koff], measurement method [SPR/BLI, steady-state/kinetic]
- **Affinity target & why:** [VALUE — e.g. 50 pM for potency at the dosed concentration]
- **Display platform & library ceiling:** [phage/yeast/mammalian], [max library size]
- **Hard constraints:** [epitope to preserve, format, developability floor, positions off-limits]

Please:
1. Diagnose whether the campaign is on-rate- or off-rate-limited and what that implies for selection.
2. Recommend a diversification strategy (focused CDR libraries / chain shuffling / error-prone / DMS-guided) with rationale against the target and ceiling.
3. Specify the library: positions, codon scheme, theoretical vs practically-sampled diversity, oversampling factor.
4. Lay out the round-by-round selection pressure, readouts, and the stop criterion.
5. State the developability guardrail and how affinity wins that add liabilities will be rejected.
```

## Expected Output

- A kon-vs-koff diagnosis driving the selection scheme.
- A justified diversification strategy.
- A concrete library design table.
- A round-by-round plan with stop criterion and developability guardrail.
