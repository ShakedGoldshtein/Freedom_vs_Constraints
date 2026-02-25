```python
def solve(T: int, test_cases: list[tuple[int, int, list[int]]]) -> list[int]:
    """
    Solves the problem of finding the number of beautiful subarrays for each test case.

    Args:
        T (int): The number of test cases.
        test_cases (list of tuples): Each tuple contains (N, K, A), where:
            - N (int): The length of the array A.
            - K (int): The integer K used in the problem.
            - A (list of int): The array of integers.

    Returns:
        list of int: A list containing the number of beautiful subarrays for each test case.
    """
    results = []
    for case in test_cases:
        N, K, A = case
        count = 0
        for l in range(N):
            freq = {}
            for r in range(l, N):
                # Count the frequency of each element in the current subarray
                freq[A[r]] = freq.get(A[r], 0) + 1
                subarray = A[l : r + 1]
                m = (K + len(subarray) - 1) // len(subarray)
                B = subarray * m
                B_sorted = sorted(B)
                X = B_sorted[K - 1]
                F = freq[X]
                # Check if F occurs in the subarray
                if any(x == F for x in subarray):
                    count += 1
        results.append(count)
    return results


# Example usage:
# T = 1
# test_cases = [(3, 3, [1, 2, 3])]
# print(solve(T, test_cases))
```