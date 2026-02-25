```python
def findLongest(s: str) -> int:
    """
    Finds the length of the longest substring with balanced parentheses.

    Args:
        s (str): The input string containing parentheses.

    Returns:
        int: The length of the longest substring with balanced parentheses.
    """
    stack = [-1]  # Initialize stack with -1 to handle edge cases
    max_length = 0  # Tracks the maximum length of valid substring

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)  # Push the index of '(' onto the stack
        else:
            stack.pop()  # Pop the last '(' index when ')' is encountered
            if not stack:  # If stack is empty after pop, push current index
                stack.append(i)
            else:
                # Calculate the length of the current valid substring
                current_length = i - stack[-1]
                # Update max_length if current_length is greater
                max_length = max(max_length, current_length)

    return max_length
```