```python
def solve(t, test_cases):
    results = []
    for i in range(t):
        dish1 = set(test_cases[i*2])
        dish2 = set(test_cases[i*2+1])
        common = dish1.intersection(dish2)
        results.append("similar" if len(common) >= 2 else "dissimilar")
    return results
```