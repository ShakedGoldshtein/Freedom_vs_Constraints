```python
def iq_test(numbers_str: str) -> int:
    """
    Finds the number that differs in evenness from the others and returns its 1-based position.

    The problem statement guarantees that exactly one number will differ in evenness from the
    rest of the numbers. This implies there will always be a clear majority of numbers
    sharing one parity (even or odd) and a single number with the opposite parity.

    Args:
        numbers_str: A string containing space-separated integers.

    Returns:
        The 1-based position of the number that differs in evenness.

    Raises:
        ValueError: If the input string is empty, contains non-integer tokens,
                    or does not contain a clear outlier based on evenness as per
                    the problem's implicit criteria (e.g., all numbers have the same
                    evenness, or there are not enough numbers to establish a clear
                    majority/minority pattern).
    """
    if not numbers_str:
        raise ValueError("Input string cannot be empty.")

    # Split the string by space and filter out any empty tokens that might result
    # from multiple spaces (e.g., "1  2" or leading/trailing spaces " 1 2 ").
    tokens = [token for token in numbers_str.split(' ') if token]
    if not tokens:
        raise ValueError("Input string must contain at least one number.")

    # According to the problem's premise ("one number differs from the others") and
    # typical IQ test scenarios (e.g., examples like "1 2 1 1" or "2 4 7 8 10"),
    # there must be at least two numbers to compare, and effectively at least three
    # to establish a clear majority/minority pattern (e.g., two evens and one odd).
    if len(tokens) < 2:
        raise ValueError("At least two numbers are required to find a difference in evenness.")

    # Variables to track the first encountered index and count for even and odd numbers.
    # These variables provide O(1) auxiliary space for the counting logic.
    first_even_idx: int = -1
    first_odd_idx: int = -1
    even_count: int = 0
    odd_count: int = 0

    # Iterate through the tokens, converting them to integers on the fly.
    # This avoids creating an intermediate list of integers, maintaining O(1) auxiliary space.
    for i, token in enumerate(tokens):
        try:
            num = int(token)
        except ValueError as e:
            raise ValueError(f"Invalid number format '{token}' in input: {e}")

        current_idx = i + 1  # Store 1-based index as required by the problem

        if num % 2 == 0:
            even_count += 1
            if first_even_idx == -1:
                first_even_idx = current_idx
        else:
            odd_count += 1
            if first_odd_idx == -1:
                first_odd_idx = current_idx

        # Early exit condition: Once we have identified a clear majority (count > 1)
        # and a single minority (count == 1), we have found the outlier.
        # This condition is typically met after processing at least 3 numbers.
        if even_count >= 1 and odd_count >= 1:  # Ensures both parities have been seen
            if even_count == 1 and odd_count > 1:
                return first_even_idx
            elif odd_count == 1 and even_count > 1:
                return first_odd_idx

    # If the loop completes without returning, it means that no single unique outlier
    # was found satisfying the "one number differs from the others" criteria.
    # This could happen in cases such as:
    # - All numbers are of the same parity (e.g., "2 4 6", "1 3 5").
    # - There are an equal number of even and odd numbers (e.g., "1 2", "2 4 1 3").
    # - There were fewer than 3 numbers, and the early exit condition wasn't met to
    #   establish a clear majority/minority pattern.
    # All these scenarios violate the problem's premise for a valid IQ test.
    raise ValueError("No unique number differs in evenness from the others. "
                     "This input does not fit the problem's criteria.")
```