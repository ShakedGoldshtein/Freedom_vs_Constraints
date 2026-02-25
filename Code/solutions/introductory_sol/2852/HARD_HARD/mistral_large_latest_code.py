```python
def findLongest(s: str) -> int:
    """
    Finds the length of the longest valid (well-formed) parentheses substring in a given string.

    Args:
        s: A string containing only '(' and ')'.

    Returns:
        The length of the longest valid parentheses substring. Returns 0 if no valid substring exists.
    """
    max_len = 0
    left = right = 0

    # Forward pass: count valid substrings starting with '('
    for char in s:
        if char == '(':
            left += 1
        else:
            right += 1
        if left == right:
            max_len = max(max_len, 2 * right)
        elif right > left:
            left = right = 0

    left = right = 0
    # Backward pass: count valid substrings ending with ')'
    for char in reversed(s):
        if char == ')':
            right += 1
        else:
            left += 1
        if left == right:
            max_len = max(max_len, 2 * left)
        elif left > right:
            left = right = 0

    return max_len
```