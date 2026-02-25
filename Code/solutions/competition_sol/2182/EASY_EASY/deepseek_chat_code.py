```python
def solve(s, t):
    n = len(s)
    s_sorted = sorted(s)
    t_sorted = sorted(t, reverse=True)
    
    res = [''] * n
    left_s, right_s = 0, (n + 1) // 2 - 1
    left_t, right_t = 0, n // 2 - 1
    
    left_res, right_res = 0, n - 1
    
    for i in range(n):
        if i % 2 == 0:
            if left_s <= right_s and s_sorted[left_s] < t_sorted[left_t]:
                res[left_res] = s_sorted[left_s]
                left_res += 1
                left_s += 1
            else:
                res[right_res] = s_sorted[right_s]
                right_res -= 1
                right_s -= 1
        else:
            if left_t <= right_t and t_sorted[left_t] > s_sorted[left_s]:
                res[left_res] = t_sorted[left_t]
                left_res += 1
                left_t += 1
            else:
                res[right_res] = t_sorted[right_t]
                right_res -= 1
                right_t -= 1
                
    return ''.join(res)
```