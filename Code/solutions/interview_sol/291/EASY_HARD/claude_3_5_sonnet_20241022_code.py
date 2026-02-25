```python
def solve(arr):
    MOD = 1000000007
    n = len(arr)
    odd = 0
    even = 0
    curr_sum = 0
    
    for num in arr:
        prev_sum = curr_sum
        curr_sum += num
        
        if prev_sum % 2 == 0:
            if curr_sum % 2 == 0:
                even += even
                odd += odd
            else:
                odd += even + 1
                even += odd - 1
        else:
            if curr_sum % 2 == 0:
                even += odd
                odd += even
            else:
                odd += even
                even += odd
                
        odd %= MOD
        even %= MOD
        
    return odd % MOD
```