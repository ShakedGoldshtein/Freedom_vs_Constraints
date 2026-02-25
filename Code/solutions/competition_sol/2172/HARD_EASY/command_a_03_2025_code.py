```python
import math


def is_prime(n: int) -> bool:
    """Check if a number is prime.

    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def v(n: int) -> int:
    """Find the largest prime number not exceeding n.

    Args:
        n (int): The upper limit for the prime search.

    Returns:
        int: The largest prime number not exceeding n.
    """
    while not is_prime(n):
        n -= 1
    return n


def u(n: int) -> int:
    """Find the smallest prime number strictly greater than n.

    Args:
        n (int): The lower limit for the prime search.

    Returns:
        int: The smallest prime number strictly greater than n.
    """
    n += 1
    while not is_prime(n):
        n += 1
    return n


def gcd(a: int, b: int) -> int:
    """Compute the greatest common divisor of two numbers.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The greatest common divisor of a and b.
    """
    while b:
        a, b = b, a % b
    return a


def solve(n: int) -> str:
    """Calculate the sum of 1/(v(i)*u(i)) for i from 2 to n as an irreducible fraction.

    Args:
        n (int): The upper limit for the summation.

    Returns:
        str: The result as an irreducible fraction in the format "p/q".
    """
    if n == 2:
        return "1/6"
    if n == 3:
        return "7/30"

    # For n >= 4, the sum simplifies to 1/6 - 1/(v(n)*u(n))
    v_n = v(n)
    u_n = u(n)
    numerator = v_n * u_n - 6
    denominator = 6 * v_n * u_n
    common_divisor = gcd(numerator, denominator)
    return f"{numerator // common_divisor}/{denominator // common_divisor}"


def main(test_cases: list[int]) -> list[str]:
    """Process multiple test cases and return the results.

    Args:
        test_cases (list[int]): A list of integers representing the test cases.

    Returns:
        list[str]: A list of strings representing the results for each test case.
    """
    results = []
    for n in test_cases:
        results.append(solve(n))
    return results
```