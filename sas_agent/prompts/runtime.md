# Runtime Contract

## 1. Execution Requirements

- The generated Python script must run as a standalone script using `python script.py`.
- Do not prompt the user for input.
- Do not depend on an active SAS session.

## 2. SAS Library: HC (Input)

- HC represents the input data library in the original SAS program.
- Read input datasets from a configurable directory provided through the `SAS_INPUT_DIR` environment variable.
- Assume input datasets are available as CSV files.
- Use the original SAS dataset names as filenames, converted to lowercase, with the `.csv` extension.
- Do not hardcode file paths.

## 3. SAS Library: R (Output)

- R represents the output data library in the original SAS program.
- Write output datasets to a configurable directory provided through the `SAS_OUTPUT_DIR` environment variable.
- Output filenames must use uppercase dataset names with the `.csv` extension.
- Export CSV files using `index=False`.
- Datasets written to R by earlier programs are available in the same output directory, following the same naming convention.

## 4. Data Types

- Read `PROVIDER_ID` and any other identifier columns as strings.
- Preserve leading zeros in identifiers.
- Preserve the column casing used in the SAS output.

## 5. SAS Session and Dependencies

- SAS session state from earlier programs, including WORK datasets and macro variables, is not available.
- Recompute anything needed from datasets stored on disk.
- Ignore `LIBNAME`, `%INCLUDE`, and path-related `%LET` statements. The runtime contract replaces these configurations.

## 6. Allowed Libraries

Use only:
- Python standard library
- pandas

Do not import or use NumPy, SciPy, scikit-learn, or other third-party libraries directly.

Implement data transformations and calculations using pandas wherever possible.

## 7. Required Output Datasets

The program must produce the following datasets:

{outputs}

## 8. Final Execution Requirement

Generate a standalone Python script that follows the input/output conventions and library restrictions described above.