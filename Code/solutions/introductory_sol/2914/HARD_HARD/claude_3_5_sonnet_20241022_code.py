```python
def array_diff(a: list, b: list) -> list:
    if not a:
        return []
    if not b:
        return a
        
    b_set = set(b)
    return [x for x in a if x not in b_set]
```