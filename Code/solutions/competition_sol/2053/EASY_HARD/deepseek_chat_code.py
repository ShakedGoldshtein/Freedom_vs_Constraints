```python
def solve(n, m, b_list, g_list):
    b_list.sort()
    g_list.sort()
    
    if b_list[-1] > g_list[0]:
        return -1
    
    total = sum(b_list) * m
    
    if b_list[-1] == g_list[0]:
        total += sum(g_list) - b_list[-1] * m
    else:
        if n == 1:
            return -1
        total += g_list[0] - b_list[-2]
        total += sum(g_list) - b_list[-1] * (m - 1) - g_list[0]
    
    return total
```