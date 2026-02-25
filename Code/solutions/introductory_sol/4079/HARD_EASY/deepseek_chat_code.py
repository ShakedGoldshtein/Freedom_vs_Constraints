```python
def encode(s):
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    result = []
    for char in s:
        if 'a' <= char <= 'z':
            result.append(str(ord(char) - ord('a') + 1))
        elif 'A' <= char <= 'Z':
            result.append(str(ord(char) - ord('A') + 1))
        else:
            result.append(char)
    
    return ''.join(result)
```