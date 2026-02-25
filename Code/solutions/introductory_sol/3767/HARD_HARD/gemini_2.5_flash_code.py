```python
# Constants for digit mapping. Digits 0-9 and letters A-Z (for 10-35).
_DIGIT_CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
_CHAR_TO_DIGIT_MAP = {char: i for i, char in enumerate(_DIGIT_CHARS)}

# The highest factorial index 'k' that can have a non-zero coefficient d_k,
# based on the problem statement "encode numbers up to 36!-1".
# A number N = d_k * k! + ... + d_0 * 0!, where 0 <= d_i <= i.
# The largest digit character 'Z' corresponds to value 35.
# Thus, d_i can be at most 35. This means the highest 'i' (factorial index)
# for which d_i can be non-zero is 35 (since d_i <= i).
_MAX_FACTORIAL_INDEX_FOR_DIGITS = len(_DIGIT_CHARS) - 1  # This is 35

# Precompute factorials.
# We need factorials from 0! up to _MAX_FACTORIAL_INDEX_FOR_DIGITS! (i.e., 35!).
# We also need (MAX_FACTORIAL_INDEX_FOR_DIGITS + 1)! (i.e., 36!)
# to determine the maximum representable decimal number.
# So, _FACTORIALS[i] stores i!. The list size will be _MAX_FACTORIAL_INDEX_FOR_DIGITS + 2.
_FACTORIALS = [1] * (_MAX_FACTORIAL_INDEX_FOR_DIGITS + 2)
for i in range(1, _MAX_FACTORIAL_INDEX_FOR_DIGITS + 2):
    _FACTORIALS[i] = _FACTORIALS[i - 1] * i

# The maximum decimal number that can be represented with the defined digit set
# is (_MAX_FACTORIAL_INDEX_FOR_DIGITS + 1)! - 1, which is 36! - 1.
_MAX_REPRESENTABLE_DECIMAL = _FACTORIALS[_MAX_FACTORIAL_INDEX_FOR_DIGITS + 1] - 1


def _get_char_for_digit(digit: int) -> str:
    """
    Converts an integer digit value (0-35) to its character representation.

    Args:
        digit: An integer representing a digit (0 to 35).

    Returns:
        The character ('0'-'9', 'A'-'Z') corresponding to the digit.

    Raises:
        ValueError: If the digit is outside the supported range.
    """
    if not (0 <= digit < len(_DIGIT_CHARS)):
        raise ValueError(
            f"Digit {digit} out of supported range (0-{len(_DIGIT_CHARS) - 1})."
        )
    return _DIGIT_CHARS[digit]


def _get_digit_for_char(char: str) -> int:
    """
    Converts a character representation ('0'-'9', 'A'-'Z') to its integer digit value.

    Args:
        char: A string representing a digit character.

    Returns:
        The integer value of the digit.

    Raises:
        ValueError: If the character is not a valid digit representation.
    """
    if char not in _CHAR_TO_DIGIT_MAP:
        raise ValueError(
            f"Invalid character '{char}' for factorial representation. "
            "Expected '0'-'9' or 'A'-'Z'."
        )
    return _CHAR_TO_DIGIT_MAP[char]


def decimal_to_factorial_representation(decimal_number: int) -> str:
    """
    Converts a positive decimal integer to its factorial number system representation string.

    The factorial number system represents a number N as:
    N = d_k * k! + d_{k-1} * (k-1)! + ... + d_1 * 1! + d_0 * 0!
    where 0 <= d_i <= i for each i, and the last digit d_0 is always 0.
    The representation is the sequence of digits d_k d_{k-1} ... d_1 d_0.

    Args:
        decimal_number: A non-negative integer to be converted. Per problem statement,
                        expected to be positive, but 0 is handled gracefully.

    Returns:
        A string representing the number in the factorial number system.

    Raises:
        ValueError: If the input decimal_number is not a non-negative integer
                    or exceeds the maximum representable value (36!-1).
    """
    if not isinstance(decimal_number, int) or decimal_number < 0:
        raise ValueError("Input decimal_number must be a non-negative integer.")
    if decimal_number == 0:
        return "0"

    # Check if number is too large to be represented with available digits (0-35).
    if decimal_number > _MAX_REPRESENTABLE_DECIMAL:
        raise ValueError(
            f"Decimal number {decimal_number} is too large to be represented "
            f"with digits '0'-'Z'. Max representable is {_MAX_REPRESENTABLE_DECIMAL} "
            f"({_MAX_FACTORIAL_INDEX_FOR_DIGITS + 1}!-1)."
        )

    # Find the largest k such that k! * d_k (where d_k <= k) contributes to decimal_number.
    # This means finding the largest k such that (k+1)! > decimal_number.
    # The `k` will be the highest factorial index for a non-zero coefficient.
    k = 0
    # Iterate as long as we haven't exceeded the max supported factorial index
    # and the next factorial (_FACTORIALS[k+1]) is less than or equal to the decimal_number.
    # This ensures that `k` is the highest index potentially needed.
    while k <= _MAX_FACTORIAL_INDEX_FOR_DIGITS and _FACTORIALS[k + 1] <= decimal_number:
        k += 1

    digits_chars = []
    current_number = decimal_number

    # Calculate digits from d_k down to d_0.
    # The loop starts from the highest determined factorial index `k` down to 0.
    for i in range(k, -1, -1):
        factorial_value = _FACTORIALS[i]
        digit_val = current_number // factorial_value

        # The factorial number system rules require 0 <= d_i <= i.
        # This conversion algorithm naturally produces digits satisfying this if the input number is valid.
        # This check provides robustness against potential logical errors or unexpected state.
        if not (0 <= digit_val <= i):
            raise ValueError(
                f"Internal error: Calculated digit {digit_val} for position {i} "
                "violates 0 <= d_i <= i rule."
            )

        digits_chars.append(_get_char_for_digit(digit_val))
        current_number %= factorial_value

    # After processing all factorial positions, the remainder should be 0.
    if current_number != 0:
        raise ValueError(
            "Internal error: Remainder is not zero after converting to factorial representation."
        )

    return "".join(digits_chars)


def factorial_representation_to_decimal(factorial_representation: str) -> int:
    """
    Converts a factorial number system representation string to its decimal integer.

    The factorial number system represents a number N as:
    N = d_k * k! + d_{k-1} * (k-1)! + ... + d_1 * 1! + d_0 * 0!
    where 0 <= d_i <= i for each i, and the last digit d_0 is always 0.
    The representation is the sequence of digits d_k d_{k-1} ... d_1 d_0.

    Args:
        factorial_representation: A string representing a number in the factorial number system.

    Returns:
        The decimal integer value of the representation.

    Raises:
        ValueError: If the input string is empty, contains invalid characters,
                    or violates the rules of the factorial number system (e.g., d_i > i, d_0 != 0).
    """
    if not isinstance(factorial_representation, str):
        raise ValueError("Input factorial_representation must be a string.")
    if not factorial_representation:
        raise ValueError("Input factorial_representation cannot be empty.")

    # Handle the "0" case directly as per definition and example.
    if factorial_representation == "0":
        return 0

    total_decimal_value = 0
    length = len(factorial_representation)

    # Validate the length of the representation string.
    # A representation string of length L represents digits d_{L-1} ... d_0.
    # The highest index supported is _MAX_FACTORIAL_INDEX_FOR_DIGITS (35).
    # So max length is 36 (for d_35...d_0).
    if length > _MAX_FACTORIAL_INDEX_FOR_DIGITS + 1:
        raise ValueError(
            f"Factorial representation string is too long ({length} digits). "
            f"Max supported length for d_k...d_0 is {_MAX_FACTORIAL_INDEX_FOR_DIGITS + 1} "
            f"(for d_{_MAX_FACTORIAL_INDEX_FOR_DIGITS}...d_0)."
        )

    # Iterate through the string from left to right (most significant digit to least significant).
    # The i-th character (0-indexed) corresponds to the (length - 1 - i)-th factorial position.
    for i, char_digit in enumerate(factorial_representation):
        digit_val = _get_digit_for_char(char_digit)
        # factorial_index is 'j' in d_j * j!
        factorial_index = length - 1 - i

        # Validate factorial number system rules: 0 <= d_j <= j.
        if not (0 <= digit_val <= factorial_index):
            raise ValueError(
                f"Invalid digit '{char_digit}' (value {digit_val}) at position {i} "
                f"for factorial index {factorial_index}. Digit value must be "
                f"between 0 and {factorial_index} (inclusive)."
            )

        # The 0-th position digit (d_0) must always be 0.
        if factorial_index == 0 and digit_val != 0:
            raise ValueError(
                f"Invalid last digit '{char_digit}' (value {digit_val}). "
                "The 0-th position digit (d_0) must be 0."
            )

        total_decimal_value += digit_val * _FACTORIALS[factorial_index]

    return total_decimal_value
```