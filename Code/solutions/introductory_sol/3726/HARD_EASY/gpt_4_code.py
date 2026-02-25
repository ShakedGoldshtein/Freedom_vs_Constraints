```python
def sort_array(array):
    odd_numbers = sorted([n for n in array if n % 2 != 0])
    return [odd_numbers.pop(0) if n % 2 != 0 else n for n in array]
```