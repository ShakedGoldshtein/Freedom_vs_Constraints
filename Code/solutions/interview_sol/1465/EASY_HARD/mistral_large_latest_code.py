```python
import sys
MOD = 10**9 + 7

def solve():
    def main():
        T = int(sys.stdin.readline())
        for _ in range(T):
            n, Q = map(int, sys.stdin.readline().split())
            adj = [[] for _ in range(n+1)]
            for __ in range(n-1):
                u, v = map(int, sys.stdin.readline().split())
                adj[u].append(v)
                adj[v].append(u)

            conditions = []
            for __ in range(Q):
                u, v, x = map(int, sys.stdin.readline().split())
                conditions.append((u, v, x))

            parent = [0]*(n+1)
            depth = [0]*(n+1)
            stack = [(1, 0)]
            while stack:
                u, p = stack.pop()
                parent[u] = p
                depth[u] = depth[p] + 1
                for v in adj[u]:
                    if v != p:
                        stack.append((v, u))

            lca = [[0]*(n+1) for _ in range(20)]
            for u in range(1, n+1):
                lca[0][u] = parent[u]
            for k in range(1, 20):
                for u in range(1, n+1):
                    lca[k][u] = lca[k-1][lca[k-1][u]]

            def get_lca(u, v):
                if depth[u] < depth[v]:
                    u, v = v, u
                for k in range(19, -1, -1):
                    if depth[u] - (1 << k) >= depth[v]:
                        u = lca[k][u]
                if u == v:
                    return u
                for k in range(19, -1, -1):
                    if lca[k][u] != lca[k][v]:
                        u = lca[k][u]
                        v = lca[k][v]
                return parent[u]

            edges = []
            for u in range(1, n+1):
                for v in adj[u]:
                    if v > u:
                        edges.append((u, v))

            m = len(edges)
            if m == 0:
                print(1)
                continue

            equations = []
            for u, v, x in conditions:
                ancestor = get_lca(u, v)
                path_u = []
                while u != ancestor:
                    path_u.append(u)
                    u = parent[u]
                path_v = []
                while v != ancestor:
                    path_v.append(v)
                    v = parent[v]
                path = path_u + [ancestor] + path_v[::-1]
                eq = []
                for i in range(len(path)-1):
                    a, b = path[i], path[i+1]
                    if a > b:
                        a, b = b, a
                    idx = edges.index((a, b))
                    eq.append(idx)
                mask = 0
                for idx in eq:
                    mask ^= (1 << idx)
                target = x
                equations.append((mask, target))

            if not equations:
                print(pow(2, m, MOD))
                continue

            from collections import defaultdict
            basis = []
            for mask, target in equations:
                x = mask
                for b in basis:
                    x = min(x, x ^ b)
                if x != 0:
                    basis.append(x)
                    for i in range(len(basis)-1):
                        if (basis[i] ^ x) < basis[i]:
                            basis[i] ^= x
                    basis.sort()
                else:
                    if target != 0:
                        print(0)
                        break
            else:
                rank = len(basis)
                free = m - rank
                print(pow(2, free, MOD))

    sys.setrecursionlimit(1 << 25)
    main()

def solve_case(n, Q, edges, conditions):
    MOD = 10**9 + 7
    adj = [[] for _ in range(n+1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    parent = [0]*(n+1)
    depth = [0]*(n+1)
    stack = [(1, 0)]
    while stack:
        u, p = stack.pop()
        parent[u] = p
        depth[u] = depth[p] + 1
        for v in adj[u]:
            if v != p:
                stack.append((v, u))

    lca = [[0