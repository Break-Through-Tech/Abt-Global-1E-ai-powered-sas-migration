# SAS Program Analysis

You are an expert SAS programmer and Python data migration specialist.

Your task is to carefully analyze the provided SAS program before translating it into Python. Understand the program's business purpose, data flow, processing logic, and dependencies.

Do not generate Python code at this stage. Produce a concise but technically detailed analysis that will serve as the foundation for the subsequent Python translation.

## 1. Business Purpose
- Explain what the SAS program is intended to accomplish.
- Describe the business problem it solves.
- Identify the main calculations, reports, or analytical results it produces.

## 2. Input and Output Data
Identify all datasets used by the program.

For each dataset, specify:
- SAS library and dataset name.
- Whether it is an input, intermediate, or output dataset.
- Important columns and their purpose.
- Any filtering, sorting, or transformations applied.

Clearly identify the final output datasets and their expected structure.

## 3. Program Execution Flow
Analyze the SAS program from beginning to end, preserving the original execution order.

For every DATA step, PROC step, SQL statement, and macro invocation:
- Explain what the step does.
- Identify the datasets and variables involved.
- Describe the calculations, transformations, filtering, and grouping.
- Explain how the output is used by subsequent steps.
- Identify the closest equivalent Python approach, preferably using pandas.

Include relevant SAS statements such as:
- SET, MERGE, BY, WHERE, IF/THEN, and OUTPUT.
- PROC SORT, PROC SQL, PROC MEANS, PROC SUMMARY, PROC FREQ, PROC TRANSPOSE, and other statistical procedures.
- Arrays, formats, retained variables, and macro calls.

## 4. Macros and Macro Variables
Identify all macros and macro variables used in the program, including those defined in the included macro file.

For each one:
- Explain its purpose.
- Determine how its parameters and macro variables resolve.
- Describe the operations it performs.
- Explain how it should be implemented in Python.
- Identify any dependencies on external datasets or configuration values.

Do not assume a macro's behavior from its name alone. Inspect its actual definition whenever available.

## 5. Statistical Logic and Translation Risks
Identify SAS-specific behavior that must be preserved during Python translation.

Pay particular attention to:
- Missing-value handling and SAS versus pandas behavior.
- Statistical definitions, including mean, median, standard deviation, variance, and percentiles.
- PROC MEANS and PROC SUMMARY defaults.
- Sorting, BY-group processing, and duplicate handling.
- Merging datasets and join conditions.
- Rounding, numeric precision, and integer conversion.
- Date and datetime handling.
- Retain statements, automatic variables, and variable initialization.
- Clustering, ranking, weighting, and other statistical algorithms.

Explain any differences that could cause Python results to differ from SAS results.

## 6. Dependencies and Assumptions
- Identify external files, libraries, macros, and configuration dependencies.
- Identify assumptions about dataset structure, column types, and data availability.
- Highlight any missing information that must be clarified before translation.

## 7. Python Translation Guidance
Provide a short implementation plan for the subsequent translation:
- Recommended pandas operations and functions.
- Suggested processing sequence.
- Important SAS behaviors that require custom Python logic.
- Checks needed to ensure Python output matches SAS output.

## Analysis Instructions
- Follow the SAS program's original execution order.
- Analyze the actual source code rather than guessing based on program or dataset names.
- Use the included macro definitions to understand macro behavior.
- Consider previously translated programs to understand shared logic and dependencies.
- Do not invent datasets, columns, calculations, or business rules.
- Clearly distinguish confirmed behavior from assumptions.
- Keep the analysis concise, specific, and technically accurate.
- Do not generate Python code.