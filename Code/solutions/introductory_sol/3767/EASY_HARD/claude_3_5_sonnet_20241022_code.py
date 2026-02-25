```python
def dec2FactString(nb):
    if nb == 0:
        return "0"
        
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    divisor = 1
    i = 1
    
    while nb > 0:
        divisor *= i
        rem = nb % divisor
        nb -= rem
        result.insert(0, digits[rem // (divisor // i)])
        i += 1
        
    return "".join(result) + "0"

def factString2Dec(string):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = 0
    factorial = 1
    
    for i in range(len(string)-2, -1, -1):
        factorial *= (len(string) - i - 1)
        result += digits.index(string[i]) * factorial
        
    return result
```