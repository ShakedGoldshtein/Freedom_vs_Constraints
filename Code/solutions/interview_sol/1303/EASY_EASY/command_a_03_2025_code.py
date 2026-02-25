```python
MOD = 10**9 + 7


def solve(T: int, test_cases: list[tuple[int, int, int, list[int]]]) -> list[int]:
    """
    Solves the problem of finding the number of valid subsequences of length K in an array A,
    where each element in the subsequence satisfies the condition S_i % M == i % M.

    Args:
        T (int): Number of test cases.
        test_cases (list): List of tuples, each containing (N, K, M, A), where:
            - N (int): Length of the array A.
            - K (int): Length of the subsequence.
            - M (int): Modulus value.
            - A (list): List of integers representing the array.

    Returns:
        list: A list of integers representing the number of valid subsequences for each test case, modulo 10^9 + 7.
    """
    results = []
    for case in test_cases:
        N, K, M, A = case
        # Initialize a dictionary to store the count of elements that satisfy S_i % M == i % M
        dp = {i % M: 0 for i in range(1, K + 1)}
        for a in A:
            a_mod = a % M
            # Update the counts for each position in the subsequence
            for i in range(K, 0, -1):
                if (i - 1) % M == a_mod:
                    if i == 1:
                        dp[a_mod] = (dp[a_mod] + 1) % MOD
                    else:
                        dp[a_mod] = (dp[a_mod] + dp[(i - 2) % M]) % MOD
        results.append(dp[(K - 1) % M])
    return results


# Example usage:
# T = 1
# test_cases = [(12, 4, 3, [4, 5, 6, 7, 1, 4, 6, 9, 0, 0, 10, 2])]
# print(solve(T, test_cases))
```