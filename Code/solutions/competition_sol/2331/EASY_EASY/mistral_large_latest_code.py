```python
import sys
from collections import deque

def solve():
    def bfs(n, adj, a, b):
        parent = [-1] * (n + 1)
        q = deque()
        q.append(a)
        parent[a] = 0
        while q:
            u = q.popleft()
            if u == b:
                break
            for v in adj[u]:
                if parent[v] == -1:
                    parent[v] = u
                    q.append(v)
        path = []
        while b != 0:
            path.append(b)
            b = parent[b]
        return path[::-1]

    def is_possible(n, adj, a, b):
        path = bfs(n, adj, a, b)
        k = len(path)
        if k == 2:
            return "YES"
        if k % 2 == 0:
            return "NO"
        for u in adj[path[0]]:
            if u != path[1]:
                return "YES"
        for u in adj[path[-1]]:
            if u != path[-2]:
                return "YES"
        return "NO"

    t = 100
    n_max = 10**5
    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.read().split()
    ptr = 0
    results = []
    for _ in range(int(input[ptr])):
        ptr += 1
        n = int(input[ptr])
        a = int(input[ptr+1])
        b = int(input[ptr+2])
        ptr +=3
        adj = [[] for _ in range(n+1)]
        for __ in range(n-1):
            u = int(input[ptr])
            v = int(input[ptr+1])
            ptr +=2
            adj[u].append(v)
            adj[v].append(u)
        results.append(is_possible(n, adj, a, b))
    return '\n'.join(results)

def solve_test_case(n, a, b, edges):
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    def bfs(a, b):
        parent = [-1] * (n + 1)
        q = deque()
        q.append(a)
        parent[a] = 0
        while q:
            u = q.popleft()
            if u == b:
                break
            for v in adj[u]:
                if parent[v] == -1:
                    parent[v] = u
                    q.append(v)
        path = []
        while b != 0:
            path.append(b)
            b = parent[b]
        return path[::-1]
    path = bfs(a, b)
    k = len(path)
    if k == 2:
        return "YES"
    if k % 2 == 0:
        return "NO"
    for u in adj[path[0]]:
        if u != path[1]:
            return "YES"
    for u in adj[path[-1]]:
        if u != path[-2]:
            return "YES"
    return "NO"
```