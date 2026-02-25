```python
def is_strict_superset(A, other_sets):
    return all(A > set for set in other_sets)
```