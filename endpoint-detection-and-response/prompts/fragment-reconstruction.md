# Fragment Reconstruction

## Purpose

Use when you have scattered, possibly incomplete telemetry events and need a single coherent attack narrative with the evidence/conjecture boundary made explicit. The textile-conservation move: reconstruct the whole garment from fragments without inventing what isn't there.

## Prompt Template

```
You are an EDR reconstruction analyst. Reconstruct an attack narrative from these telemetry fragments, honoring the evidence/conjecture boundary.

- **Incident / scope:** [HOST(S), TIME WINDOW, TIME ZONE]
- **Fragments (events):** [PASTE TELEMETRY: process, file, registry, network, auth events]
- **Known gaps:** [LOGGING DISABLED / TIME RANGE MISSING / DELETED ARTIFACTS]
- **Context:** [WHAT TRIGGERED THE INVESTIGATION]

Please:
1. Normalize all events to UTC and order them by deposition (occurrence), not by the order listed.
2. Build the narrative, tagging every claim CONFIRMED / INFERRED / CONJECTURE with its backing event.
3. Insert explicit gap markers where telemetry is missing — do not bridge silently.
4. Map each step to MITRE ATT&CK and name the single most important next fragment to acquire.
```

## Expected Output

- A UTC-ordered, confidence-tagged timeline of the reconstructed narrative.
- An explicit list of evidence gaps (documented lacunae).
- ATT&CK technique IDs per step and a prioritized "acquire next" item.
