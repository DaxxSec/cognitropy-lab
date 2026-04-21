# Prompt: RPN Scoring Walkthrough

Use when the user needs help translating a failure mode into S, O, D numbers.

---

I will ask you five questions per failure mode to assign S, O, D:

**Severity**
- Q1: If this mode occurs in the field, what is the consequence? (safety / full loss / degraded / cosmetic)

**Occurrence**
- Q2: What is the estimated failure rate per unit or per year?
- Q3: Have we seen this mode in prior designs?

**Detection**
- Q4: Is there an inspection, test, or sensor that catches this BEFORE shipment?
- Q5: If it escapes, will the customer detect it immediately?

Map answers to 1–10 using `resources/rpn-rubric.md`. Then compute RPN and flag any S=10.

Walk the user through **one mode at a time.** Do not batch.
