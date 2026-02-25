```python
def array_diff(a: list, b: list) -> list:
    """
    Subtracts list `b` from list `a` and returns the result.

    Removes all values from list `a` that are present in list `b`.
    If a value is present in `b`, all of its occurrences are removed from `a`.

    Args:
        a (list): The original list from which elements will be removed.
        b (list): The list containing elements to be removed from `a`.

    Returns:
        list: A new list with elements from `a` that are not in `b`.
    """
    # Convert list `b` to a set for O(1) lookups
    b_set = set(b)
    
    # Use list comprehension to filter out elements in `a` that are in `b_set`
    # This ensures all occurrences of elements in `b` are removed
    return [x for x in a if x not in b_set]
```