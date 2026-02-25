```python
def thirt(n: int) -> int:
    """
    Calculates a stationary sum based on a specific weighting pattern.

    The process involves multiplying the digits of a number (from right to left)
    by a repeating sequence of weights ([1, 10, 9, 12, 3, 4]) and summing the products.
    This operation is repeated with the new sum until the sum becomes stationary
    (i.e., the sum produced in the current step is identical to the number used
    as input for that step).

    Args:
        n: A non-negative integer for which to perform the calculation.

    Returns:
        The stationary number obtained after repeated calculations.

    Raises:
        ValueError: If the input 'n' is a negative integer.
    """
    if n < 0:
        raise ValueError("Input 'n' must be a non-negative integer.")
    if n == 0:
        return 0

    # The repeating sequence of remainders when powers of 10 are divided by 13.
    # These serve as weights for the digits.
    WEIGHTS = [1, 10, 9, 12, 3, 4]

    def _calculate_next_sum(num: int, weights: list[int]) -> int:
        """
        Performs one step of the sum calculation.

        Multiplies the digits of `num` from right to left by the `weights` sequence,
        which cycles as needed, and returns the sum of these products.

        Args:
            num: The integer to process.
            weights: The list of weights to use for multiplication.

        Returns:
            The calculated sum for the given number and weights.
        """
        current_sum = 0
        weight_index = 0
        temp_num = num

        # Process digits from right to left
        while temp_num > 0:
            digit = temp_num % 10  # Get the rightmost digit
            current_sum += digit * weights[weight_index % len(weights)]
            temp_num //= 10  # Remove the rightmost digit
            weight_index += 1
        return current_sum

    current_n = n
    # Initialize previous_n with a value that ensures the loop runs at least once
    previous_n = -1 

    # Keep calculating until the sum becomes stationary
    while current_n != previous_n:
        previous_n = current_n
        current_n = _calculate_next_sum(current_n, WEIGHTS)

    return current_n
```