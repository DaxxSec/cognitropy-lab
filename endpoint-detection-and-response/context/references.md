# References — Lookup Tables & Catalogues

Compact lookup data for fast recall during a reconstruction. Prose lives in `concepts.md`; methodology in `workflows.md`.

## MITRE ATT&CK tactics (the typology spine)

| ID | Tactic | "Stratigraphic" role |
|----|--------|----------------------|
| TA0043 | Reconnaissance | pre-find context |
| TA0042 | Resource Development | workshop / supply line |
| TA0001 | Initial Access | bottom stratum |
| TA0002 | Execution | first deposit on host |
| TA0003 | Persistence | the layer that survives reboot |
| TA0004 | Privilege Escalation | mid stratum |
| TA0005 | Defense Evasion | the tampering (anachronisms live here) |
| TA0006 | Credential Access | enables geovelocity abuse |
| TA0007 | Discovery | actor's own recon on-host |
| TA0008 | Lateral Movement | the diffusion process |
| TA0009 | Collection | staging |
| TA0011 | Command and Control | top stratum / supply line |
| TA0010 | Exfiltration | egress |
| TA0040 | Impact | the damage in the condition report |

## Windows telemetry & artifact sources

| Source | What it tells you | Reconstruction use |
|--------|-------------------|--------------------|
| Sysmon Event ID 1 | process create + full cmdline + hashes | provenance, lineage |
| Security 4688 / 4624 / 4625 | process create / logon / failed logon | timeline, geovelocity |
| Sysmon 3 / 5156 (WFP) | network connection | C2 mapping |
| Sysmon 11 / 23 | file create / file delete (w/ archived data) | stratigraphy, deletions |
| Sysmon 13 | registry value set | persistence |
| Prefetch (`.pf`) | program executed, run count, first/last run | anachronism, first-seen |
| Amcache.hve | program presence + SHA-1 + first-execution | provenance, anachronism |
| ShimCache (AppCompatCache) | program presence/path (order ≠ exec) | corroboration |
| SRUM | per-app network/resource usage over time | exfil sizing |
| USN Journal / $LogFile | file-system change record | deletion recovery, order |
| MFT `$SI` vs `$FN` | the timestamp pair | **timestomp detection** |

## Anachronism indicators (the "zipper on the gown")

| Tell | Meaning |
|------|---------|
| `$SI` < `$FN` creation time | timestamps backdated (T1070.006) |
| Zeroed `$SI` sub-second precision | tool wrote whole-second times |
| Amcache first-exec < PE compile time | impossible chronology |
| Code-signing cert valid window mismatch | reused/forged signature |
| Binary requires OS build newer than host claims | planted from elsewhere |
| Prefetch run-count vs. "first seen" disagree | history rewritten |

## Geospatial data sources (today's technique)

| Source | Resolution | Caveat |
|--------|-----------|--------|
| MaxMind GeoLite2 / GeoIP2 | country good; city ~mediocre | free tier coarse |
| IPinfo / IP2Location | country + ASN | commercial accuracy varies |
| RIR WHOIS (ARIN/RIPE/APNIC/LACNIC/AFRINIC) | allocation org/country | registrant ≠ user location |
| BGP / ASN (bgp.he.net, Team Cymry) | network ownership | best for "supply line" |
| Reverse DNS / passive DNS | hosting & history | rented infra obscures actor |

**Geovelocity rule of thumb:** flag if `distance_km / hours_between_logons` > ~900 km/h (commercial-flight ceiling) for the same identity.

## Detection-rule references

- **Sigma** — generic detection rule format, converts to many EDR/SIEM query languages: <https://github.com/SigmaHQ/sigma>
- **KQL** — Microsoft Defender / Sentinel query language.
- **EQL** — Elastic / event query language for sequence detection.
- **Atomic Red Team** — test cases to validate a drafted rule: <https://github.com/redcanaryco/atomic-red-team>

## External catalogues & standards

- MITRE ATT&CK — <https://attack.mitre.org/>
- MITRE ATT&CK Groups (campaign typology) — <https://attack.mitre.org/groups/>
- NIST SP 800-86, *Guide to Integrating Forensic Techniques into IR* — <https://csrc.nist.gov/publications/detail/sp/800-86/final>
- NIST SP 800-61r2, *Computer Security Incident Handling Guide* — <https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final>
- RFC 3227, *Guidelines for Evidence Collection and Archiving* (order of volatility) — <https://www.rfc-editor.org/rfc/rfc3227>
- LOLBAS (living-off-the-land binaries) — <https://lolbas-project.github.io/>

## Costume-reconstruction lineage (the imported discipline)

- Janet Arnold, *Patterns of Fashion* — the gold standard for evidence-based reconstruction from extant garments.
- ICOM-CC textile conservation condition-report practice — the model for `/condition-report`.
- Dye chronology (e.g. aniline mauveine, 1856) and sewing-machine-stitch dating — the original "anachronism detection" that `/anachronism-sweep` ports to host forensics.
