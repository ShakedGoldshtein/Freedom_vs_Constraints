```python
def build_graph(n, edges):
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph

def get_path_to_node(graph, target, n):
    visited = [False] * (n + 1)
    path = []
    
    def dfs(node, target):
        visited[node] = True
        path.append(node)
        
        if node == target:
            return True
            
        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor, target):
                    return True
                    
        path.pop()
        return False
        
    dfs(1, target)
    return path

def solve_queries(n, sweetness, edges, queries):
    graph = build_graph(n, edges)
    result = []
    
    for query in queries:
        if query[0] == 1:
            # Type 1: Find path from root to target node and sum sweetness
            path = get_path_to_node(graph, query[1], n)
            total = sum(sweetness[node-1] for node in path)
            result.append(total)
            
        else:
            # Type 2: Update sweetness of a node
            node, new_sweetness = query[1], query[2]
            sweetness[node-1] = new_sweetness
            
    return result

def solve(n, sweetness, edges, queries):
    """
    Main solving function that processes queries on tree structure
    
    Args:
        n: Number of nodes
        sweetness: List of sweetness values for each node
        edges: List of edge pairs connecting nodes
        queries: List of queries to process
        
    Returns:
        List of results for type 1 queries
    """
    return solve_queries(n, sweetness, edges, queries)
```