# Prompt — Indicator Elicitation from Supervisor / Source Interview

> A reusable interview-prompt scaffold for eliciting behavioral indicators from a supervisor, peer, or other human source. Use the prompt as a foundation; phrase it conversationally for the actual interview.

## When to Use
- Indicator checklist has gaps that only human sources can fill
- A supervisor referral is the originating predicate
- Periodic reinvestigation requires fresh peer/supervisor input
- Walk-in source vetting (where the questions are inverted toward the source)

## Pre-Interview Setup
- Confirm authority for the interview
- Confirm the interviewee has been read in to the appropriate level of inquiry
- Note any restrictions on what may be discussed (classified compartments, ongoing legal matters)
- Plan to record only with consent and per applicable policy
- Have the indicator taxonomy at hand for taxonomy-aligned probing

## Opening Frame (read or paraphrase)
*"I'm conducting [authorized inquiry / periodic review] regarding [Subject ref]. I'd like to ask about your observations of their work, behavior, and any changes you've noticed. Anything you tell me may be incorporated into an analytic product. The product will be used by [recipient]. Your name and identifying details will be protected per source-protection conventions. There is no expectation that any one observation is significant — I'm gathering many pieces. Are you willing to proceed?"*

## Domain-Aligned Question Set

### Financial Domain Cues
- Have you noticed any unexplained changes in [Subject]'s financial situation? Significant new purchases, signs of financial distress, mentions of money worries?
- Have you observed any unusual cash patterns at work?
- Has [Subject] mentioned debts, gambling, family financial issues, or addiction?
- Have you observed any changes in lifestyle that you couldn't square with their compensation?

### Foreign Contacts Domain Cues
- To your knowledge, does [Subject] have personal or professional relationships with non-US persons that you've observed?
- Has [Subject] discussed travel? What destinations? What's their stated purpose?
- Have you observed any contact patterns that struck you as unusual — unfamiliar names, unexpected channels, secrecy around communications?
- Do you know of family or close associates of [Subject] in foreign countries?

### Lifestyle Domain Cues
- Has [Subject]'s behavior at work changed in any noticeable way over the past [period]?
- Have you observed signs of personal stress — marital, family, legal, health, addiction?
- Have they made new social associations or dropped longstanding ones?
- Has their work pattern, hours, or energy noticeably shifted?

### Ideological Domain Cues
- Has [Subject] expressed strong views about the organization's mission, the country, or particular foreign matters?
- Have they made statements you'd characterize as durably hostile to the organization?
- Have you observed any expression of alignment with any external cause that gives you concern?
- (Calibrate carefully: ordinary political opinion is not an indicator. Probe for documentable, durable hostility expressed in actionable form.)

### Technical / Access Domain Cues
- Have you observed [Subject] accessing information or systems that didn't seem to fit their role?
- Have you noticed unusual hours, unusual download patterns, USB or device anomalies?
- Have you observed [Subject] probing security controls or asking questions about systems beyond their need?
- Are there any access incidents in the system audit logs you'd flag?

## Closing Frame
- *"Is there anything else — even small or seemingly trivial — that you've noticed that I haven't asked about?"*
- *"Do you think there's a benign explanation for any of the things you mentioned that I should consider?"* (Force the interviewee to articulate the null hypothesis.)
- *"Is there anyone else you'd recommend I speak with for additional perspective?"*

## Post-Interview Capture
For each volunteered observation, record:
- Domain (or note "uncategorized" if it does not fit the taxonomy)
- Observation in interviewee's words (quoted where possible)
- Interviewee's interpretation (separately from observation)
- Interviewee's named alternative (benign) explanation, if offered
- Reliability rating of the source (Admiralty Code A–F)
- Date of observation as recalled
- Date of interview

Append to `outputs/<date>-indicator-checklist.md` under the appropriate domain. Mark each as **Possible indicator (uncorroborated)** until corroboration from a second source is obtained.

## Cautions
- Do not lead the interviewee. Open questions before specific ones.
- Do not paraphrase observations into a frame of guilt; record what was said.
- Reactions, body language, and demeanor of the interviewee are not the subject of analysis here.
- The interviewee's relationship to the subject is itself relevant context (peer with grievance? rival? trusted associate?). Document it.
- Whistleblower-protected disclosures by the interviewee about [Subject] are not adverse indicators and must not be used as such.
