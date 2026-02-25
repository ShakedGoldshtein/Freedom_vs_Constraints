```python
def calculate_minimum_score(T, tests):
    results = []
    for _ in range(T):
        N, K, E, M, scores, sergey = tests[_]
        scores.sort()
        needed = scores[-K] - sum(sergey) + 1
        if needed <= 0:
            results.append(0)
        elif needed <= M:
            results.append(needed)
        else:
            results.append('Impossible')
    return results
```