```python
MOD = 10**9 + 7

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.parity = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            root, p = self.find(self.parent[x])
            self.parity[x] ^= self.parity[self.parent[x]]
            self.parent[x] = root
        return self.parent[x], self.parity[x]
    
    def union(self, x, y, p):
        rx, px = self.find(x)
        ry, py = self.find(y)
        if rx == ry:
            return (px ^ py) == p
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
            px, py = py, px
        self.parent[ry] = rx
        self.parity[ry] = px ^ py ^ p
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True

def solve_test_case(n, edges, conditions):
    dsu = DSU(n)
    for u, v, x in conditions:
        u -= 1
        v -= 1
        if not dsu.union(u, v, x):
            return 0
    
    comp_count = 0
    for i in range(n):
        if dsu.parent[i] == i:
            comp_count += 1
    
    return pow(2, comp_count - 1, MOD)

def main(T, test_cases):
    results = []
    for i in range(T):
        n, Q = test_cases[i][0]
        edges = test_cases[i][1]
        conditions = test_cases[i][2]
        results.append(solve_test_case(n, edges, conditions))
    return results
```