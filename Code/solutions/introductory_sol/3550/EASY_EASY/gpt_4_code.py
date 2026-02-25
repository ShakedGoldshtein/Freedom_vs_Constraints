```python
def sum_square_even_root_odd(nums):
    from math import sqrt
    return round(sum([sqrt(num) if num % 2 != 0 else num ** 2 for num in nums]), 2)
```