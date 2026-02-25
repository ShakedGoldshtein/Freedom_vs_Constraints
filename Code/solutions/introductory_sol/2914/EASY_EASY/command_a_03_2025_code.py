```python
def array_diff(a: list[int], b: list[int]) -> list[int]:
    """
    Subtracts list b from list a, removing all elements in a that are present in b.

    Args:
        a (list): The original list from which elements will be removed.
        b (list): The list containing elements to be removed from list a.

    Returns:
        list: A new list with elements from a that are not present in b.
    """
    # Use list comprehension to filter out elements in a that are not in b
    return [x for x in a if x not in b]
```