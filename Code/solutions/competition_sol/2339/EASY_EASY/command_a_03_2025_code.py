```python
def solve(n: int, a: str, b: str) -> list[int]:
    """
    Transforms binary string `a` into `b` using prefix operations.

    Args:
        n (int): Length of the binary strings.
        a (str): The initial binary string.
        b (str): The target binary string.

    Returns:
        list[int]: A list containing the number of operations followed by the lengths of prefixes to flip.
    """
    operations: list[int] = []

    # Iterate from the end to the start to minimize operations
    for i in range(n - 1, -1, -1):
        if a[i] != b[i]:
            # If the current bit doesn't match, flip the entire prefix up to this point
            operations.append(i + 1)
            a = a[: i + 1][::-1].translate(
                str.maketrans("01", "10")
            ) + a[i + 1 :]  # Flip and reverse the prefix
            if i > 0:
                # Flip the first bit to correct any mismatch caused by the previous operation
                operations.append(1)
                a = "1" + a[1:] if a[0] == "0" else "0" + a[1:]

    return [len(operations)] + operations


def main() -> list[list[int]]:
    """
    Handles multiple test cases and processes each one using the solve function.

    Returns:
        list[list[int]]: A list of results for each test case.
    """
    import sys

    input = sys.stdin.read
    data: list[str] = input().split()
    idx: int = 0
    t: int = int(data[idx])  # Number of test cases
    idx += 1
    results: list[list[int]] = []
    for _ in range(t):
        n: int = int(data[idx])  # Length of binary strings
        idx += 1
        a: str = data[idx]  # Initial binary string
        idx += 1
        b: str = data[idx]  # Target binary string
        idx += 1
        result: list[int] = solve(n, a, b)
        results.append(result)
    return results


# Example usage:
# results = main()
# for result in results:
#     print(*result)
```