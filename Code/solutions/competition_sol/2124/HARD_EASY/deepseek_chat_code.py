```python
def solve(n, m, x, edges):
    from collections import deque
    import math

    graph = [[] for _ in range(n)]
    for a, b, c in edges:
        graph[a-1].append((b-1, c))

    def bfs_flow(capacity, source, sink):
        parent = [-1] * n
        min_capacity = [0] * n
        queue = deque([source])
        min_capacity[source] = math.inf
        parent[source] = source
        
        while queue:
            u = queue.popleft()
            for v, cap in graph[u]:
                if parent[v] == -1 and capacity[u][v] > 0:
                    parent[v] = u
                    min_capacity[v] = min(min_capacity[u], capacity[u][v])
                    if v == sink:
                        return min_capacity[sink], parent
                    queue.append(v)
        return 0, parent

    def max_flow(source, sink):
        capacity = [[0] * n for _ in range(n)]
        for u in range(n):
            for v, cap in graph[u]:
                capacity[u][v] += cap
        
        total_flow = 0
        while True:
            flow, parent = bfs_flow(capacity, source, sink)
            if flow == 0:
                break
            total_flow += flow
            v = sink
            while v != source:
                u = parent[v]
                capacity[u][v] -= flow
                capacity[v][u] += flow
                v = u
        return total_flow

    source, sink = 0, n-1
    max_f = max_flow(source, sink)
    
    if max_f == 0:
        return 0.0
    
    low, high = 0.0, float(x * max_f)
    for _ in range(60):
        mid = (low + high) / 2.0
        if mid == 0:
            low = mid
            continue
            
        graph_weighted = [[] for _ in range(n)]
        for u in range(n):
            for v, cap in graph[u]:
                graph_weighted[u].append((v, cap / mid))
        
        def bfs_weighted(source, sink):
            dist = [math.inf] * n
            dist[source] = 0
            queue = deque([source])
            while queue:
                u = queue.popleft()
                for v, weight in graph_weighted[u]:
                    if dist[v] > dist[u] + weight:
                        dist[v] = dist[u] + weight
                        queue.append(v)
            return dist[sink]

        min_path_weight = bfs_weighted(source, sink)
        if min_path_weight <= x:
            low = mid
        else:
            high = mid
    
    return low
```