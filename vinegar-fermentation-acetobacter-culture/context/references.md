# Vinegar Fermentation & Acetobacter Culture — Reference Tables

Compact lookup data. Not prose — scan for the number/term you need.

---

## AAB genera at a glance

| Genus | Ethanol tol. | Acetic tol. | Overoxidizes? | Cellulose? | Typical use |
|---|---|---|---|---|---|
| *Acetobacter* | moderate | moderate | **Yes** (watch harvest) | some | classic surface vinegar |
| *Komagataeibacter* | **high** | **high** | low | **strong** (the mother) | high-acidity / submerged |
| *Gluconacetobacter* | moderate | moderate | yes | strong | cellulose, kombucha overlap |
| *Gluconobacter* | low–mod | low | weak | weak | sugary fruit ferments, gluconate |

Representative species: `A. aceti`, `A. pasteurianus`, `K. xylinus` (ex-*A. xylinum*), `K. europaeus` (industrial high-acidity), `K. hansenii`, `G. oxydans`.

---

## Process conditions (orientation)

| Parameter | Typical range | Note |
|---|---|---|
| Optimal temperature | 28–32 °C | *K. europaeus* tolerates higher |
| Starting ABV | 5–9% | dilute if >12% (ethanol toxicity) |
| Harvest residual ethanol | 0.2–0.5% (non-zero) | leaving 0% invites overoxidation |
| Finished acidity (table vinegar) | 5–7% | check regulatory floor |
| Pasteurization hold | ~60–65 °C | stabilizes for sale; kills the mother |
| Surface ferment time | weeks–months | Orleans |
| Submerged ferment time | hours–days | Frings acetator |

---

## Regulatory acidity floors (verify locally before relying)

| Jurisdiction | Minimum | Notes |
|---|---|---|
| US (FDA, CPG 525.825) | **≥4 g/100 mL (4%)** | below = not "vinegar" |
| EU / many national codes | **≥5%** typical | product-specific |
| Wine vinegar (EU) | **≥6%** | |
| Spirit vinegar | **≥5%** | |

---

## Formulas

- **Titratable acidity (% as acetic acid, w/v):**
  `acidity% = (V_NaOH(mL) × N_NaOH × 6.005) / V_sample(mL)`
  (6.005 = 60.05 g/mol acetic acid ÷ 1000 × 100; with 0.1 N NaOH and a 10 mL sample, each mL ≈ 0.06% acidity.)
- **GK value (total concentration):** `GK = % acetic acid + % residual ethanol`
- **Yield rule of thumb:** `~1% ABV → ~1% acetic acid` (stoichiometric max ≈ 1.04 g acetic per g ethanol).
- **pH is not acidity:** finished vinegar plateaus near pH 2.4–3.4 while % acidity keeps rising — always titrate.

---

## Titration quick procedure

1. Standardize NaOH (commonly 0.1 N or 1.0 N).
2. Pipette a known sample volume (e.g. 10 mL), add ~3 drops phenolphthalein.
3. Titrate to the first persistent faint-pink endpoint.
4. Apply the formula above. Run in duplicate; average.

---

## KB taxonomy tags (canonical)

`microbiology` · `biochemistry` · `methods` · `parameters` · `troubleshooting` · `measurement` · `safety-and-labeling` · `styles` · `equipment`

Confidence levels: `measured` · `published` · `practitioner-lore` · `inferred`
FAQ audiences: `home-fermenter` · `craft-producer` · `educator`

---

## Culture collections & sourcing

- **[DSMZ](https://www.dsmz.de/)** — German collection; *Acetobacter* / *Komagataeibacter* / *Gluconobacter* strains with documented optima.
- **[ATCC](https://www.atcc.org/)** — US collection; reference AAB strains.
- **[NCBI Taxonomy: Acetobacteraceae](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?name=Acetobacteraceae)** — current nomenclature.
- Raw, unpasteurized, "with the mother" commercial vinegars — practical wild starters for home programs.

---

## Key references

- FDA CPG Sec. 525.825 — Vinegar, Definitions/Adulteration: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/cpg-sec-525825-vinegar-definitions-adulteration-vinegar-water
- Yamada et al., reclassification → *Komagataeibacter*: https://doi.org/10.1007/s12275-012-2249-4
- Annu. Rev. Food Sci. Technol., Acetic Acid Bacteria review: https://doi.org/10.1146/annurev-food-030212-182512
- Solieri & Giudici (eds.), *Vinegars of the World*: https://doi.org/10.1007/978-88-470-0866-3
- Frings acetator (submerged process) background: https://www.frings.com/

---

## Tools / software

| Need | Tool |
|---|---|
| Acidity | NaOH titration kit, phenolphthalein |
| Starting ABV / Brix | hydrometer, refractometer |
| Residual ethanol | ebulliometer, enzymatic assay |
| Temp control | seedling heat mat + controller, fermentation chamber |
| Aeration (submerged) | aquarium/diaphragm pump + fine air stone (small scale) |
| Logging | this workspace's `outputs/` + a CSV/spreadsheet of batches |
