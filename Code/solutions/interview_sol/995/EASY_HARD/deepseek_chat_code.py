```python
def solve(n, A, k):
    if k == 0:
        return 0
    if n == 1:
        return A[0]
    
    left = [0] * (k + 1)
    right = [0] * (k + 1)
    
    for i in range(1, k + 1):
        left[i] = left[i - 1] + A[i - 1]
    
    for i in range(1, k + 1):
        right[i] = right[i - 1] + A[n - i]
    
    max_money = 0
    for i in range(0, k + 1):
        max_money = max(max_money, left[i] + right[k - i])
    
    return max_money
```