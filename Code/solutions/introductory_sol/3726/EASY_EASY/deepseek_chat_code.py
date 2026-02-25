```python
def sort_array(source_array):
    if not source_array:
        return source_array
    
    odd_numbers = sorted([x for x in source_array if x % 2 != 0])
    
    result = []
    odd_index = 0
    
    for num in source_array:
        if num % 2 != 0:
            result.append(odd_numbers[odd_index])
            odd_index += 1
        else:
            result.append(num)
    
    return result
```