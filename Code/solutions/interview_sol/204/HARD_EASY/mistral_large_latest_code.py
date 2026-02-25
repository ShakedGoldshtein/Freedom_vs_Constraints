```python
def search_in_rotated_sorted_array(nums: list[int], target: int) -> int:
    """
    Searches for a target value in a rotated sorted array with O(log n) time complexity.

    Args:
        nums: A list of integers representing the rotated sorted array (ascending order).
        target: The integer value to search for in the array.

    Returns:
        The index of the target if found, otherwise -1.
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        # Determine which half is sorted
        if nums[left] <= nums[mid]:
            # Left half is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # Right half is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1
```