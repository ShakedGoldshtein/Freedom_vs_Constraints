```python
def solve(n, k):
    result = [0] * n
    left, right = 1, n
    for i in range(k):
        if i % 2 == 0:
            result[i] = left
            left += 1
        else:
            result[i] = right
            right -= 1
    if k % 2 == 1:
        for i in range(k, n):
            result[i] = left
            left += 1
    else:
        for i in range(k, n):
            result[i] = right
            right -= 1
    return result
```