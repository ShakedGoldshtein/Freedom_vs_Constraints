```python
def iq_test(numbers):
    nums = [int(x) for x in numbers.split()]
    evens = [n % 2 == 0 for n in nums]
    
    if evens.count(True) == 1:
        return evens.index(True) + 1
    else:
        return evens.index(False) + 1
```