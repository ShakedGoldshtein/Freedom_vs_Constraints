```python
def solve(friday, saturday, total_sheep):
    return total_sheep - (sum(friday) + sum(saturday))
```