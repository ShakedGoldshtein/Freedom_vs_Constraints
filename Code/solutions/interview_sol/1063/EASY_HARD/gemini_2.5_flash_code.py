```python
def solve(test_cases):
    """
    Calculates the remainder for a list of (A, B) integer pairs.

    Args:
        test_cases: A list of tuples, where each tuple (A, B) represents
                    a test case. A is the dividend and B is the divisor.

    Returns:
        A list of integers, where each element is the remainder when A is
        divided by B for the corresponding test case.
    """
    results = []
    for A, B in test_cases:
        results.append(A % B)
    return results
```