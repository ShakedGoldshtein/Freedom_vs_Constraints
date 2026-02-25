```python
def findUnsortedSubarray(nums):
    if not nums or len(nums) < 2:
        return 0
        
    n = len(nums)
    
    # Find first misplaced element from left
    left = 0
    while left < n-1 and nums[left] <= nums[left+1]:
        left += 1
    
    if left == n-1:  # Array is already sorted
        return 0
        
    # Find first misplaced element from right    
    right = n-1
    while right > 0 and nums[right] >= nums[right-1]:
        right -= 1
        
    # Find min and max in the window
    window_min = float('inf')
    window_max = float('-inf')
    for i in range(left, right+1):
        window_min = min(window_min, nums[i])
        window_max = max(window_max, nums[i])
    
    # Extend window left if needed
    while left > 0 and nums[left-1] > window_min:
        left -= 1
        
    # Extend window right if needed    
    while right < n-1 and nums[right+1] < window_max:
        right += 1
        
    return right - left + 1
```