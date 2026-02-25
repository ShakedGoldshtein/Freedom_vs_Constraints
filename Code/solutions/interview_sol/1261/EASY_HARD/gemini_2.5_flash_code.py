```python
def solve(N, M):
    if N < 3:
        return (-1, -1)
    
    if M != N:
        return (-1, -1)
    
    connections = []
    for i in range(1, N):
        connections.append((i, i + 1))
    connections.append((N, 1))
    
    return connections
```