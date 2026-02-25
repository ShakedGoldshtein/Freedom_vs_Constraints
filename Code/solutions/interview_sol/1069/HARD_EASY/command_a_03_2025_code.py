```python
def add_numbers(a: int, b: int) -> int:
    """
    Adds two integers together.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The sum of a and b.
    """
    return a + b


def solve(test_cases: list[tuple[int, int]]) -> list[int]:
    """
    Solves the problem of adding pairs of numbers for multiple test cases.

    Args:
        test_cases (list of tuples): A list where each tuple contains two integers (A, B) to be added.

    Returns:
        list of int: A list containing the sum of each pair of numbers from the test cases.
    """
    results = []
    for a, b in test_cases:
        results.append(add_numbers(a, b))
    return results
```