# /audit-fixity-integrity — Plan and verify bit-level integrity over time

Establish and run a fixity regime that detects bit rot, silent corruption, and unauthorized change across the lifetime of the digital masters, and turns a checksum mismatch into a recovery action rather than a surprise.

## Inputs

- The package(s) or directory tree of preservation masters and their existing fixity manifest (from `/assemble-aip-package`), if any.
- Storage topology: number of replicas, locations, media types, and whether storage is self-healing (e.g. checksummed filesystem) or not.
- Verification cadence policy, or none yet (this command can set one).

## Steps

1. **Baseline checksums.** If no manifest exists, generate SHA-256 for every master and derivative and record file, size, algorithm, and timestamp. This baseline is the source of truth for all future checks.
2. **Set a risk-based cadence.** Decide verification frequency by replica count and media risk — fewer replicas / aging media verify more often. Capture the policy in `context/workflows.md` terms.
3. **Run verification.** Recompute checksums and diff against the manifest. Classify each file: verified / changed / missing / new. A "changed" master with no logged preservation event is a corruption or tampering signal.
4. **Cross-check replicas.** On a mismatch, compare the failing copy against its replicas to determine the good copy; never overwrite from an unverified source.
5. **Recover and log.** Restore the corrupted file from a verified replica, then record a PREMIS fixity-failure + recovery event so the history is auditable.
6. **Report integrity health.** Summarize the verified/changed/missing counts, any recovery actions, replica divergence, and the date of the next scheduled check.

## Output

`outputs/fixity-audit-<date>.md`: the verification results by class, mismatches with their resolution, replica comparison outcomes, recovery events logged, and the next-check date. Update the fixity manifest only after verified recovery.

## Notes

- Fixity without replicas is a smoke alarm with no exit — it tells you the master is corrupt but gives you nothing to restore from. The cadence policy and the replication policy are one decision.
- A changed checksum on a file with no corresponding preservation event is the canonical signal of silent corruption or tampering — treat it as an incident, not a glitch.
- Self-healing checksummed storage reduces but does not eliminate the need for independent fixity — verify across the storage boundary, not just within it.
