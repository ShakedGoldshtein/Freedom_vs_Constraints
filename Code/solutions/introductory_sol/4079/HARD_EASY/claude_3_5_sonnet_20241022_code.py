```python
def encode(str):
    result = []
    
    for char in str:
        if char.isalpha():
            # Get position (1-based) in alphabet, handling both upper and lower case
            if char.isupper():
                pos = ord(char) - ord('A') + 1
            else:
                pos = ord(char) - ord('a') + 1
            result.append(str(pos))
        else:
            result.append(char)
            
    return ''.join(result)
```