```python
def findShortestSubarray(nums):
    sorted_nums = sorted(nums)
    start, end = 0, len(nums) - 1
    
    while start < len(nums) and nums[start] == sorted_nums[start]:
        start += 1
    while end > start and nums[end] == sorted_nums[end]:
        end -= 1
        
    return end - start + 1
```