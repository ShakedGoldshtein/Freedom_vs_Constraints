```python
def thirt(n):
    remainder = [1, 10, 9, 12, 3, 4]
    while True:
        n1 = sum(int(c) * remainder[i % 6] for i, c in enumerate(reversed(str(n))))
        if n == n1:
            return n
        n = n1
```