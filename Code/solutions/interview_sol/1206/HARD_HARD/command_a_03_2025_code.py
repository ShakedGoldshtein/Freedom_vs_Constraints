```python
def solve(list1: list[int], list2: list[int], list3: list[int]) -> list[int]:
    """
    Constructs the final list of voters by selecting IDs that appear in at least 2 out of 3 lists.

    Args:
        list1 (list[int]): The first list of voter IDs in ascending order.
        list2 (list[int]): The second list of voter IDs in ascending order.
        list3 (list[int]): The third list of voter IDs in ascending order.

    Returns:
        list[int]: The final list of voter IDs that appear in at least 2 lists, in ascending order.
    """

    def merge_sorted_lists(list_a: list[int], list_b: list[int]) -> list[int]:
        """
        Merges two sorted lists into a single sorted list.

        Args:
            list_a (list[int]): The first sorted list.
            list_b (list[int]): The second sorted list.

        Returns:
            list[int]: A new sorted list containing all elements from both input lists.
        """
        result = []
        i, j = 0, 0
        while i < len(list_a) and j < len(list_b):
            if list_a[i] < list_b[j]:
                result.append(list_a[i])
                i += 1
            elif list_a[i] > list_b[j]:
                result.append(list_b[j])
                j += 1
            else:
                result.append(list_a[i])
                i += 1
                j += 1
        result.extend(list_a[i:])
        result.extend(list_b[j:])
        return result

    def count_occurrences(merged_list: list[int], target_list: list[int]) -> dict[int, int]:
        """
        Counts the occurrences of each ID in the merged list within the target list.

        Args:
            merged_list (list[int]): The merged list of voter IDs.
            target_list (list[int]): The list to count occurrences against.

        Returns:
            dict[int, int]: A dictionary mapping each ID to its count in the target list.
        """
        counts = {}
        i, j = 0, 0
        while i < len(merged_list) and j < len(target_list):
            if merged_list[i] < target_list[j]:
                i += 1
            elif merged_list[i] > target_list[j]:
                j += 1
            else:
                counts[merged_list[i]] = counts.get(merged_list[i], 0) + 1
                i += 1
                j += 1
        return counts

    # Merge all three lists into one sorted list
    merged_list = merge_sorted_lists(merge_sorted_lists(list1, list2), list3)

    # Count occurrences of each ID in each list
    count1 = count_occurrences(merged_list, list1)
    count2 = count_occurrences(merged_list, list2)
    count3 = count_occurrences(merged_list, list3)

    # Construct the final list with IDs appearing in at least 2 lists
    final_list = []
    for voter_id in merged_list:
        total_count = count1.get(voter_id, 0) + count2.get(voter_id, 0) + count3.get(voter_id, 0)
        if total_count >= 2:
            final_list.append(voter_id)

    return [len(final_list)] + final_list
```