```python
def max_possible_gcd(T, nums):
    gcd_values = []
    for t in range(T):
        N = nums[t][0]
        array = nums[t][1]
        new_array_1 = array[1:] if len(array) > 1 else array
        new_array_2 = array[:N-1] if len(array) > 1 else array
        max_gcd = max(max(new_array_1), max(new_array_2))
        gcd_values.append(max_gcd)
    return gcd_values
```