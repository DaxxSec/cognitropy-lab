# Domain Knowledge: Railway Signaling Systems

## Discipline Overview

Railway signaling controls the movement of trains on a shared network. It is a safety-critical engineering discipline where failures can cause loss of life. All design, installation, testing, and maintenance activities are governed by formal standards with mandatory safety integrity requirements.

**Key principle:** Fail-safe design. Every component defaults to the most restrictive state on failure. A track circuit failure shows the section as *occupied*. A signal power failure shows *red* (danger). This principle must never be violated.

---

## Signal Aspects and Indications

### UK Colour Light Aspects (4-aspect signaling)

| Aspect | Meaning | Driver action |
|--------|---------|---------------|
| Red (Stop) | Section ahead occupied or route not set | Stop before signal |
| Single Yellow | Caution — next signal may be at red | Prepare to stop at next |
| Double Yellow | Preliminary caution — next is single yellow | Reduce speed |
| Green | Line clear — proceed at permitted speed | Continue |

### Signal Features
- **Position light signals:** Used in some yards and depot areas (white lights in position patterns)
- **Route indicators:** Alphanumeric or theatre-type indicators showing which route is set
- **Banner repeaters:** Supplementary signals providing advance warning at limited-visibility locations
- **Ground signals (dolls/shunts):** Low signals for shunting movements within stations/yards

---

## Track Circuits

Track circuits are the primary train detection method on most main-line railways.

### DC Track Circuits
- Battery or rectified supply feeds current through one rail
- Return path via opposite rail
- Train wheels short-circuit the circuit, causing relay to drop
- **Failure mode:** If the feed or return wire breaks, the relay drops → section shows occupied (fail-safe)
- Sensitive to ballast contamination (reduced rail-to-rail resistance)

### AC Track Circuits
- Audio frequency (usually 83.3 Hz, 91.6 Hz, etc.) to avoid interference with DC traction return
- Used on electrified lines where DC traction currents would saturate DC track circuit transformers
- Coded AC (jointless track circuits) used in areas where rail joints are impractical

### Jointless Track Circuits (JTCs)
- No insulated joints between adjacent sections
- Tuned impedance bonds at section boundaries
- Different frequencies for adjacent sections prevent cross-talk
- Standard on modern main lines and high-speed routes

### Track Circuit Block (TCB)
- Automatic block working using track circuits instead of traditional block instruments
- Train entering section proves clear by track circuit occupation → signal automatically restores to red
- Reduces reliance on signaller operation for routine movements

---

## Axle Counters

### Principle of Operation
- Sensors mounted on rails count axle passages (wheel flanges displace magnetic field)
- Each section has an *in* counter and an *out* counter
- Section is clear when in-count equals out-count (net zero)
- Section is occupied when counts differ

### Advantages Over Track Circuits
- Not affected by leaf contamination or poor ballast resistance
- No insulated rail joints required
- Can monitor longer sections economically
- Better performance in extreme temperatures

### Critical Competency: Axle Counter Resets
Axle counters require a controlled reset procedure when a section count is disturbed (e.g., failed train, engineering possession). **Incorrect resets are a known safety hazard.** Resetting an axle counter while a train is still in the section removes the protection and can allow another train to be signalled into an occupied section.

Reset procedures are covered in NR/SP/SIG/11231 and require competency assessment before unsupervised work.

---

## Points and Switches

### Switch Operation
- Points (switches) divert trains from one route to another
- **Normal position:** Usually the main running line
- **Reverse position:** Diverted route (loop, branch, siding)
- Operated electrically by point machines (HW (Hydraulic-electric), MJ (motor), clamp lock, etc.)

### Detection
- Points must be *detected* (proven in position) before a signal can clear
- Detection circuits confirm the switch blade is within tolerance of the stock rail
- If detection is lost, the signal cannot be cleared (fail-safe)

### Facing Point Locks (FPL)
- Mechanical or electromechanical lock prevents point movement under a train
- Required for all facing movements on running lines
- Clamp-lock machines combine FPL and detection in a single unit

---

## Interlocking Systems

### Mechanical Interlockings
- Lever frame with physical mechanical connections
- Locking bed prevents conflicting lever combinations mechanically
- Still in use on heritage railways and some low-traffic rural lines
- Apprentices benefit from mechanical understanding before moving to electronic systems — the logic is identical

### Relay Interlockings (RI)
- Electromechanical relay logic implements interlocking conditions
- Vital relays: fail-safe components with forced-guided contacts
- Relay circuits implement route locking, approach locking, back locking, flank protection
- Dominant UK technology ~1950–1990; extensive legacy still in service
- Maintenance competency: reading relay circuit diagrams (geographical and tabular)

### Solid-State Interlockings (SSI)
- UK-developed microprocessor interlocking (British Rail Research / Westinghouse / GEC, 1985+)
- Central processor units (CPUs) with trackside functional modules (TFMs)
- Dual-redundant processing with cross-comparison
- Still extensively deployed on Network Rail

### Computer-Based Interlockings (CBI)
- Software-defined interlocking logic on COTS safety hardware
- Examples: Westinghouse IXL, Alstom Smartlock 400, Siemens Sicas ECC
- Route tables define permitted routes; interlocking engine evaluates conditions
- Requires IEC 62279 SIL 4 certification for vital functions

### Interlocking Logic Concepts

**Route locking:** Once a route is set and a train has entered it, the route cannot be cancelled until the train has cleared all occupied sections.

**Approach locking:** A route cannot be cancelled once a train has approached the signal — prevents the signal being put back to danger when a train is close and cannot stop.

**Back locking:** Points in a cleared route are locked once a train passes each point, maintaining protection through the route.

**Flank protection:** Adjacent signals and points set to protect against unauthorized movements into the flanks of a cleared route.

---

## Automatic Train Protection and Control

### AWS (Automatic Warning System)
- UK legacy magnetic system (1956+)
- Permanent magnet: horn sounds in cab (all-clear)
- Electromagnet (energized at clear signal): bell sounds (all-clear)
- Electromagnet (de-energized at caution/danger): horn — driver must press reset within ~3 seconds or emergency brake applies
- Does not prevent SPAD (Signal Passed At Danger) — driver can acknowledge and continue

### TPWS (Train Protection & Warning System)
- UK overlay to AWS, installed 2001–2003 following Ladbroke Grove
- Track loops fitted at all signals, speed traps on high-speed approaches
- If train overruns a trigger loop at excessive speed → emergency brake
- Provides protection against SPADs and overspeeding
- Does not provide full ATP (no continuous speed supervision)

### ETCS (European Train Control System)
ETCS is the European standard ATP/ATC system, part of ERTMS.

**ETCS Level 1:**
- Lineside signals retained
- Balises transmit static data to passing trains
- Train receives Movement Authority via balise at signal
- Cab display supplements lineside signals

**ETCS Level 2:**
- No lineside signals (or as backup only)
- Continuous communication via GSM-R radio between train and Radio Block Centre (RBC)
- RBC sends Movement Authorities in real-time based on interlocking state
- Train continuously supervised against speed profile

**ETCS Level 3 (Moving Block):**
- No fixed block sections
- Train position continuously reported; MA based on actual rear of preceding train
- Maximum theoretical capacity utilization
- Requires reliable, continuous train integrity reporting
- Not yet deployed at scale (as of 2026)

**ETCS Onboard Equipment:**
- European Vital Computer (EVC) — safety-critical processing unit
- Juridical Recording Unit (JRU) — black box equivalent
- Driver-Machine Interface (DMI) — cab display
- Balise Transmission Module (BTM) — reads Eurobalises
- GSM-R radio interface

---

## Level Crossings

Level crossings are the most complex single point of interface between the railway and the public. They have their own extensive standards (NR/GN/SIG/11292 etc.).

**Types (UK):**
- ABCL (Automatic Barrier Crossing, Locally monitored)
- MCB-OD (Manually Controlled Barriers, CCTV Obstacle Detection)
- AHB (Automatic Half Barrier)
- AOCL (Automatic Open Crossing, Locally monitored)
- UWC (User Worked Crossing)

**Signaling Interface:** Level crossing equipment is interlocked with signaling — barriers must be fully lowered before the associated signal can clear.

---

## Key Standards

| Standard | Scope |
|----------|-------|
| IEC 62279 / EN 50128 | Software for railway control systems |
| IEC 62280 / EN 50159 | Safety-related communication |
| IEC 62425 | Safety-related interlocking systems |
| EN 50121 | Electromagnetic compatibility (railway) |
| NR/SP/SIG/11231 | Network Rail axle counter principles |
| NR/SP/SIG/10971 | Signaling design |
| GM/RT2447 | TPWS requirements |
| ERA ETCS Subsets | ETCS functional/interface specifications |

---

## Historical Incidents (Learning Reference)

**Ladbroke Grove (Paddington), 1999:** Two trains collided after a driver passed a signal at danger. 31 fatalities. Revealed systematic issues with sighting of signal SN109, driver training gaps, and absence of ATP. Led directly to TPWS deployment.

**Potters Bar, 2002:** Points failure caused derailment of a passenger train. 7 fatalities. Highlighted risks of inadequate maintenance regimes and the importance of detection circuit integrity.

**Grayrigg, 2007:** Points defect caused high-speed derailment. 1 fatality, 88 injured. Points had a missing stretcher bar. Maintenance recording failures were a contributing factor.

**Quintinshill, 1915:** Worst UK railway disaster (226 fatalities). Signaller allowed passenger express to collide with stationary troop train. Fundamental block working failure combined with complacency.

Each incident demonstrates that signaling failures rarely occur in isolation — they involve combinations of equipment defects, procedural failures, training gaps, and organizational factors.
