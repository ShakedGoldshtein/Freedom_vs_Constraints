```python
def count_good_substrings(s: str) -> int:
    """
    Counts the number of good substrings in a binary string.

    A substring is good if its length equals the decimal representation of the substring itself.

    Args:
        s (str): A binary string consisting of '0's and '1's.

    Returns:
        int: The number of good substrings in the input string.
    """
    count = 0
    n = len(s)
    for i in range(n):
        num = 0
        for j in range(i, min(i + 20, n)):  # Limit to 20 to avoid overflow
            num = num * 2 + int(s[j])
            if num == j - i + 1:
                count += 1
    return count


def solve(queries: list[str]) -> list[int]:
    """
    Solves multiple queries for counting good substrings in binary strings.

    Args:
        queries (list[str]): A list of binary strings, each representing a query.

    Returns:
        list[int]: A list of integers, where each integer is the count of good substrings for the corresponding query.
    """
    return [count_good_substrings(s) for s in queries]
```