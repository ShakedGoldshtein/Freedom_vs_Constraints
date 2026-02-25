```python
def max_money(n, A, k):
    if n == 0 or k == 0:
        return 0

    dp_prev = [0] * n
    dp_prev[0] = A[0]
    dp_prev[-1] = A[-1]

    for _ in range(1, k):
        dp_curr = [0] * n
        for i in range(n):
            if i == 0:
                dp_curr[i] = dp_prev[i+1] + A[i]
            elif i == n - 1:
                dp_curr[i] = dp_prev[i-1] + A[i]
            else:
                dp_curr[i] = max(dp_prev[i-1], dp_prev[i+1]) + A[i]
        dp_prev = dp_curr

    return max(dp_prev)
```