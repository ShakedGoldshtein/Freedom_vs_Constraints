```python
from collections import defaultdict 

def solve(n, m, edges):
    adj = defaultdict(list)
    for i in range(0, len(edges)): 
        u, v = edges[i]
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)

    visited = [0]*n
    set_1 = []
    set_2 = []
    for i in range(n):
        if visited[i] == 0 and not dfs(i,0,adj,visited,set_1,set_2):
            return -1
    return set_1, set_2

def dfs(v, c, adj, visited, set_1, set_2): 
    visited[v] = 1
    if c % 2 == 0:
        set_1.append(v+1)
    else:
        set_2.append(v+1)
    for i in range(len(adj[v])):
        if (visited[adj[v][i]] == 0 and
            dfs(adj[v][i], c ^ 1, adj, visited, set_1, set_2) == 0):
            return 0
        elif (visited[adj[v][i]] == 1 and
             (visited[adj[v][i]] ^ visited[v]) == 0):
            return 0
    return 1
```