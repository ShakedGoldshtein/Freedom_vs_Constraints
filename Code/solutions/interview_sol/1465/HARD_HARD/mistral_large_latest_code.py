```python
import sys
MOD = 10**9 + 7

def solve():
    def main():
        def read_int():
            return int(sys.stdin.readline())

        def read_ints():
            return map(int, sys.stdin.readline().split())

        T = read_int()
        for _ in range(T):
            n, Q = read_ints()
            adj = [[] for _ in range(n + 1)]
            for __ in range(n - 1):
                u, v = read_ints()
                adj[u].append(v)
                adj[v].append(u)

            conditions = []
            for __ in range(Q):
                u, v, x = read_ints()
                conditions.append((u, v, x))

            # Preprocess LCA and parent relationships
            parent = [0] * (n + 1)
            depth = [0] * (n + 1)
            visited = [False] * (n + 1)
            stack = [(1, 0)]
            visited[1] = True
            while stack:
                u, p = stack.pop()
                parent[u] = p
                for v in adj[u]:
                    if not visited[v] and v != p:
                        depth[v] = depth[u] + 1
                        visited[v] = True
                        stack.append((v, u))

            # Binary lifting for LCA
            LOG = 20
            up = [[0] * (n + 1) for _ in range(LOG)]
            up[0] = parent[:]
            for k in range(1, LOG):
                for v in range(1, n + 1):
                    up[k][v] = up[k - 1][up[k - 1][v]]

            def lca(u, v):
                if depth[u] < depth[v]:
                    u, v = v, u
                # Bring u up to depth of v
                for k in range(LOG - 1, -1, -1):
                    if depth[u] - (1 << k) >= depth[v]:
                        u = up[k][u]
                if u == v:
                    return u
                for k in range(LOG - 1, -1, -1):
                    if up[k][u] != up[k][v]:
                        u = up[k][u]
                        v = up[k][v]
                return parent[u]

            # Process conditions: for each condition (u, v, x), we need the sum of edge weights on path u-v to be even if x=0, odd if x=1
            # This is equivalent to: sum_{e in path(u,v)} w_e ≡ x mod 2
            # We can represent this as a linear equation over GF(2)
            # Variables: edge weights (binary)
            # Each condition gives one equation: sum of edge weights in path(u,v) ≡ x mod 2
            # We need to count the number of solutions to this system of equations

            # First, represent each condition as a sum of edges in the path
            # We can use the tree structure to express the path as a sum of edges from root to u and root to v
            # Specifically, for path(u,v), the edges are those in (root to u) XOR (root to v), excluding the LCA part

            # We'll represent each edge as a variable, and each condition as a sum of variables ≡ x mod 2
            # Then, we can use Gaussian elimination over GF(2) to solve the system

            # Assign edge indices: perform BFS to assign indices to edges
            edge_index = {}
            edge_list = []
            index = 0
            visited_edges = set()
            stack = [(1, 0)]
            while stack:
                u, p = stack.pop()
                for v in adj[u]:
                    if v != p and (u, v) not in visited_edges and (v, u) not in visited_edges:
                        edge_index[(u, v)] = index
                        edge_index[(v, u)] = index
                        edge_list.append((u, v))
                        visited_edges.add((u, v))
                        visited_edges.add((v, u))
                        index += 1
                        stack.append((v, u))

            num_edges = n - 1
            num_conditions = Q

            # For each condition, compute the edges in the path u-v
            # The edges are all edges in the path from u to v, which can be found by:
            # edges = (edges in path from root to u) XOR (edges in path from root to v)
            # But we need to exclude the edges that are common to both paths