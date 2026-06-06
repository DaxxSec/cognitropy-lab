# /mortar-key

Run the dichotomous identification key to place an unknown mortar in a binder class from field and simple-lab characters.

## Inputs

- Field characters: colour, scratch hardness, friability, visible lime lumps, visible aggregate (hand lens), grey cement haze (y/n).
- Acid (dilute HCl) reaction: fizz vigour, residue colour/feel.
- Optional simple-lab: approximate binder:aggregate after digestion, aggregate sieve grading.

## Steps

1. Read `context/references.md` "Binder classes" and `context/workflows.md` "Keying out an unknown mortar".
2. Begin at couplet 1 and work down, recording which lead is taken and the character that justified it:
   - **1.** Vigorous fizz, soft, scratches easily, lime lumps present → go to 2. / Sluggish fizz or grey hydraulic residue, hard → go to 4.
   - **2.** No hydraulic phases, sets soft and slow → **air lime**. / Brick-dust/pozzolan inclusions, slightly faster/harder → **pozzolan-gauged / feebly hydraulic**.
   - **4.** Moderate hardness, HI ~0.16–0.31 if known → **moderately hydraulic (NHL 2/3.5)**. / Hard, HI ~0.31–0.42 → **eminently hydraulic (NHL 5)** → go to 5.
   - **5.** Very fast/hard, natural-cement character → **natural / Roman cement**. / Grey, dense, alite, modern → **Portland-cement mortar (distant clade — flag incompatibility)**.
3. Note any character that pushes toward two clades; mark the determination *ambiguous* if the key forks.
4. State a provisional binder class and confidence.
5. Recommend the next step: confirm with `/characterize-historic-mortar`, or `/delimit-mix` if a later campaign is suspected.

## Output

A short keyed determination `outputs/key-<slug>-YYYY-MM-DD.md`: the lead path taken, the character at each couplet, the provisional class, confidence, and the recommended confirmatory action.

## Notes

- The key is provisional by design — it narrows, it doesn't confirm. Calcareous aggregate and contamination both mislead it.
- Cement haze on an otherwise soft, lime building almost always signals a later repointing, not the original.
