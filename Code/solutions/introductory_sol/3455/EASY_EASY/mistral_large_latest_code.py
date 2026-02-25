```python
def disarium_number(n):
    digits = [int(d) for d in str(n)]
    total = sum(d ** (i + 1) for i, d in enumerate(digits))
    return "Disarium !!" if total == n else "Not !!"
```