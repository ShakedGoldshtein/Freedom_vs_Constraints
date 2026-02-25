```python
def moreZeros(s):
    def count_zeros_ones(c):
        binary = bin(ord(c))[2:]
        zeros = binary.count('0')
        ones = binary.count('1')
        return zeros > ones
    
    seen = set()
    result = []
    
    for char in s:
        if char not in seen and count_zeros_ones(char):
            seen.add(char)
            result.append(char)
    
    return result
```