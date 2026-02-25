```python
def solve(A1, A2, A3, A4, A5, P):
    total_office_workload_hours = A1 + A2 + A3 + A4 + A5
    required_home_workload_hours = total_office_workload_hours * P
    
    max_available_weekday_hours = 5 * 24 # 5 weekdays * 24 hours/day
    
    if required_home_workload_hours <= max_available_weekday_hours:
        return "No"
    else:
        return "Yes"

```