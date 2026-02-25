```python
def disarium_number(n):
    return "Disarium !!" if sum(int(d)**i for i, d in enumerate(str(n), 1)) == n else "Not !!"
```