```python
def merge_sorted_arrays(arr1: list[int], arr2: list[int]) -> list[int]:
    """
    Merges two sorted arrays into a single sorted array without duplicates.

    Args:
        arr1 (list[int]): The first sorted array of integers.
        arr2 (list[int]): The second sorted array of integers.

    Returns:
        list[int]: A new sorted array containing all unique elements from both input arrays.
    """
    # Combine the two arrays into one
    combined = arr1 + arr2
    
    # Use a set to remove duplicates and convert back to a list
    unique_elements = list(set(combined))
    
    # Sort the list of unique elements
    unique_elements.sort()
    
    return unique_elements
```