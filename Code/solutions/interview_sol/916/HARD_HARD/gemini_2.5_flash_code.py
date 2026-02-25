```python
def _gcd(a: int, b: int) -> int:
    """
    Calculates the greatest common divisor (GCD) of two non-negative integers
    using the Euclidean algorithm.

    Args:
        a: The first non-negative integer.
        b: The second non-negative integer.

    Returns:
        The greatest common divisor of a and b.
    """
    while b:
        a, b = b, a % b
    return a

def find_minimum_cake_price(n: int, m: int) -> int:
    """
    Calculates the minimum amount to be spent by Chef and Chefu to purchase
    cakes of equal price.

    Chef has coins of denomination N, and Chefu has coins of denomination M.
    They both need to pay for cakes of the same price, meaning the price
    must be a multiple of both N and M. The minimum such price is the
    Least Common Multiple (LCM) of N and M.

    Optimal Time Complexity: O(log(min(N, M))) due to GCD calculation.
    Optimal Space Complexity: O(1).

    Args:
        n: The denomination of coins Chef has (N >= 2).
        m: The denomination of coins Chefu has (M >= 2).

    Returns:
        The minimum amount to be spent (LCM of N and M).
    """
    # The Least Common Multiple (LCM) of two numbers 'n' and 'm' is given by
    # the formula: LCM(n, m) = (n * m) / GCD(n, m).
    # To prevent potential intermediate overflow if 'n * m' exceeds the maximum
    # integer size in some languages (though Python handles large integers automatically),
    # it's generally safer and computationally equivalent to calculate it as:
    # LCM(n, m) = (n // GCD(n, m)) * m.
    # This ensures that the division happens first, resulting in a smaller intermediate number
    # before multiplication, which is guaranteed to be an integer.
    
    common_divisor = _gcd(n, m)
    
    # Since N and M are guaranteed to be >= 2, common_divisor will always be >= 1,
    # preventing division by zero.
    return (n // common_divisor) * m
```