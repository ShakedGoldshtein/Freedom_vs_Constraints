```python
def solve(n, a):
    if n == 1:
        return [-1]
    a_sorted = sorted(a)
    b = []
    left = 0
    right = n - 1
    for i in range(n):
        if i % 2 == 0:
            b.append(a_sorted[right])
            right -= 1
        else:
            b.append(a_sorted[left])
            left += 1
    return b
```