```python
def solve_test_case(A1, A2, A3, A4, A5, P):
    total_work_hours = 0
    for hours in [A1, A2, A3, A4, A5]:
        total_work_hours += hours * P
    
    total_available_hours = 5 * 24
    
    return "Yes" if total_work_hours > total_available_hours else "No"

def main(T, test_cases):
    results = []
    for test_case in test_cases:
        result = solve_test_case(*test_case)
        results.append(result)
    return results
```