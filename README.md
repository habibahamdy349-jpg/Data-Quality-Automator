# Data-Quality-Automator
Automated Python pipeline for data cleaning, preprocessing, and quality reporting.
# 🧹 Data Quality Automator & Cleaning Pipeline

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/pandas-data%20analysis-150458.svg)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An automated Python-based data cleaning and preprocessing pipeline designed to handle raw datasets, clean messy records, standardize text columns, handle missing values, and generate summary reports for downstream analytics.

---

## 📌 Features

- **Automated Duplicate Removal:** Detects and drops duplicate records automatically.
- **Smart Missing Value Handling:** Fills numeric gaps with baseline values and handles categorical missing data seamlessly.
- **Text Standardization:** Cleans whitespaces, converts casing, and normalizes messy user inputs.
- **Data Quality Reporting:** Generates visual reports highlighting clean vs. removed records.
- **Export Options:** Outputs clean dataset ready for business intelligence tools (PowerBI, Tableau, Excel).

---

## 📁 Repository Structure

```text
Data-Quality-Automator/
├── data/
│   ├── sample_raw_data.csv       # Raw input dataset
│   └── cleaned_output_data.csv   # Cleaned dataset result
├── src/
│   └── cleaner.py                # Main automation logic
├── outputs/
│   └── data_report.png           # Visual quality summary
├── README.md                     # Project documentation
└── requirements.txt              # Project dependencies
