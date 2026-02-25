```python
import heapq
from collections import defaultdict

def solve(n, m, x, edges):
    graph = defaultdict(list)
    for a, b, c in edges:
        graph[a].append((b, c))

    def max_flow_per_bear():
        parent = {}
        max_flow = float('inf')
        heap = []
        heapq.heappush(heap, (-float('inf'), 1))
        visited = set()
        while heap:
            neg_flow, u = heapq.heappop(heap)
            current_flow = -neg_flow
            if u in visited:
                continue
            visited.add(u)
            if u == n:
                max_flow = min(max_flow, current_flow)
                break
            for v, c in graph[u]:
                if v not in visited:
                    heapq.heappush(heap, (-min(current_flow, c), v))
        return max_flow if max_flow != float('inf') else 0

    max_bear_capacity = max_flow_per_bear()
    total_max_weight = x * max_bear_capacity
    return total_max_weight
```