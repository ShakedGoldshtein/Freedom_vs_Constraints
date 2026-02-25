```python
def findUnsortedSubarray(nums):
    n = len(nums)
    if n <= 1:
        return 0
    
    left = 0
    right = n - 1
    
    while left < n - 1 and nums[left] <= nums[left + 1]:
        left += 1
    
    if left == n - 1:
        return 0
    
    while right > 0 and nums[right] >= nums[right - 1]:
        right -= 1
    
    sub_min = float('inf')
    sub_max = float('-inf')
    
    for i in range(left, right + 1):
        sub_min = min(sub_min, nums[i])
        sub_max = max(sub_max, nums[i])
    
    while left > 0 and nums[left - 1] > sub_min:
        left -= 1
    
    while right < n - 1 and nums[right + 1] < sub_max:
        right += 1
    
    return right - left + 1
```