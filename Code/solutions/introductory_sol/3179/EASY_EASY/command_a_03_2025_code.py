```python
def min_and_max_sum_of_digits(l: int, d: int, x: int) -> list[int]:
    """
    Finds the minimal and maximal integers within the range [l, d] whose digits sum to x.

    Args:
        l (int): The lower bound of the range.
        d (int): The upper bound of the range.
        x (int): The target sum of digits.

    Returns:
        list[int]: A list containing two integers, the minimal and maximal numbers whose digits sum to x.
    """

    def sum_digits(n: int) -> int:
        """Helper function to calculate the sum of digits of a number."""
        return sum(int(digit) for digit in str(n))

    # Find the minimal number n such that l <= n <= d and sum of digits equals x
    n = next(num for num in range(l, d + 1) if sum_digits(num) == x)

    # Find the maximal number m such that l <= m <= d and sum of digits equals x
    m = next(num for num in range(d, l - 1, -1) if sum_digits(num) == x)

    return [n, m]
```