# QA Report: G1_Probability (IGCSE 0580)
**Date:** 2026-06-05  
**Reviewer:** Hermes Agent (automated QA)

---

## Summary

| Category | Files | Status |
|---|---|---|
| Curriculum JSONs | 7 | ✅ All passed |
| Problem Sets | 7 | ✅ 1 bug fixed |
| Manim Scripts | 14 | ✅ All passed |
| GIFs | 14 | ✅ All passed |

---

## 1. Curriculum JSONs (7 files)

**Files reviewed:**
- `G1_Q1_basic-probability.json` — ✅
- `G1_Q2_sample-space.json` — ✅
- `G1_Q3_tree-diagrams.json` — ✅
- `G1_Q4_conditional-probability.json` — ✅
- `G1_Q5_venn-diagrams.json` — ✅
- `G1_Q6_expected-value.json` — ✅
- `G1_Q7_experimental-theoretical.json` — ✅

**Checks performed:**
| Check | Result |
|---|---|
| Valid JSON syntax | ✅ All valid |
| All required top-level fields (`track`, `unit`, `topic_id`, `title`, `syllabus_ref`, `version`, `created_at`, `sections`) | ✅ All present |
| All required sections (`hook`, `prerequisites`, `core_explanation`, `worked_example`, `common_mistakes`, `summary`) | ✅ All present |
| `common_mistakes` entries have both `mistake` and `correction` fields | ✅ All valid |
| All probabilities between 0 and 1 | ✅ No issues |
| No LaTeX/MathTex patterns (`\frac`, `\text`, `MathTex`, etc.) | ✅ Clean |
| No `$$` (double dollar) LaTeX delimiters | ✅ Clean |

**Verdict: PASS** ✅

---

## 2. Problem Sets (7 files)

**Files reviewed:**
- `basic-probability_problems.json` — 16 problems (4F+6C+4E+2X)
- `sample-space_problems.json` — 16 problems (4F+6C+4E+2X)
- `tree-diagrams_problems.json` — 16 problems (4F+6C+4E+2X)
- `conditional-probability_problems.json` — 16 problems (4F+6C+4E+2X)
- `venn-diagrams_problems.json` — 16 problems (4F+6C+4E+2X)
- `expected-value_problems.json` — 16 problems (4F+6C+4E+2X)
- `experimental-theoretical_problems.json` — 16 problems (4F+6C+4E+2X)

**Checks performed:**
| Check | Result |
|---|---|
| Valid JSON syntax | ✅ All valid |
| Required fields per problem (`id`, `difficulty`, `problem_text`, `answer`, `solution`) | ✅ All present |
| Problem count = 16 per file | ✅ All correct |
| Difficulty distribution (4F+6C+4E+2X) | ✅ All correct |
| All probabilities between 0 and 1 | ✅ All correct |
| Fractions simplified correctly | ✅ All verified |
| Answer fractions match computed values | ✅ All verified |

**Bug Found & Fixed:**
| File | Problem ID | Issue | Fix |
|---|---|---|---|
| `conditional-probability_problems.json` | `G1_Q4_X1` | **Mathematical error:** Problem stated P(both red) = 1/5 and solution found n=4, but n=4 gives P(both red) = 6/10 × 5/9 = 1/3, not 1/5. The solution used a factorization `(n+15)(n-4)=0` for quadratic `n²+11n-120=0`, which was mathematically inconsistent (correct factorization would be for `n²+11n-60=0`). | Changed problem text from "1/5" to "1/3" and updated solution equation from `1/5`/`150`/`n²+11n-120=0` to `1/3`/`90`/`n²+11n-60=0`. Now n=4 correctly gives P(RR)=1/3. |

**Verdict: PASS** ✅ (1 bug fixed)

---

## 3. Manim Scripts (14 files)

**Files reviewed:**
- `G1_Q1_probability-scale.py` — ✅
- `G1_Q1_single-event.py` — ✅
- `G1_Q2_sample-space.py` — ✅
- `G1_Q2_two-way-table.py` — ✅
- `G1_Q3_tree-diagram.py` — ✅
- `G1_Q3_tree-multiply.py` — ✅
- `G1_Q4_conditional-intro.py` — ✅
- `G1_Q4_conditional-with-tree.py` — ✅
- `G1_Q5_venn-formula.py` — ✅
- `G1_Q5_venn-probability.py` — ✅
- `G1_Q6_expected-frequency.py` — ✅
- `G1_Q6_expected-value.py` — ✅
- `G1_Q7_experimental-vs-theoretical.py` — ✅
- `G1_Q7_relative-frequency.py` — ✅

**Checks performed:**
| Check | Result |
|---|---|
| `ast.parse()` validates (no syntax errors) | ✅ All valid |
| First line is `from manim import *` | ✅ All correct |
| Second line is `import math` | ✅ All correct |
| No `Axes` class usage | ✅ Clean |
| No `get_axis_labels()` usage | ✅ Clean |
| No `MathTex` class usage | ✅ Clean |
| No `Tex` class usage (distinct from `Text`) | ✅ Clean |
| No `$$` (LaTeX delimiter) | ✅ Clean |
| No `\\` (LaTeX backslash) | ✅ Clean |
| All class names are unique | ✅ 14 unique names |
| All classes extend `Scene` | ✅ All extend Scene |

**Verdict: PASS** ✅

---

## 4. GIFs (14 files)

**Files in `/gifs/igcse_o/G1_Probability/`:**

| File | Size | Status |
|---|---|---|
| `G1_Q1_probability-scale.gif` | 30.9 KB | ✅ >1KB |
| `G1_Q1_single-event.gif` | 32.9 KB | ✅ >1KB |
| `G1_Q2_sample-space.gif` | 41.0 KB | ✅ >1KB |
| `G1_Q2_two-way-table.gif` | 58.5 KB | ✅ >1KB |
| `G1_Q3_tree-diagram.gif` | 43.7 KB | ✅ >1KB |
| `G1_Q3_tree-multiply.gif` | 56.2 KB | ✅ >1KB |
| `G1_Q4_conditional-intro.gif` | 62.0 KB | ✅ >1KB |
| `G1_Q4_conditional-with-tree.gif` | 53.5 KB | ✅ >1KB |
| `G1_Q5_venn-formula.gif` | 56.1 KB | ✅ >1KB |
| `G1_Q5_venn-probability.gif` | 59.1 KB | ✅ >1KB |
| `G1_Q6_expected-frequency.gif` | 52.2 KB | ✅ >1KB |
| `G1_Q6_expected-value.gif` | 32.9 KB | ✅ >1KB |
| `G1_Q7_experimental-vs-theoretical.gif` | 53.0 KB | ✅ >1KB |
| `G1_Q7_relative-frequency.gif` | 70.2 KB | ✅ >1KB |

**Checks performed:**
| Check | Result |
|---|---|
| All 14 GIFs exist | ✅ Present |
| All file sizes > 1KB | ✅ All pass (min: 30.9 KB) |

**Verdict: PASS** ✅

---

## Overall Result: ✅ PASS (1 issue found and fixed)

| Category | Status |
|---|---|
| Curriculum JSONs | ✅ 7/7 pass |
| Problem Sets | ✅ 7/7 pass (1 bug fixed) |
| Manim Scripts | ✅ 14/14 pass |
| GIFs | ✅ 14/14 pass |

**Files modified:**
- `/opt/data/.hermes/content/problems/igcse_o/G1_Probability/conditional-probability_problems.json` — Fixed mathematical error in problem G1_Q4_X1 (changed P(both red) from 1/5 to 1/3, updated solution equations).

**Files created:**
- `/opt/data/.hermes/content/qa-reports/2026-06-05_G1_Probability_qa-review.md` — This report.
