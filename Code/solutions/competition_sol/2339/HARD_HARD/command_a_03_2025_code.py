```python
def solve(n: int, a: str, b: str) -> list[int]:
    """
    Transform binary string `a` into `b` using prefix operations.

    Args:
        n (int): Length of the binary strings.
        a (str): Initial binary string.
        b (str): Target binary string.

    Returns:
        list[int]: List of operations where each operation is the length of the prefix to flip.
    """
    operations: list[int] = []

    for i in range(n):
        if a[i] != b[i]:
            # If the current bit is different, flip the prefix of length i+1
            operations.append(i + 1)
            a = a[:i] + str(1 - int(a[i])) + a[i + 1 :]
            a = a[::-1]  # Reverse the entire string after flipping

    return operations


def main(test_cases: list[tuple[int, str, str]]) -> list[list[int]]:
    """
    Process multiple test cases and return the operations for each.

    Args:
        test_cases (list[tuple[int, str, str]]): List of tuples containing (n, a, b) for each test case.

    Returns:
        list[list[int]]: List of operations for each test case.
    """
    results: list[list[int]] = []
    for case in test_cases:
        n, a, b = case
        operations = solve(n, a, b)
        results.append([len(operations)] + operations)
    return results
```