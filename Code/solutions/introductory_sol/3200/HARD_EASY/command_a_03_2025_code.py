```python
def thirt(n: int) -> int:
    """
    Calculate the stationary number using the Thirt algorithm.

    The Thirt algorithm processes a number by repeatedly applying a specific
    sequence of operations until the result becomes stationary.

    Args:
        n (int): The input number (>= 0).

    Returns:
        int: The stationary number after applying the Thirt algorithm.
    """
    # Sequence of remainders when dividing successive powers of 10 by 13
    remainders = [1, 10, 9, 12, 3, 4]

    def calculate_sum(num: int) -> int:
        """
        Calculate the sum of products of digits and corresponding remainders.

        Args:
            num (int): The number to process.

        Returns:
            int: The sum of products of digits and remainders.
        """
        digits = list(map(int, str(num)))
        sequence_length = len(remainders)
        total = 0
        for i, digit in enumerate(reversed(digits)):
            total += digit * remainders[i % sequence_length]
        return total

    # Repeatedly apply the calculation until the result is stationary
    while True:
        new_n = calculate_sum(n)
        if new_n == n:
            return n
        n = new_n
```