# Artist Role and Operating Context

This file captures who the user is, their experience level, and the context they operate in. Populated through `/onboard`.

## Schema

- **Name:** workspace owner's name
- **Years working glass:** rough total
- **Strongest forms:** what the artist makes most reliably
- **Weakest forms:** the failure-prone areas where the workspace's value will show first
- **Glass families experienced in:** subset of {Bullseye 90, System 96, Effetre 104, Borosilicate 33, others}
- **Studio role:** solo artist / lead gaffer with assistant / studio owner with multiple workers
- **Day job vs. full-time:** affects how often pre-flight discipline is realistic
- **Apprenticeship lineage:** who they trained under, what tradition (Italian, Pacific Northwest, Czech, etc.) — context for technique nomenclature

## How the Agent Uses This

- **`/form-sim`** verdict thresholds shift slightly: an experienced artist can be trusted with a yellow verdict on a familiar form; a beginner gets a hard recommendation to dry-run first
- **`/post-mortem`** confidence levels factor experience: if the artist has done a form 50+ times and it's failing in a new mode, that's a stronger signal than the same failure on a first attempt
- **Tone of explanations:** if "beginner," include more background; if "experienced," be terse and assume nomenclature
- **Apprenticeship lineage** affects vocabulary defaults — Italian-tradition gaffers use "punty" vs. some other traditions' "pontil"; the agent matches the artist's preferred term in outputs

## Worked Example (replace at /onboard)

```
- Name: Mara Chen
- Years working glass: 8
- Strongest forms: blown vessels (cups, vases up to 250 mm)
- Weakest forms: stemware (goblets) — transfer fractures and stem alignment
- Glass families experienced in: Spectrum/System 96 (primary), occasional Bullseye 90 fusing
- Studio role: lead gaffer with rotating assistants (3-4 different people across the year)
- Day job vs. full-time: full-time studio practice
- Apprenticeship lineage: trained at Pilchuck under a Czech-tradition gaffer; technique vocabulary skews European
```

## Multi-User Studio Notes

If the studio is multi-user, this file describes the workspace owner only. Each additional artist who logs sessions gets their own short profile under `context/contributors/<name>.md` (created on demand by `/batch-log` when a new artist's name appears). Their experience level and habits inform sim verdicts and post-mortem context for sessions they ran.
