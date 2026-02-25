```python
def merge_sorted_arrays(arr1, arr2):
    merged = []
    i, j = 0, 0
    len1, len2 = len(arr1), len(arr2)

    while i < len1 and j < len2:
        if arr1[i] < arr2[j]:
            if not merged or merged[-1] != arr1[i]:
                merged.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            if not merged or merged[-1] != arr2[j]:
                merged.append(arr2[j])
            j += 1
        else:
            if not merged or merged[-1] != arr1[i]:
                merged.append(arr1[i])
            i += 1
            j += 1

    while i < len1:
        if not merged or merged[-1] != arr1[i]:
            merged.append(arr1[i])
        i += 1

    while j < len2:
        if not merged or merged[-1] != arr2[j]:
            merged.append(arr2[j])
        j += 1

    return merged
```