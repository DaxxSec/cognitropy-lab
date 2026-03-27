# /gear-check — Pre-Deployment Equipment & PPE Inspection

Run a pre-deployment checklist for all equipment and safety gear before heading to the field.

## Procedure

1. Ask the user for deployment details:
   - What type of sampling? (boat-based, shore-based, wading, through-ice)
   - What parameters are being measured? (determines instrument list)
   - Water body type and known conditions
   - Number of personnel

2. Generate a tailored checklist organized by category:

### Safety Equipment (ALWAYS required)
- [ ] PFDs — one per person, properly sized, in good condition
- [ ] Throw bag / rescue rope (20m minimum)
- [ ] First aid kit — waterproof, stocked, within expiration dates
- [ ] Emergency whistle (one per person)
- [ ] Communication device — VHF radio / cell phone (in dry bag)
- [ ] Sun protection — SPF 50+, wide-brim hats, UV sunglasses
- [ ] Drinking water — minimum 1L per person per 4 hours
- [ ] Emergency contact card — laminated, in field kit

### Conditional Safety Equipment
- [ ] Cold water: Immersion suit / dry suit, hot beverages, extra dry clothing
- [ ] Ice operations: Ice picks, cleats, rescue board, ice auger for thickness checks
- [ ] HAB conditions: Nitrile gloves, respiratory protection (N95 minimum), eye protection
- [ ] Remote site: PLB (personal locator beacon), satellite communicator
- [ ] Night operations: Navigation lights, headlamps, reflective gear

### Sampling Instruments
- [ ] Multi-parameter sonde — charged, cleaned, calibrated today
- [ ] Calibration standards — pH buffers, conductivity standard, turbidity standards
- [ ] Calibration log — pre-field readings recorded
- [ ] Sample bottles — correct type for each analyte, labeled, sufficient quantity
- [ ] Cooler with ice packs — for sample preservation
- [ ] Secchi disk — clean, line marked at 0.5m intervals
- [ ] Field notebook — waterproof, with pencil (not pen)

### Watercraft (if applicable)
- [ ] Hull integrity — no cracks, drain plug installed
- [ ] Motor — fuel level, starts reliably, kill switch functional
- [ ] Anchor and line — appropriate for depth
- [ ] Paddle/oars — backup propulsion
- [ ] Navigation lights (if applicable)
- [ ] Registration current, safety equipment per USCG/state requirements

### Documentation
- [ ] Sampling plan — printed copy in dry bag
- [ ] Site safety plan — printed copy accessible
- [ ] Chain of custody forms — sufficient quantity
- [ ] Map with station locations and GPS coordinates
- [ ] Emergency action plan with hospital route

3. Ask the user to confirm each category. Flag any missing items as **HOLD** — do not recommend deploying with safety equipment gaps.

4. Save completed checklist to `outputs/gear-check-[DATE].md`
