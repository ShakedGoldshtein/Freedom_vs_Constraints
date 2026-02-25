```python
def solve(nums):
    if len(nums) < 2:
        return 0
        
    left = len(nums)
    right = 0
    
    curr_max = float('-inf')
    curr_min = float('inf')
    
    for i in range(len(nums)):
        curr_max = max(curr_max, nums[i])
        if nums[i] < curr_max:
            right = i
    
    for i in range(len(nums)-1, -1, -1):
        curr_min = min(curr_min, nums[i]) 
        if nums[i] > curr_min:
            left = i
            
    return 0 if right <= left else right - left + 1
```