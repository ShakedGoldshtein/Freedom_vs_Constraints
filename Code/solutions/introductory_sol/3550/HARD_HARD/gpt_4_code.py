```python
import math

def sum_square_even_root_odd(nums):

    return round(sum(num ** 2 if num % 2 == 0 else math.sqrt(num) for num in nums), 2)
```