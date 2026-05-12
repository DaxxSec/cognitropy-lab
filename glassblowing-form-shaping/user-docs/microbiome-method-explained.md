# Why a Glass Studio Borrows From Soil-Microbiome Research

Most studio notebooks are running diaries: "Tuesday, made the green vases, the second one had a weird crack at the lip." This is a perfectly reasonable way to remember yesterday. It is a terrible way to answer the question "what changed in the last six weeks that explains the cluster of post-anneal cracks I'm seeing now?"

Soil microbiome researchers ran into the same problem on a different scale. A plot's microbial community shifts over months in response to upstream interventions: the seed lot, the inoculant, the amendments, the rainfall, the temperature swing during a critical week. By the time the researcher notices that yields are off, the cause is buried under months of poorly recorded variables. The discipline that emerged — strict per-plot batch records with explicit lineage, environmental envelopes, intervention sequences, and successional follow-ups — exists because anything looser proved unrecoverable.

This workspace borrows that discipline.

## The Five Slots

Every batch record has five slots, each one earning its place by being indexable later:

### 1. Lineage (the upstream inputs)
Soil version: seed lot, inoculant strain, amendment source. Glass version: cullet melt batch ID, every color rod lot with supplier and lot number, any leftover stock from a prior session with its originating batch ID. The lineage is the chain of upstream causes you will walk back through six months later.

### 2. Environmental Envelope (the conditions)
Soil version: air temperature, soil moisture, soil pH at sampling. Glass version: studio ambient temperature and humidity, glory hole soak temperature, lehr starting temperature. These are the variables that the form simulation reasons against and that explain "weird session" outcomes after the fact.

### 3. Intervention Sequence (what was done, in order)
Soil version: tilling, watering, amending — date, quantity, location. Glass version: gathers, marvering, jacks, blocks, optic mold use, transfer, lehr load — time-stamped. Order matters because thermal history matters; a cold check that initiated at gather 2 didn't propagate until block-3.

### 4. Outcome (the immediate result)
Soil version: yield, biomass, taxonomic assay. Glass version: pieces produced, mass, geometry, finished/abandoned state, lehr position. The deliverable of the session.

### 5. Successional Follow-Up (the deferred truth)
Soil version: 7-day, 30-day, 90-day plot revisits. Glass version: 24-hour post-anneal inspection, 7-day shelf check, 30-day crack survey, 90-day shelf check. Modes 4 (residual strain) and 5 (COE mismatch) only show up on follow-up. Without scheduled revisits, you will discover them weeks later as inexplicable losses with no traceable cause.

## What This Buys You

### Queryability
Six months of strict batch records is a queryable database. `grep` finds every batch that touched a specific color rod lot. A `wc -l` of `outputs/post-mortems/` tells you how many failures you've actually had. A walk through `work-log/INDEX.md` filtered to one form name shows you the consistency curve.

A six-month notebook is a stack of pages. You can flip through it, but you cannot ask it questions.

### Causal Inference Instead of Vibes
When three pieces crack the same way in the same week, the loose-records artist asks "what was different?" and gets an answer made of impressions. The strict-records artist asks the same question of the records and gets a list of upstream variables that those three pieces shared and the comparison group did not. The list is short enough to act on.

### Apprentice Onboarding
A new studio assistant who reads the last quarter's batch records, post-mortems, and the failure-mode taxonomy will absorb in a week what would otherwise take six months of "watch and learn." The records make tacit knowledge legible.

### Reproducibility
You made something good in March. The strict record contains the exact parameters: gather count, color rod lots, lehr program, even the studio ambient that day. You can reproduce the conditions, not approximate them. For a studio that sells production lines, this is the difference between "we make something like that" and "we make exactly that."

## What This Costs You

About 5–10 minutes per session in active logging time. Some up-front friction learning the schema. A small ongoing cost in maintaining the lineage discipline (every new rod lot must be entered with full traceability; that's 30 seconds of inventory work).

For most artists who try the workspace for a month, the cost crosses break-even on the first surprise — the first time a `/lineage-trace` answers a question they couldn't have answered any other way. After that, it becomes infrastructure, like keeping the glory hole at temperature.

## The Honest Limit

This workspace cannot make you a better gaffer at the bench. The form-sim will catch knowable failures, but it will not teach you to feel a gather's heat in your hands. The taxonomy will help you diagnose, but it cannot supervise a beginner. The records will help you reason, but they cannot reason for you.

What the workspace does is convert the slow, tacit accumulation of "ten years of studio experience" into something that can be examined, queried, and shared. That is a smaller claim than "this will make your work better." But it is, over months and years, the discipline that compounds.
