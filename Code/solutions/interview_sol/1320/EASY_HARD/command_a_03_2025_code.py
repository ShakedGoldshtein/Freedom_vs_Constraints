```python
def solve(T: int, test_cases: list[int]) -> list[str]:
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
        # If the number of marbles is a multiple of 3, player B loses
        if N % 3 == 0:
            results.append("B")
        # Otherwise, player A loses
        else:
            results.append("A")
    return results
```