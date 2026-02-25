```python
def sort_array(arr):
    odds = sorted([x for x in arr if x % 2 == 1])
    odd_index = 0
    result = []
    for num in arr:
        if num % 2 == 0:
            result.append(num)
        else:
            result.append(odds[odd_index])
            odd_index += 1
    return result
```