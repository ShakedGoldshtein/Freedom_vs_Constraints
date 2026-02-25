```python
def thirt(n):
    pattern = [1, 10, 9, 12, 3, 4]
    while True:
        n, last = sum(d * pattern[i%6] for i, d in enumerate(map(int, str(n)[::-1]))), n
        if n == last:
            return n
```