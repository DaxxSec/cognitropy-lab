# /recyclability-eol-assessment

Assess end-of-life recyclability of an SMA part and the nickel-release / biocompatibility risk it carries through use and disposal.

## Inputs

- Alloy (binary NiTi, ternary, or Cu-based) and the part's contamination history (oxide scale, brazing/joining materials, coatings, biological exposure).
- The end-of-life pathway under consideration: closed-loop remelt, downcycle into non-functional stock, or disposal.
- Exposure context for Ni release: implanted device, skin contact, or environmental leaching.

## Steps

1. Read `context/concepts.md` on why functional-grade NiTi is **hard to recycle**: oxygen and carbon pickup during remelting forms Ti₄Ni₂O / TiC, embrittling the alloy and shifting transformation temperatures — so scrap rarely returns to medical/actuator grade.
2. Classify the realistic EOL route: closed-loop (requires vacuum remelt + tight interstitial control, expensive), downcycle (Ni and Ti recovered as feedstock for non-SMA uses), or landfill.
3. Estimate recoverable value and the contamination penalty; note that mixed scrap and joined assemblies are far harder to recycle than clean monolithic parts.
4. Assess **nickel release**: for implants/skin contact, evaluate the TiO₂ passive layer and surface finish (electropolishing lowers Ni leaching) against the REACH nickel-release limit and ISO 10993 biocompatibility expectations.
5. For environmental disposal, flag Ni as a regulated, bioaccumulative metal; recommend recovery over landfill where feasible.
6. Feed the recyclability score and Ni-risk rating into `/eco-performance-frontier` so end-of-life is weighed alongside performance, not bolted on after.

## Output

`outputs/eol-assessment-<part>-YYYY-MM-DD.md`: the realistic EOL route, a recyclability rating with the contamination rationale, the Ni-release / biocompatibility assessment against REACH + ISO 10993, and design-for-recycling recommendations (avoid dissimilar-metal joins, prefer monolithic, specify surface finish).

## Notes

- "Recyclable in principle" ≠ "recycled in practice" — NiTi's interstitial sensitivity is the real barrier. Be specific about which applies.
- Surface finish is a dual lever: electropolishing improves both fatigue life and Ni-release safety. Surface this synergy.
- Cu-based SMAs sidestep the Ni allergen issue but introduce Cu/Al recovery and their own toxicity questions — don't treat "non-NiTi" as automatically greener.
