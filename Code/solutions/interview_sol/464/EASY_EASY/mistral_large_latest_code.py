```python
def min_operations_to_equal(n):
    total_sum = n * n
    target = total_sum // n
    operations = 0
    for i in range(n):
        current = (2 * i) + 1
        if current > target:
            operations += current - target
    return operations
```