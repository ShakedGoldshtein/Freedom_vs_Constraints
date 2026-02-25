```python
import string

def dec2FactString(nb):
    digits = string.digits + string.ascii_uppercase
    factorials = [1]
    for i in range(1, 36):
        factorials.append(factorials[-1] * i)
    res = ''
    i = 35
    while nb > 0:
        q, nb = divmod(nb, factorials[i])
        res = digits[q] + res
        i -= 1
    return res

def factString2Dec(s):
    digits = string.digits + string.ascii_uppercase
    factorials = [1]
    for i in range(1, 36):
        factorials.append(factorials[-1] * i)
    res = 0
    for i, c in enumerate(s[::-1]):
        res += digits.index(c) * factorials[i]
    return res
```
