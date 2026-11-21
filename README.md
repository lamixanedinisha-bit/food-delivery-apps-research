# Consumer Attitudes Toward Food Delivery Apps — BUS227

> **Research summary, recreated from the BUS227 presentation in Google Drive — original survey file / raw data are no longer accessible (student email closed).**
>
> Dinisha Lamichhane was a member of the team of 5; her individual contribution is **[to confirm]**.

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

See `data/reported_results.csv` — these are the **reported percentages only**, not raw survey rows. Do not treat them as individual responses.

## Recommendations (from the original project)

Fee transparency, a student loyalty tier, and order bundling.

## Reproduce the summary

```bash
python analysis/summary.py
```

This prints the reported table from `data/reported_results.csv`. It does not re-run the original survey analysis, because the raw data is not available.
