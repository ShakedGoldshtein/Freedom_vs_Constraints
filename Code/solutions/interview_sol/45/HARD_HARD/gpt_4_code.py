```python
def find_max_nice_staircases(t, test_cases):
    results = []
    for x in test_cases:
        total_cells = 0
        n = 1
        while True:
            total_cells += ((n * (n + 1)) // 2) ** 2
            if total_cells > x:
                break
            n = 2 * n + 1
        results.append((n - 1) // 2)
    return results

t = 4
test_cases = [1, 8, 6, 1000000000000000000]
print(find_max_nice_staircases(t, test_cases))
```