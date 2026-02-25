```python
def solve(n, commands):
    a_success = 0
    a_total = 0
    b_success = 0 
    b_total = 0
    
    for t, x, y in commands:
        if t == 1:
            a_success += x
            a_total += 10
        else:
            b_success += x
            b_total += 10
            
    result = []
    result.append("LIVE" if a_success * 2 >= a_total else "DEAD")
    result.append("LIVE" if b_success * 2 >= b_total else "DEAD")
    
    return result
```