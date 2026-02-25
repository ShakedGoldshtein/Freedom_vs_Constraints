```python
def findLongest(s):
    max_len = 0
    left = right = 0
    stack = [-1]

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                left = i + 1
            else:
                current_len = i - stack[-1]
                if current_len > max_len:
                    max_len = current_len

    return max_len
```