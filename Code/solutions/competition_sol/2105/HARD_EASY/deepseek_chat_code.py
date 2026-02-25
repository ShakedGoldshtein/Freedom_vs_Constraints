```python
def solve(n):
    if n <= 1:
        return 1, [1] if n == 1 else []
    
    is_prime = [True] * (n + 2)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int((n + 2) ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 2, i):
                is_prime[j] = False
    
    colors = []
    for i in range(2, n + 2):
        if is_prime[i]:
            colors.append(1)
        else:
            colors.append(2)
    
    k = 1 if n == 1 else (1 if all(c == 1 for c in colors) else 2)
    return k, colors
```