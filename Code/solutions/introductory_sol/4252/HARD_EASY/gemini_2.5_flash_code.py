```python
def merge_sorted_arrays_unique(arr1: list[int], arr2: list[int]) -> list[int]:
    """
    Merges two sorted arrays of integers into a single sorted array without duplicates.

    This function uses a two-pointer approach to achieve optimal time complexity.
    It iterates through both arrays simultaneously, adding elements to the result
    array while maintaining sorted order and ensuring no duplicates are included.

    Args:
        arr1: The first sorted list of integers.
        arr2: The second sorted list of integers.

    Returns:
        A new list containing all unique elements from both input arrays,
        sorted in ascending order.
    """
    merged_arr: list[int] = []
    i, j = 0, 0
    n, m = len(arr1), len(arr2)

    while i < n and j < m:
        current_val: int

        if arr1[i] < arr2[j]:
            current_val = arr1[i]
            i += 1
        elif arr2[j] < arr1[i]:
            current_val = arr2[j]
            j += 1
        else:  # arr1[i] == arr2[j]
            current_val = arr1[i]
            i += 1
            j += 1

        # Add current_val to merged_arr if it's not a duplicate of the last element
        if not merged_arr or merged_arr[-1] != current_val:
            merged_arr.append(current_val)

    # Add any remaining elements from arr1, checking for duplicates
    while i < n:
        current_val = arr1[i]
        if not merged_arr or merged_arr[-1] != current_val:
            merged_arr.append(current_val)
        i += 1

    # Add any remaining elements from arr2, checking for duplicates
    while j < m:
        current_val = arr2[j]
        if not merged_arr or merged_arr[-1] != current_val:
            merged_arr.append(current_val)
        j += 1

    return merged_arr
```