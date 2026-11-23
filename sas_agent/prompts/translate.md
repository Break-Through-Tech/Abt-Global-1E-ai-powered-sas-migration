Translate the SAS program below into a single, complete, runnable Python script.

You are an expert SAS and Python (pandas/numpy/scipy/scikit-learn) engineer migrating a legacy SAS 9.4 analytics pipeline -- the CMS Overall Hospital Quality Star Rating SAS pack -- to Python.

Your translations must reproduce the SAS outputs exactly (within floating-point tolerance), so pay close attention to SAS semantics that differ from pandas defaults, for example:

## Code Structure
- Write clear, well-structured, readable code.
- Use one function per logical SAS processing step.
- Convert SAS macros into reusable Python functions.
- Include a `main()` entry point.
- Execute functions in the same order as the original SAS program.
- Include comments referencing the corresponding SAS step being reproduced.

## Translation Instructions
- Use the provided analysis to understand the SAS program's logic and processing flow.
- Use `Star_Macros.sas` to understand and reproduce relevant macro definitions.
- Preserve the original SAS program's calculations, transformations, filtering, sorting, and output logic.
- Pay attention to SAS-specific behavior that may differ from pandas defaults.
- Use prior Python translations as references for reusable logic where applicable.
- Do not omit processing steps or invent business logic.
- Preserve output dataset names and column casing.
- Keep the implementation straightforward and avoid unnecessary abstractions.

## Runtime Contract

{contract}

## Analysis of the Program

{analysis}

## Star_Macros.sas

{macros}

## SAS Program: {sas_file}

{sas_code}

## Prior Python Translations

{prior}

Return the full Python script in a single `python` code block. Do not include explanatory text outside the code block.