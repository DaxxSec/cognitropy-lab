# Prompt Template: Tune Safety Audit

Use this template when asking Claude to evaluate a tune for safety before driving or pulling on it.

---

## Full Audit Template

```
I need a safety audit of my current tune before I put the car under load.

**Vehicle:** [Year Make Model]
**Engine:** [Engine code, displacement, build level — stock/built]
**Turbo:** [Spec or OEM]
**Fuel:** [Octane, ethanol content]
**Current boost target (peak):** [X psi]
**Injectors:** [Size and type]
**ECU platform:** [Name and tuning software]

**What I'm specifically concerned about:**
[Describe any areas of worry, or say "general safety check"]

**Tune data / tables:**
[Paste relevant maps here, or describe values for key cells]

Key tables I want checked (mark which you're providing):
- [ ] Ignition advance / timing table
- [ ] Fuel map / VE table / injector PW
- [ ] Boost target / boost control table
- [ ] AFR target map
- [ ] Rev limiter / fuel cut settings
- [ ] Knock retard sensitivity / response
- [ ] Cold start enrichment

Please do a safety audit first, then give me performance observations.
```

---

## Pre-Dyno Quick Check Template

```
Quick pre-dyno safety check. I'm heading to the dyno [TODAY/TOMORROW].

[VEHICLE from project.md] running [FUEL].
Current tune was set up for [TARGET BOOST] on [INJECTORS].
Last dyno was [DATE] — [POWER] on [FUEL].

Changes since last dyno: [list or "none"]
Anything I should verify in the tune before loading on the rollers?
```

---

## Post-Tune-Change Verification Template

```
My tuner just sent me a revised map. Before I drive on it, I want to verify
it's safe for my setup.

My constraints:
- Max boost: [X psi] (hard limit per my build)
- AFR target at WOT: [X.X:1] on [FUEL]
- Injectors: [size] at [impedance]
- Max knock retard I'm comfortable with: [X degrees]

The tuner's changes (as described to me): [describe or paste tune diff]

Can you flag anything that approaches my limits or looks concerning for my setup?
```
