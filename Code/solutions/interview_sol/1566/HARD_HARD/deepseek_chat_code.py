```python
import sys
from collections import defaultdict, deque

def solve_test_case(n, constraints):
    graph = defaultdict(list)
    for i, j, val in constraints:
        if i == j:
            if val != 0:
                return "no"
            continue
        graph[i].append((j, val))
        graph[j].append((i, val))
    
    colors = {}
    for node in range(1, n + 1):
        if node not in colors:
            queue = deque([node])
            colors[node] = 0
            while queue:
                current = queue.popleft()
                for neighbor, val in graph[current]:
                    expected_color = colors[current] ^ val
                    if neighbor in colors:
                        if colors[neighbor] != expected_color:
                            return "no"
                    else:
                        colors[neighbor] = expected_color
                        queue.append(neighbor)
    return "yes"

def main():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    idx = 1
    results = []
    for _ in range(t):
        n = int(data[idx]); idx += 1
        q = int(data[idx]); idx += 1
        constraints = []
        for __ in range(q):
            i = int(data[idx]); idx += 1
            j = int(data[idx]); idx += 1
            val = int(data[idx]); idx += 1
            constraints.append((i, j, val))
        results.append(solve_test_case(n, constraints))
    print("\n".join(results))

if __name__ == "__main__":
    main()
```