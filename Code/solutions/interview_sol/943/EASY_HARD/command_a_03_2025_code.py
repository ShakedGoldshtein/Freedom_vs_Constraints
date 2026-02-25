```python
def solve(T: int, test_cases: list[tuple[int, int]]) -> list[int]:
    """
    Calculate the number of ways Tejas can serve the Clash Team.

    Args:
        T (int): Number of test cases.
        test_cases (list of tuples): Each tuple contains two integers (V, W) representing the number of plates and servings of dish B.

    Returns:
        list of int: A list containing the number of ways for each test case.
    """
    results = []
    for V, W in test_cases:
        # If there are more servings of dish B than plates, the number of ways is V + 1
        if W >= V:
            results.append(V + 1)
        else:
            # Otherwise, the number of ways is W + 1
            results.append(W + 1)
    return results


# Example usage:
# T = 1
# test_cases = [(3, 3)]
# print(solve(T, test_cases))  # Output: [4]
```