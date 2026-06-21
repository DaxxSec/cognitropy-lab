# /binding-kinetics

Design and QC a label-free binding-kinetics experiment (SPR / BLI) to determine kon, koff, and KD for an antibody–antigen pair, with sanity checks against the most common fitting artifacts.

## Inputs

- The pair (antibody + antigen) and which partner is immobilized/captured vs in solution.
- Platform (Biacore SPR, Octet BLI), capture chemistry (anti-Fc, amine coupling, streptavidin-biotin), and antigen valency (monomeric is essential for clean 1:1).
- Expected affinity range (sets the analyte concentration series and contact/dissociation times).
- Optional: prior or replicate data to compare against.

## Steps

1. Read `context/concepts.md` "Characterization" and `context/references.md` "Affinity & kinetics reference ranges".
2. Choose orientation to avoid avidity: capture the antibody and flow monomeric antigen (or vice versa) so the interaction is genuinely 1:1; never flow a bivalent IgG over a densely-coupled antigen if you want intrinsic affinity.
3. Design the analyte series (typically a 2–3× dilution series bracketing the expected KD), include buffer-only and a regeneration scout; set association/dissociation times so koff is observable within the window.
4. Specify referencing: reference surface subtraction + buffer (double referencing); plan regeneration that doesn't denature the capture.
5. Define the QC gates: fit to 1:1 Langmuir, residuals within noise, Rmax consistent with capture level, koff not faster than the instrument can resolve, and Chi²/U-value within tolerance — flag mass-transport limitation and rebinding.
6. Report KD with kon/koff, the concentration range it's valid over, and a confidence note; feed koff into `/affinity-maturation-plan` if a kinetic campaign follows.

## Output

- `outputs/kinetics/<pair>-kinetics-<date>.md` — experiment design, sensorgram QC checklist, fitted kon/koff/KD with error, fit-quality verdict, and any artifact flags (avidity, mass transport, rebinding, drift).
- Demonstrates competency: **binding-kinetics QC**.

## Notes

- Avidity inflates apparent affinity by orders of magnitude — a "20 pM" bivalent number over a 1:1 monomeric KD of 5 nM is the classic trap.
- Very fast on-rates can be mass-transport-limited; lower the surface density or raise the flow rate before trusting kon.
- Steady-state (equilibrium) affinity fitting is the fallback when koff is too fast to fit kinetically — report which method was used.
