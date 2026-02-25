```python
def solve(n):
    def get_prime_factors(n):
        factors = set()
        i = 2
        while i * i <= n:
            while n % i == 0:
                factors.add(i)
                n //= i
            i += 1
        if n > 1:
            factors.add(n)
        return factors

    # Build graph of numbers that can't have same color
    adj = [[] for _ in range(n+2)]
    for i in range(2, n+2):
        prime_factors = get_prime_factors(i)
        for p in prime_factors:
            if p <= n+1:
                adj[p].append(i)
                adj[i].append(p)
                
    # Color the graph
    colors = [0] * (n+2)
    max_color = 0
    
    for v in range(2, n+2):
        used = set(colors[u] for u in adj[v])
        color = 1
        while color in used:
            color += 1
        colors[v] = color
        max_color = max(max_color, color)
        
    return [max_color, colors[2:n+2]]
```