```python
def solve_tuzik_vanya_game(test_cases):
    results = []
    for N, M in test_cases:
        if (N - 1) % 4 == 0 and (M - 1) % 2 == 0:
            results.append("Vanya")
        else:
            results.append("Tuzik")
    return results
```