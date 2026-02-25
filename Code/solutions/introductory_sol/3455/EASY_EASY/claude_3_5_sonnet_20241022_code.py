```python
def disarium_number(n):
    digits = str(n)
    total = sum(int(d) ** (i + 1) for i, d in enumerate(digits))
    return "Disarium !!" if total == n else "Not !!"
```