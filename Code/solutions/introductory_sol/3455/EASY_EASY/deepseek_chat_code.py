```python
def disarium_number(n):
    s = str(n)
    total = sum(int(d) ** (i + 1) for i, d in enumerate(s))
    return "Disarium !!" if total == n else "Not !!"
```