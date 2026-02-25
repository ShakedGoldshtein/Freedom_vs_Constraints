```python
def min_and_max(l: int, d: int, x: int) -> list[int]:
    """
    Find the minimal and maximal integers within a range [l, d] whose digits sum to x.

    Args:
        l (int): The lower bound of the range (inclusive).
        d (int): The upper bound of the range (inclusive).
        x (int): The target sum of digits.

    Returns:
        list[int]: A list containing two integers: the minimal integer n and the maximal integer m.
    """

    def sum_digits(n: int) -> int:
        """
        Calculate the sum of digits of a given integer.

        Args:
            n (int): The integer whose digits are to be summed.

        Returns:
            int: The sum of the digits of n.
        """
        return sum(int(digit) for digit in str(n))

    # Find the minimal integer n in [l, d] with digit sum x
    n = next(i for i in range(l, d + 1) if sum_digits(i) == x)

    # Find the maximal integer m in [l, d] with digit sum x
    m = next(i for i in range(d, l - 1, -1) if sum_digits(i) == x)

    return [n, m]
```