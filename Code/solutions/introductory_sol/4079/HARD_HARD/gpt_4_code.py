```python
def encode(str):
    """
    Function that takes in a string str and replaces all the letters with their respective 
    positions in the English alphabet.
    """
    result = []
    for char in str:
        if char.isalpha():
            result.append(str(ord(char.lower()) - 96))
        else:
            result.append(char)
            
    return "".join(result)
```