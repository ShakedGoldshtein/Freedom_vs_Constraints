```python
def solve(n, k, chains):
    pos = [0] * (n + 1)
    for chain in chains:
        m = chain[0]
        for idx, val in enumerate(chain[1:]):
            pos[val] = idx + 1
    
    result = 0
    i = 1
    while i <= n:
        if pos[i] != 1:
            result += 2 * (pos[i] - 1)
        j = i + 1
        while j <= n and pos[j] == pos[j - 1] + 1:
            j += 1
        result += 1
        i = j
    
    return result - 1
```