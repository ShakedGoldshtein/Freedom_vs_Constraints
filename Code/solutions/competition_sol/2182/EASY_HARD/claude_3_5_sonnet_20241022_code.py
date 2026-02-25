```python
def solve(s, t):
    n = len(s)
    s = sorted(list(s))
    t = sorted(list(t))
    res = [''] * n
    
    s_ptr = 0
    s_ptr_right = len(s) - 1
    t_ptr = len(t) - 1
    t_ptr_right = 0
    
    for i in range(n):
        if i % 2 == 0:  # Oleg's turn
            if (n-i) % 2 == 1:  # Odd number of positions left
                res[i] = s[s_ptr]
                s_ptr += 1
            else:  # Even number of positions left 
                res[n-1-(i//2)] = s[s_ptr_right]
                s_ptr_right -= 1
        else:  # Igor's turn
            if (n-i) % 2 == 0:  # Even number of positions left
                res[i] = t[t_ptr]
                t_ptr -= 1
            else:  # Odd number of positions left
                res[n-1-((i-1)//2)] = t[t_ptr_right]
                t_ptr_right += 1
    
    return ''.join(res)
```