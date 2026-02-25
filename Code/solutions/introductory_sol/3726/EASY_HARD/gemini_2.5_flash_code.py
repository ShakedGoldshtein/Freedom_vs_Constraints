```python
def sort_array(arr):
    if not arr:
        return []

    # Extract all odd numbers and sort them in ascending order
    # Zero is not considered an odd number, and x % 2 != 0 correctly excludes 0
    odd_numbers = sorted([x for x in arr if x % 2 != 0])

    result = []
    odd_idx = 0
    for x in arr:
        if x % 2 == 0:  # If the number is even (or zero)
            result.append(x)  # Keep it in its original place
        else:  # If the number is odd
            result.append(odd_numbers[odd_idx])  # Replace with the next sorted odd number
            odd_idx += 1
            
    return result
```