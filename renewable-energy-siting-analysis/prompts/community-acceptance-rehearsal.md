# Community-Acceptance Rehearsal

## Purpose

Renewable siting fails on community acceptance more often than on resource or grid. This prompt rehearses the project's most-likely host-community objections through the same choreography lens the rest of the workspace uses — naming, for each objection, *which* joint's articulation the objection threatens and how the project's response can be staged. It is a rehearsal in the puppetry sense: every cue is walked before opening night so the actual public comment period contains no surprise stumbles.

## Prompt Template

```
You are a renewable-energy siting analyst working in the renewable-energy-siting-analysis
workspace. The user is preparing for the public comment / community open-house period for
project [project_id]. Walk through a community-acceptance rehearsal.

Project: [project_id]
Geography: [host_county / township / region]
Asset summary: [joints from the articulation graph]
Known stakeholder groups: [e.g. township board, neighbouring landowners, tribal nation,
fisheries co-op, eagle preservation groups]
Public comment milestones: [dates / process — NEPA scoping, draft EIS comment, township
zoning hearing, etc.]

For each likely objection class below, walk through what the workspace's analysis can / cannot
say in response. Use the articulation vocabulary so the response naturally maps back to a joint,
a linkage, or a drive.

1. **Visual / shadow flicker** — name the joints implicated (which turbines / arrays cause it),
   the modeling that exists, and the mitigation drives (curtailment by hour-of-day, ADLS,
   setback adjustment).
2. **Noise / low-frequency / infrasound** — same form.
3. **Avian / bat / pollinator** — which centerlines fall in flyway / hibernaculum / pollinator
   corridor data, which joints would need monitoring or curtailment drives, what permits apply.
4. **Property value** — what comparable-study data is publicly available, what the project's
   community-benefit drive (host-community fund, decommissioning bond) looks like.
5. **Decommissioning / EOL** — financial assurance posture per joint, per state statute.
6. **Tax base** — PILOT vs property tax math; cite the host-county's current per-acre yield.
7. **Glare / agricultural co-use** — agrivoltaic options, glare modeling per FAA Tech Note 22.
8. **Cultural / tribal** — Section 106 consultation status, traditional cultural property
   identification, any tribal nation comment letters already received.

For each objection, the rehearsal output should be structured as:

  ### Objection: <name>
  - **Articulation cue** — which joint(s) / linkage(s) / drive(s) the objection actually
    targets. (This is what makes the response disciplined; vague "the project" responses are
    where stumbles happen.)
  - **What the workspace can substantiate** — analyses already in `outputs/` that bear on
    this objection.
  - **What the workspace cannot substantiate** — gaps the project should fill before the
    comment hearing.
  - **Proposed mitigation / drive** — the binding lever the project can offer (curtailment
    schedule, setback, community fund, monitoring commitment).
  - **Failure mode** — the response that would *worsen* community acceptance (e.g. invoking
    state-preemption statute as the first response on a contested setback).

End with a portfolio-level "rehearsal-day" summary: across all objections, which joints carry
the most community-acceptance risk, and which drives the project should be ready to commit at
the hearing.

Save to `outputs/<project_id>/community-rehearsal-<YYYYMMDD>.md`.
```

## Expected Output

A markdown rehearsal document at `outputs/<project_id>/community-rehearsal-<YYYYMMDD>.md` that the development team can use as the brief for the actual public hearing. The document's discipline is the value: every response ties back to a joint, a linkage, or a drive, so the project speaks with one voice and the community hears a structured response rather than improvisation.
