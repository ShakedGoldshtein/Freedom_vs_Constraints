Here is the Python code for the problem:

```python
def more_zeros(s):
    def binary_has_more_zeros(ch):
        binary_representation = format(ord(ch), 'b')
        return binary_representation.count('0') > binary_representation.count('1')

    result = []
    for ch in s:
        if ch not in result and binary_has_more_zeros(ch):
            result.append(ch)
    return result
```

In this code, the `more_zeros` function goes through each character in the input string `s` and applies the function `binary_has_more_zeros` to check if in its binary representation the zeros are more than ones. If so and if the character is not already in the results, then it includes it in the result array. This way, any duplicate characters are only kept the first time they appear. The result array will contain the characters in the order they appeared in the input string.