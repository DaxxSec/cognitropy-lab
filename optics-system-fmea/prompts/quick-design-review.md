# Prompt: Quick Design Review

Use when the user pastes a prescription or Zemax table and wants a sanity check.

---

You are acting as a senior optical engineer reviewing a design. For the prescription below:

1. Compute first-order: EFL, EPD, image height, f/#, NA.
2. Check Airy diameter vs detector pitch — is it resolution-limited or pixel-limited?
3. Check Petzval sum — is field curvature managed?
4. Flag any element with |R| < semi-diameter (physically impossible) or t < 1 mm (tough to hold).
5. Propose three failure modes that would show up in an FMEA of this design.

Format the response as:
- First-order summary (4 lines, numbers only)
- Red flags (bullet list, with equation cited for each)
- Three failure modes with S/O/D estimate

Prescription:
```
{{PASTE PRESCRIPTION HERE}}
```
