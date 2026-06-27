# Mobile Forensics — iOS Extraction — Core Concepts

Background the agent reads before acting. Optimised for fast recall during an examination, not exhaustive theory. Pair this with `references.md` (lookup tables) and `workflows.md` (procedures).

## The governing variables

Before any tool runs, four facts decide what is technically achievable on an iOS device. Establish all four first.

1. **SoC generation** — the System-on-Chip (A-series). It determines whether the `checkm8` BootROM exploit applies (A5–A11, i.e. iPhone 4S → iPhone 8/X) and which Secure Enclave (SEP) generation guards the keys. A12 and later (iPhone XS onward) closed the BootROM hole; acquisition there depends on agent-based tooling and software vulnerabilities, not a permanent hardware exploit.
2. **iOS version** — gates the software exploit chain a commercial tool can use, and changes artifact schemas (e.g. `KnowledgeC`, biome).
3. **Lock state at seizure (BFU vs AFU)** — see below. The single most consequential perishable fact.
4. **Passcode condition** — known / unknown / no passcode. Without the passcode (or a brute-force capability), keys in classes that require user authentication stay sealed.

## iOS Data Protection

iOS encrypts user data file-by-file. Each file's class key is wrapped in a way that controls *when* it is available. The hardware AES engine and the device **UID key** (fused into the SoC, never exported) entangle file keys with the user passcode, which is why a passcode is required to derive most class keys.

| Class | Name | Key available… |
|-------|------|----------------|
| A | `NSFileProtectionComplete` | Only while device is unlocked |
| B | `NSFileProtectionCompleteUnlessOpen` | Can write while locked (asymmetric); read needs unlock |
| C | `NSFileProtectionCompleteUntilFirstUserAuthentication` | After the first unlock since boot — **the default for most app data** |
| D | `NSFileProtectionNone` | Always (key wrapped only by UID, not passcode) |

The **Secure Enclave (SEP)** holds the cryptographic operations and enforces passcode-attempt escalation (delays after wrong guesses) and, on Touch ID/Face ID devices, biometric matching. **Effaceable Storage** holds keys that can be wiped instantly to render the device cryptographically unrecoverable ("Erase All Content and Settings" is effectively an Effaceable-Storage wipe).

## BFU vs AFU — the decisive distinction

- **BFU (Before First Unlock):** the device has been powered on but not unlocked since boot. Class C keys (most user data) are **not** derived. You can read only Class D (`None`) data — very little of evidentiary value. Most app databases, Messages, Mail, and Photos are inaccessible.
- **AFU (After First Unlock):** the user has unlocked at least once since boot. Class C keys are now resident in memory and **stay available until reboot or shutdown**, even when the screen relocks. The overwhelming majority of user data is decryptable in AFU.

**Operational consequence:** an AFU device is a melting ice cube. A reboot, a battery death, or a `>` 1-hour idle (USB Restricted Mode aside) can drop it to BFU. Keep it powered, isolated, and do not reboot. `/assess-lock-state` and `/isolate-evidence` exist to capture and hold this state.

**USB Restricted Mode:** after ~1 hour locked, iOS disables data over the Lightning/USB-C port until the next unlock, blocking many wired acquisition paths. Established pairing/lockdown records can bypass it within a window — capture them early.

## Extraction method taxonomy

Ordered roughly least → most invasive and least → most complete:

- **Logical (backup-based):** a normal iTunes/Finder backup over `idevicebackup2` or AFC. Gets what a backup gets (Messages, contacts, call history, some app data, photos) but misses sandboxed app data and system databases not included in backups. An **encrypted backup** (set a backup password) actually returns *more* — it includes Keychain items, Health, and call history that an unencrypted backup omits.
- **File system / Full File System (FFS):** a copy of the live (decrypted, in AFU) file system, including app sandboxes, `KnowledgeC`, biome, and many databases backups never see. Requires an agent or exploit and an AFU device.
- **Agent-based:** a signed forensic agent is installed (developer/enterprise cert or exploit) to perform an FFS extraction and, where possible, a keychain dump. The mainstream method for A12+ AFU devices via commercial tools.
- **checkm8 / BootROM:** for A5–A11, a permanent unpatchable BootROM exploit (`checkra1n`/`palera1n`) enables a low-level acquisition. Still cannot defeat passcode-derived keys on a BFU device without brute force, but on AFU (or with a known/brute-forced passcode) it yields a full physical-equivalent image.
- **Physical (legacy):** raw NAND imaging — largely obsolete on modern encrypted devices because the result is ciphertext without the class keys.

## Keychain and keybags

The **keychain** (`keychain-2.db`) stores credentials, tokens, and certificates, each tagged with its own protection class. A **keybag** holds the wrapped class keys: the *system keybag* (device), the *backup keybag* (for encrypted backups, with its own `BackupKeyBag` and password-derived key), and the *escrow keybag* (lets a paired host unlock without the passcode — the basis of lockdown-record bypass). Completeness of an extraction is judged against the keybag: which classes were unwrapped and which stayed sealed.

## The iOS artifact map (where evidence lives)

- **Messages:** `sms.db` (SMS/iMessage), with `message`, `chat`, `attachment` tables; heavy WAL usage.
- **Call history:** `CallHistory.storedata`.
- **Contacts:** `AddressBook.sqlitedb`.
- **Pattern-of-life:** `KnowledgeC.db` (app usage, device lock/unlock, focus, now-playing) and the newer **biome** streams; `powerlog` / `CurrentPowerlog.PLSQL` (charge, battery, screen-on).
- **Photos & media:** `Photos.sqlite` (asset metadata, EXIF, faces, moments).
- **Browsing:** Safari `History.db`, `Bookmarks.db`; `Cache.db` for many apps.
- **Health & location:** `healthdb_secure.sqlite`; location historically `cache_encryptedB.db` / routined `Cache.sqlite`.
- **Accounts & wallet:** `Accounts3.sqlite`, Apple Wallet/passes.

Most of these are SQLite, which means **WAL (Write-Ahead Log)**, `-shm`, and rollback journals must be collected and considered — deleted/edited rows frequently survive there and in freelist pages.

## Analysis of Competing Hypotheses (ACH)

Heuer's ACH is the reasoning backbone for this workspace:

1. **Enumerate** a mutually-exclusive, collectively-exhaustive set of hypotheses *before* deep-diving the data.
2. **List evidence/arguments** — every artifact, plus assumptions and absences.
3. **Build the matrix** — for each (evidence, hypothesis) cell mark Consistent / Inconsistent / Not-applicable. The crucial scoring is *diagnosticity*: evidence consistent with *every* hypothesis has near-zero value; evidence that is **inconsistent** with some hypotheses is what moves the needle.
4. **Refute, don't confirm** — rank hypotheses by the *weight of inconsistent evidence* against them. The surviving hypothesis is the least disconfirmed, not the most "supported."
5. **Sensitivity analysis** — identify the few items of evidence that drive the conclusion; if any is wrong (misdated, tool artifact, planted), does the conclusion flip? Note the dependencies.
6. **Report** with confidence and the explicit alternatives that were ruled out and why.

## Common Failure Modes

- **Rebooting an AFU device** — drops to BFU and forfeits Class C data. The most expensive mistake in iOS forensics.
- **Confirmation bias** — collecting only artifacts that support the lead hypothesis; ACH and the diagnosticity matrix exist to counter this.
- **Ignoring the WAL** — analysing `sms.db` without its `-wal`/`-shm` files misses recent and deleted records still pending checkpoint.
- **Timezone/epoch errors** — iOS mixes Unix, Mac absolute time (epoch 2001-01-01), and Core Data timestamps; misconverting them produces fabricated timelines.
- **Method/state mismatch** — attempting FFS on a BFU device, or an unencrypted backup when an encrypted one would yield Keychain + Health.
- **Tool monoculture** — trusting one parser's interpretation of an artifact without cross-validation.

## Operating Constraints

- **Authority before acquisition.** Warrant, consent, or ownership — documented — is non-negotiable; legality of compelled passcodes is jurisdiction-specific.
- **Perishable state.** Lock state, pairing records, and USB Restricted Mode windows degrade with time; isolation and capture are urgent.
- **Reproducibility.** Every step pins tool + version, device UDID hash, timestamps, and image hashes; critical findings are cross-validated with a second tool or method.
