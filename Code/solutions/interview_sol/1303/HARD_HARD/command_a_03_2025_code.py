```python
MOD = 10**9 + 7


def count_valid_subsequences(N: int, K: int, M: int, A: list[int]) -> int:
    """
    Counts the number of valid subsequences of length K in array A that satisfy the given property.

    Args:
        N (int): Length of the array A.
        K (int): Length of the subsequence.
        M (int): Modulus value for the property.
        A (list[int]): List of non-negative integers.

    Returns:
        int: Number of valid subsequences modulo 10^9 + 7.
    """
    # Initialize a dictionary to store the count of each remainder
    remainder_counts: dict[int, int] = {}
    for i in range(1, K + 1):
        remainder = i % M
        remainder_counts[remainder] = 0

    # Count the occurrences of each remainder in the array
    for num in A:
        remainder = num % M
        if remainder in remainder_counts:
            remainder_counts[remainder] += 1

    # Calculate the number of valid subsequences using dynamic programming
    dp: list[int] = [0] * (K + 1)
    dp[0] = 1  # Base case: empty subsequence
    for i in range(1, K + 1):
        remainder = i % M
        if remainder in remainder_counts and remainder_counts[remainder] > 0:
            dp[i] = dp[i - 1] * remainder_counts[remainder] % MOD
        else:
            dp[i] = 0

    return dp[K]


def solve(test_cases: list[tuple[int, int, int, list[int]]]) -> list[int]:
    """
    Solves the problem for multiple test cases.

    Args:
        test_cases (list[tuple[int, int, int, list[int]]]): List of tuples, each containing (N, K, M, A).

    Returns:
        list[int]: List of results for each test case.
    """
    results: list[int] = []
    for case in test_cases:
        N, K, M, A = case
        result = count_valid_subsequences(N, K, M, A)
        results.append(result)
    return results
```