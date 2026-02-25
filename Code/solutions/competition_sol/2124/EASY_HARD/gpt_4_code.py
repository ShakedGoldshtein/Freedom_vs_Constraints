```python
import heapq
def solve(n, m, x, edges):
    MAX = 10**6
    start = [0]
    end = [n - 1]
    graph = [[] for _ in range(n)]
    home = [[] for _ in range(n)]
    capacity = [[0]*n for _ in range(n)]
    flows = [[0]*n for _ in range(n)]
    for u, v, cap in edges:
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)
        home[u - 1].append(len(home[v - 1]))
        home[v - 1].append(len(home[u - 1]) - 1)
        capacity[u - 1][v - 1] = cap
    lo = 0
    hi = MAX
    while hi - lo > 1e-6:
        mid = (hi + lo) / 2
        q = [(0, start[0])]
        vis = [0]*n
        prevnode = [-1]*n
        prevedge = [-1]*n
        flow = [0]*n
        vis[start[0]] = 1
        flow[start[0]] = MAX
        while q:
            _, node = heapq.heappop(q)
            for idx in range(len(graph[node])):
                v = graph[node][idx]
                if flow[node] * 1.0 > capacity[node][v] * mid:
                    newFlow = capacity[node][v] * mid
                else:
                    newFlow = flow[node]
                if vis[v] or newFlow == 0:
                    continue
                if newFlow > flow[v]:
                    prevnode[v] = node
                    flow[v] = newFlow
                    prevedge[v] = idx
                    heapq.heappush(q, (-newFlow, v))
            vis[node] = 1
            if node == end[0]:
                break
        total = sum(flow[end[0]] for _ in range(x))
        if total < mid:
            hi = mid
        else:
            lo = mid
    return "{:.10f}".format(lo)
```

In this python code, function `solve` takes four parameters `n` represents the number of nodes, `m` represents the number of directed edges, `x` represents the number of bears and `edges` represents all the directed edges.

As output, it returns the maximum amount of weight Niwel can deliver if he uses exactly `x` bears. It uses `Dijkstra's algorithm` to find the minimum possible weight that can be transferred from source to sink. Then, it applies `binary search` to minimize the maximum weight that can be transferred.