```python
def array_diff(a, b):
    """
    This function subtracts one list from another and returns the result.
    It removes all values from list `a`, which are present in list `b`.
    If a value is present in `b`, all of its occurrences are removed from `a`.
    """
    return [x for x in a if x not in b]
```