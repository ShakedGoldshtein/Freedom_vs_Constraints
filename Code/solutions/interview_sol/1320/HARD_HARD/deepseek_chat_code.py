```python
def determine_winner(n):
    if n % 2 == 1:
        return "B" if (n + 1) % 4 == 0 else "A"
    else:
        return "A" if n % 4 == 0 else "B"

def solve(T, test_cases):
    results = []
    for i in range(T):
        n = test_cases[i]
        results.append(determine_winner(n))
    return results
```