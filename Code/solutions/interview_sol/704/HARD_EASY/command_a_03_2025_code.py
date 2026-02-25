```python
def solve(A: int, N: int, M: int) -> int:
    """
    Calculate the value of X modulo M, where X is the number formed by appending A to itself N times.

    Args:
        A (int): The number to be appended.
        N (int): The number of times A is appended.
        M (int): The modulo value.

    Returns:
        int: The value of X modulo M.
    """
    if A == 0:
        return 0

    # Convert A to a string to easily calculate its length
    s = str(A)
    length = len(s)

    # Calculate the modulo of 10^length with M
    # This is equivalent to the modulo of the number formed by appending A once
    mod = pow(10, length, M)

    # Calculate the geometric series sum using the formula for the sum of a geometric series
    # The sum is (mod^N - 1) / (mod - 1), but we need to handle the case where mod == 1 separately
    if mod == 1:
        # If mod == 1, then mod^N - 1 == 0, so the sum is N
        total = N
    else:
        # Otherwise, calculate the sum using the geometric series formula
        total = (pow(mod, N, M - 1) - 1) * pow(mod - 1, M - 2, M - 1) % (M - 1)

    # Calculate the final result by multiplying the sum with A and taking modulo M
    return (total * A) % M


def main(test_cases: list[tuple[int, int, int]]) -> list[int]:
    """
    Process multiple test cases and return the results.

    Args:
        test_cases (list of tuples): Each tuple contains (A, N, M) for a test case.

    Returns:
        list of int: The results for each test case.
    """
    results = []
    for A, N, M in test_cases:
        results.append(solve(A, N, M))
    return results
```