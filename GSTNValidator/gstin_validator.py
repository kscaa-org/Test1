"""
GSTIN Validator
----------------
Validates a GSTIN (Goods and Services Tax Identification Number) on two fronts:
1. Format check — 15-character structure per GSTN spec.
2. Checksum check — verifies the last character (check digit) using GSTN's
   modulus-36 algorithm.

GSTIN structure (15 chars):
  [2 state code][10 PAN][1 entity code][1 'Z' by default][1 checksum]
"""

import re

# GSTN uses this 36-character code list for checksum math
CODE_LIST = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
FACTOR = [1, 2]  # alternating multiplier, GSTN spec

GSTIN_FORMAT = re.compile(
    r"^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[1-9A-Z]{1}Z[0-9A-Z]{1}$"
)


def is_valid_format(gstin: str) -> bool:
    """Checks the 15-character structural pattern only (no checksum)."""
    if not gstin or len(gstin) != 15:
        return False
    return bool(GSTIN_FORMAT.match(gstin.upper()))


def calculate_checksum(gstin: str) -> str:
    """
    Recomputes the check digit (15th character) from the first 14 characters,
    using GSTN's modulus-36 algorithm.
    """
    gstin = gstin.upper()
    total = 0
    for i, char in enumerate(gstin[:14]):
        code_value = CODE_LIST.index(char)
        factor = FACTOR[i % 2]
        product = code_value * factor
        # fold down into single base-36 digit
        total += (product // 36) + (product % 36)
    checksum_value = (36 - (total % 36)) % 36
    return CODE_LIST[checksum_value]


def is_valid_gstin(gstin: str) -> bool:
    """Full validation: format + checksum. Returns True only if both pass."""
    if not is_valid_format(gstin):
        return False
    gstin = gstin.upper()
    expected_checksum = calculate_checksum(gstin)
    return gstin[-1] == expected_checksum


def validate_with_reason(gstin: str) -> dict:
    """Returns a breakdown — useful for audit trails, not just pass/fail."""
    result = {"gstin": gstin, "valid": False, "reason": ""}
    if not gstin or len(gstin) != 15:
        result["reason"] = "Length must be 15 characters."
        return result
    if not is_valid_format(gstin):
        result["reason"] = "Structural format mismatch."
        return result
    gstin = gstin.upper()
    expected = calculate_checksum(gstin)
    if gstin[-1] != expected:
        result["reason"] = f"Checksum mismatch. Expected '{expected}'."
        return result
    result["valid"] = True
    result["reason"] = "Valid GSTIN."
    return result


def run_test_cases():
    """Runs bundled sample GSTINs from test_cases.py."""
    from test_cases import SAMPLE_GSTINS
    for g in SAMPLE_GSTINS:
        print(validate_with_reason(g))


def run_user_input():
    """Asks user for one GSTIN, prints validity."""
    gstin = input("Enter GSTIN: ").strip()
    result = validate_with_reason(gstin)
    print(f"{result['gstin']} → {'VALID' if result['valid'] else 'INVALID'}")
    print(f"Reason: {result['reason']}")


if __name__ == "__main__":
    choice = input("Test cases (T) or enter own GSTIN (U)? ").strip().upper()
    if choice == "T":
        run_test_cases()
    elif choice == "U":
        run_user_input()
    else:
        print("Invalid choice. Enter T or U.")
