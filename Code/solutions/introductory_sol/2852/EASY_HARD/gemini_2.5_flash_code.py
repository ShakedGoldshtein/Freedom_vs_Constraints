```python
def findLongest(s: str) -> int:
    """
    Finds the length of the longest valid (balanced) parenthesis substring.

    Args:
        s: The input string containing '(' and ')'.

    Returns:
        The length of the longest valid parenthesis substring.
        Returns 0 if no such substring is found.
    """
    max_len = 0
    # The stack stores the indices of opening parentheses.
    # We initialize it with -1 to handle cases where the first character is ')'
    # or to correctly calculate the length of a valid substring that starts at index 0.
    # If the stack becomes empty after popping a '(', it means a valid
    # sequence has just ended. The next character's index is pushed to serve
    # as a new 'base' for measuring subsequent valid sequences.
    stack = [-1] 

    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:  # s[i] == ')'
            if stack:
                stack.pop() # Try to match with the last '('
            
            if not stack:
                # If the stack is empty after popping (meaning the ')' matched
                # the last '(' which itself was matched with the stack's base or was the last '('.
                # Or if the stack was already empty before popping (unmatched ')' at current i).
                # Push the current index as a new base for the next potential valid substring.
                stack.append(i)
            else:
                # If the stack is not empty, it means the current ')' successfully
                # closed a parenthesis sequence. The length of this sequence is
                # the current index minus the index of the element at the top of the stack.
                # This top element is either an unmatched '(' or the base index.
                max_len = max(max_len, i - stack[-1])
                
    return max_len

```