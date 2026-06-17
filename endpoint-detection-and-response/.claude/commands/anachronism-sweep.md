# /anachronism-sweep — Hunt Temporal Inconsistencies

Find artifacts whose chronology could not be genuine — the EDR analogue of spotting a metal zipper on a "1600s" gown or aniline dye before 1856. This is timestomp and backdating detection (MITRE T1070.006).

## Inputs

- A set of artifacts or a host's MFT / Amcache / Prefetch / event-log exports.
- The claimed timeline or baseline you are testing against.
- Time zone of each source (normalize to UTC; record offsets).

## Steps

1. **Pair the timestamps**: for each file compare `$STANDARD_INFORMATION` vs `$FILE_NAME` create/modify times. `$SI` < `$FN`, or `$SI` with zeroed sub-seconds while neighbors carry precision, is a tampering tell.
2. **Cross-chronology check**: compare Amcache/Prefetch first-execution against the binary's PE compile timestamp. Execution before compilation is impossible — flag it.
3. **Authenticity checks**: code-signing certificate validity window vs. observed time; required OS build vs. host's actual build; version-resource vs. on-disk metadata.
4. **Sequence integrity**: verify event-log record numbers and `$LogFile`/USN ordering are monotonic; gaps or resets indicate log tampering or rollback.
5. **Cluster the hits**: group anachronisms by toolset/path; a cluster marks an adversary-controlled component to re-provenance with suspicion.

## Output

`outputs/anachronism-sweep-<host>-<date>.md`: a table of flagged artifacts with the specific inconsistency, the two sources that disagree, and a tamper-confidence rating; a short "trusted timeline" list of artifacts that passed.

## Notes

- Most timestomping tools alter `$SI` but not `$FN` — the pair is your sharpest instrument.
- A passed sweep promotes artifacts into the trusted set used by `/reconstruct-timeline`; a failed one routes them back to `/artifact-provenance`.
