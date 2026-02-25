```python
def has_to_work_on_weekends(T, test_cases):
    results = []
    for i in range(T):
        A, P = test_cases[i][:-1], test_cases[i][-1]
        total_work_hours = sum(A) * P
        total_available_hours = 5 * 24
        if total_work_hours > total_available_hours:
            results.append("Yes")
        else:
            results.append("No")
    return results
```
