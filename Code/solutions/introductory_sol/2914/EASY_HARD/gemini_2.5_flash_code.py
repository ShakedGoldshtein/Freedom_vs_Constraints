```python
def array_diff(a, b):
    b_set = set(b)
    return [item for item in a if item not in b_set]
```