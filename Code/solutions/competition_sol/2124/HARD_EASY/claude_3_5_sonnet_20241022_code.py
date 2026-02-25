```python
def max_flow(graph, source, sink):
    n = len(graph)
    flow = [[0] * n for _ in range(n)]
    
    def bfs():
        visited = [False] * n
        visited[source] = True
        queue = [(source, float('inf'))]
        parent = [-1] * n
        
        while queue:
            u, curr_flow = queue.pop(0)
            if u == sink:
                path_flow = curr_flow
                while u != source:
                    v = parent[u]
                    flow[v][u] += path_flow
                    flow[u][v] -= path_flow
                    u = v
                return path_flow
            
            for v in range(n):
                if not visited[v] and graph[u][v] > flow[u][v]:
                    visited[v] = True
                    parent[v] = u
                    queue.append((v, min(curr_flow, graph[u][v] - flow[u][v])))
        return 0

    max_flow = 0
    while True:
        path_flow = bfs()
        if path_flow == 0:
            break
        max_flow += path_flow
    return max_flow

def solve(n, m, x, edges):
    def check(weight):
        # Build graph with scaled capacities
        graph = [[0] * n for _ in range(n)]
        for a, b, c in edges:
            graph[a-1][b-1] = c / weight
            
        # Check if max flow >= x
        flow = max_flow(graph, 0, n-1)
        return flow >= x

    # Binary search for maximum weight
    left, right = 0, 1e6
    for _ in range(60):  # Sufficient iterations for precision
        mid = (left + right) / 2
        if check(mid):
            left = mid
        else:
            right = mid
            
    return left * x

def main(n, m, x, edges):
    return solve(n, m, x, edges)
```