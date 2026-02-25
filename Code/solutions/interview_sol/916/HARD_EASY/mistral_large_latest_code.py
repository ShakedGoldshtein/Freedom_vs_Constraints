```python
import math

def solve_single_test_case(N, M):
    """
    Calculate the minimum amount to be spent by Chef and Chefu to purchase cakes of equal price,
    given their coin denominations N and M respectively.

    Args:
        N (int): Denomination of Chef's coins.
        M (int): Denomination of Chefu's coins.

    Returns:
        int: The minimum amount to be spent.
    """
    if N == M:
        return N
    gcd = math.gcd(N, M)
    return (N // gcd) * (M // gcd) * gcd

def solve(T, test_cases):
    """
    Solve multiple test cases for the cake purchase problem.

    Args:
        T (int): Number of test cases.
        test_cases (list of tuple): List of (N, M) pairs for each test case.

    Returns:
        list: List of results for each test case.
    """
    return [solve_single_test_case(N, M) for N, M in test_cases]
```