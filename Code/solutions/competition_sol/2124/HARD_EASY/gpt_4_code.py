Here is your python code:

```python
from collections import deque

def Edmond_Karp(n, m, x, graph):
    flow_value = float('inf')
    while True:
        parents = [-1 for _ in range(n)]
        parents[0] = -2
        q = deque()
        q.append(0)
        while q:
            node = q.popleft()
            for edge in graph[node]:
                if edge[0] not in q and parents[edge[0]] == -1 and edge[1] > 0:
                    parents[edge[0]] = (node, edge)
                    if edge[0] == n-1:
                        min_edge = min(edge[1] for edge in get_Path(n, parents))
                        flow_value = min(flow_value, min_edge)
                        augment(n, graph, min_edge, parents)
                        return flow_value
                    q.append(edge[0])

def augment(n, graph, path_flow, parents):
    node = n-1
    while node:
        parent_edge = parents[node]
        parent_edge[1] -= path_flow
        graph[node].append([parent_edge[3], path_flow, parent_edge[2], node])
        node = parent_edge[3]

def get_Path(n, parents):
    path = []
    node = n-1
    while node:
        edge = parents[node]
        path.append(edge)
        node = edge[3]
    return path

def max_delivery(n, m, x, edges):
    low = 0
    high = 10**6 + 1
    while high - low > 1e-1:
        mid = (high+low) / 2.0
        graph = [[] for _ in range(n)]
        for i, edge in enumerate(edges):
            a, b, capacity = edge
            a -= 1
            b -= 1
            graph[a].append([b, capacity // mid, -1, a])
            edges[i].append(a)
        temp = sum(Edmond_Karp(n, m, x, graph) for _ in range(x))
        if temp >= x:
            low = mid
        else:
            high = mid
    return low
```
Please note, you have to call the "max_delivery" function to solve the problem.