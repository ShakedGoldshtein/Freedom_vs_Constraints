```python
def moreZeros(s):
    seen = set()
    result = []
    for char in s:
        if char in seen:
            continue
        ascii_val = ord(char)
        binary = bin(ascii_val)[2:]
        zero_count = binary.count('0')
        one_count = binary.count('1')
        if zero_count > one_count:
            result.append(char)
            seen.add(char)
    return result
```