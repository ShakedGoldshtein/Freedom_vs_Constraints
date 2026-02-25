```python
def solve(s: str) -> int:
    """
    Calculate the number of good substrings in a binary string.

    A substring is good if its length equals the decimal representation of the substring itself.

    Args:
        s (str): A binary string consisting of '0's and '1's.

    Returns:
        int: The number of good substrings in the string.
    """
    n = len(s)
    count = 0

    # Iterate over each character in the string
    for i in range(n):
        num = 0
        # Build the binary number starting from the current position
        for j in range(i, min(n, i + 20)):  # Limit to 20 to avoid large numbers
            num = num * 2 + int(s[j])
            length = j - i + 1
            # Check if the length of the substring equals the decimal value
            if length == num:
                count += 1
            # If the number exceeds the length, break to avoid unnecessary checks
            if num > n:
                break

    return count


def main(queries: list[str]) -> list[int]:
    """
    Process multiple queries and return the count of good substrings for each query.

    Args:
        queries (list[str]): A list of binary strings, each representing a query.

    Returns:
        list[int]: A list of integers representing the count of good substrings for each query.
    """
    return [solve(s) for s in queries]
```