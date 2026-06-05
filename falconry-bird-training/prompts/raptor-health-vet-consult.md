# Raptor Health Vet Consult

## Purpose

Use when a bird shows a health concern and you need to hand an avian veterinarian a clear, complete history fast. This organizes the facts for the vet — it is **not** a diagnosis. Pairs with `/vet-intake`. Call the vet; don't wait.

## Prompt Template

```
You are helping me prepare a health-concern summary for my avian veterinarian. This is
for the vet to act on — do not diagnose or prescribe.

- **Bird (signalment):** [species, age, source, band #, sex if known]
- **Presenting signs:** [going light / fluffed / reluctant / mouth lesions / labored breathing / vomiting / lameness / abnormal mutes]
- **Onset & progression:** [when it started, getting better/worse]
- **Weight trend (7–14 days):** [from the log]
- **Recent diet:** [species, source, dates — note any pigeon/dove]
- **Mutes & castings:** [appearance, timing]
- **Housing / recent changes:** [mews, ventilation, new bird, stressor]

Please assemble this into a tight intake summary for the vet, list the candidate
differentials to raise (e.g. frounce, aspergillosis, parasites, sour crop), and
remind me to call the clinic immediately.
```

## Expected Output

- A structured intake: signalment, signs with onset, weight trend, diet, mutes/castings, housing.
- A short list of candidate differentials to raise with the vet (not a diagnosis).
- An explicit prompt to call the avian vet now and stop flying the bird.
