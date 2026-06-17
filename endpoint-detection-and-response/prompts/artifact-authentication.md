# Artifact Authentication

## Purpose

Use to decide whether an endpoint artifact is a genuine system component or a planted/tampered one, by hunting anachronisms — the cyber version of authenticating a garment by spotting materials that couldn't exist in the claimed period.

## Prompt Template

```
You are authenticating an endpoint artifact for tampering or planting. Treat it as suspect until its chronology proves consistent.

- **Artifact:** [PATH, SHA-256, SIGNER, CLAIMED IDENTITY e.g. "legit System32 binary"]
- **Timestamps:** [$SI and $FN create/modify; Amcache/Prefetch first-exec; PE compile time]
- **Environment:** [HOST OS BUILD, CERT VALIDITY WINDOW, BASELINE EXPECTATION]
- **Context:** [WHY IT WAS FLAGGED]

Please:
1. Compare $SI vs $FN and first-execution vs compile time; identify any impossible chronology.
2. Check signer validity window and OS-build compatibility against the host.
3. Compare path/presence to the expected baseline for this artifact.
4. Return a verdict: GENUINE / TAMPERED / PLANTED, with a tamper-confidence and the specific tells.
```

## Expected Output

- A verdict (GENUINE / TAMPERED / PLANTED) with confidence.
- The specific anachronism(s) found, naming the two sources that disagree.
- A recommended next action (trust, re-provenance, or escalate).
