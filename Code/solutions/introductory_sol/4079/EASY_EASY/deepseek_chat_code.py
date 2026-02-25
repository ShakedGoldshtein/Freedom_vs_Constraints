```python
def encode(s):
    result = []
    for char in s:
        if char.isalpha():
            if char.islower():
                result.append(str(ord(char) - 96))
            else:
                result.append(str(ord(char) - 64))
        else:
            result.append(char)
    return ''.join(result)
```