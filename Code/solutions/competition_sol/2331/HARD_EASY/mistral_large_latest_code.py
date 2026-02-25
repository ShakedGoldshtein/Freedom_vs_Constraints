```python
import sys
from collections import deque

def solve():
    def read_input():
        import sys
        input = sys.stdin.read().split()
        ptr = 0
        t = int(input[ptr])
        ptr += 1
        test_cases = []
        for _ in range(t):
            n, a, b = map(int, input[ptr:ptr+3])
            ptr += 3
            edges = []
            for __ in range(n-1):
                u, v = map(int, input[ptr:ptr+2])
                ptr += 2
                edges.append((u, v))
            test_cases.append((n, a, b, edges))
        return test_cases

    def build_adjacency_list(n, edges):
        adj = [[] for _ in range(n+1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        return adj

    def bfs_parent_and_depth(adj, start):
        n = len(adj) - 1
        parent = [0]*(n+1)
        depth = [-1]*(n+1)
        q = deque()
        depth[start] = 0
        q.append(start)
        while q:
            u = q.popleft()
            for v in adj[u]:
                if depth[v] == -1 and v != parent[u]:
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    q.append(v)
        return parent, depth

    def get_path(parent, a, b):
        path_a = []
        path_b = []
        while a != 0:
            path_a.append(a)
            a = parent[a]
        while b != 0:
            path_b.append(b)
            b = parent[b]
        path_a.reverse()
        path_b.reverse()
        lca = None
        min_len = min(len(path_a), len(path_b))
        for i in range(min_len):
            if path_a[i] == path_b[i]:
                lca = path_a[i]
            else:
                break
        path = []
        if lca is not None:
            idx_a = path_a.index(lca)
            idx_b = path_b.index(lca)
            path = path_a[:idx_a] + path_b[idx_b::-1]
        return path

    def is_possible_to_reverse(n, a, b, edges):
        adj = build_adjacency_list(n, edges)
        parent_a, depth_a = bfs_parent_and_depth(adj, a)
        parent_b, depth_b = bfs_parent_and_depth(adj, b)
        path = get_path(parent_a, a, b)
        if len(path) < 2:
            return False
        head, tail = path[0], path[-1]
        if len(path) == 2:
            return True
        if len(path) == 3:
            middle = path[1]
            for neighbor in adj[middle]:
                if neighbor != head and neighbor != tail:
                    return True
            return False
        if len(path) % 2 == 0:
            return True
        else:
            middle = path[len(path)//2]
            for neighbor in adj[middle]:
                if neighbor not in path:
                    return True
            return False

    test_cases = read_input()
    results = []
    for n, a, b, edges in test_cases:
        if is_possible_to_reverse(n, a, b, edges):
            results.append("YES")
        else:
            results.append("NO")
    return '\n'.join(results)

def solve_single_case(n, a, b, edges):
    def build_adjacency_list(n, edges):
        adj = [[] for _ in range(n+1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        return adj

    def bfs_parent_and_depth(adj, start):
        n = len(adj) - 1
        parent = [0]*(n+1)
        depth = [-1]*(n+1)
        q = deque()
        depth[start] = 0
        q.append(start)
        while q:
            u = q.popleft()
            for v in adj[u]:
                if depth[v] == -1 and v != parent[u]:
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    q.append(v)
        return parent, depth

    def get_path(parent, a, b):
        path_a = []
        path_b = []
        while a != 0:
            path_a.append(a)
            a = parent[a]
       