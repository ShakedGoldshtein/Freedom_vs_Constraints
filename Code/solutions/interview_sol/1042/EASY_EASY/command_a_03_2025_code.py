```python
import math


def gcd(a: int, b: int) -> int:
    """Compute the greatest common divisor of a and b."""
    while b:
        a, b = b, a % b
    return a


def count_good_pairs(N: int, P: int) -> int:
    """Count the number of good pairs (a, b) where 1 <= a < b <= N and GCD(a*b, P) == 1."""
    count = 0
    for a in range(1, N + 1):
        if gcd(a, P) == 1:  # Check if a is coprime with P
            for b in range(a + 1, N + 1):
                if gcd(b, P) == 1:  # Check if b is coprime with P
                    if gcd(a * b, P) == 1:  # Check if the pair (a, b) is a good pair
                        count += 1
    return count


def solve(test_cases: list[tuple[int, int]]) -> list[int]:
    """Solve the problem for multiple test cases."""
    results = []
    for N, P in test_cases:
        results.append(count_good_pairs(N, P))
    return results
```