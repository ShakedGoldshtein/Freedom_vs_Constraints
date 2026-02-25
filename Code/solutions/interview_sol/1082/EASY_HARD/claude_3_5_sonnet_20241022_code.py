```python
def build_graph(n, edges):
    graph = [[] for _ in range(n+1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph

def find_path(graph, start, end, visited):
    if start == end:
        return [start]
    visited[start] = True
    for next_node in graph[start]:
        if not visited[next_node]:
            path = find_path(graph, next_node, end, visited)
            if path:
                return [start] + path
    return []

def solve(n, sweetness, edges, queries):
    graph = build_graph(n, edges)
    result = []
    
    for query in queries:
        if query[0] == 1:
            # Find path from node 1 to target node
            visited = [False] * (n+1)
            path = find_path(graph, 1, query[1], visited)
            
            # Calculate sum of sweetness along path
            total = 0
            for node in path:
                total += sweetness[node-1]
            result.append(total)
            
        else: # query[0] == 2
            # Update sweetness
            sweetness[query[1]-1] = query[2]
            
    return result

# Example usage:
n = 10
sweetness = [10, 12, 6, 8, 1, 19, 0, 5, 13, 17]
edges = [(1,2), (1,3), (1,4), (3,10), (4,8), (8,9), (4,5), (5,7), (5,6)]
queries = [(1,1), (2,3,20), (1,8)]
result = solve(n, sweetness, edges, queries)
```