```python
def find_majority_voters(
    list1: list[int],
    list2: list[int],
    list3: list[int]
) -> list[int]:
    """
    Identifies voter IDs that appear in at least two out of three sorted lists.

    This function efficiently finds common voter ID numbers across three
    already sorted lists. It utilizes a three-pointer approach to traverse
    the lists simultaneously, ensuring optimal time complexity.

    Args:
        list1: A list of voter ID numbers, sorted in ascending order.
               Assumes unique elements within this list.
        list2: A list of voter ID numbers, sorted in ascending order.
               Assumes unique elements within this list.
        list3: A list of voter ID numbers, sorted in ascending order.
               Assumes unique elements within this list.

    Returns:
        A new list containing voter ID numbers that appear in at least two
        of the three input lists. The returned list will be sorted in
        ascending order.
    """
    len1, len2, len3 = len(list1), len(list2), len(list3)
    p1, p2, p3 = 0, 0, 0  # Pointers for each list
    
    # Stores the voter IDs that appear in at least two lists
    majority_voters = []

    # Continue as long as there are elements left in any of the lists
    while p1 < len1 or p2 < len2 or p3 < len3:
        # Get the current element from each list,
        # or float('inf') if the list has been exhausted
        val1 = list1[p1] if p1 < len1 else float('inf')
        val2 = list2[p2] if p2 < len2 else float('inf')
        val3 = list3[p3] if p3 < len3 else float('inf')

        # Find the smallest current value among the active pointers
        current_min_val = min(val1, val2, val3)

        # If current_min_val is infinity, all lists are exhausted
        if current_min_val == float('inf'):
            break

        # Count how many lists contain the current_min_val
        count = 0
        if val1 == current_min_val:
            count += 1
            p1 += 1  # Advance pointer for list1
        if val2 == current_min_val:
            count += 1
            p2 += 1  # Advance pointer for list2
        if val3 == current_min_val:
            count += 1
            p3 += 1  # Advance pointer for list3

        # If the current_min_val appeared in at least two lists, add it to the result
        if count >= 2:
            majority_voters.append(current_min_val)
            
    return majority_voters
```