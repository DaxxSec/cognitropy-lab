# /geo-spread-map — Geographic & Spatial Analysis of the Spread

Map the spatial structure of the incident — host geography, lateral diffusion, identity geovelocity, and C2 supply lines — the way a costume historian maps regional dress and the trade routes that moved dyes and patterns between regions. (Today's technique.)

## Inputs

- Affected-host list with site/subnet/business-unit placement.
- Authentication events with source IPs (VPN, RDP, cloud sign-in) over the incident window.
- C2 destination IPs/domains; optional GeoIP/ASN/WHOIS/passive-DNS access.

## Steps

1. **Host layer**: plot affected endpoints on the org's spatial topology (sites, subnets, BUs); identify the spatial cluster and the candidate patient-zero.
2. **Diffusion layer**: model lateral movement as a spread/graph process; time-order the diffusion frontier from patient-zero outward.
3. **Identity layer**: run geovelocity / impossible-travel on the auth events (flag > ~900 km/h between successive logons for one identity — T1078 abuse).
4. **Infrastructure layer**: resolve C2 to geolocation + ASN + RIR + hosting provider; draw the "supply line" and note infrastructure reuse.
5. **Annotate accuracy**: tag every geo claim with its **resolution and source**; mark city-level GeoIP as low-confidence.

## Output

`outputs/geo-spread-<incident>-<date>.md`: a four-layer geospatial annex — host cluster map, diffusion sequence with patient-zero, geovelocity exceptions table, and C2 supply-line map (IP · geo · ASN · provider · resolution/source).

## Notes

- C2 is rented infrastructure: geolocation is a lead toward the supply line, never a verdict on actor nationality.
- The diffusion sequence and patient-zero feed `/reconstruct-timeline` and `/campaign-typology`.
