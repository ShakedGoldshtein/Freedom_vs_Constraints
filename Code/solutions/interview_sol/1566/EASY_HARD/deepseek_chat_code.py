```python
import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    t = int(input_data[0])
    idx = 1
    results = []
    
    for _ in range(t):
        N = int(input_data[idx]); idx += 1
        Q = int(input_data[idx]); idx += 1
        
        graph = [[] for _ in range(N)]
        constraints = []
        
        for __ in range(Q):
            i = int(input_data[idx]) - 1; idx += 1
            j = int(input_data[idx]) - 1; idx += 1
            val = int(input_data[idx]); idx += 1
            constraints.append((i, j, val))
            graph[i].append((j, val))
            graph[j].append((i, val))
        
        visited = [-1] * N
        valid = True
        
        for i in range(N):
            if visited[i] == -1:
                visited[i] = 0
                queue = deque([i])
                while queue:
                    u = queue.popleft()
                    for v, w in graph[u]:
                        if visited[v] == -1:
                            visited[v] = visited[u] ^ w
                            queue.append(v)
                        else:
                            if visited[v] != (visited[u] ^ w):
                                valid = False
                                break
                    if not valid:
                        break
                if not valid:
                    break
        
        results.append("yes" if valid else "no")
    
    print("\n".join(results))

if __name__ == "__main__":
    solve()
```