# Juan Contreras

#10/15/2026
#validator/Fixer agent  compares the original SAS code and the generated Python code, as well as the output CSVs from both. 
#It generates a validation report that includes discrepancies, migration mistakes, recommended fixes, and corrected Python code. 
#The agent uses the Gemini-3.8-flash model to analyze the code and provide recommendations for achieving 99% agreement with the SAS output. 

from pathlib import Path
from google import genai
import pandas as pd
import numpy as np
import os

def agent_validator():

    client = genai.Client(
        api_key="MY_API_KEY"
    )

    # ORIGINAL SAS SOURCE
    sas_file = Path("data/0 - Data and Measure Standardization_2025Jul.sas")
    with open(sas_file,"r",encoding="utf-8") as f:
        sas_code = f.read()

    # TRANSLATED PYTHON
    python_file = Path("generated/program_0.py")
    with open(python_file,"r",encoding="utf-8") as f:
        python_code = f.read()

    # SAS output CSV
    sas_output = Path("sas_output_csv/STD_DATA_2025Jul.csv")
    sas_df = pd.read_csv(sas_output)

    # PYTHON GENERATED CSV
    python_output = Path("REPLACE_WITH_PYTHON_OUTPUT_CSV")
    py_df = pd.read_csv(python_output)

   #validation checks
    sas_rows = len(sas_df)
    py_rows = len(py_df)

    row_match = (
        sas_rows == py_rows
    )

    sas_columns = set(
        sas_df.columns
    )

    py_columns = set(
        py_df.columns
    )

    missing_columns = (
        sas_columns - py_columns
    )

    extra_columns = (
        py_columns - sas_columns
    )

    column_match = (
        len(missing_columns) == 0
        and
        len(extra_columns) == 0
    )

    # Value Comparison
    common_columns = list(sas_columns.intersection(py_columns))

    matching_columns = []
    mismatched_columns = []

    for col in common_columns:
        try:
            if sas_df[col].equals(py_df[col]):
                matching_columns.append(col)
            else:
                mismatched_columns.append(col)
        except Exception:
            mismatched_columns.append(col)

    # Data check for numeric columns
    numeric_matches = []
    numeric_failures = []

    numeric_columns = (sas_df.select_dtypes(include=np.number).columns)
    for col in numeric_columns:
        if col not in py_df.columns:
            continue
        try:
            sas_mean = (sas_df[col].mean())

            py_mean = (py_df[col].mean())

            if np.isclose(sas_mean,py_mean,rtol=0.01):
                numeric_matches.append(col)
            else:
                numeric_failures.append(col)
        except Exception:
            numeric_failures.append(col)

    # Accuracy Score
    score = 0

    if row_match:
        score += 25

    if column_match:
        score += 25

    if len(mismatched_columns) == 0:
        score += 25

    if len(numeric_failures) == 0:
        score += 25

    accuracy = score

    #Compares original SAS code and generated Python code 
    #Compares SAS output and generated Python output csv 

    validation_summary = f"""
SAS Rows: {sas_rows}
Python Rows: {py_rows}

Rows Match:
{row_match}

Missing Columns:
{missing_columns}

Extra Columns:
{extra_columns}

Matching Columns:
{len(matching_columns)}

Mismatched Columns:
{mismatched_columns}

Statistics Failures:
{numeric_failures}

Accuracy:
{accuracy}%
"""

    # Fixes and Recommendations Prompt
    prompt = f"""
You are a SAS-to-Python migration validator and fixer.

Original SAS:

{sas_code}

Generated Python:

{python_code}

Validation Results:

{validation_summary}

Goal:
Reach 99% agreement with SAS output.

Tasks:

1. Explain all discrepancies.
2. Identify migration mistakes.
3. Recommend fixes.
4. Generate corrected Python.

Format your response exactly as:

=== VALIDATION REPORT ===

...

=== RECOMMENDED FIXES ===

...

=== CORRECTED PYTHON ===

...
"""

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt
    )

    # Save Report
    report_file = Path(
        "generated/validation_report.md"
    )

    with open(report_file,"w",encoding="utf-8") as f:   
        f.write(response.text)

    print("Validation Complete")
    print(f"Accuracy Score: {accuracy}%")
    print(
        "Saved: generated/validation_report.md"
    )

if __name__ == "__main__":
    agent_validator()