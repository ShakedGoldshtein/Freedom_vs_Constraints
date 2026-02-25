```python
def search(nums: list[int], target: int) -> int:
    """
    Searches for a target value in a rotated sorted array.

    Args:
        nums (list[int]): A sorted array that has been rotated at some pivot.
        target (int): The value to search for in the array.

    Returns:
        int: The index of the target value if found, otherwise -1.
    """
    if not nums:
        return -1

    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        # Check if the left half is sorted
        if nums[left] <= nums[mid]:
            # If the target is in the left half
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Check if the right half is sorted
        else:
            # If the target is in the right half
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1
```