```python
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def solve(T, test_cases):
    result = []
    for r in range(T):
        N, K = test_cases[r]
        if (N >= 2 * K) and ((N % 2 == 0 and K <= N // 2) or (N % 2 == 1 and K <= N // 2 + 1 and N/K >= 2)):
            result.append(1)
        else:
            result.append(0)
    return result
```