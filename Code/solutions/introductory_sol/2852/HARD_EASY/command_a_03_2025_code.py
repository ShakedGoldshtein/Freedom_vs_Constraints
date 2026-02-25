```python
def findLongest(s: str) -> int:
    """
    Find the length of the longest substring with balanced parentheses.

    Args:
        s (str): Input string containing parentheses.

    Returns:
        int: Length of the longest substring with balanced parentheses.
    """
    stack = [-1]  # Initialize stack with -1 to handle edge cases
    max_length = 0

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)  # Push index of '(' onto stack
        else:
            stack.pop()  # Pop the last '(' index
            if not stack:  # If stack is empty after pop, push current index
                stack.append(i)
            else:
                # Calculate the length of the current valid substring
                current_length = i - stack[-1]
                max_length = max(max_length, current_length)

    return max_length
```