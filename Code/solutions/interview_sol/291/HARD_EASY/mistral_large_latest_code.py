```python
MOD = 10**9 + 7

def count_odd_subarrays(arr):
    n = len(arr)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = (prefix[i] + arr[i]) % 2

    count = {0: 1}
    result = 0
    for num in prefix[1:]:
        if num == 1:
            result += count.get(0, 0)
        else:
            result += count.get(1, 0)
        count[num] = count.get(num, 0) + 1
    return result % MOD
```