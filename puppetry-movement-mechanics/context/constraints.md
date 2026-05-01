# Constraints

> Populated by `/onboard`. Boundaries the agent must respect.

## Artistic Constraints

- **Detection rules describe failure modes, not aesthetic choices.** A choreographer's deliberate hesitation is not an anomaly to flag. The agent must distinguish between intentional artistic choices (which belong in `context/project.md`) and unintended drift (which belong in detection rules). When uncertain, ask before flagging.
- **Tradition-bearer authority.** For Bunraku, Wayang Kulit, Sicilian opera dei pupi, or any other living-lineage tradition, the company's tradition-bearer (or named consultant in `context/project.md`) has authority over what is or is not a "failure mode" in that tradition. Detection-engineering taxonomy never overrides tradition-bearer judgment.
- **Director's intent overrides rule firings during a run.** Once a show is in performance, the agent surfaces detected anomalies after the show, not during it. No real-time flags during a live performance unless the director specifically opts in.

## Safety Constraints

- **Mechanism-failure rules are advisory, not authoritative.** A rigger's body sense and on-the-ground judgment is the final word on whether a mechanism is safe to fly, lift, drop, or hand off. The agent's silence does not constitute a safety clearance.
- **Performer safety overrides logging completeness.** If logging would slow down a performer's pre-show prep to the point of stress, drop the log; never sacrifice prep time for completeness.
- **Audience safety: no streamed motion telemetry to public networks.** Calibration data, IMU streams, and servo telemetry stay on company hardware.

## Privacy & Consent Constraints

- **Performer likeness in raw video.** If video is captured, store it on company-controlled storage; the workspace's logs (timestamps + numbers) are derived artifacts and do not need the same access controls. Confirm performer consent before storing video.
- **Junior performer logs.** Training logs of junior puppeteers (e.g. a hidarizukai trainee under a senior omozukai) carry sensitivity. Default access: trainee + senior + company training lead.
- **Audience-side observations.** Notes from house staff or audience reactions stay anonymized in logs.

## Detection-Engineering Constraints

- **No silent rule merges.** Every rule moving from `outputs/rules/draft/` to `outputs/rules/active/` must have a written peer-review record in `outputs/reviews/`. The agent enforces this as a precondition for `/detect-anomaly` to use a rule against logs.
- **Rules are versioned.** Use `git` for rule history; never edit a rule in place without bumping the rule's `version:` field and adding a new review record.
- **No rule against a single observation.** A rule needs at least two distinct logs as evidence before drafting. The peer-review red role specifically tests for this.

## Workspace Hygiene Constraints

- **No PII in rule descriptions.** Rules describe mechanism behavior; performer names belong in roster files, not rule files.
- **No raw video in this repo.** Video lives in company storage; logs reference video by URI / file path / timestamp.
- **No autosharing of rules outside the company.** Sharing the rule set externally is a deliberate, opt-in act — see `legal & ethical considerations` in `README.md`.
