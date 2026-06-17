# Geospatial Incident Narrative

## Purpose

Use for multi-host incidents to produce a spatial narrative — host clustering, lateral diffusion, identity geovelocity, and C2 supply lines — with accuracy caveats made explicit. The costume-history move: map the style across regions and trace the trade routes.

## Prompt Template

```
You are producing the geospatial annex for an incident. Map the spread in space and flag the accuracy of every geo claim.

- **Affected hosts:** [HOST → SITE / SUBNET / BUSINESS UNIT]
- **Auth events:** [IDENTITY, SOURCE IP, TIMESTAMP for VPN/RDP/cloud sign-ins]
- **C2 destinations:** [IPs / DOMAINS]
- **Geo sources available:** [MAXMIND / IPINFO / WHOIS / PASSIVE DNS]

Please:
1. Cluster affected hosts on the org topology and name the candidate patient-zero.
2. Time-order lateral movement as a diffusion frontier from patient-zero.
3. Run geovelocity on the auth events; flag any > ~900 km/h between successive logons per identity.
4. Resolve C2 to geo + ASN + provider as a supply-line map, tagging each with resolution and source.
```

## Expected Output

- Host-cluster map with patient-zero and a time-ordered diffusion sequence.
- A geovelocity exceptions table (impossible-travel events).
- A C2 supply-line map (IP · geo · ASN · provider · resolution/source) with a "geolocation is a lead, not a verdict" caveat.
