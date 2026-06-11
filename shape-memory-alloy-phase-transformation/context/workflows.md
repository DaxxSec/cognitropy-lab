# Workflows — Transformation Engineering Under an Environmental-Impact Lens

Step-by-step methodology. Today's technique is **environmental impact assessment**, so the spine of every workflow is the same: characterize and tune the transformation, *then* carry the decision into a life-cycle ledger — never one without the other.

---

## A. The integrated design loop (master workflow)

```
characterize → tune to spec → check functional limits → run LCA → use-phase balance → end-of-life → eco-performance frontier → decide
```

1. **Characterize** the transformation: `/dsc-transformation-map` for Ms/Mf/As/Af + hysteresis + enthalpy; `/clausius-clapeyron-fit` for the σ–T slope.
2. **Tune to spec**: `/composition-temperature-tune` to land Af, then capture the manufacturing tolerance budget (the Ni-sensitivity headline).
3. **Check functional limits**: `/superelasticity-window` for the operating window; `/functional-fatigue-budget` for cycle life; `/training-protocol` if a two-way effect is needed.
4. **Run the life-cycle ledger**: `/lca-cradle-to-gate` for embodied burden; `/use-phase-energy-balance` for the in-service comparison vs. the conventional alternative; `/recyclability-eol-assessment` for end of life and Ni risk.
5. **Integrate**: `/eco-performance-frontier` puts performance and environmental cost on one Pareto chart and recommends the knee.
6. **Decide** with the weighting made explicit, then save everything to `outputs/` so the decision is reproducible.

---

## B. Transformation-temperature targeting (decision tree)

```
Need a target Af.
├─ Is binary NiTi acceptable (biomedical / cost)?
│   ├─ Yes → tune Ni:Ti ratio. Compute the melt-control tolerance (~0.01 at% Ni per ~1 °C).
│   │        └─ Tolerance too tight to cast? → add a post-melt aging step (Ni₄Ti₃, raises Af).
│   └─ No / need >110 °C → add a ternary:
│         Hf or Zr (cheaper high-T) → check embrittlement + processing.
│         Pd or Pt (effective, narrow hysteresis) → STOP: cross-check `/lca-cradle-to-gate`,
│                                                   these carry large embodied-carbon + supply-risk penalties.
└─ Confirm composition by ICP / calibrated WDS, NOT EDS (too imprecise at this resolution).
```

The deliverable of temperature targeting is the **tolerance budget**, not just the nominal composition — the Ni-sensitivity makes manufacturability the real constraint.

---

## C. Functional-mode selection

| Need | Mode | Key workflow |
|------|------|--------------|
| Recover a set shape on heating | One-way SME | tune Af below service heat; verify stroke vs. `/functional-fatigue-budget` |
| Spontaneous cooling-driven motion, no load | Two-way SME | `/training-protocol`; accept ~2–5% strain and fade |
| Large recoverable strain at constant T | Superelasticity | `/superelasticity-window`; keep Af < T < Md with margin |
| Vibration damping | Hysteretic damping | maximize hysteresis loop area; Cu/Fe alloys can compete |

---

## D. The environmental-assessment workflow (the technique, in detail)

1. **Define goal, scope, functional unit, and boundary first.** A footprint without a functional unit is meaningless. State cut-offs.
2. **Build the cradle-to-gate inventory** (`/lca-cradle-to-gate`): material mass × buy-to-fly ratio, melting energy, working/annealing energy, shape-set, finishing. Tag each line with a data-quality flag.
3. **Reconcile against a named database** (ecoinvent / GaBi-Sphera / GREET). Report GWP and CED as **ranges**, never single point values — Ni/Ti extraction figures swing widely with ore type and energy mix.
4. **Attribute hotspots.** Usually raw-material extraction and the scrap ratio dominate; name the single biggest reduction lever.
5. **Use-phase balance** (`/use-phase-energy-balance`): the actuation duty cycle and grid intensity decide whether low actuation efficiency erases the system-level benefits. Compute the break-even cycle count vs. the conventional alternative — and accept "no break-even" as a valid, honest answer.
6. **End of life** (`/recyclability-eol-assessment`): pick the realistic route (closed-loop / downcycle / landfill), rate recyclability honestly given interstitial sensitivity, and assess Ni release against REACH + ISO 10993.
7. **Interpret**: pull it together in `/eco-performance-frontier`. Make the impact weighting visible; re-run when a feed changes.

---

## E. Reproducibility discipline (applies to every workflow)

- Always record scan rate, sample mass, test temperature, strain rate, and cycle count — transformation data is meaningless without them.
- State which temperature convention (onset/tangent vs. peak) and which standard you used.
- For LCA, log the database, version, functional unit, boundary, and every assumption. An LCA you cannot reproduce is an opinion, not an assessment.
- Save analyses to `outputs/` with the date in the filename so the decision trail survives.
