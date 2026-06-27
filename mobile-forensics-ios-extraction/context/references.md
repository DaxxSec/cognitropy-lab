# Mobile Forensics — iOS Extraction — Reference Tables

Compact lookup data for use during an examination. Defer to upstream sources (Apple Platform Security, NIST SP 800-101r1, iLEAPP) for fuller specs.

## SoC → acquisition eligibility

| SoC | Representative devices | checkm8 (BootROM)? | Notes |
|-----|------------------------|--------------------|-------|
| A5–A7 | iPhone 4S–5S | Yes | Oldest; weak/no SEP on A5/A6 |
| A8–A9 | iPhone 6 / 6S / SE(1) | Yes | SEP present |
| A10 | iPhone 7 | Yes | |
| A11 | iPhone 8 / X | Yes | **Last checkm8-eligible** SoC |
| A12–A13 | iPhone XS–11 | No | Agent-based FFS in AFU; SEP hardened |
| A14–A16 | iPhone 12–14 | No | Commercial exploit-dependent |
| A17+ | iPhone 15 Pro onward | No | Newest; most constrained |

checkm8 is a permanent BootROM exploit (unpatchable by software) but does **not** by itself defeat passcode-derived class keys on a BFU device.

## Data Protection classes (quick recall)

| Class | Constant | Available when |
|-------|----------|----------------|
| A | `NSFileProtectionComplete` | Unlocked only |
| B | `NSFileProtectionCompleteUnlessOpen` | Write-while-locked; read needs unlock |
| C | `NSFileProtectionCompleteUntilFirstUserAuthentication` | After first unlock until reboot (**default**) |
| D | `NSFileProtectionNone` | Always (UID-wrapped only) → the only class readable BFU |

## Lock-state reachability cheat-sheet

| State | Class C data | Typical method | Urgency |
|-------|--------------|----------------|---------|
| AFU | Decryptable | FFS / agent / backup | **High** — melting ice cube; don't reboot |
| BFU | Sealed | Class D only / await passcode | Hold + isolate |

## Key iOS artifacts (paths under the data volume)

| Artifact | Path (typical) | Yields |
|----------|----------------|--------|
| Messages | `private/var/mobile/Library/SMS/sms.db` | SMS/iMessage, attachments |
| Call history | `.../Library/CallHistoryDB/CallHistory.storedata` | Calls, FaceTime |
| Contacts | `.../Library/AddressBook/AddressBook.sqlitedb` | Contacts |
| App/device usage | `.../Library/CoreDuet/Knowledge/knowledgeC.db` | Pattern-of-life, lock/unlock |
| Power/battery | `.../powerlog/.../CurrentPowerlog.PLSQL` | Charge, screen-on, events |
| Photos | `.../Media/PhotoData/Photos.sqlite` | Asset metadata, EXIF, faces |
| Safari | `.../Library/Safari/History.db` | Browsing history |
| Health | `.../Library/Health/healthdb_secure.sqlite` | Health metrics (encrypted backup/FFS) |
| Keychain | `keychain-2.db` | Credentials/tokens (per-class) |

Always collect the sidecar `-wal` and `-shm` (and any `-journal`) for every SQLite DB.

## SQLite carving targets

- **WAL (`-wal`)** — recent and pre-checkpoint rows, including some deleted.
- **Freelist pages** — pages released by deletes; rows often intact until reused.
- **Unallocated / slack** — remnants after `VACUUM` may still hold fragments.
- **`-journal`** — rollback journal for the older journaling mode.

## iOS timestamp epochs (convert to UTC; record which)

| Epoch | Reference date | Seen in |
|-------|----------------|---------|
| Unix | 1970-01-01 | Many UNIX-derived fields |
| Mac absolute / Core Data | 2001-01-01 | `KnowledgeC`, `sms.db` `date` (×10⁹ ns on newer iOS), Cocoa |
| Mach continuous | boot-relative | `powerlog` deltas |

## Open / commercial tooling

| Tool | Type | Use |
|------|------|-----|
| `libimobiledevice` | Open | Device info, logical backup (`idevicebackup2`) |
| `checkra1n` / `palera1n` | Open | checkm8 acquisition (A5–A11) |
| iLEAPP | Open | Artifact parsing/reporting |
| Cellebrite UFED/Premium | Commercial | Logical/FFS/agent, unlock |
| Magnet GrayKey / AXIOM | Commercial | Unlock + FFS + analysis |
| ELCOMSOFT iOS Forensic Toolkit | Commercial | checkm8 + agent acquisition |

## Upstream catalogues and standards

- **Apple Platform Security Guide** — https://support.apple.com/guide/security/welcome/web — Data Protection, SEP, keybags.
- **NIST SP 800-101r1** — https://csrc.nist.gov/pubs/sp/800/101/r1/final — mobile forensics method + validation.
- **SWGDE** — https://www.swgde.org/ — best-practice docs for mobile/SQLite forensics.
- **iLEAPP artifact list** — https://github.com/abrignoni/iLEAPP — current parseable iOS artifacts.
- **Heuer, ACH (CIA CSI)** — https://www.cia.gov/resources/csi/books-monographs/psychology-of-intelligence-analysis-2/ — the hypothesis-testing method.
