# Tools: Railway Signaling Systems Workspace

## Test and Measurement Equipment

### Track Circuit Testing
- **Multimeter (Fluke 87V or equivalent):** Voltage and resistance measurements across rails and circuit elements
- **Milliammeter:** Measuring track circuit feed current (critical — too high burns relay, too low fails to detect)
- **Track circuit analyzer:** Proprietary tools (Schweitzer, Network Rail approved) for frequency analysis on AC/JTC track circuits
- **Shunt resistance tool:** Calibrated resistor to simulate worst-case shunting conditions (typically 0.5 Ω across rails)

### Points Testing
- **Force/current gauge:** Measuring point machine drive force and motor current profile
- **Detection gauge:** Go/no-go gauge for checking switch blade detection clearances (typically 3mm go, 7mm no-go on NR)
- **Tracing voltmeter:** For verifying contact states in detection circuits under live conditions

### General Signaling Test Equipment
- **Safety barrier tester:** For verifying IS (intrinsically safe) barriers in potentially hazardous areas
- **Insulation resistance tester:** 500V/1000V Megger for cable insulation checks
- **Oscilloscope:** For waveform analysis on coded track circuits and SSI/CBI communication links

## Software Tools

### Simulation and Learning
- **NXSIM / NX Simulator:** Network Rail interlocking simulation environment — used in training centers
- **SIMATIC WinCC (Siemens):** SCADA-type visualization, used in some control rooms
- **Relay Logic Simulators:** Various proprietary trainers (some IRSE training centers have custom relay bench trainers)

### Documentation and Design
- **AutoCAD / MicroStation:** Used for signaling layout drawings (geographical plans, signal box diagram sheets)
- **SigPlan:** Network Rail standard for signaling design documentation
- **ReqIf / DOORS:** Requirements management for safety-critical ETCS projects
- **Enterprise Architect:** System modeling on larger ETCS/CBTC projects

### Standards Access
- **Network Rail Standards portal (SPARK):** Access requires Network Rail login — contains all NR/SP/SIG documents
- **BSI Knowledge:** Access to BS EN standards (IEC 62279, 62280, 62425 etc.)
- **ERA ETCS subsets:** Freely available at www.era.europa.eu (ETCS Baseline 3 specification documents)

## Documentation Standards

### Signaling Drawing Types (Network Rail)
- **Signalling Control Sheet (SCS):** The master layout drawing showing all signals, points, and track circuits in a geographical layout
- **Circuit Diagrams (Geographical):** Relay circuit logic laid out geographically matching physical equipment locations
- **Circuit Diagrams (Tabular):** Relay contact lists in tabular form — easier to read for complex route logic
- **Track Circuit/Point Machine Specification Sheets:** Data sheets for individual equipment settings
- **Maintenance Manuals (MM):** Equipment-specific procedures, approved test methods, fault-finding guides

### Fault Recording
All faults on NR infrastructure are recorded in the Fault Management System (FMS). A good fault report includes:
1. Exact location (ELR, mileage, signal/point reference)
2. Date and time fault found
3. Description of fault symptoms
4. Steps taken to diagnose
5. Root cause identified
6. Actions taken to repair
7. Test result after repair (signal tested, circuit measures taken)
8. Any recurrence risk or follow-up required

## Safety-Critical Working Practices

### Permit to Work System
- All work on live signaling equipment requires a Possession or Permit to Work
- Line blockages or possessions required for track work near running lines
- COSS (Controller of Site Safety) role is mandatory for lineside work

### Testing Isolation
- Before testing any live circuit, must confirm circuit and its interaction with adjacent circuits
- SSI/CBI systems: configuration management systems track which cards/modules are in service — always check before replacement
- Axle counter resets: minimum two-person operation, both authorized and competent

### Witness Testing
- All commissioning tests require an independent witness
- Witness must be independent of the design/installation team
- Results recorded in a signed-off Test Record (TR) document
