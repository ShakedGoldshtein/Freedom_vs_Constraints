```python
def iq_test(numbers):
    nums = list(map(int, numbers.split()))
    even_count = sum(1 for num in nums if num % 2 == 0)
    odd_pos = next((i+1 for i, num in enumerate(nums) if num % 2 != 0), None)
    even_pos = next((i+1 for i, num in enumerate(nums) if num % 2 == 0), None)
    return odd_pos if even_count == 1 else even_pos
```