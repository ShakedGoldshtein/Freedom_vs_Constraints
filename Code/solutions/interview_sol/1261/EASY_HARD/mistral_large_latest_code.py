```python
def solve_network_design(T, test_cases):
    results = []
    for N, M in test_cases:
        if M < N - 1 or M > N * (N - 1) // 2:
            results.append([[-1, -1]])
            continue

        if N == 1:
            if M == 0:
                results.append([])
            else:
                results.append([[-1, -1]])
            continue

        min_edges = N
        max_edges = N * (N - 1) // 2

        if M < min_edges or M > max_edges:
            results.append([[-1, -1]])
            continue

        if N == 2:
            if M == 1:
                results.append([[1, 2]])
            else:
                results.append([[-1, -1]])
            continue

        edges = []
        if M == N * (N - 1) // 2:
            for i in range(1, N + 1):
                for j in range(i + 1, N + 1):
                    edges.append([i, j])
        else:
            if M < N:
                results.append([[-1, -1]])
                continue
            for i in range(1, N):
                edges.append([i, i + 1])
            edges.append([1, N])

            remaining = M - N
            if remaining > 0:
                for i in range(1, N - 1):
                    for j in range(i + 2, N + 1):
                        if remaining == 0:
                            break
                        edges.append([i, j])
                        remaining -= 1
                if remaining > 0:
                    for i in range(2, N):
                        for j in range(i + 2, N + 1):
                            if remaining == 0:
                                break
                            edges.append([i, j])
                            remaining -= 1
        results.append(edges)
    return results
```