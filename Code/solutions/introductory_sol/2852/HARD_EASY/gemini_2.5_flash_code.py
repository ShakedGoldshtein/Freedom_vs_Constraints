```python
import collections

def find_longest(s: str) -> int:
    """
    Finds the length of the longest valid (well-formed and balanced) parentheses substring.

    This function uses a stack-based approach to achieve optimal O(N) time complexity
    and O(N) space complexity, where N is the length of the input string.
    The stack stores indices of opening parentheses or boundary markers.

    Args:
        s: The input string containing parentheses '(' and ')'.

    Returns:
        The length of the longest valid parentheses substring. Returns 0 if no such
        substring is found or the input string is empty.
    """
    max_length = 0
    # The stack stores indices. We initialize it with -1.
    # This -1 acts as a base marker for the start of the string
    # or the position of the last unmatched closing parenthesis.
    # For example, in "()", when the ')' at index 1 is encountered,
    # the length is 1 - stack.top() = 1 - (-1) = 2.
    stack = collections.deque([-1])

    for i, char in enumerate(s):
        if char == '(':
            # Push the index of an opening parenthesis onto the stack.
            stack.append(i)
        elif char == ')':
            # When a closing parenthesis is encountered, pop from the stack.
            stack.pop()

            if not stack:
                # If the stack becomes empty after popping, it means the popped
                # element was the last unmatched opening parenthesis or the base marker.
                # In this case, the current ')' is unmatched.
                # Push the current index onto the stack to serve as the new base marker
                # for any subsequent valid parentheses substrings.
                stack.append(i)
            else:
                # If the stack is not empty, it means the current ')' has a matching
                # opening parenthesis (or a base marker) at stack.top().
                # The length of the current valid substring is the difference
                # between the current index and the index at the top of the stack.
                max_length = max(max_length, i - stack[-1])
    
    return max_length
```