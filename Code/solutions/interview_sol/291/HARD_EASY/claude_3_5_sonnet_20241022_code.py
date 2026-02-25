```python
def count_odd_sum_subarrays(arr):
    MOD = 1000000007
    n = len(arr)
    odd, even = 0, 0
    curr_sum = 0
    result = 0

    for num in arr:
        # Add current number to running sum
        curr_sum += num
        
        # If current running sum is odd
        if curr_sum % 2 == 1:
            # Add previous even count + 1 for current odd sum 
            result = (result + even + 1) % MOD
            odd += 1
        else:
            # Add previous odd count for current even sum
            result = (result + odd) % MOD 
            even += 1
    
    return result
```