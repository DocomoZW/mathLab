# QA Report — A1_Number / IGCSE O Level
## Status: FLAGGED
## Reviewed: 2026-06-05T14:00:00Z

## Artifacts Reviewed

### Concept Scripts (7)
- /opt/data/.hermes/content/curriculum/igcse_o/A1_Number/2026-06-04_A1_Q1_number-types.json
- /opt/data/.hermes/content/curriculum/igcse_o/A1_Number/2026-06-04_A1_Q2_factors-multiples-primes.json
- /opt/data/.hermes/content/curriculum/igcse_o/A1_Number/2026-06-04_A1_Q3_fractions-decimals.json
- /opt/data/.hermes/content/curriculum/igcse_o/A1_Number/2026-06-04_A1_Q4_percentages.json
- /opt/data/.hermes/content/curriculum/igcse_o/A1_Number/2026-06-04_A1_Q5_rounding-estimation.json
- /opt/data/.hermes/content/curriculum/igcse_o/A1_Number/2026-06-04_A1_Q6_ratios-proportion.json
- /opt/data/.hermes/content/curriculum/igcse_o/A1_Number/2026-06-04_A1_Q7_indices-standard-form.json

### Problem Sets (7)
- /opt/data/.hermes/content/problems/igcse_o/A1_Number/2026-06-04_A1_Q1_number-types_problems.json
- /opt/data/.hermes/content/problems/igcse_o/A1_Number/2026-06-04_A1_Q2_factors-multiples-primes_problems.json
- /opt/data/.hermes/content/problems/igcse_o/A1_Number/2026-06-04_A1_Q3_fractions-decimals_problems.json
- /opt/data/.hermes/content/problems/igcse_o/A1_Number/2026-06-04_A1_Q4_percentages_problems.json
- /opt/data/.hermes/content/problems/igcse_o/A1_Number/2026-06-04_A1_Q5_rounding-estimation_problems.json
- /opt/data/.hermes/content/problems/igcse_o/A1_Number/2026-06-04_A1_Q6_ratios-proportion_problems.json
- /opt/data/.hermes/content/problems/igcse_o/A1_Number/2026-06-04_A1_Q7_indices-standard-form_problems.json

### GIF Renders (14)
- /opt/data/.hermes/content/gifs/igcse_o/2026-06-04_A1_Q1_venn-diagram-classification.gif
- /opt/data/.hermes/content/gifs/igcse_o/2026-06-04_A1_Q3_recurring-decimal-to-fraction.gif
- /opt/data/.hermes/content/gifs/igcse_o/2026-06-04_A1_Q4_compound-interest.gif
- /opt/data/.hermes/content/gifs/igcse_o/2026-06-04_A1_Q4_percentage-change-bars.gif
- /opt/data/.hermes/content/gifs/igcse_o/2026-06-04_A1_Q5_bounds-error-intervals.gif
- /opt/data/.hermes/content/gifs/igcse_o/2026-06-04_A1_Q5_significant-figures-zoom.gif
- /opt/data/.hermes/content/gifs/igcse_o/2026-06-04_A1_Q6_direct-proportion-graph.gif
- /opt/data/.hermes/content/gifs/igcse_o/2026-06-04_A1_Q6_sharing-ratio-bars.gif
- /opt/data/.hermes/content/gifs/igcse_o/2026-06-04_A1_Q7_laws-of-indices.gif
- /opt/data/.hermes/content/gifs/igcse_o/2026-06-04_A1_Q7_standard-form-decimal.gif
- /opt/data/.hermes/content/gifs/igcse_o/fraction-addition-pies.gif
- /opt/data/.hermes/content/gifs/igcse_o/prime-factor-tree.gif
- /opt/data/.hermes/content/gifs/igcse_o/hcf-lcm-sets.gif
- /opt/data/.hermes/content/gifs/igcse_o/number-sets-on-line.gif

---

## Findings

### ERROR 1
- **Artifact:** /opt/data/.hermes/content/curriculum/igcse_o/A1_Number/2026-06-04_A1_Q5_rounding-estimation.json
- **Location:** `sections.core_explanation` — Decimal Places example
- **Description:** The explanation for rounding 3.14159 to 2 decimal places contains a mathematical error in the initial reasoning. It states: "Look at the third decimal digit: $9$". The third decimal digit (thousandths place) of 3.14159 is **1**, not 9. The digit 9 is the **5th** decimal place (hundred-thousandths). The text then follows with contradictory statements: "$3.14159 \approx 3.14$ (actually $3.142$ since $9 \geq 5$ means we round up the $1$ to $2$)". The parenthetical "$3.142$" is the result of rounding to **3** decimal places, not 2. While the final self-correction ("Wait — let me redo that carefully") does arrive at the correct answer (3.14 to 2 d.p.), the preceding incorrect working confuses rather than instructs.
- **Suggested Fix:** Remove the incorrect initial attempt entirely. Replace with clean, correct working:
  > **Round $3.14159$ to $2$ decimal places:**
  > - 1st d.p. (tenths): $3.1$
  > - 2nd d.p. (hundredths): look at the 3rd decimal digit $= 1$. Since $1 < 5$, round down → $3.14$
  > 
  > **Round $3.14159$ to $3$ decimal places:**
  > - 3rd d.p. (thousandths): look at the 4th decimal digit $= 5$. Since $5 \geq 5$, round up → $3.142$

### ERROR 2
- **Artifact:** GIF Renders (9 files)
- **Location:** `/opt/data/.hermes/content/gifs/igcse_o/2026-06-04_A1_*` — 9 of 10 date-stamped GIFs
- **Description:** Nine of the ten date-stamped GIF renders have identical MD5 hashes and identical file sizes (6,789,493 bytes). Specifically:
  - 2026-06-04_A1_Q1_venn-diagram-classification.gif
  - 2026-06-04_A1_Q3_recurring-decimal-to-fraction.gif
  - 2026-06-04_A1_Q4_compound-interest.gif
  - 2026-06-04_A1_Q4_percentage-change-bars.gif
  - 2026-06-04_A1_Q5_bounds-error-intervals.gif
  - 2026-06-04_A1_Q5_significant-figures-zoom.gif
  - 2026-06-04_A1_Q6_direct-proportion-graph.gif
  - 2026-06-04_A1_Q6_sharing-ratio-bars.gif
  - 2026-06-04_A1_Q7_standard-form-decimal.gif
  
  These are not genuine renders — they are the same placeholder/stub file copied to multiple names. Only `2026-06-04_A1_Q7_laws-of-indices.gif` (2,113,274 bytes) appears to be a distinct render.
- **Suggested Fix:** Re-run the Manim rendering pipeline for all 9 affected GIFs to produce genuine, distinct animations. Verify each render produces a unique hash before deploying.

### WARNING 1
- **Artifact:** /opt/data/.hermes/content/curriculum/igcse_o/A1_Number/2026-06-04_A1_Q5_rounding-estimation.json
- **Location:** `sections.core_explanation` — Decimal Places section, self-correction dialogue
- **Description:** The "Wait — let me redo that carefully" meta-commentary is informal and presents a wrong-then-correct pattern that is confusing for students aged 14–16. Final concept scripts should show correct mathematics only, not the author's debugging process.
- **Suggested Fix:** Replace the entire self-correcting dialogue with clean, authoritative examples (as described in ERROR 1's suggested fix).

### WARNING 2
- **Artifact:** /opt/data/.hermes/content/gifs/igcse_o/fractions.gif
- **Location:** File metadata
- **Description:** `fractions.gif` is only 29 bytes — essentially an empty/broken file. It cannot be a valid GIF animation.
- **Suggested Fix:** Remove the broken file or regenerate the animation.

### WARNING 3
- **Artifact:** /opt/data/.hermes/content/gifs/igcse_o/number_types.gif
- **Location:** File metadata
- **Description:** `number_types.gif` is only 27 bytes — essentially an empty/broken file. It cannot be a valid GIF animation.
- **Suggested Fix:** Remove the broken file or regenerate the animation.

### INFO 1
- **Artifact:** /opt/data/.hermes/content/curriculum/igcse_o/A1_Number/2026-06-04_A1_Q5_rounding-estimation.json
- **Location:** `sections.core_explanation` — Bounds section
- **Description:** The worked example for bounds correctly calculates LB and UB areas, but the question mentions 2 decimal places on the original measurements. It would be helpful to briefly explain why the bounds are (measurement ± 0.05) for 1 d.p. rounding, to reinforce the concept for students.
- **Suggested Fix:** Optionally add a brief explanation: "Since 12.4 is to 1 d.p., the true value lies in [12.35, 12.45). The ±0.05 comes from half of the rounding precision (0.1 ÷ 2 = 0.05)."

### INFO 2
- **Artifact:** /opt/data/.hermes/content/curriculum/igcse_o/A1_Number/2026-06-04_A1_Q1_number-types.json
- **Location:** `sections.hook`
- **Description:** The hook mentions "mathematicians were executed for discovering" controversial numbers. While historically true (Hippasus and irrational numbers), this could be slightly alarming for younger students. Consider softening the tone.
- **Suggested Fix:** Optional — rephrase to "some numbers were so controversial that mathematicians faced serious consequences for discovering them" to keep the intrigue without the graphic detail.

---

## Summary
- Total findings: 7
- Errors: 2
- Warnings: 3
- Infos: 2
- Verdict: **FLAGGED**

### Verdict Rationale
The mathematical content in the concept scripts and problem sets is generally sound — all equations, worked examples, problem solutions, and cross-references have been independently verified and are correct. The seven problem sets were fully cross-checked against their solutions and all match.

However, two blocking issues prevent promotion:

1. **ERROR 1:** The rounding explanation in A1_Q5 contains an incorrect identification of decimal digit positions (claiming the 3rd decimal digit of 3.14159 is 9 when it is 1), alongside self-contradictory statements. This is a mathematical accuracy error in a concept script that must be fixed.

2. **ERROR 2:** 9 of 10 Manim GIF renders are identical placeholder/stub files (same MD5 hash, same file size of 6,789,493 bytes), meaning genuine animations were not produced. This renders the visual content pipeline non-functional for this unit.

Both issues must be resolved before the unit can be promoted to 'Live'.
