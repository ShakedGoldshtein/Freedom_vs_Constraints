```python
def count_staircases(x):
    total = 0
    k = 1
    while True:
        cells_needed = (2**k - 1) * (2**(k - 1))
        if cells_needed > x:
            break
        total += 1
        x -= cells_needed
        k += 1
    return total

def solve(t, test_cases):
    results = []
    for x in test_cases:
        results.append(count_staircases(x))
    return results
```