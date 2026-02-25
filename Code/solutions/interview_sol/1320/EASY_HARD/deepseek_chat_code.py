```python
def solve(T, N_list):
    results = []
    for N in N_list:
        if N % 2 == 1 or N == 2:
            results.append("B")
        else:
            results.append("A")
    return results
```