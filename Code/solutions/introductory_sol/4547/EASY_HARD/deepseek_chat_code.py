```python
def moreZeros(s):
    seen = set()
    result = []
    for char in s:
        if char in seen:
            continue
        binary = bin(ord(char))[2:]
        zeros = binary.count('0')
        ones = binary.count('1')
        if zeros > ones:
            result.append(char)
            seen.add(char)
    return result
```