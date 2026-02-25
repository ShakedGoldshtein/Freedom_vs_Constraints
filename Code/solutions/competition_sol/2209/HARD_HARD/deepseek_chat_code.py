```python
import sys
from collections import deque, defaultdict

def solve(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    degree = [0] * (n + 1)
    for i in range(1, n + 1):
        degree[i] = len(graph[i])
    
    leaves = [i for i in range(1, n + 1) if degree[i] == 1]
    
    if n == 3:
        return (1, 1)
    
    leaf_neighbors = defaultdict(list)
    for leaf in leaves:
        for neighbor in graph[leaf]:
            leaf_neighbors[neighbor].append(leaf)
    
    max_f = n - 1
    min_f = 1
    
    for node in leaf_neighbors:
        if len(leaf_neighbors[node]) > 1:
            max_f -= (len(leaf_neighbors[node]) - 1)
    
    visited = [False] * (n + 1)
    distances = [0] * (n + 1)
    
    def bfs(start):
        queue = deque([start])
        visited[start] = True
        distances[start] = 0
        farthest_node = start
        max_dist = 0
        
        while queue:
            current = queue.popleft()
            for neighbor in graph[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    distances[neighbor] = distances[current] + 1
                    queue.append(neighbor)
                    if distances[neighbor] > max_dist:
                        max_dist = distances[neighbor]
                        farthest_node = neighbor
        return farthest_node, max_dist
    
    start_node = 1
    farthest1, _ = bfs(start_node)
    
    visited = [False] * (n + 1)
    distances = [0] * (n + 1)
    farthest2, diameter = bfs(farthest1)
    
    visited = [False] * (n + 1)
    distances = [0] * (n + 1)
    
    def bfs_distances(start):
        queue = deque([start])
        visited[start] = True
        distances[start] = 0
        
        while queue:
            current = queue.popleft()
            for neighbor in graph[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    distances[neighbor] = distances[current] + 1
                    queue.append(neighbor)
    
    bfs_distances(farthest1)
    dist_from_farthest1 = distances[:]
    
    visited = [False] * (n + 1)
    distances = [0] * (n + 1)
    bfs_distances(farthest2)
    dist_from_farthest2 = distances[:]
    
    is_on_diameter = [False] * (n + 1)
    for i in range(1, n + 1):
        if dist_from_farthest1[i] + dist_from_farthest2[i] == diameter:
            is_on_diameter[i] = True
    
    has_branch = False
    for i in range(1, n + 1):
        if is_on_diameter[i]:
            count_non_diameter = 0
            for neighbor in graph[i]:
                if not is_on_diameter[neighbor]:
                    count_non_diameter += 1
                    if count_non_diameter >= 2:
                        has_branch = True
                        break
            if has_branch:
                break
    
    if not has_branch:
        min_f = 1
    else:
        min_f = 3
    
    return (min_f, max_f)

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    edges = []
    index = 1
    for _ in range(n - 1):
        u = int(data[index])
        v = int(data[index + 1])
        edges.append((u, v))
        index += 2
    result = solve(n, edges)
    print(f"{result[0]} {result[1]}")

if __name__ == "__main__":
    main()
```