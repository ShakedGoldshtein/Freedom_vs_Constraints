```python
def num_subarrays_odd_sum(arr):
    mod = 10**9+7
    counts = [1, 0]
    s = 0
    res = 0
    for a in arr:
        s ^= a & 1
        res += counts[s ^ 1]
        counts[s] += 1
    return res%mod
```