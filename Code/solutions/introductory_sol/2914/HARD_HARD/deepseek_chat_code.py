```python
def array_diff(a, b):
    """
    Remove all occurrences of elements in list b from list a.
    
    Args:
        a: List from which elements will be removed
        b: List containing elements to remove from a
    
    Returns:
        List containing elements from a that are not in b
    """
    if not a:
        return []
    
    if not b:
        return a[:]
    
    b_set = set(b)
    return [x for x in a if x not in b_set]
```