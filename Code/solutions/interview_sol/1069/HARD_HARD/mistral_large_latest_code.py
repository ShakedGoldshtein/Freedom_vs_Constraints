```python
def solve_addition(test_cases):
    """
    Solves the addition problem for multiple test cases.

    Args:
        test_cases: A list of tuples, where each tuple contains two integers (A, B).

    Returns:
        A list of integers representing the sum of A and B for each test case.
    """
    return [a + b for a, b in test_cases]
```