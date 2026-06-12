# Red-Team Attack Narrative

## Purpose

Generate a plausible adversary attack narrative to stress-test a protective posture *and* to test an apprentice's detection and interdiction reasoning. Defensive red-teaming only — used to harden, never to plan real harm.

## Prompt Template

```
You are a red-team analyst building a defensive attack hypothesis to test an EP posture.

I have the following inputs:

- **Principal exposure summary:** [FROM /protectee-risk-profile, REDACTED]
- **Posture to test:** [ADVANCE/ROUTE/SDR/EAP UNDER REVIEW]
- **Adversary archetype:** [FIXATED PERSON / GROUP / INSIDER — CAPABILITY TIER]
- **Constraint:** [WHAT THE ADVERSARY DOES NOT KNOW OR CANNOT DO]

Please:
1. Walk a plausible adversary through the hostile planning cycle against this posture.
2. At each phase, name the protective measure that *should* detect them and whether the current posture would.
3. Identify the single weakest link the posture leaves open.
4. Recommend the cheapest hardening that closes it, and the indicator the detail should now watch for.
```

## Expected Output

- A phase-by-phase attack narrative mapped to detection opportunities (the inverse of `/attack-cycle-map`).
- The weakest link and a cost-ranked hardening recommendation.
- Framed as a defensive test; no operational attack detail beyond what's needed to harden.
- Doubles as a WBA of the apprentice's adversary-perspective reasoning.
