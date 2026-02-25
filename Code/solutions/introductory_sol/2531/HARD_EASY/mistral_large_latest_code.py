```python
def find_unsorted_subarray(nums):
    """
    Finds the length of the shortest continuous subarray that, when sorted in ascending order,
    makes the entire array sorted in ascending order.

    Args:
        nums: List[int] - The input array of integers.

    Returns:
        int - The length of the shortest unsorted subarray. Returns 0 if the array is already sorted.
    """
    n = len(nums)
    if n <= 1:
        return 0

    # Find the left boundary of the unsorted subarray
    left = 0
    while left < n - 1 and nums[left] <= nums[left + 1]:
        left += 1

    if left == n - 1:
        return 0  # Array is already sorted

    # Find the right boundary of the unsorted subarray
    right = n - 1
    while right > 0 and nums[right] >= nums[right - 1]:
        right -= 1

    # Find the min and max within the unsorted subarray
    subarray_min = min(nums[left:right + 1])
    subarray_max = max(nums[left:right + 1])

    # Expand the left boundary to include any elements greater than subarray_min
    while left > 0 and nums[left - 1] > subarray_min:
        left -= 1

    # Expand the right boundary to include any elements less than subarray_max
    while right < n - 1 and nums[right + 1] < subarray_max:
        right += 1

    return right - left + 1
```