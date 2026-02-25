```python
def merge_sorted_arrays(arr1, arr2):
    """
    Merge two sorted integer arrays into a single sorted array without duplicates.
    
    Args:
        arr1: First sorted list of integers
        arr2: Second sorted list of integers
    
    Returns:
        List: Merged sorted list without duplicates
    """
    if not arr1 and not arr2:
        return []
    
    if not arr1:
        return remove_duplicates(arr2)
    
    if not arr2:
        return remove_duplicates(arr1)
    
    merged = []
    i, j = 0, 0
    len1, len2 = len(arr1), len(arr2)
    
    while i < len1 and j < len2:
        if arr1[i] < arr2[j]:
            append_if_unique(merged, arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            append_if_unique(merged, arr2[j])
            j += 1
        else:
            append_if_unique(merged, arr1[i])
            i += 1
            j += 1
    
    while i < len1:
        append_if_unique(merged, arr1[i])
        i += 1
    
    while j < len2:
        append_if_unique(merged, arr2[j])
        j += 1
    
    return merged

def append_if_unique(arr, value):
    """
    Append value to array if it's not equal to the last element.
    
    Args:
        arr: List to append to
        value: Value to append if unique
    """
    if not arr or arr[-1] != value:
        arr.append(value)

def remove_duplicates(arr):
    """
    Remove duplicates from a sorted array.
    
    Args:
        arr: Sorted list of integers
    
    Returns:
        List: Array without duplicates
    """
    if not arr:
        return []
    
    result = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != result[-1]:
            result.append(arr[i])
    return result
```