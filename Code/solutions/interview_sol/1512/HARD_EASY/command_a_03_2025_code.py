```python
def solve(T: int, test_cases: list[tuple[int, int]]) -> list[str]:
    """
    Determines the winner of the game for each test case.

    Args:
        T (int): Number of test cases.
        test_cases (list of tuples): Each tuple contains two integers (N, M) representing the board dimensions.

    Returns:
        list of str: A list of strings indicating the winner ("Tuzik" or "Vanya") for each test case.
    """
    results = []
    for N, M in test_cases:
        # The game outcome depends on the parity of the sum of (N-1) and (M-1).
        # If the sum is odd, Tuzik wins; if even, Vanya wins.
        if (N - 1 + M - 1) % 2 == 1:
            results.append("Tuzik")
        else:
            results.append("Vanya")
    return results


def main(T: int, test_cases: list[tuple[int, int]]) -> list[str]:
    """
    Main function to handle input and output.

    Args:
        T (int): Number of test cases.
        test_cases (list of tuples): Each tuple contains two integers (N, M) representing the board dimensions.

    Returns:
        list of str: A list of strings indicating the winner for each test case.
    """
    return solve(T, test_cases)
```