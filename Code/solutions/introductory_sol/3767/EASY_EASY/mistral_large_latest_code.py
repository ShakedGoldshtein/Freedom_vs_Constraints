```python
def decimal_to_factorial(n):
    if n == 0:
        return "0"
    digits = []
    i = 1
    while True:
        factorial = 1
        for j in range(1, i + 1):
            factorial *= j
        if factorial > n:
            break
        i += 1
    i -= 1
    remaining = n
    while i >= 0:
        factorial = 1
        for j in range(1, i + 1):
            factorial *= j
        digit = remaining // factorial
        digits.append(str(digit))
        remaining %= factorial
        i -= 1
    return ''.join(digits)

def factorial_to_decimal(s):
    total = 0
    for i, c in enumerate(reversed(s)):
        digit = int(c, 36) if c.isalpha() else int(c)
        factorial = 1
        for j in range(1, i + 1):
            factorial *= j
        total += digit * factorial
    return total
```