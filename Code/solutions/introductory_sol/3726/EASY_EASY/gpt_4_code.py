```python
def sort_array(source_array):
    odd_numbers = sorted(x for x in source_array if x % 2 != 0)
    return [odd_numbers.pop(0) if i % 2 != 0 else i for i in source_array]
```