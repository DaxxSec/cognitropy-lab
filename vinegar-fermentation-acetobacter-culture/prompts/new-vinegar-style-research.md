# New Vinegar Style Research

## Purpose

Use this prompt when starting a new vinegar style or substrate (e.g. pineapple, black garlic, honey/mead, rice) and you need a sourced KB foundation before the first batch. Produces canonical `styles` entries plus the parameter set to start from.

## Prompt Template

```
You are a vinegar R&D researcher building a knowledge-base foundation for a new style.

I want to start producing:

- **Target style / substrate:** [e.g. pineapple scrap vinegar]
- **Starting material:** [juice, scraps, must, wash; approx sugar/Brix]
- **Equipment & method available:** [Orleans / generator / submerged]
- **Goal acidity & use:** [table vinegar 5% / drinking / culinary]
- **Constraints:** [organic, no added culture, time budget]
- **Sources I have:** [paste references, papers, recipes]

Please:
1. Summarize how this style is traditionally made and where it differs from generic cider/wine vinegar.
2. Recommend a starting parameter set: target starting ABV, strain/genus fit, temperature, method, expected timeline, harvest acidity.
3. Identify the top risks for THIS substrate (sugar level, off-flavors, contamination, ethanol tolerance).
4. Draft 3–6 atomic KB entries (taxonomy=styles/methods, provenance to the sources, confidence=published or inferred as appropriate).
5. List the open questions a first batch should answer (to be confirmed as `measured` later).
```

## Expected Output

- A traditional-method summary and how it diverges from baseline vinegar.
- A concrete starting parameter set (ABV, strain, temperature, method, timeline, target acidity).
- A ranked risk list specific to the substrate.
- 3–6 KB-entry drafts ready for `/kb-ingest`, plus open questions for the first batch.
