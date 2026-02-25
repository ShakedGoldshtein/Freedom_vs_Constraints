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
    # Initialize pointers for both arrays and the result array
    i, j = 0, 0
    result = []

    # Merge smaller elements first, ensuring no duplicates
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1
        elif arr2[j] < arr1[i]:
            if not result or result[-1] != arr2[j]:
                result.append(arr2[j])
            j += 1
        else:
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1
            j += 1

    # Append remaining elements from arr1, if any
    while i < len(arr1):
        if not result or result[-1] != arr1[i]:
            result.append(arr1[i])
        i += 1

    # Append remaining elements from arr2, if any
    while j < len(arr2):
        if not result or result[-1] != arr2[j]:
            result.append(arr2[j])
        j += 1

    return result
```