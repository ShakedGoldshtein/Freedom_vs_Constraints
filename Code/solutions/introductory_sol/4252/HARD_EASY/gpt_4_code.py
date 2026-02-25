```python
def mergeSortedArrays(arr1, arr2):
    """
    Function to merge two sorted arrays into a single one, 
    remove duplicates and return the result sorted.
    """
    # merging both lists and create a set to remove duplicates
    merged_list = list(set(arr1 + arr2))
    
    # sorting the list
    merged_list.sort()

    return merged_list
```