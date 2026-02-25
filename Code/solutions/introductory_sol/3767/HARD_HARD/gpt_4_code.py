```python
from math import factorial
from string import ascii_uppercase

def dec2FactString(nb):
    digits = [str(n) for n in range(10)] + list(ascii_uppercase)
    output = ''
    for i in range(35, -1, -1):
        quotient, nb = divmod(nb, factorial(i))
        output += digits[quotient]

    return output.lstrip('0') or '0'


def factString2Dec(s):
    s = s[::-1]
    digits = {str(n): n for n in range(10)}
    digits.update({c: ord(c) - 55 for c in ascii_uppercase})

    return sum(factorial(i) * digits[s[i]] for i in range(len(s)))
```