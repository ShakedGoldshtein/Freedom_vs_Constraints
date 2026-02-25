```python
def sort_array(arr):
    if not arr:
        return arr
        
    # Get odd numbers in sorted order
    odd_nums = sorted([x for x in arr if x % 2 == 1])
    
    # Place odd numbers back in original positions
    odd_index = 0
    result = []
    
    for num in arr:
        if num % 2 == 0:
            result.append(num)
        else:
            result.append(odd_nums[odd_index])
            odd_index += 1
            
    return result
```