Here is the Python code for the given problem:

```python
def more_zeros(s):
    chars = []
    for char in s:
        if char not in chars:
            binary_repr = bin(ord(char))[2:]
            if binary_repr.count('0') > binary_repr.count('1'):
                chars.append(char)
    return chars
```
This code will work for a string of any length, as long as it contains valid characters. It will return an array of unique characters from the input string whose binary representation have more zeros than ones, in the same order they first appeared in the input string.