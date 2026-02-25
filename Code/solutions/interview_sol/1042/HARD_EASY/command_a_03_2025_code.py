```python
import math

def gcd(a: int, b: int) -> int:
    """Compute the greatest common divisor of a and b."""
    while b:
        a, b = b, a % b
    return a

def count_good_pairs(n: int, p: int) -> int:
    """Count the number of good pairs (a, b) where 1 <= a < b <= n and GCD(a*b, p) == 1."""
    count = 0
    for a in range(1, n + 1):
        if gcd(a, p) == 1:  # a must be coprime with p
            for b in range(a + 1, n + 1):
                if gcd(b, p) == 1 and gcd(a * b, p) == 1:
                    count += 1
    return count

def solve(test_cases: list[tuple[int, int]]) -> list[int]:
    """Solve the problem for multiple test cases.
    
    Args:
        test_cases: A list of tuples, where each tuple contains (N, P).
    
    Returns:
        A list of integers representing the number of good pairs for each test case.
    """
    results = []
    for n, p in test_cases:
        results.append(count_good_pairs(n, p))
    return results
```