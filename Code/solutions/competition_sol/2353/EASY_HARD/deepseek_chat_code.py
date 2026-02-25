```python
def solve(n, a):
    a_sorted = sorted(a)
    for i in range(n - 1):
        if a_sorted[i] == a_sorted[i + 1]:
            return [-1]
    
    for attempt in range(100):
        import random
        b = a_sorted[:]
        random.shuffle(b)
        valid = True
        
        total_mask = (1 << n) - 1
        for mask in range(1, total_mask):
            sum_a = 0
            sum_b = 0
            for i in range(n):
                if mask & (1 << i):
                    sum_a += a_sorted[i]
                    sum_b += b[i]
            if sum_a == sum_b:
                valid = False
                break
                
        if valid:
            return b
    
    return [-1]
```