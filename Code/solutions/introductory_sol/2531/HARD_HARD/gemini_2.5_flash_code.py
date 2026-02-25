```python
import math

def findUnsortedSubarray(nums: list[int]) -> int:
    """
    Finds the length of the shortest continuous subarray that, if sorted,
    makes the entire array sorted in non-decreasing order.

    The algorithm works in O(N) time and O(1) space complexity.
    It identifies the minimum and maximum values that are out of place within
    the potential unsorted subarray, then uses these values to determine the
    exact boundaries of the shortest continuous subarray that needs to be sorted.

    Args:
        nums: A list of integers. Ascending order means non-decreasing (nums[i] <= nums[i+1]).

    Returns:
        The length of the shortest unsorted subarray. Returns 0 if the array
        is already sorted.
    """
    n = len(nums)

    # Edge case: If the array has 0 or 1 element, it's already sorted.
    if n <= 1:
        return 0

    min_val_in_displaced_section = math.inf
    max_val_in_displaced_section = -math.inf

    # Pass 1: Iterate from left to right to find the minimum value that is out of place.
    # We maintain a `max_so_far` value representing the maximum element encountered
    # in the sorted prefix of the array. If `nums[i]` is less than `max_so_far`,
    # it means `nums[i]` is out of order relative to some element to its left
    # and must be part of the unsorted subarray. We track the minimum of all such
    # out-of-order elements.
    max_so_far = nums[0]
    for i in range(1, n):
        if nums[i] < max_so_far:
            min_val_in_displaced_section = min(min_val_in_displaced_section, nums[i])
        else:
            # If nums[i] is greater than or equal to max_so_far, it's in a sorted position
            # relative to elements encountered so far. Update max_so_far.
            max_so_far = nums[i]

    # Pass 2: Iterate from right to left to find the maximum value that is out of place.
    # We maintain a `min_so_far` value representing the minimum element encountered
    # in the sorted suffix of the array. If `nums[i]` is greater than `min_so_far`,
    # it means `nums[i]` is out of order relative to some element to its right
    # and must be part of the unsorted subarray. We track the maximum of all such
    # out-of-order elements.
    min_so_far = nums[n - 1]
    for i in range(n - 2, -1, -1):
        if nums[i] > min_so_far:
            max_val_in_displaced_section = max(max_val_in_displaced_section, nums[i])
        else:
            # If nums[i] is less than or equal to min_so_far, it's in a sorted position
            # relative to elements encountered so far. Update min_so_far.
            min_so_far = nums[i]

    # If `min_val_in_displaced_section` is still its initial `math.inf` value,
    # it means no elements were found to be out of order in the first pass.
    # This implies the entire array is already sorted in non-decreasing order.
    if min_val_in_displaced_section == math.inf:
        return 0

    # Find the left boundary (`left`) of the unsorted subarray.
    # This is the first index `l` from the left such that `nums[l]` is greater
    # than `min_val_in_displaced_section`. All elements to the left of `l` are
    # correctly positioned and are less than or equal to the minimum element
    # that needs to be sorted within the subarray.
    left = 0
    while left < n and nums[left] <= min_val_in_displaced_section:
        left += 1

    # Find the right boundary (`right`) of the unsorted subarray.
    # This is the first index `r` from the right such that `nums[r]` is smaller
    # than `max_val_in_displaced_section`. All elements to the right of `r` are
    # correctly positioned and are greater than or equal to the maximum element
    # that needs to be sorted within the subarray.
    right = n - 1
    while right >= 0 and nums[right] >= max_val_in_displaced_section:
        right -= 1

    # The length of the unsorted subarray is `right - left + 1`.
    # This value will always be positive because if `left` were to be greater
    # than `right`, it would imply that no unsorted subarray exists,
    # a scenario already handled by the `min_val_in_displaced_section == math.inf` check.
    return right - left + 1
```