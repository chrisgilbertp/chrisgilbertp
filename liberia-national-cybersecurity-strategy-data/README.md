# liberia-national-cybersecurity-strategy-data

**Data S1 and Data S2** for the manuscript:

**Developing a national cybersecurity strategy for a safer digital future in Liberia**

Authors: Chris Gilbert, Jeremiah Duah Leakpor, Kwitee D. Gaylah, John K. Constance, and Mercy Abiola Gilbert  
William V. S. Tubman University, Harper, Maryland County, Liberia

This package supports the **Data availability** statement. It contains aggregate survey results, GCI benchmarks, KPI feasibility calculations, risk-class counts, internal consistency checks, and the analysis script that recomputes every derived value from the values reported in the article. **No respondent-level data are included.**

## Contents

| File | Description |
|------|-------------|
| `Data_S1_Supplementary_Dataset.xlsx` | Multi-sheet workbook: Survey_items, Sample_composition, Survey_results (with 95% Wilson intervals), Interview_sample, GCI_benchmark, KPI_feasibility, Planning_power, Risk_classes, Checks |
| `Data_S2_Analysis.py` | Python 3 script (standard library only) that recomputes counts, Wilson intervals, sample-size and power planning, GCI gaps, KPI pace, risk classes, and checks |
| `Questionnaire_and_Interview_Guides.docx` | Survey questionnaire and semi-structured interview guide (research instruments) |
| `README.md` | This file |
| `LICENSE` | Creative Commons Attribution 4.0 International |

Attach the Excel workbook and the instruments document on the **GitHub Release** and on **Zenodo** (they are binary and are not stored as plain text in this folder tree).

## Reproduce the analysis

```bash
python3 Data_S2_Analysis.py [output_directory]
```

Default output directory: `Data_S2_outputs/`. The script writes eight CSV files and prints a full report (including PASS / INFO / FLAG checks).

Requirements: Python 3.8 or later. Standard library only (no pip packages).

## What the script computes

- Derived counts from reported percentages (base *n* = 1,000; affected base *n* = 400)
- Wilson score 95% intervals for every proportion with a stated base
- Respondents per group for 80% power (two-sided α = 0.05) and power with the reported urban (250) and rural (200) group sizes
- GCI 2024 gap statistics for Liberia versus six African comparators
- Required change and annual pace for the quantitative KPIs to 2029
- Distribution of all 125 ordered (P × I × V) risk-score combinations across Low / Moderate / High / Critical classes
- Internal consistency checks documented in the Checks sheet

## Important limitations (also stated in the manuscript)

- The survey used a **stratified convenience (non-probability)** design. Wilson intervals assume simple random sampling and **understate** true uncertainty.
- Sector and location are **separate classifications**; their shares must not be summed into one partition of 1,000.
- Some items (incident response route, barriers, suggested improvements) have **no stated base**; intervals are not computed for those rows.
- GCI scores for Botswana and Sierra Leone differ slightly between the article Table 2 and the GCI 2024 summary pages; ranking is identical under both sets.
- Raw survey and interview data are **not** public, to protect participant confidentiality.

## Suggested citation (update DOI after Zenodo publication)

```text
Gilbert, C., Leakpor, J. D., Gaylah, K. D., Constance, J. K., & Gilbert, M. A. (2026).
Data S1 and Data S2 for "Developing a national cybersecurity strategy for a safer digital future in Liberia" (v1.0.0).
[GitHub release URL]. Zenodo. https://doi.org/10.5281/zenodo.XXXXXXX
```

## Paper data availability statement (template)

```text
Aggregate survey results, sample composition, GCI benchmark values, KPI calculations,
risk-class counts, consistency checks, and the analysis script are available as
Supporting Information (Data S1 and Data S2) on Zenodo under DOI
https://doi.org/10.5281/zenodo.XXXXXXX and on GitHub at
https://github.com/chrisgilbertp/chrisgilbertp/tree/main/liberia-national-cybersecurity-strategy-data.
Raw survey and interview data are not publicly available to protect participant confidentiality.
```

## Licence

Creative Commons Attribution 4.0 International (CC BY 4.0).
