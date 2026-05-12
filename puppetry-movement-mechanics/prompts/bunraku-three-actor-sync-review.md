# Prompt — Bunraku Three-Actor Sync Review

A reusable prompt for a `/peer-review` pass focused specifically on bunraku-style triple-actor coordination (omozukai + hidarizukai + ashizukai). Use this when the rule under review touches the `tactic.ensemble-sync-loss` family.

## When to Use

- A new rule draft exists in `outputs/rules/draft/` tagged with `tactic.ensemble-sync-loss`
- A tuning is proposed for an active rule in that family
- A post-show report flags multiple firings of an existing ensemble-sync-loss rule

## Prompt Body

> You are reviewing a movement-detection rule that targets bunraku-style ensemble-sync coordination. Bunraku is a triple-actor form: the omozukai operates head + right arm, the hidarizukai operates left arm, the ashizukai operates legs (or the kimono for female puppets). Senior ensembles target <50 ms phase lag between omozukai head-turn and hidarizukai counter-arm; training ensembles run at 100–200 ms; "unintegrated" reads emerge past ~250 ms.
>
> You have been assigned the **<color>** role for this review. Refer to your role's prompt below.
>
> ### If Red:
> Construct three logs in which the rule should fire but might not, then three logs in which the rule might fire but should not. Pay particular attention to:
> - Female-puppet kimono manipulation (no ashizukai legs; the ashizukai role is different — focus on weight-cue rather than foot mark)
> - Cross-stage moves where the omozukai is intentionally rushing the cue (the rule should NOT fire; this is dramaturgical)
> - Training-pair sessions where 100–200 ms phase lag is expected and acceptable (rule should NOT fire below the senior threshold)
>
> ### If Blue:
> Walk the rule against its cited example logs. Confirm:
> - The phase-lag computation is between the right manipulator pair (omozukai-hidari for arm coordination; omozukai-ashi for body-foot coordination)
> - The threshold matches the ensemble's stated experience tier (senior / training / unintegrated)
> - The tags reference `technique.omozukai-hidari-phase-lag` or `technique.ashizukai-floor-drift` from the failure-mode catalog
>
> ### If Purple:
> Propose one specific change. Common improvements in this family:
> - Add a `puppet_metadata.female_puppet: true` filter to suppress ashizukai-floor-drift firings on legless puppets
> - Add a `cue_metadata.intent: rushed` filter to suppress firings during dramaturgical rushes
> - Tighten or relax the phase-lag threshold by ensemble experience tier
>
> ### Disposition Required
> Write one of: `accepted`, `tune <field>`, `reject`, `escalate`. Include a written rationale of at least two sentences.

## Why This Prompt Exists

Bunraku ensemble-sync-loss rules are the workspace's most common false-positive source — bunraku has many *intentional* asymmetries (kimono-puppets, cued rushes, breath-cued holds) that look like sync loss to a naive rule. This prompt's checklist forces reviewers to walk the named cases, not just the cited logs.

## Reference

- Adachi, Barbara — *The Voices and Hands of Bunraku* (Kodansha, 1978)
- Brandon, James R. — *Theatre in Southeast Asia* (Harvard, 1967), bunraku chapter
- Workshop materials from the Bunraku Kyokai (Osaka), if accessible to the company through a tradition-bearer
