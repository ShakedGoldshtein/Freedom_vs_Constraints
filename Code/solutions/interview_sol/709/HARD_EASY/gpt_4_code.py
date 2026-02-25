```python
def max_gcd(T, test_cases):
    result = []
    for i in range(T):
        N, arr = test_cases[i]
        arr = arr + arr
        gcd = [0] * (2 * N + 1)
        for j in range(1, 2 * N + 1):
            for k in range(j, 2 * N + 1, j):
                gcd[j] = max(gcd[j], arr[k - 1])
            if j > N:
                gcd[j] = max(gcd[j - 1], gcd[j])
        result.append(gcd[2 * N])
    return result
```