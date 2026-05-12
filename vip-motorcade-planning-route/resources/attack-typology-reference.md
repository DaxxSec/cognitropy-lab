# Attack Typology Reference — Defensive Indicators and Mitigations

A defensive reference for the attack types this workspace scores against. Each entry is structured: what it is (briefly), what indicators the advance and counter-surveillance teams watch for, and what mitigation primarily moves which axis of the matrix.

> This document is *defensive*. Indicators are listed so they can be detected and reported, not so attacks can be planned. The agent refuses any request that re-frames this content as an offensive guide.

## Complex Ambush

**Brief:** Coordinated kinetic attack involving multiple elements (initiator, support, blocking, escape disruption). Often combines an IED initiator with small-arms support.

**Defensive indicators:**
- Pre-attack surveillance — vehicles or individuals lingering at known motorcade routes, repeated observations across days.
- Pre-positioned vehicles (parked but with running engines, late-model, drivers present).
- Communications discipline anomalies on host-nation channels (silence on a frequency normally chatty).
- Local population behavior change (shopkeepers closing early, normally crowded street empty).
- Block vehicles staged at chokepoints.

**Mitigation primary:** Route variation (L↓), advance sweep within 30 min (L↓), CAT vehicle (I↓), hardened principal vehicle (I↓).

## Single-Shot Sniper / Long-Range Precision

**Brief:** Single, planned shot at a predictable point — usually venue arrival/departure or a known dwell.

**Defensive indicators:**
- Standoff line-of-sight to predictable points; rooftops or upper-floor windows with a view of a known curb.
- Unusual access requests at buildings overlooking arrival points.
- Vehicle parked with line-of-sight to dwell point, occupant not exiting.

**Mitigation primary:** Block sightlines (I↓), shorten dwell time (L↓), vary stops (L↓), move arrival to less-exposed entrance (L↓).

## VBIED / Roadside IED

**Brief:** Vehicle-borne or roadside emplaced explosive, detonated at a fixed point on a route the attacker expects the motorcade to take.

**Defensive indicators:**
- Vehicle parked unusually close to a likely motorcade chokepoint; sagging suspension; tinted windows, occupant remaining.
- Trash bag, crate, abandoned moped on a chokepoint where it wasn't yesterday.
- Disturbed pavement, fresh roadwork in a stretch where work wasn't scheduled.
- Cell-tower outages near a chokepoint at the planned movement time.

**Mitigation primary:** Route variation (L↓), advance sweep within 30 min (L↓), standoff (I↓), route closure (L↓).

## Crowd Surge / Crush

**Brief:** Public motorcade encounters dense crowd; vehicles trapped or principal exposed to crush forces.

**Defensive indicators:**
- Crowd density estimate from advance — > 4 persons/m² is a hard danger threshold.
- Bottleneck geometry between motorcade route and crowd flow.
- Public events, political rallies, sports concentrations on or near the route.

**Mitigation primary:** Crowd line (L↓ + I↓), alternate ingress (L↓), reduce dwell at venue (L↓), push-through plan (I↓).

## Vehicle Ramming

**Brief:** Heavy vehicle drives into the motorcade or the principal's path at a slow chokepoint.

**Defensive indicators:**
- Heavy vehicle (truck, SUV) idling near a chokepoint, occupant present.
- Physical absence of hostile-vehicle mitigation infrastructure (bollards, barriers) where one would expect it.

**Mitigation primary:** Route closure / police escort (L↓), HVM infrastructure at venue (L↓ + I↓), motorcade speed maintained through chokepoint (I↓).

## Lone-Actor (Edged or Firearm)

**Brief:** Close-range opportunist attack at venue arrival/departure or dwell point.

**Defensive indicators:**
- Pre-attack surveillance by a single individual; same individual observed at multiple movements.
- Concealed-carry indicators (printing, asymmetric posture, hand drift).
- Threat communications received by principal, especially identifying motorcade or schedule details.

**Mitigation primary:** Arrival hardening (L↓ + I↓), curb scanning by detail (L↓), decoy timing (L↓).

## Kidnap-for-Ransom

**Brief:** Forced motorcade stop and principal extraction; common in specific regions (parts of Latin America, West Africa, parts of South Asia).

**Defensive indicators:**
- Surveillance against pattern-of-life (residence, frequent venues, school drop-off).
- Local kidnap rates trending in the AOR.
- Probing — fake police checkpoints, road-rage incidents, faked accidents.

**Mitigation primary:** Hardened motorcade (I↓), CAT (I↓), counter-surveillance running (L↓), unpredictable scheduling (L↓), local QRF arrangements (I↓).

## Spoofed Comms / Fake Checkpoint

**Brief:** Adversary impersonates host-nation police, military, or emergency response to force a motorcade stop or divert it onto a chosen route.

**Defensive indicators:**
- Checkpoint not in liaison-confirmed list; uniforms with composition errors; vehicles without expected callsigns.
- Communication on an unexpected frequency claiming to be a known liaison; cannot verify on the channel they originally used.
- Pressure to take a specific alternate route from an unverified source.

**Mitigation primary:** Verification protocol via known callback number (L↓), refuse-to-stop authority (L↓), host-nation liaison pre-coordination (L↓).

## Cyber-Physical Disruption

**Brief:** GPS spoofing, cellular jamming, or vehicle-OBC attack disrupts motorcade navigation or comms.

**Defensive indicators:**
- Sudden GPS displacement or "teleport" of detail's tracking systems.
- Cellular network outage in a localized area at a sensitive time.
- ECU / OBC anomalies on motorcade vehicles after an unattended period.

**Mitigation primary:** Map-and-compass fallback (L↓), comms diversity (sat + cell + radio) (L↓), vehicle-access discipline pre-movement (L↓).
