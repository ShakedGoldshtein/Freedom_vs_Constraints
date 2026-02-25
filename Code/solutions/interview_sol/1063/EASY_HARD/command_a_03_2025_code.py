```python
def solve(test_cases: list[tuple[int, int]]) -> list[int]:
    """
    Calculate the remainder when A is divided by B for each test case.

    Args:
        test_cases (list of tuples): A list of tuples where each tuple contains two integers (A, B).

    Returns:
        list of int: A list of remainders corresponding to each test case.
    """
    results = []
    for A, B in test_cases:
        results.append(A % B)
    return results
```