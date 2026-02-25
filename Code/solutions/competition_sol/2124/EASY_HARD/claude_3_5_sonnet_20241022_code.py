```python
def solve(n, m, x, edges):
    def can_flow(flow):
        def dfs(node, seen):
            if node == n:
                return True
            seen.add(node)
            for nxt, cap in adj[node]:
                if nxt not in seen and cap >= flow:
                    if dfs(nxt, seen):
                        return True
            return False
            
        count = 0
        while count < x:
            seen = set()
            if not dfs(1, seen):
                return False
            count += 1
        return True

    adj = [[] for _ in range(n+1)]
    for u, v, c in edges:
        adj[u].append((v, c))
        
    left, right = 0, 1e6
    for _ in range(100):
        mid = (left + right) / 2
        if can_flow(mid):
            left = mid
        else:
            right = mid
            
    return left * x
```