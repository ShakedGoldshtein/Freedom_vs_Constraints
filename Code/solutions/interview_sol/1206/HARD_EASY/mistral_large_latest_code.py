```python
from collections import defaultdict

def find_common_voters(list1, list2, list3):
    """
    Finds the intersection of at least two out of three sorted lists of voter IDs.

    Args:
        list1: First sorted list of voter IDs.
        list2: Second sorted list of voter IDs.
        list3: Third sorted list of voter IDs.

    Returns:
        A sorted list of voter IDs that appear in at least two of the three lists.
    """
    def merge_two_lists(a, b):
        """Merges two sorted lists and counts occurrences of each element."""
        count = defaultdict(int)
        i, j = 0, 0
        len_a, len_b = len(a), len(b)

        while i < len_a and j < len_b:
            if a[i] < b[j]:
                count[a[i]] += 1
                i += 1
            elif a[i] > b[j]:
                count[b[j]] += 1
                j += 1
            else:
                count[a[i]] += 2
                i += 1
                j += 1

        while i < len_a:
            count[a[i]] += 1
            i += 1

        while j < len_b:
            count[b[j]] += 1
            j += 1

        return count

    # Merge list1 and list2, then merge the result with list3
    merged_12 = merge_two_lists(list1, list2)
    merged_all = merge_two_lists(list3, list(merged_12.keys()))

    # Collect IDs that appear in at least two lists
    result = []
    for id_num in merged_all:
        total = merged_12.get(id_num, 0) + merged_all.get(id_num, 0)
        if total >= 2:
            result.append(id_num)

    return sorted(result)

def solve(n1, n2, n3, list1, list2, list3):
    """
    Solves the voter list problem by finding IDs present in at least two of the three lists.

    Args:
        n1: Number of voters in the first list.
        n2: Number of voters in the second list.
        n3: Number of voters in the third list.
        list1: First sorted list of voter IDs.
        list2: Second sorted list of voter IDs.
        list3: Third sorted list of voter IDs.

    Returns:
        A tuple where the first element is the count of common voters,
        and the second element is the sorted list of common voter IDs.
    """
    common_voters = find_common_voters(list1, list2, list3)
    return (len(common_voters), common_voters)
```