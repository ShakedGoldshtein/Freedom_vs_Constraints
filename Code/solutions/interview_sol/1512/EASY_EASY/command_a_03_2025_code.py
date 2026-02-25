```python
def solve(T: int, test_cases: list[tuple[int, int]]) -> list[str]:
    """
    Determines the winner of the game for each test case.

    Args:
        T (int): Number of test cases.
        test_cases (list of tuples): Each tuple contains two integers (N, M) representing the board dimensions.

    Returns:
        list of str: A list of strings, each being either "Tuzik" or "Vanya", indicating the winner for each test case.
    """
    results = []
    for N, M in test_cases:
        # The game outcome depends on whether the sum of (N-1) and (M-1) is divisible by 4.
        # If the sum is divisible by 4, Vanya wins; otherwise, Tuzik wins.
        if (N + M - 2) % 4 == 0:
            results.append("Vanya")
        else:
            results.append("Tuzik")
    return results


# Example usage:
# T = 2
# test_cases = [(4, 4), (2, 2)]
# print(solve(T, test_cases))
```