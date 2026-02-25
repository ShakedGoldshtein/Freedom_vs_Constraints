```python
import heapq
from collections import defaultdict

def max_delivery_weight(n, m, x, edges):
    # Build adjacency list
    adj = defaultdict(list)
    for a, b, c in edges:
        adj[a].append((b, c))

    # Find all simple paths from 1 to n using BFS with path tracking
    paths = []
    stack = [(1, [1])]
    while stack:
        node, path = stack.pop()
        if node == n:
            paths.append(path)
            continue
        for neighbor, _ in adj[node]:
            if neighbor not in path:
                stack.append((neighbor, path + [neighbor]))

    if not paths:
        return 0.0

    # For each path, find the minimum capacity edge (bottleneck)
    path_bottlenecks = []
    for path in paths:
        min_capacity = float('inf')
        for i in range(len(path) - 1):
            a, b = path[i], path[i+1]
            for neighbor, capacity in adj[a]:
                if neighbor == b:
                    min_capacity = min(min_capacity, capacity)
                    break
        path_bottlenecks.append(min_capacity)

    # Binary search for the maximum possible weight per bear
    left = 0.0
    right = min(path_bottlenecks)
    best = 0.0
    epsilon = 1e-9

    while right - left > epsilon:
        mid = (left + right) / 2
        total_bears = 0
        for bottleneck in path_bottlenecks:
            if bottleneck >= mid:
                total_bears += 1
                if total_bears >= x:
                    break

        if total_bears >= x:
            best = mid
            left = mid
        else:
            right = mid

    return best * x
```