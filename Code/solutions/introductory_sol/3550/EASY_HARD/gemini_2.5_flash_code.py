```python
def sum_square_even_root_odd(nums):
    total_sum = 0.0
    for num in nums:
        if num % 2 == 0:  # Even number
            total_sum += num * num
        else:  # Odd number
            total_sum += num ** 0.5  # Square root
    return round(total_sum, 2)
```