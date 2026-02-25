```python
def findLongest(s):
    stack = [-1]
    longest = 0
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if len(stack) != 0:
                longest = max(longest, i - stack[-1])
            else:
                stack.append(i)
    return longest
```