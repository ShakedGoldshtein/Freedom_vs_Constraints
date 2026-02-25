```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_prime_divisors(n):
    divisors = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if is_prime(i):
                divisors.add(i)
            if is_prime(n // i):
                divisors.add(n // i)
    if is_prime(n):
        divisors.add(n)
    return divisors

def solve(n):
    # Build graph where edges connect numbers that can't have same color
    graph = [[] for _ in range(n+2)]
    for i in range(2, n+2):
        prime_divs = get_prime_divisors(i)
        for prime in prime_divs:
            if prime <= n+1:
                graph[i].append(prime)
                graph[prime].append(i)
    
    # Color nodes using greedy approach
    colors = [0] * (n+2)
    max_color = 0
    
    # For each node
    for node in range(2, n+2):
        # Get colors of neighbors
        used_colors = set()
        for neighbor in graph[node]:
            if colors[neighbor] != 0:
                used_colors.add(colors[neighbor])
        
        # Find first unused color
        color = 1
        while color in used_colors:
            color += 1
            
        colors[node] = color
        max_color = max(max_color, color)
    
    # Return results in required format
    result = []
    result.append(max_color)
    result.append(colors[2:n+2])
    return result

```