```python
def solve(test_cases):
    MOD = 1000000007
    result = []
    
    def get_path(adj, u, v, parent):
        if u == v:
            return []
        for next_node in adj[u]:
            if next_node != parent:
                path = get_path(adj, next_node, v, u)
                if path is not None:
                    return [(u, next_node)] + path
        return None

    for _ in range(test_cases):
        n, q = map(int, next(test_cases))
        
        # Build adjacency list
        adj = [[] for _ in range(n+1)]
        edges = []
        for _ in range(n-1):
            u, v = map(int, next(test_cases))
            adj[u].append(v)
            adj[v].append(u)
            edges.append((u, v))
            
        # Process conditions
        paths = []
        constraints = []
        for _ in range(q):
            u, v, x = map(int, next(test_cases))
            path = get_path(adj, u, v, -1)
            paths.append(path)
            constraints.append(x)
            
        # Build system of linear equations
        equations = []
        for i in range(q):
            equation = [0] * (n-1)
            for edge in paths[i]:
                edge = tuple(sorted(edge))
                idx = edges.index(edge)
                equation[idx] = 1
            equations.append((equation, constraints[i]))
            
        # Check if system is consistent and count solutions
        def solve_equations(equations, n):
            if not equations:
                return pow(2, n, MOD)
                
            # Gaussian elimination
            curr = 0
            variables = n
            for i in range(len(equations)):
                found = False
                for j in range(curr, variables):
                    if equations[i][0][j] == 1:
                        found = True
                        if j != curr:
                            for eq in equations:
                                eq[0][curr], eq[0][j] = eq[0][j], eq[0][curr]
                        break
                if not found:
                    if equations[i][1] == 1:
                        return 0
                    continue
                    
                for j in range(i+1, len(equations)):
                    if equations[j][0][curr] == 1:
                        for k in range(variables):
                            equations[j][0][k] ^= equations[i][0][k]
                        equations[j][1] ^= equations[i][1]
                curr += 1
                
            return pow(2, variables - curr, MOD)
            
        result.append(solve_equations(equations, n-1))
        
    return result
```