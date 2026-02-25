```python
import math

def sum_square_even_root_odd(nums):
    """
    Calculate the sum of squared even numbers and square rooted odd numbers.
    
    Args:
        nums: List of non-negative numbers
        
    Returns:
        float: Sum rounded to two decimal places
    """
    total = 0.0
    
    for num in nums:
        if num % 2 == 0:
            total += num * num
        else:
            total += math.sqrt(num)
    
    return round(total, 2)
```