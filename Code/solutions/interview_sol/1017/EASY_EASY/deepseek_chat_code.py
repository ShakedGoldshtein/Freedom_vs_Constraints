```python
def solve(A1, A2, A3, A4, A5, P):
    total_hours_needed = (A1 + A2 + A3 + A4 + A5) * P
    max_weekday_hours = 5 * 24
    return "Yes" if total_hours_needed > max_weekday_hours else "No"

t = int(input())
for _ in range(t):
    data = list(map(int, input().split()))
    print(solve(*data))
```