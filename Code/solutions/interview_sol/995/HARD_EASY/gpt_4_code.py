```python
def max_money(n, A, k):
    prefix_sum = [0]*(n+1)
    suffix_sum = [0]*(n+2)
 
    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + A[i]
 
    for i in range(n - 1, -1, -1):
        suffix_sum[i+1] = suffix_sum[i+2] + A[i]
 
    max_money = -1
    for i in range(k+1):
        if(i<=n and k-i <=n):
            max_money = max(max_money, prefix_sum[i] + suffix_sum[k-i+1])
 
    return max_money
```