```python
import math


def solve(T: int, test_cases: list[tuple[int, int]]) -> list[int]:
    """
    Solves the problem of finding the minimum amount to be spent on cakes for Chef and Chefu.

    Args:
        T (int): Number of test cases.
        test_cases (list of tuples): List of tuples where each tuple contains two integers (N, M).

    Returns:
        list of int: List of results for each test case, where each result is the minimum amount to be spent.
    """
    results = []
    for N, M in test_cases:
        # Calculate the least common multiple (LCM) of N and M
        # LCM(a, b) = |a * b| / GCD(a, b)
        lcm = abs(N * M) // math.gcd(N, M)
        results.append(lcm)
    return results


# Example usage:
# test_cases = [(2, 3)]
# print(solve(1, test_cases))  # Output: [6]
```