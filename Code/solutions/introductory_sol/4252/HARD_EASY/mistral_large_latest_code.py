```python
from typing import List

def merge_sorted_arrays(arr1: List[int], arr2: List[int]) -> List[int]:
    """
    Merges two sorted arrays of integers into a single sorted array without duplicates.

    Args:
        arr1: First sorted array of integers.
        arr2: Second sorted array of integers.

    Returns:
        A new sorted array containing all unique elements from both input arrays.
    """
    def _merge_unique(a: List[int], b: List[int]) -> List[int]:
        merged = []
        i, j = 0, 0
        len_a, len_b = len(a), len(b)

        while i < len_a and j < len_b:
            if a[i] < b[j]:
                if not merged or merged[-1] != a[i]:
                    merged.append(a[i])
                i += 1
            elif a[i] > b[j]:
                if not merged or merged[-1] != b[j]:
                    merged.append(b[j])
                j += 1
            else:  # Equal elements
                if not merged or merged[-1] != a[i]:
                    merged.append(a[i])
                i += 1
                j += 1

        # Add remaining elements from arr1
        while i < len_a:
            if not merged or merged[-1] != a[i]:
                merged.append(a[i])
            i += 1

        # Add remaining elements from arr2
        while j < len_b:
            if not merged or merged[-1] != b[j]:
                merged.append(b[j])
            j += 1

        return merged

    return _merge_unique(arr1, arr2)
```