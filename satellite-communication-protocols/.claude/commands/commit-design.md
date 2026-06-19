# /commit-design

Lock a link design point with full provenance — only once the budget closes, the Shannon gap is understood, and every lever carries a cost-benefit justification. This is the "final prescription" of the optical system: the agreed configuration that goes to build review, with every surface and every dB accounted for.

## Inputs

- The completed `budget-<direction>.md`, `shannon-gap.md`, `aberration-audit.md`, `aperture-tradeoff.md`, `modcod-pareto.md`, and `rain-margin-economics.md` for the case
- The target requirements from `mission.md` (rate, availability, quality floor)
- A sensitivity range for the most uncertain inputs (rain region, antenna efficiency, phase-noise mask)

## Steps

1. **Gate checks — refuse to commit if any fails:** link margin ≥ required at the target availability; spectral efficiency below the Shannon ceiling (no impossible claims); every dB term in the ledger has a source; EIRP/PFD within ITU regulatory limits.
2. Assemble the **design prescription**: chosen band, antenna sizes/efficiencies, Tx power, G/T, MODCOD or ACM ladder, FEC, and the margin allocation across rain / pointing / aging / interference.
3. Attach the **cost-benefit dossier**: for every lever pulled, its marginal dB and marginal $, why it was chosen over the next-best lever, and the levers explicitly *not* pulled (and why they failed the knee test).
4. Run **sensitivity analysis**: perturb the top uncertain inputs ±1σ and report which ones flip the margin negative — the design's "tolerancing," exactly like an optical tolerance budget. Flag anything that makes the link fragile.
5. Record the **residual risks and watch-items** (e.g. "margin assumes 99.5% rain region D; verify site"), stamp the inputs and tool versions for reproducibility, and write the committed prescription.

## Output

`outputs/links/<mission-id>/committed-design.md` — the locked prescription, the cost-benefit justification per lever, the sensitivity/tolerance table, the residual risks, and full provenance. This is the document a design review, a customer, or an auditor reads.

## Notes

- Commit is **append-only**: a later change is a *new* committed design that cites and supersedes this one, never an in-place edit — so the rationale history survives.
- If the sensitivity analysis shows a single input flipping the link negative, the design is not done — either buy tolerance (margin) for that input or pin it down before committing.
