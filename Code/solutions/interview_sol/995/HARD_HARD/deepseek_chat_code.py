```python
def solve(n, A, k):
    if k == 0:
        return 0
    
    if n == 1:
        return A[0] if k >= 1 else 0
    
    left_sum = [0] * (k + 1)
    right_sum = [0] * (k + 1)
    
    for i in range(1, min(k, n) + 1):
        left_sum[i] = left_sum[i - 1] + A[i - 1]
    
    for i in range(1, min(k, n) + 1):
        right_sum[i] = right_sum[i - 1] + A[n - i]
    
    max_money = 0
    for i in range(0, k + 1):
        j = k - i
        if i <= n and j <= n:
            current_sum = left_sum[i] + right_sum[j]
            if current_sum > max_money:
                max_money = current_sum
    
    return max_money
```