```python
def solve(n, commands):
    total_a = 0
    total_b = 0
    success_a = 0
    success_b = 0
    
    for cmd in commands:
        t, x, y = cmd
        if t == 1:
            success_a += x
            total_a += 10
        else:
            success_b += x
            total_b += 10
    
    result_a = "LIVE" if success_a * 2 >= total_a else "DEAD"
    result_b = "LIVE" if success_b * 2 >= total_b else "DEAD"
    
    return result_a + "\n" + result_b
```