```python
MOD = 10**9 + 7

def solve_tree_coloring(test_cases):
    results = []
    for case in test_cases:
        n, k, edges = case
        if n == 1:
            results.append(k % MOD)
            continue

        adj = [[] for _ in range(n+1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        parent = [0] * (n + 1)
        children = [[] for _ in range(n + 1)]
        stack = [(1, None)]
        while stack:
            u, p = stack.pop()
            parent[u] = p
            for v in adj[u]:
                if v != p:
                    children[u].append(v)
                    stack.append((v, u))

        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for u in range(1, n+1):
            if not children[u]:
                for c in range(1, k+1):
                    dp[u][c] = 1

        for u in reversed(range(1, n+1)):
            if not children[u]:
                continue
            total = 0
            for c in range(1, k+1):
                product = 1
                for v in children[u]:
                    product = (product * sum(dp[v])) % MOD
                dp[u][c] = product

        total_ways = sum(dp[1]) % MOD
        results.append(total_ways)

    return results

def solve(T, cases):
    test_cases = []
    for case in cases:
        n, k, edges = case
        test_cases.append((n, k, edges))
    return solve_tree_coloring(test_cases)
```