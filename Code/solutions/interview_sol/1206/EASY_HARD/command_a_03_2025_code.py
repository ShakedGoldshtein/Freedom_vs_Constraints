```python
def solve(n1, n2, n3, list1, list2, list3):
    """
    This function takes three sorted lists of voter IDs and returns a new list containing IDs that appear in at least two of the input lists.

    Args:
        n1 (int): Number of elements in list1.
        n2 (int): Number of elements in list2.
        n3 (int): Number of elements in list3.
        list1 (list): First sorted list of voter IDs.
        list2 (list): Second sorted list of voter IDs.
        list3 (list): Third sorted list of voter IDs.

    Returns:
        tuple: A tuple containing the count of IDs in the final list and the final list itself.
    """

    # Initialize pointers for each list
    i, j, k = 0, 0, 0
    # Initialize a dictionary to count occurrences of each ID
    count = {}

    # Traverse all three lists simultaneously
    while i < n1 and j < n2 and k < n3:
        if list1[i] == list2[j] and list2[j] == list3[k]:
            # If all three IDs are the same, increment count by 3
            count[list1[i]] = count.get(list1[i], 0) + 3
            i += 1
            j += 1
            k += 1
        elif list1[i] == list2[j]:
            # If IDs in list1 and list2 are the same, increment count by 2
            count[list1[i]] = count.get(list1[i], 0) + 2
            i += 1
            j += 1
        elif list1[i] == list3[k]:
            # If IDs in list1 and list3 are the same, increment count by 2
            count[list1[i]] = count.get(list1[i], 0) + 2
            i += 1
            k += 1
        elif list2[j] == list3[k]:
            # If IDs in list2 and list3 are the same, increment count by 2
            count[list2[j]] = count.get(list2[j], 0) + 2
            j += 1
            k += 1
        else:
            # Move the pointer of the smallest ID
            if list1[i] < list2[j]:
                if list1[i] < list3[k]:
                    i += 1
                else:
                    k += 1
            else:
                if list2[j] < list3[k]:
                    j += 1
                else:
                    k += 1

    # Continue traversing the remaining elements in each list
    for remaining_list, n in [(list1, n1), (list2, n2), (list3, n3)]:
        for idx in range(i if remaining_list == list1 else j if remaining_list == list2 else k, n):
            id = remaining_list[idx]
            count[id] = count.get(id, 0) + 1

    # Filter IDs that appear at least twice and sort them
    final_list = sorted([id for id, cnt in count.items() if cnt >= 2])

    return len(final_list), final_list
```