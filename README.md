# Test1

This repository contains the `GSTNValidator` Python exercise.

## GSTIN Validator

The validator checks Indian GSTIN values on two levels:

- 15-character GSTIN format validation
- GSTIN checksum validation using the modulus-36 algorithm

## Files

- `GSTNValidator/gstin_validator.py` - validation logic and command-line entry point
- `GSTNValidator/test_cases.py` - sample GSTIN values for testing
- `GSTNValidator/README.md` - exercise-specific notes

## Run

```powershell
python GSTNValidator\gstin_validator.py
```

Choose `T` to run the bundled sample cases, or `U` to enter a GSTIN manually.
