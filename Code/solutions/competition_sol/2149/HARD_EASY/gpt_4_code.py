```python
from collections import defaultdict

def solve(n, m, a):
    MAX = (1 << n)
    
    edge = [False] * MAX
    visit = [False] * MAX
    graph = defaultdict(list)

    for x in a:
        edge[x] = True

    for x in a:
        for i in range(n):
            y = x ^ (1 << i)
            if edge[y]:
                graph[x].append(y)
                graph[y].append(x)

    def dfs(v):
        visit[v] = True
        for w in graph[v]:
            if not visit[w]:
                dfs(w)

    count = 0
    for i in range(MAX):
        if edge[i] and not visit[i]:
            dfs(i)
            count += 1
    
    return count
```
