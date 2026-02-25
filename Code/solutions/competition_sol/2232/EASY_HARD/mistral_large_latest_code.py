```python
def solve(n):
    result = []
    current = 2
    level = 1
    for _ in range(n):
        target = (level + 1) ** 2
        if current < target:
            add = (target - current + level - 1) // level
            current += add * level
        else:
            add = 0
        result.append(add)
        current = int(current ** 0.5)
        level += 1
    return result
```