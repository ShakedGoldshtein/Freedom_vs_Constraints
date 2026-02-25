```python
def solve(n, k, chains):
    pos = [0] * (n + 1)
    for chain in chains:
        m = chain[0]
        for idx, doll in enumerate(chain[1:1 + m]):
            pos[doll] = idx
    
    total_ops = 0
    i = 1
    while i <= n:
        if pos[i] > 0:
            total_ops += 2 * pos[i] + 1
            i += 1
        else:
            j = i
            while j < n and pos[j + 1] == pos[j] + 1:
                j += 1
            total_ops += (j - i)
            i = j + 1
    
    return total_ops
```