```python
MOD = 10**9 + 7

def solve():
    pass

def solve_problem(N, K, M, A):
    from collections import defaultdict

    dp_prev = defaultdict(int)
    dp_prev[0] = 1

    for num in A:
        dp_current = defaultdict(int)
        for mask in dp_prev:
            new_mask = mask
            for i in range(1, K + 1):
                if not (mask & (1 << (i - 1))):
                    if (num % M) == (i % M):
                        new_mask |= (1 << (i - 1))
                        break
            dp_current[new_mask] = (dp_current[new_mask] + dp_prev[mask]) % MOD
        for mask in dp_prev:
            dp_current[mask] = (dp_current[mask] + dp_prev[mask]) % MOD
        dp_prev = dp_current

    return dp_prev[(1 << K) - 1]

def solve_all(test_cases):
    results = []
    for case in test_cases:
        N, K, M, A = case
        results.append(solve_problem(N, K, M, A))
    return results
```