```python
def solve(test_cases: list[tuple[int, int]]) -> list[int]:
    """
    Solves the problem of adding pairs of integers for multiple test cases.

    Args:
        test_cases (list of tuples): A list where each tuple contains two integers (A, B) to be added.

    Returns:
        list: A list of sums corresponding to each test case.
    """
    return [a + b for a, b in test_cases]
```