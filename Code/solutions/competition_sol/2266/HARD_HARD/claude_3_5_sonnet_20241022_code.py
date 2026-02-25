```python
def solve(n, m, lr_pairs):
    """
    Find minimum additional chairs needed for N people with M existing chairs.
    Args:
        n: Number of people
        m: Number of existing chairs 
        lr_pairs: List of [L,R] pairs specifying valid range for each person
    Returns:
        Minimum number of additional chairs needed
    """
    def maximum_bipartite_matching(graph, seen, match, u):
        for v in range(len(graph[u])):
            if graph[u][v] and not seen[v]:
                seen[v] = True
                if match[v] == -1 or maximum_bipartite_matching(graph, seen, match, match[v]):
                    match[v] = u
                    return True
        return False

    # Build adjacency matrix between people and chairs
    graph = [[0] * m for _ in range(n)]
    
    # For each person, mark valid chair positions
    for i in range(n):
        l, r = lr_pairs[i]
        for j in range(m):
            pos = j + 1
            if pos <= l or pos >= r:
                graph[i][j] = 1
                
    # Find maximum bipartite matching
    match = [-1] * m
    max_matches = 0
    
    for i in range(n):
        seen = [False] * m
        if maximum_bipartite_matching(graph, seen, match, i):
            max_matches += 1
            
    # Additional chairs needed = total people - maximum matches possible
    return n - max_matches
```