"""
Sample GSTINs for testing. Add your own edge case at the bottom.
"""

from gstin_validator import validate_with_reason

SAMPLE_GSTINS = [
    "29ABCDE1234F1Z5",   # valid format, check digit may vary
    "27AAAPL1234C1ZV",
    "07AAACH7409R1ZZ",
    "1234567890ABCDE",   # bad format
    "",                  # empty string
    # TODO: participant — add one edge case you found below
]

if __name__ == "__main__":
    for g in SAMPLE_GSTINS:
        print(validate_with_reason(g))
