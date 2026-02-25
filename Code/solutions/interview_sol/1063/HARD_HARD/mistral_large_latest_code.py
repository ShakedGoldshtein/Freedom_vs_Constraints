```python
def compute_remainders(test_cases):
    """
    Compute the remainder of A divided by B for each test case.

    Args:
        test_cases: A list of tuples, where each tuple contains two integers (A, B).

    Returns:
        A list of integers representing the remainders of A % B for each test case.

    Raises:
        ValueError: If B is zero for any test case (division by zero).
    """
    results = []
    for a, b in test_cases:
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        results.append(a % b)
    return results
```