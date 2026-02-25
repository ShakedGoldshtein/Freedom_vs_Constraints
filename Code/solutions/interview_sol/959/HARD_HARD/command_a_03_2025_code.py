```python
def max_sum_after_permutation(test_cases: list[tuple[int, list[int]]]) -> list[int]:
    """
    Calculate the maximum sum achievable after permuting the array for each test case.

    Args:
        test_cases (list of tuples): Each tuple contains (N, A), where N is the number of elements
                                     and A is the list of integers.

    Returns:
        list of int: A list containing the maximum sum for each test case.
    """
    results = []
    for case in test_cases:
        N, A = case
        # Sort the array to easily pair the smallest with the largest
        A_sorted = sorted(A)
        total = 0
        # Pair the smallest with the largest to maximize the absolute difference
        for i in range(N // 2):
            total += abs(A_sorted[i] - A_sorted[N - 1 - i])
        results.append(total)
    return results


def solve(test_cases: list[tuple[int, list[int]]]) -> list[int]:
    """
    Wrapper function to call max_sum_after_permutation and return the results.

    Args:
        test_cases (list of tuples): Each tuple contains (N, A), where N is the number of elements
                                     and A is the list of integers.

    Returns:
        list of int: A list containing the maximum sum for each test case.
    """
    return max_sum_after_permutation(test_cases)
```