```python
def merge_arrays(arr1, arr2):
    i, j = 0, 0
    merged = []
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            if not merged or arr1[i] != merged[-1]:
                merged.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            if not merged or arr2[j] != merged[-1]:
                merged.append(arr2[j])
            j += 1
        else:
            if not merged or arr1[i] != merged[-1]:
                merged.append(arr1[i])
            i += 1
            j += 1
    
    while i < len(arr1):
        if not merged or arr1[i] != merged[-1]:
            merged.append(arr1[i])
        i += 1
    
    while j < len(arr2):
        if not merged or arr2[j] != merged[-1]:
            merged.append(arr2[j])
        j += 1
    
    return merged
```