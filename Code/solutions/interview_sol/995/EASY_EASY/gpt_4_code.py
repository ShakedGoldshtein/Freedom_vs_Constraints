```python
def max_money(n, A, k):
    left = [0 for _ in range(n+1)]
    right = [0 for _ in range(n+1)]
    left_sum, right_sum = 0, 0
    for i in range(n):
        left_sum += A[i]
        right_sum += A[-i-1]
        left[i+1] = max(left[i], left_sum)
        right[i+1] = max(right[i], right_sum)
    max_money_obtained = 0
    for i in range(k+1):
        max_money_obtained = max(max_money_obtained, left[i] + right[k-i])
    return max_money_obtained
```