```python
def minimum_change(n, leaf_values):
    if n == 1:
        return 0
    sum_leaves = sum(leaf_values)
    avg = sum_leaves // (n // 2)
    diff = abs(sum_leaves - avg * (n // 2))
    if (diff % 2 == 1):
        diff += 1
    return diff // 2

# Here's an example of how to call this function:
# print(minimum_change(30, [29, 33, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]))
```