```python
def find_unsorted_subarray(nums):
    """
    Find the length of the shortest continuous subarray that when sorted, 
    makes the entire array sorted in ascending order.
    
    Args:
        nums: List of integers
        
    Returns:
        int: Length of the shortest unsorted subarray
    """
    if not nums or len(nums) == 1:
        return 0
    
    n = len(nums)
    
    # Find the first index where order breaks from left
    left = 0
    while left < n - 1 and nums[left] <= nums[left + 1]:
        left += 1
    
    # If we reached the end, array is already sorted
    if left == n - 1:
        return 0
    
    # Find the first index where order breaks from right
    right = n - 1
    while right > 0 and nums[right] >= nums[right - 1]:
        right -= 1
    
    # Find min and max in the unsorted segment [left, right]
    segment_min = float('inf')
    segment_max = float('-inf')
    
    for i in range(left, right + 1):
        if nums[i] < segment_min:
            segment_min = nums[i]
        if nums[i] > segment_max:
            segment_max = nums[i]
    
    # Expand left boundary if needed
    while left > 0 and nums[left - 1] > segment_min:
        left -= 1
    
    # Expand right boundary if needed
    while right < n - 1 and nums[right + 1] < segment_max:
        right += 1
    
    return right - left + 1
```