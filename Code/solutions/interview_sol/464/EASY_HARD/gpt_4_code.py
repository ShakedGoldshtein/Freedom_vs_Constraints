```python
def min_operations(n):
    middle_number = n // 2
    return middle_number * middle_number if n % 2 == 0 else middle_number * (middle_number + 1)
```