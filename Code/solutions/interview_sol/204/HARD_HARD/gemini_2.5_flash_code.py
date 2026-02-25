```python
def search(nums: list[int], target: int) -> int:
    """
    Searches for a target value in a rotated sorted array.

    The array is sorted in ascending order but might have been rotated at
    some unknown pivot. No duplicate elements are assumed to exist.
    The algorithm's runtime complexity is O(log n).

    Args:
        nums: A list of integers, sorted in ascending order and rotated.
        target: The integer value to search for.

    Returns:
        The index of the target if found, otherwise -1.
    """
    if not nums:
        return -1

    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Determine which half is sorted
        if nums[left] <= nums[mid]:
            # The left half (from nums[left] to nums[mid]) is sorted
            if nums[left] <= target < nums[mid]:
                # Target is within the range of the sorted left half
                right = mid - 1
            else:
                # Target is in the right half (or not present)
                left = mid + 1
        else:
            # The right half (from nums[mid] to nums[right]) is sorted
            # This implies the pivot is in the left half, i.e., nums[left] > nums[mid]
            if nums[mid] < target <= nums[right]:
                # Target is within the range of the sorted right half
                left = mid + 1
            else:
                # Target is in the left half (or not present)
                right = mid - 1

    return -1
```