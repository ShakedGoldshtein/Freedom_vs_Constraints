```python
def solve(x):
    def reverse_word(word):
        length = len(word)
        if length <= 1:
            return word
            
        if length % 2 == 0:
            # Even length word
            left = word[:length//2]
            right = word[length//2:]
            return right[::-1] + left[::-1]
        else:
            # Odd length word
            left = word[:length//2] 
            mid = word[length//2]
            right = word[length//2 + 1:]
            return right[::-1] + mid + left[::-1]
            
    words = x.split()
    turned_words = [reverse_word(word) for word in words]
    return ' '.join(turned_words)
```