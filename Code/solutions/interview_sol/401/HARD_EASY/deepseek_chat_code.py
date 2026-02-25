```python
def max_sum_divisible_by_three(nums):
    """
    Calculate the maximum possible sum of elements divisible by three.
    
    Args:
        nums: List of integers
        
    Returns:
        Maximum sum divisible by three
    """
    if not nums:
        return 0
    
    total_sum = 0
    remainder_one = []
    remainder_two = []
    
    for num in nums:
        total_sum += num
        remainder = num % 3
        if remainder == 1:
            remainder_one.append(num)
        elif remainder == 2:
            remainder_two.append(num)
    
    remainder_one.sort()
    remainder_two.sort()
    
    if total_sum % 3 == 0:
        return total_sum
    
    min_remove = float('inf')
    
    if total_sum % 3 == 1:
        if len(remainder_one) >= 1:
            min_remove = min(min_remove, remainder_one[0])
        if len(remainder_two) >= 2:
            min_remove = min(min_remove, remainder_two[0] + remainder_two[1])
    elif total_sum % 3 == 2:
        if len(remainder_two) >= 1:
            min_remove = min(min_remove, remainder_two[0])
        if len(remainder_one) >= 2:
            min_remove = min(min_remove, remainder_one[0] + remainder_one[1])
    
    return total_sum - min_remove if min_remove != float('inf') else 0
```