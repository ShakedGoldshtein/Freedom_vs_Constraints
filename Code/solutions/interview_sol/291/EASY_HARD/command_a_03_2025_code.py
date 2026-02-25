```python
def solve(arr: list[int]) -> int:
    MOD = 10**9 + 7
    n = len(arr)
    prefix = 0
    count = 0
    odd_count = 1 if arr[0] % 2 != 0 else 0

    for i in range(n):
        prefix ^= arr[i] % 2
        if prefix:
            count += i + 1 - odd_count
        else:
            count += i + 1 - (i + 1 - odd_count)
        odd_count += 1 if arr[i] % 2 != 0 else 0

    return count % MOD
```