```python
def array_diff(a: list, b: list) -> list:
    """
    Subtracts one list from another, removing all values from list 'a'
    that are present in list 'b'.

    If a value is present in 'b', all of its occurrences are removed from 'a'.

    This implementation achieves optimal time complexity of O(N + M) and
    optimal space complexity of O(M) where N is the length of list 'a' and
    M is the length of list 'b'. The time complexity comes from converting
    list 'b' to a set (O(M)) and then iterating through list 'a' (O(N)) with
    O(1) average time complexity lookups in the set. The space complexity
    comes from storing the set of elements from 'b' and the resulting list.

    Args:
        a: The list from which elements will be removed.
        b: The list containing values to be removed from 'a'.

    Returns:
        A new list containing elements from 'a' that are not in 'b'.

    Raises:
        ValueError: If elements in list 'b' are not hashable (e.g., lists, dicts),
                    which prevents the creation of a set for efficient lookups.

    Examples:
        >>> array_diff([1, 2], [1])
        [2]
        >>> array_diff([1, 2, 2, 2, 3], [2])
        [1, 3]
        >>> array_diff([], [1, 2])
        []
        >>> array_diff([1, 2, 3], [])
        [1, 2, 3]
        >>> array_diff([1, 2, 3], [4, 5])
        [1, 2, 3]
        >>> array_diff([1, 2, 3], [1, 2, 3])
        []
        >>> array_diff([1, [2]], [[2]]) # Example for unhashable elements in b
        Traceback (most recent call last):
            ...
        ValueError: Elements in list 'b' must be hashable.
    """
    # Edge case: If 'a' is empty, no elements can be kept.
    # The list comprehension below would also correctly produce an empty list.
    if not a:
        return []

    # Edge case: If 'b' is empty, no elements are to be removed from 'a'.
    # Return a shallow copy of 'a' to prevent unexpected side effects if
    # the original 'a' list were to be modified by the caller later.
    if not b:
        return list(a)

    # Convert list 'b' to a set for O(1) average time complexity lookups.
    # This is the critical step for achieving optimal performance.
    try:
        b_set = set(b)
    except TypeError as e:
        # Handle cases where elements in 'b' might be unhashable (e.g., lists, dicts).
        # The problem implies simple integer lists, but a generic list can contain anything.
        raise ValueError("Elements in list 'b' must be hashable for efficient difference calculation.") from e

    # Use a list comprehension to build the result list. This is concise, readable,
    # and often performs better than a manual loop with appends.
    # Iterate through 'a' and include an item only if it's not present in 'b_set'.
    result = [item for item in a if item not in b_set]

    return result
```