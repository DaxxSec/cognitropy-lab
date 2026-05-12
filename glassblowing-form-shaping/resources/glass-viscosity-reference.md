# Glass Viscosity & COE Reference

Studio-grade approximations. **Always defer to manufacturer datasheets when they conflict with values here.**

## Anchor Temperatures by Glass Family

| Family | Working pt (10⁴ poise) | Softening (10⁷·⁶) | Annealing (10¹³) | Strain (10¹⁴·⁵) | COE (×10⁻⁷/K) |
|--------|------------------------|-------------------|------------------|-----------------|----------------|
| Bullseye COE 90 | ~1050 °C | ~720 °C | 516 °C | 482 °C | 90 |
| System 96 (Spectrum/Uroboros/Oceanside) | ~1050 °C | ~720 °C | 510 °C | 480 °C | 96 |
| Effetre / Moretti COE 104 | ~1040 °C | ~720 °C | 516 °C | 482 °C | 104 |
| Reichenbach RW104 | ~1040 °C | ~720 °C | 516 °C | 482 °C | 104 (lot variable; pretest!) |
| Kugler COE 104 | ~1040 °C | ~720 °C | 516 °C | 482 °C | 104 |
| Schott Borosilicate 33 (Pyrex/Duran/Northstar/GA) | ~1250 °C | ~820 °C | 565 °C | 525 °C | 33 |

Sources: Bullseye TipSheets (annealing tables), Schott Borofloat 33 datasheet, Effetre / Moretti technical literature, Frantz Art Glass cross-supplier compatibility chart. **All temperatures are nominal; use manufacturer SDS for the specific product when working a critical piece.**

## COE Compatibility Matrix

Mark `OK` if same family, `BLOCK` if hard incompatible, `PRETEST` if rated compatible by one or more suppliers but with documented lot-to-lot variation.

|  | Bullseye 90 | System 96 | Effetre 104 | Reichenbach RW104 | Kugler 104 | Borosilicate 33 |
|--|--|--|--|--|--|--|
| **Bullseye 90** | OK | BLOCK | BLOCK | BLOCK | BLOCK | BLOCK |
| **System 96** | BLOCK | OK | BLOCK | BLOCK | BLOCK | BLOCK |
| **Effetre 104** | BLOCK | BLOCK | OK | PRETEST | PRETEST | BLOCK |
| **Reichenbach RW104** | BLOCK | BLOCK | PRETEST | OK | PRETEST | BLOCK |
| **Kugler 104** | BLOCK | BLOCK | PRETEST | PRETEST | OK | BLOCK |
| **Borosilicate 33** | BLOCK | BLOCK | BLOCK | BLOCK | BLOCK | OK |

**`PRETEST` procedure:** fuse a small strip (~2 cm) of each in contact, anneal under the standard borosilicate or soda-lime program, and inspect under crossed polarizers for stress fringes. No fringes = compatible enough for this lot pair; visible fringes = treat as BLOCK for this lot pair.

## Anneal Hold Times (Soda-Lime Reference)

| Max wall thickness | Hold at anneal point | Anneal-to-strain rate (max) | Notes |
|--------------------|----------------------|------------------------------|-------|
| ≤ 6 mm | 30 min | 200 °C/h (controller cap) | Beads, thin-walled vessels |
| 7–12 mm | 60 min | 100 °C/h | Standard goblets, vases |
| 13–25 mm | 2 h | 50 °C/h | Heavy-walled vessels, paperweights |
| 26–50 mm | 4 h | 20 °C/h | Sculpture, light castings |
| > 50 mm | scale ∝ thickness² | < 10 °C/h | Castings — defer to Bullseye TipSheets |

Add 30 min base hold for any piece > 1 kg regardless of thickness. Borosilicate uses the same table but at its own anneal point (565 °C) with K ≈ 800.

## Working Time Reference (300 g Gather, Soda-Lime, Glory Hole Soak 1170 °C)

Approximate seconds of working time before surface drops below 1050 °C:

| Operation sequence | Cumulative working time used (s) | Working time remaining |
|--------------------|----------------------------------|------------------------|
| Out of glory hole | 0 | ~60 s baseline |
| + 5 s marver | ~10 s | ~50 s |
| + 3 s block | ~14 s | ~46 s |
| + 5 s jacks | ~20 s | ~40 s |
| + 3 s blow-puff | ~24 s | ~36 s |

After ~36 s usable time runs out, return to glory hole for a reheat (typically 8–15 s soak depending on mass and glory hole temp). Reheat resets the budget.

## Studio Observations Section

(Append rows here as the studio's actual measurements diverge from the table values. The table values are starting points; *the studio's batch records are ground truth.*)

| Date | Observation | Family | Notes |
|------|-------------|--------|-------|
| | | | |
