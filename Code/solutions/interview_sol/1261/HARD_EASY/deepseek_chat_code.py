```python
def solve_test_case(N, M):
    if N == 1:
        if M == 0:
            return []
        else:
            return None
    
    min_edges = N
    max_edges = 2 * (N - 1)
    
    if M < min_edges or M > max_edges:
        return None
    
    edges = []
    
    if N == 2:
        if M == 1:
            edges.append((1, 2))
        elif M == 2:
            edges.append((1, 2))
            edges.append((1, 2))
        return edges
    
    cycle_edges = []
    for i in range(1, N + 1):
        cycle_edges.append((i, i % N + 1))
    
    if M == N:
        return cycle_edges
    
    remaining = M - N
    extra_edges = []
    
    for i in range(1, N - 1):
        if remaining == 0:
            break
        for j in range(i + 2, N + 1):
            if remaining == 0:
                break
            if (i == 1 and j == N):
                continue
            extra_edges.append((i, j))
            remaining -= 1
    
    if remaining > 0:
        return None
    
    return cycle_edges + extra_edges

def main():
    import sys
    data = sys.stdin.read().split()
    t = int(data[0])
    index = 1
    results = []
    
    for _ in range(t):
        N = int(data[index])
        M = int(data[index + 1])
        index += 2
        result = solve_test_case(N, M)
        if result is None:
            results.append("-1 -1")
        else:
            for edge in result:
                results.append(f"{edge[0]} {edge[1]}")
    
    print("\n".join(results))

if __name__ == "__main__":
    main()
```