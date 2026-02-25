```python
def thirt(n):
    pattern = [1, 10, 9, 12, 3, 4]
    prev = n
    while True:
        digits = [int(d) for d in str(prev)]
        digits.reverse()
        total = 0
        for i, digit in enumerate(digits):
            total += digit * pattern[i % len(pattern)]
        if total == prev:
            return total
        prev = total
```