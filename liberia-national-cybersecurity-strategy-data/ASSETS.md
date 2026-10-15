# Binary and large assets

Place these files in this folder when preparing the GitHub Release and Zenodo deposit:

1. `Data_S1_Supplementary_Dataset.xlsx` (aggregate survey tables, GCI, KPI, risk classes, checks)
2. `Questionnaire_and_Interview_Guides.docx` (research instruments)
3. `Data_S2_Analysis.py` (full analysis script; standard library only)

Run:

```bash
python3 Data_S2_Analysis.py
```

The script writes eight CSV files under `Data_S2_outputs/` by default and prints Wilson intervals, planning power, GCI gaps, KPI pace, risk classes, and consistency checks.
