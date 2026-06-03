# /provenance-trace

Record ingredient batch provenance and chain of custody — the manuscript-provenance analogue, so a build can be reproduced and any quality shift traced to a lot.

## Inputs

- Ingredient lots in use: flour (mill, lot #, protein %), butter (brand/AOP, lot #, fat %), water source if relevant.
- Receipt dates and storage conditions.
- The product(s) the lots feed into.

## Steps

1. Record each lot as a **provenance entry**: ingredient, supplier, lot/batch #, key spec (protein % / fat %), receipt date.
2. Note **storage and handling** (temperature, time held) that could alter behaviour by use-time.
3. Link lots to the **products and codices** they were used in (the chain of custody).
4. Record any **substitution event** (lot change mid-run) with date and reason — these are prime suspects when quality drifts.
5. Flag provenance-dependent **claims** (AOP, organic, origin) so menu copy can only assert what the record supports.

## Output

A provenance log appended at `outputs/provenance-log.md` (one running file): dated lot entries, product links, substitution events, and supportable-claims flags.

## Notes

- When a previously-stable product suddenly faults, check the provenance log first — a new lot at a different fat/protein % is the most common hidden cause.
- Provenance honesty is a legal matter for origin/AOP claims, not just good practice (see `context/concepts.md` constraints).
