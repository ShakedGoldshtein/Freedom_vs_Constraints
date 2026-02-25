```python
def search(nums: list[int], target: int) -> int:
    """
    Searches for a target value in a rotated sorted array.

    Args:
        nums: A list of integers sorted in ascending order,
              but possibly rotated at an unknown pivot. No duplicates exist.
        target: The integer value to search for.

    Returns:
        The index of the target if found, otherwise -1.
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Determine which half is sorted
        # Case 1: The left half (from left to mid) is sorted
        if nums[left] <= nums[mid]:
            # Check if target falls within the sorted left half
            if nums[left] <= target < nums[mid]:
                right = mid - 1  # Search in the left half
            else:
                left = mid + 1   # Target must be in the right half (or not present)
        # Case 2: The right half (from mid to right) is sorted
        else:
            # Check if target falls within the sorted right half
            if nums[mid] < target <= nums[right]:
                left = mid + 1   # Search in the right half
            else:
                right = mid - 1  # Target must be in the left half (or not present)

    return -1

```