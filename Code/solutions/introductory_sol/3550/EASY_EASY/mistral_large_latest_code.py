```python
import math

def sum_square_even_root_odd(nums):
    total = 0.0
    for num in nums:
        if num % 2 == 0:
            total += num ** 2
        else:
            total += math.sqrt(num)
    return round(total, 2)
```