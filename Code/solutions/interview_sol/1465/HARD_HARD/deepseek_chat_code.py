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
            p ^= 1
        self.parent[ry] = rx
        self.parity[ry] = px ^ py ^ p
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True

def solve(T, test_cases):
    results = []
    for case in test_cases:
        n, Q = case['n'], case['Q']
        edges = case['edges']
        queries = case['queries']
        
        dsu = DSU(n)
        valid = True
        for u, v, x in queries:
            u_idx, v_idx = u - 1, v - 1
            if not dsu.union(u_idx, v_idx, x):
                valid = False
                break
        
        if not valid:
            results.append(0)
            continue
        
        components = 0
        for i in range(n):
            if dsu.parent[i] == i:
                components += 1
        
        ways = pow(2, n - 1 - (n - components), MOD)
        results.append(ways)
    
    return results
```