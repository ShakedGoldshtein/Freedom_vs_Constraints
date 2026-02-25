```python
def solve(x):
    def reverse_word(word):
        length = len(word)
        if length <= 1:
            return word
            
        if length % 2 == 0:
            left = word[:length//2][::-1]
            right = word[length//2:][::-1]
            return left + right
        else:
            left = word[:length//2][::-1]
            middle = word[length//2]
            right = word[length//2+1:][::-1]
            return left + middle + right
            
    words = x.split()
    return ' '.join(reverse_word(word) for word in words)
```