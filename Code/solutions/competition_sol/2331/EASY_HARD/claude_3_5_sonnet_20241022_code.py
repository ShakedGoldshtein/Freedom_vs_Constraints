```python
def solve(t, cases):
    def find_path(adj, start, end, n):
        visited = [False] * (n+1)
        path = []
        
        def dfs(curr, target):
            visited[curr] = True
            path.append(curr)
            
            if curr == target:
                return True
                
            for next_node in adj[curr]:
                if not visited[next_node]:
                    if dfs(next_node, target):
                        return True
                        
            path.pop()
            return False
            
        dfs(start, end)
        return path

    def can_reverse(n, a, b, edges):
        # Build adjacency list
        adj = [[] for _ in range(n+1)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # Get path from head to tail
        snake_path = find_path(adj, a, b, n)
        snake_len = len(snake_path)
        
        # BFS to find all possible head positions
        start = (a,b) # (head, tail)
        visited = {start}
        queue = [(start, 0)]
        
        while queue:
            (head, tail), d = queue.pop(0)
            
            # Found valid reversal
            if head == b and tail == a:
                return "YES"
                
            snake_nodes = set(find_path(adj, head, tail, n))
            
            # Try moving head
            for next_head in adj[head]:
                if next_head not in snake_nodes:
                    new_tail = find_path(adj, head, tail, n)[1]
                    if (next_head, new_tail) not in visited:
                        visited.add((next_head, new_tail))
                        queue.append(((next_head, new_tail), d+1))
                        
            # Try moving tail 
            for next_tail in adj[tail]:
                if next_tail not in snake_nodes:
                    new_head = find_path(adj, head, tail, n)[-2]
                    if (new_head, next_tail) not in visited:
                        visited.add((new_head, next_tail))
                        queue.append(((new_head, next_tail), d+1))
                        
        return "NO"

    results = []
    curr_case = 0
    while curr_case < t:
        n,a,b = cases[curr_case]
        edges = cases[curr_case+1:curr_case+n]
        results.append(can_reverse(n,a,b,edges))
        curr_case += n
        
    return results
```