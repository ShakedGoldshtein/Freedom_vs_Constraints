```python
def solve(T, tests):
    results = []
    for N, M in tests:
        n = N - 1
        m = M - 1
        if n % 4 == 0 and m % 3 == 0:
            results.append("Vanya")
        elif n % 4 == 1 and m % 3 == 2:
            results.append("Vanya")
        elif n % 4 == 2 and m % 3 == 1:
            results.append("Vanya")
        elif n % 4 == 3 and m % 3 == 0:
            results.append("Vanya")
        else:
            results.append("Tuzik")
    return results
```