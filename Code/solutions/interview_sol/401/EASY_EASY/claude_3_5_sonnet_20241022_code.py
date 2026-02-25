```python
def solve(nums):
    if not nums:
        return 0
        
    total = sum(nums)
    remainder = total % 3
    
    if remainder == 0:
        return total
        
    n = len(nums)
    min_one = float('inf')
    min_two = float('inf')
    
    for num in nums:
        r = num % 3
        if r == 1:
            if min_one != float('inf'):
                min_two = min(min_two, min_one + num)
            min_one = min(min_one, num)
        elif r == 2: 
            if min_one != float('inf'):
                min_two = min(min_two, min_one + num)
            min_one = min(min_one, num)
    
    if remainder == 1:
        if min_one != float('inf'):
            return max(total - min_one, total - min_two if min_two != float('inf') else 0)
        return 0
    else:
        if min_one != float('inf'):
            return max(total - min_one, total - min_two if min_two != float('inf') else 0) 
        return 0
```