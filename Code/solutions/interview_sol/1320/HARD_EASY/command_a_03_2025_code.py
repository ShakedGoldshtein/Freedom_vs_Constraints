```python
def determine_loser(T: int, test_cases: list[int]) -> list[str]:
    """
    Determines the loser of the marble game for each test case.

    Args:
        T (int): Number of test cases.
        test_cases (list[int]): List of integers representing the number of marbles for each test case.

    Returns:
        list[str]: List of strings indicating the loser ('A' or 'B') for each test case.
    """
    results = []
    for N in test_cases:
        # If the number of marbles is odd, player B loses; otherwise, player A loses.
        if N % 2 == 1:
            results.append("B")
        else:
            results.append("A")
    return results


def solve(T: int, test_cases: list[int]) -> list[str]:
    """
    Solves the marble game problem for multiple test cases.

    Args:
        T (int): Number of test cases.
        test_cases (list[int]): List of integers representing the number of marbles for each test case.

    Returns:
        list[str]: List of strings indicating the loser ('A' or 'B') for each test case.
    """
    return determine_loser(T, test_cases)
```