# Tools, Formulas, and File Schemas

This file is what the agent reaches for when it needs an actual computation or a canonical file shape, not background concepts (those live in `domain-knowledge.md`).

## Computational Helpers

The agent doesn't need an external simulator — every relevant calculation fits in pure stdlib Python or even mental arithmetic. The formulas below are the operating set.

### Working-Time Budget
```python
def working_time_remaining_s(initial_T_C, current_T_C, ambient_T_C, gather_mass_g, ops_planned):
    """
    Crude estimator. Returns seconds until surface drops below working point (1050 C
    soda-lime, 1250 C borosilicate). 'ops_planned' is a list of (op_name, duration_s).
    Looks up per-op surface delta-T from the table in domain-knowledge.md.
    Assumes radiative cooling baseline of ~12 C/s for a 300 g gather, scaling as mass^(-1/3).
    """
    BASELINE_RAD_COOL_C_PER_S = 12.0
    MASS_REF_G = 300
    radiative_rate = BASELINE_RAD_COOL_C_PER_S * (MASS_REF_G / gather_mass_g) ** (1/3)
    op_delta_lookup = {
        "marver_5s": 80, "block_3s": 50, "jacks_5s": 40,
        "blow_puff": 10, "optic_3s": 70, "paddle_3s": 30,
    }
    cumulative_drop = current_T_C and (initial_T_C - current_T_C) or 0
    for op_name, dur_s in ops_planned:
        cumulative_drop += op_delta_lookup.get(op_name, 30)
        cumulative_drop += radiative_rate * dur_s
    target_drop_to_working_point = initial_T_C - 1050  # soda-lime; pass 1250 for boro
    margin_C = target_drop_to_working_point - cumulative_drop
    if margin_C <= 0:
        return 0
    return margin_C / radiative_rate
```

### Gravity Sag Estimator
```python
def sag_mm_in_window(unsupported_length_mm, viscosity_poise, duration_s, density_g_cm3=2.5):
    """
    Indicative sag estimator. Output is order-of-magnitude, not predictive to <1 mm.
    Compare to the form-type threshold from domain-knowledge.md.
    """
    g_mm_s2 = 9800.0
    rho_g_mm3 = density_g_cm3 / 1000.0
    # Convert poise to Pa·s: 1 poise = 0.1 Pa·s
    eta_Pa_s = viscosity_poise * 0.1
    # eta in g/(mm·s) for unit consistency: 1 Pa·s = 1 g/(mm·s) actually, keep SI
    # Indicative formula; see Trier "Glasschmelzofen" for real treatment
    sag = (rho_g_mm3 * g_mm_s2 * unsupported_length_mm**2 * duration_s) / (3 * eta_Pa_s * 1000)
    return sag
```

### Cool Curve Anneal-to-Strain Rate
```python
def safe_anneal_to_strain_rate_C_per_h(max_wall_thickness_mm, glass_family):
    K = {"soda-lime": 1500, "borosilicate-33": 800, "bullseye-90": 1500,
         "system-96": 1500, "effetre-104": 1500}.get(glass_family, 1500)
    raw = K / (max_wall_thickness_mm ** 2)
    capped = min(raw, 200.0)  # most lehr controllers cap at 200 C/h ramp
    # Round down to controller-friendly value
    for r in [200, 150, 120, 100, 80, 60, 50, 40, 30, 20, 10]:
        if capped >= r:
            return r
    return 10
```

### COE Compatibility Check
```python
def compatible(coe_a, coe_b, tolerance=0.5):
    """COE values in 10^-7 / K. Tolerance 0.5 is studio-conservative; manufacturer
    fused-strip tests use ~0.7 as boundary."""
    return abs(coe_a - coe_b) <= tolerance
```

## File Schemas

### Form Spec (`planning/form-<slug>-v<n>.md`)
```
# Form: <human name>
- Slug: <kebab-case>
- Version: <n>
- Created: <YYYY-MM-DD>
- Sim verdict: <green/yellow/red>
- Scenario test: <summary>

## Geometry
- Total mass (g): <n>
- Max wall thickness (mm): <n>
- Max horizontal reach (mm): <n>
- Distinct features: <list>

## Glass & Color
- Glass family: <name>
- Base glass: <melt batch ID or supplier+lot>
- Colors: <list of {name, supplier, lot, COE}>

## Gather Plan
- Gather 1: <mass>, <ops between this and next>
- Gather 2: ...

## Cool Curve
- Segment 1: load <T> -> hold <T> for <hh:mm>
- Segment 2: <T> -> <T> @ <C/h>
- Segment 3: <T> -> <T> @ <C/h>
- Segment 4: <T> -> off

## Sim Notes
- Working time per heat: <s>
- Sag risk: <green/yellow/red>
- COE compatibility: <pass/fail>

## Scenario Test
- Scenario | Verdict | Notes
- Glory hole crash | <v> | ...
- Color rod break | <v> | ...
- Punty failure | <v> | ...
- Cool curve crash | <v> | ...
- Devit onset | <v> | ...
- COE mismatch | <v> | ...
- Gather over-mass | <v> | ...
```

### Batch Record (`work-log/<YYYY-MM-DD><seq>.md`)
See `resources/batch-record-card.md` for the canonical schema; this file just points to it.

### Piece Record (`outputs/pieces/<piece-id>.md`)
```
# Piece: <piece-id>
- Form spec: <link>
- Originating batch: <link>
- Mass (g): <n>
- Geometry: <h x w x d mm>
- Date completed: <YYYY-MM-DD>

## Follow-Up Schedule
- 24h: <date> — <observations>
- 7d: <date> — <observations>
- 30d: <date> — <observations>
- 90d: <date> — <observations>

## Diagnostic Followups
(populated by /post-mortem if it cracks)
```

### Lehr Program Notation
Programs are written compactly as `[loadT -> holdT @ rate, hold for time], ...`. Example for a 12 mm wall borosilicate piece:
```
[room -> 565 @ ramp_max, hold 60 min] -> [565 -> 525 @ 60 C/h] -> [525 -> 100 @ 120 C/h] -> [100 -> off, natural]
```

## Tool Cross-Reference

| Studio tool | What it observes / produces | How the agent uses it |
|------------|------------------------------|------------------------|
| Optical pyrometer | Glory hole interior T | Calibrates working-time budget per heat |
| Kitchen scale | Gather mass after marver | Verifies sim mass assumption |
| Hygrometer | Studio RH | Goes into ambient envelope |
| Lehr controller log | Actual program executed | Confirms vs. planned program in batch closeout |
| Polariscope (crossed polarizers) | Residual stress fringes | Compatibility test verification |
| Phone camera | Piece photos, fracture surfaces | Stored under outputs/photos/, referenced from post-mortems |
| Notebook (legacy) | Pre-workspace observations | Source for backfilling early batch records |

## What the Agent Does *Not* Do

- Run any calculation that requires real CFD/FEA — those are referenced (e.g., for thick castings) but never simulated here
- Operate any controller, valve, or piece of physical equipment — every action is the user's
- Substitute for safety supervision of beginners
- Accept manufacturer claims uncritically when they conflict with observed studio outcomes — the batch record is the ground truth
