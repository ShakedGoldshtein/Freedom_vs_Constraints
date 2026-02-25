```python
def dec2FactString(nb):
    """Convert decimal to factorial base string representation"""
    result = ['0']  # Always ends with 0
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    pos = 1
    
    while nb > 0:
        nb, rem = divmod(nb, pos)
        result.append(digits[rem])
        pos += 1
        
    return ''.join(reversed(result))

def factString2Dec(string):
    """Convert factorial base string to decimal number"""
    result = 0
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    pos = len(string) - 1
    
    for c in string:
        if c in digits:
            digit = digits.index(c)
            if digit > pos:
                raise ValueError(f"Invalid digit {c} at position {pos}")
            result += digit * factorial(pos)
        pos -= 1
        
    return result

def factorial(n):
    """Calculate n!"""
    if n < 2:
        return 1
    result = 1
    for i in range(2, n+1):
        result *= i
    return result
```