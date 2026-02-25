```python
def solve(n, m, b_list, g_list):
    b_list.sort()
    g_list.sort()
    
    if b_list[-1] > g_list[0]:
        return -1
    
    total_sweets = 0
    for b in b_list:
        total_sweets += b * m
    
    if b_list[-1] == g_list[0]:
        for g in g_list:
            total_sweets += g - b_list[-1]
    else:
        if n == 1:
            return -1
        
        for i in range(1, m):
            total_sweets += g_list[i] - b_list[-1]
        
        if g_list[0] > b_list[-2]:
            total_sweets += g_list[0] - b_list[-2]
        else:
            total_sweets += g_list[0] - b_list[-1]
    
    return total_sweets
```