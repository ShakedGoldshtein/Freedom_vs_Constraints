```python
def iq_test(numbers):
    nums = list(map(int, numbers.split()))
    evens = [i for i, num in enumerate(nums, 1) if num % 2 == 0]
    odds = [i for i, num in enumerate(nums, 1) if num % 2 == 1]
    return evens[0] if len(evens) == 1 else odds[0]
```