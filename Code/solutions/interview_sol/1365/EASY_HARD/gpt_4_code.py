```python
def solve(s):
    mod = 10**9+7
    f, g = 0, 0
    if 'c' in s or 'k' in s:
        return 0
    for char in s:
        if char == 'f':
            g, f = f, (f+1)%mod
        if char == 'g':
            f, g = g, (g+f)%mod
    return (f+g)%mod
```