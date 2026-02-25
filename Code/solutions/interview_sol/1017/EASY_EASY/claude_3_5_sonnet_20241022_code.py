```python
def solve(a1, a2, a3, a4, a5, p):
    total_work = (a1 + a2 + a3 + a4 + a5) * p
    total_available_time = 24 * 5
    return "Yes" if total_work > total_available_time else "No"
```