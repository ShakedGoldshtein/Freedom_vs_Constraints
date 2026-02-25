```python
def merge_sorted_unique(arr1, arr2):
    """
    Merges two sorted arrays of integers into a single sorted array without duplicates.

    Args:
        arr1 (list): The first sorted list of integers.
        arr2 (list): The second sorted list of integers.

    Returns:
        list: A new sorted list containing unique integers from both input arrays.
    """
    merged_list = []
    i, j = 0, 0
    n1, n2 = len(arr1), len(arr2)

    # Helper to add an element to merged_list if it's not a duplicate of the last element
    def append_unique(value):
        if not merged_list or merged_list[-1] != value:
            merged_list.append(value)

    # Traverse both arrays
    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            append_unique(arr1[i])
            i += 1
        elif arr2[j] < arr1[i]:
            append_unique(arr2[j])
            j += 1
        else:  # arr1[i] == arr2[j]
            append_unique(arr1[i])  # Add either, as they are equal
            i += 1
            j += 1

    # Add remaining elements from arr1 (if any)
    while i < n1:
        append_unique(arr1[i])
        i += 1

    # Add remaining elements from arr2 (if any)
    while j < n2:
        append_unique(arr2[j])
        j += 1

    return merged_list
```