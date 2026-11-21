# Consumer Attitudes Toward Food Delivery Apps

**My BUS227 research project — Dinisha Lamichhane, Bachelor of IT (Cyber Security), Sydney Metropolitan Institute of Technology. Team of 5.**

Portfolio version recreated from my university project work — original files are no longer accessible after my student email closed.

## Question

What actually drives Sydney university students' choice of food delivery app — price, speed, variety, or usability?

## Method

- Bias-free survey: Likert + multiple-choice + open-ended questions, rotated question order, pre-tested
- **n = 62 Sydney students, July 2026**
- Coded and cleaned in Excel; descriptive statistics and Pearson correlation
- Limitations honestly noted in the original work: convenience sample, self-report bias, single time point

## Reported results

| Finding | Reported value |
| --- | --- |
| Most-used app: Uber Eats | 44% |
| DoorDash | 28% |
| Menulog | 18% |
| Top choice factor: delivery fee | 38% (variety 27%, speed 22%, usability 13%) |
| Fee sensitivity vs ordering frequency | Pearson r = −0.52 (moderate negative association — association, not causation) |

See `data/reported_results.csv` — these are the **reported percentages only**, not raw survey rows.

## Recommendations (from the project)

Fee transparency, a student loyalty tier, and order bundling.

## Reproduce the summary

```bash
python analysis/summary.py
```

This prints the reported table from `data/reported_results.csv`. It does not re-run the original survey analysis, because the raw data is no longer accessible.
