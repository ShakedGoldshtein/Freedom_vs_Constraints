```python
import math

def findUnsortedSubarray(nums: list[int]) -> int:
    n = len(nums)
    if n <= 1:
        return 0

    # Step 1: Find the minimum value that is 'out of place' in the unsorted segment.
    # We iterate from left to right, keeping track of the maximum element seen so far.
    # If the current element is less than the maximum seen so far, it means this
    # element is 'out of place' and contributes to the unsorted segment.
    # We update `min_val_in_unsorted_segment` with the smallest such 'out of place' element.
    min_val_in_unsorted_segment = math.inf
    max_prefix = -math.inf 

    for i in range(n):
        if nums[i] < max_prefix:
            min_val_in_unsorted_segment = min(min_val_in_unsorted_segment, nums[i])
        else:
            max_prefix = nums[i]

    # If `min_val_in_unsorted_segment` is still infinity, it means no element was
    # found to be out of place from the left scan, implying the array is already sorted.
    if min_val_in_unsorted_segment == math.inf:
        return 0

    # Step 2: Find the maximum value that is 'out of place' in the unsorted segment.
    # We iterate from right to left, keeping track of the minimum element seen so far.
    # If the current element is greater than the minimum seen so far, it means this
    # element is 'out of place' and contributes to the unsorted segment.
    # We update `max_val_in_unsorted_segment` with the largest such 'out of place' element.
    max_val_in_unsorted_segment = -math.inf
    min_suffix = math.inf 

    for i in range(n - 1, -1, -1):
        if nums[i] > min_suffix:
            max_val_in_unsorted_segment = max(max_val_in_unsorted_segment, nums[i])
        else:
            min_suffix = nums[i]

    # Step 3: Find the left boundary (`left_idx`) of the shortest unsorted subarray.
    # This is the first index from the left where `nums[left_idx]` is greater than
    # `min_val_in_unsorted_segment`. All elements to its left must be less than or
    # equal to `min_val_in_unsorted_segment` to maintain sorted order after sorting the subarray.
    left_idx = 0
    while left_idx < n and nums[left_idx] <= min_val_in_unsorted_segment:
        left_idx += 1

    # Step 4: Find the right boundary (`right_idx`) of the shortest unsorted subarray.
    # This is the first index from the right where `nums[right_idx]` is less than
    # `max_val_in_unsorted_segment`. All elements to its right must be greater than or
    # equal to `max_val_in_unsorted_segment` to maintain sorted order.
    right_idx = n - 1
    while right_idx >= 0 and nums[right_idx] >= max_val_in_unsorted_segment:
        right_idx -= 1
    
    # The length of the unsorted subarray is `right_idx - left_idx + 1`.
    return right_idx - left_idx + 1

```