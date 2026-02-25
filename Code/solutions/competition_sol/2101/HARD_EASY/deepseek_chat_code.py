```python
def solve(n, m, edges=None):
    if m == 0:
        return 0
    
    adj = [set() for _ in range(n)]
    for a, b in edges:
        u = a - 1
        v = b - 1
        adj[u].add(v)
        adj[v].add(u)
    
    unvisited = set(range(n))
    comp_count = 0
    
    for i in range(n):
        if i in unvisited:
            comp_count += 1
            stack = [i]
            unvisited.remove(i)
            while stack:
                u = stack.pop()
                neighbors = list(unvisited - adj[u])
                for v in neighbors:
                    unvisited.remove(v)
                    stack.append(v)
    
    return comp_count - 1

def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    m = int(data[1])
    edges = []
    index = 2
    for i in range(m):
        a = int(data[index])
        b = int(data[index + 1])
        edges.append((a, b))
        index += 2
    result = solve(n, m, edges)
    print(result)

if __name__ == "__main__":
    main()
```