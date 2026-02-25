```python
def count_odd_subarrays(arr):
    MOD = 10**9 + 7
    count = 0
    odd = 0
    even = 1
    prefix_sum = 0

    for num in arr:
        prefix_sum += num
        if prefix_sum % 2 == 1:
            count = (count + even) % MOD
            odd += 1
        else:
            count = (count + odd) % MOD
            even += 1
    return count
```